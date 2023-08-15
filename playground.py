from funcoes import formattedPrint
from play_alu_operations import *
from play_memory_operations import *
from play_jump_operations import *


def playground():
    formattedPrint("Você entrou no modo playground", True)

class ARM32Simulator:
    def __init__(self):
        self.registers = {f'R{i}': 0 for i in range(15)}
        self.registers['PC'] = 0
        self.flags = {'N': False, 'Z': False, 'C': False, 'V': False}
        self.memory = [0] * 1024
        self.labels = {}

    def update_flags(self, result):
        self.flags['N'] = result < 0
        self.flags['Z'] = result == 0
        self.flags['C'] = result > 0xFFFFFFFF
        self.flags['V'] = (result > 0x7FFFFFFF) or (result < -0x80000000)
    
    def check_condition_execution(self, condition):
        condition = condition[-2:].lower()
        if condition == 'eq':
            return self.flags['Z']
        elif condition == 'ne':
            return not self.flags['Z']
        elif condition == 'hi':
            return self.flags['C'] and not self.flags['Z']
        elif condition == 'ls':
            return not self.flags['C'] or self.flags['Z']
        elif condition == 'cs':
            return self.flags['C']
        elif condition == 'cc':
            return not self.flags['C']
        elif condition == 'ge':
            return self.flags['N'] == self.flags['V']
        elif condition == 'lt':
            return self.flags['N'] != self.flags['V']
        elif condition == 'mi':
            return self.flags['N']
        elif condition == 'pl':
            return not self.flags['N']
        elif condition == 'gt':
            return not self.flags['Z'] and (self.flags['N'] == self.flags['V'])
        elif condition == 'le':
            return self.flags['Z'] or (self.flags['N'] != self.flags['V'])
        elif condition == 'vs':
            return self.flags['V']
        elif condition == 'vc':
            return not self.flags['V']
        else:
            return True  # 'always' condition
    
    def check_condition_update_flags(self, condition):
        if condition[0] == 'S':
            return True
        if condition[-1] == 'S' and condition[1:] not in ['LS', 'CS', 'VS']:
            return True
        return False
    
    def is_label(self,instruction):
        if instruction.endswith(':'):
            label = instruction[:-1]
            self.labels[label] = self.registers['PC']
            self.registers['PC'] += 4
            return True
        return False
    
    def check_barrel_shift(self, instruction):
        barrel_shift_types = ['LSL', 'LSR', 'ASR', 'ROR']
        return any(shift_type in instruction for shift_type in barrel_shift_types)
            
    def execute_instruction(self, instruction):
        parts = instruction.split()
        if not self.is_label(parts[0]):
            if len(parts[0]) >= 3:
                condition = parts[0][-3:]
                update_flag = self.check_condition_update_flags(condition)
                execute = self.check_condition_execution(condition)
            else:
                execute = parts[0][0] == 'B' or parts[0][:1] == 'BL'
            if len(parts) > 4: 
                barrel = self.check_barrel_shift(parts[3])
            else:
                barrel = False
            if execute:
                if len(parts[0]) >= 3:
                    operation_name = (parts[0][:3]).title()
                    if hasattr(Operations, operation_name):
                        getattr(Operations, operation_name)(self, parts, update_flag, barrel)
                    elif hasattr(MemoryOperations, operation_name.lower()):
                        getattr(MemoryOperations, operation_name.lower())(self, parts, update_flag)
                    else:
                        print("Instrução não reconhecida.")
                        return
                else:
                    operation_name = (parts[0]).title()
                    if hasattr(JumpOperations, operation_name):
                        getattr(JumpOperations, operation_name)(self, parts)
                    else:
                        print("Instrução não reconhecida.")
                        return
                self.registers['PC'] += 4
        print("Instrução não reconhecida.")

    def print_registers(self):
        for reg, value in self.registers.items():
            print(f"{reg}: {value}")

        print("Flags:")
        for flag, value in self.flags.items():
            print(f"{flag}: {value}")

        print("Memory:")
        for i in range(32):
            for j in range(32):
                print(f"{self.memory[32*i+j]}",end='')
        print(f'')


def playground():
    simulator = ARM32Simulator()
    while True:
        instruction = input("Digite a próxima instrução (ou 'voltar' para encerrar o modo playground): ")
        
        if instruction.lower() == 'voltar':
            break
        
        simulator.execute_instruction(instruction)
        simulator.print_registers()
class MemoryOperations:
    @staticmethod
    def ldr(simulator, parts, update_flag):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução LDR.")
            return

        dest_reg = parts[1]
        address_reg = parts[2]

        if address_reg not in simulator.registers:
            print("Registrador de endereço inválido na instrução LDR.")
            return

        memory_address = simulator.registers[address_reg]
        if memory_address < 0 or memory_address >= len(simulator.memory):
            print("Endereço de memória inválido na instrução LDR.")
            return

        value = simulator.memory[memory_address]
        simulator.registers[dest_reg] = value

    @staticmethod
    def str(simulator, parts):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução STR.")
            return

        src_reg = parts[1]
        address_reg = parts[2]

        if address_reg not in simulator.registers:
            print("Registrador de endereço inválido na instrução STR.")
            return

        memory_address = simulator.registers[address_reg]
        if memory_address < 0 or memory_address >= len(simulator.memory):
            print("Endereço de memória inválido na instrução STR.")
            return

        value = simulator.registers[src_reg]
        simulator.memory[memory_address] = value
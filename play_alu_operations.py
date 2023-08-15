class Operations:
    @staticmethod
    def barrel_shift(simulator, value, shift_type, shift_amount):
        if isinstance(value, str) and value.startswith('R'):
            value = simulator.registers[value]

        if shift_type == 'LSL':
            result = value << shift_amount
        elif shift_type == 'LSR':
            result = value >> shift_amount
        elif shift_type == 'ASR':
            result = value >> shift_amount
            if value < 0:
                result |= (0xFFFFFFFF << (32 - shift_amount))
        elif shift_type == 'ROR':
            result = (value >> shift_amount) | (value << (32 - shift_amount)) & 0xFFFFFFFF
        return result

    @staticmethod
    def Add(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução ADD.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_shift = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução ADD com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_shift] if src_reg2_or_shift.startswith('R') else int(src_reg2_or_shift)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] + shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_shift] if src_reg2_or_shift.startswith('R') else int(src_reg2_or_shift)
            result = simulator.registers[src_reg1] + src_reg2
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Sub(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução SUB.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_shift = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução SUB com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_shift] if src_reg2_or_shift.startswith('R') else int(src_reg2_or_shift)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] - shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_shift] if src_reg2_or_shift.startswith('R') else int(src_reg2_or_shift)
            result = simulator.registers[src_reg1] - src_reg2
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)
            
    @staticmethod
    def And(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução AND.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução AND com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] & shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] & src_reg2
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Rsb(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução RSB.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução RSB com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = shifted_value - simulator.registers[src_reg1]
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = src_reg2 - simulator.registers[src_reg1]
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Adc(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução ADC.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        carry = 1 if simulator.flags['C'] else 0
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução ADC com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] + shifted_value + carry
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] + src_reg2 + carry
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Sbc(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução SBC.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        carry = 1 if simulator.flags['C'] else 0
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução SBC com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] - shifted_value - carry
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] - src_reg2 - carry
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Rsc(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução RSC.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        carry = 1 if simulator.flags['C'] else 0
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução RSC com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = shifted_value - simulator.registers[src_reg1] - carry
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = src_reg2 - simulator.registers[src_reg1] - carry
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Tst(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução TST.")
            return
        
        src_reg1 = parts[1]
        src_reg2_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução TST com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] & shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] & src_reg2
        
        simulator.update_flags(result)

    @staticmethod
    def Teq(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução TEQ.")
            return
        
        src_reg1 = parts[1]
        src_reg2_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução TEQ com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] ^ shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] ^ src_reg2
        
        simulator.update_flags(result)

    @staticmethod
    def Cmp(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução CMP.")
            return
        
        src_reg1 = parts[1]
        src_reg2_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução CMP com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] - shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] - src_reg2
        
        simulator.update_flags(result)

    @staticmethod
    def Cmn(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução CMN.")
            return
        
        src_reg1 = parts[1]
        src_reg2_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução CMN com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] + shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] + src_reg2
        
        simulator.update_flags(result)

    @staticmethod
    def Orr(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução ORR.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução ORR com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] | shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] | src_reg2
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Mov(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução MOV.")
            return
        
        dest_reg = parts[1]
        src_reg_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução MOV com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg_or_imm] if src_reg_or_imm.startswith('R') else int(src_reg_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = shifted_value
        else:
            result = simulator.registers[src_reg_or_imm] if src_reg_or_imm.startswith('R') else int(src_reg_or_imm)
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Bic(simulator, parts, update_flag, barrel):
        if len(parts) < 4:
            print("Erro de sintaxe na instrução BIC.")
            return
        
        dest_reg = parts[1]
        src_reg1 = parts[2]
        src_reg2_or_imm = parts[3]
        
        if barrel:
            if len(parts) < 6:
                print("Erro de sintaxe na instrução BIC com deslocamento barrel.")
                return
            
            shift_type = parts[4]
            shift_amount = int(parts[5][1:])
            
            value = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = simulator.registers[src_reg1] & ~shifted_value
        else:
            src_reg2 = simulator.registers[src_reg2_or_imm] if src_reg2_or_imm.startswith('R') else int(src_reg2_or_imm)
            result = simulator.registers[src_reg1] & ~src_reg2
        
        simulator.registers[dest_reg] = result
        if update_flag:
            simulator.update_flags(result)

    @staticmethod
    def Mvn(simulator, parts, update_flag, barrel):
        if len(parts) < 3:
            print("Erro de sintaxe na instrução MVN.")
            return
        
        dest_reg = parts[1]
        src_reg_or_imm = parts[2]
        
        if barrel:
            if len(parts) < 5:
                print("Erro de sintaxe na instrução MVN com deslocamento barrel.")
                return
            
            shift_type = parts[3]
            shift_amount = int(parts[4][1:])
            
            value = simulator.registers[src_reg_or_imm] if src_reg_or_imm.startswith('R') else int(src_reg_or_imm)
            shifted_value = Operations.barrel_shift(simulator, value, shift_type, shift_amount)
            result = ~shifted_value
        else:
            result = ~ (simulator.registers[src_reg_or_imm] if src_reg_or_imm.startswith('R') else int(src_reg_or_imm))
        
        simulator.registers[dest_reg] = result
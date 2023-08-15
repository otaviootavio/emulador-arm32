class JumpOperations:
    @staticmethod
    def b(simulator, parts):
        if len(parts) < 2:
            print("Erro de sintaxe na instrução B.")
            return
        
        label = parts[1]
        
        if label in simulator.labels:
            target_address = simulator.labels[label]
            simulator.registers['PC'] = target_address
        else:
            print("Rótulo de destino não encontrado na instrução B.")
    
    @staticmethod
    def bl(simulator, parts):
        if len(parts) < 2:
            print("Erro de sintaxe na instrução BL.")
            return
        
        label = parts[1]
        
        if label in simulator.labels:
            target_address = simulator.labels[label]
            simulator.registers['R14'] = simulator.registers['PC'] + 4
            simulator.registers['PC'] = target_address
        else:
            print("Rótulo de destino não encontrado na instrução BL.")
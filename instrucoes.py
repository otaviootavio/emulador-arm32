instructions = [
    [
        "Instruções de transferência de dados:",
        [
            "MOV",
            "A instrução MOV (move) tem como função copiar o conteúdo do operando Y para X",
            "1101",
            "MOV X, Y",
            [
                "X: Registrador destino",
                "Y: Registrador ou valor imediato",
            ],
        ],
        [
            "LDR",
            "Carrega o valor do endereço Y para o registrador X",
            "",
            "LDR X, [Y]",
            ["X: Registrador destino", "Y: Endereço de memória"],
        ],
        [
            "STR",
            "Armazena o valor do registrador X no endereço Y",
            "",
            "STR X, [Y]",
            ["X: Registrador fonte", "Y: Endereço de memória"],
        ],
    ],
    [
        "Instruções aritméticas e lógicas:",
        [
            "AND",
            "A instrução AND realiza a operação lógica AND bit a bit entre os operandos Y e Z, armazenando o valor em X",
            "0000",
            "AND X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "EOR",
            "A instrução EOR realiza a operação lógica OR bit a bit entre os operandos",
            "0001",
            "EOR X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "SUB",
            "A instrução SUB realiza a operação de subtração do operando Y pelo operando Z, armazenando o valor em X (X = Y - Z)",
            "0010",
            "SUB X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador (Minuendo)",
                "Z: Registrador ou valor imediato (Subtraendo)",
            ],
        ],
        [
            "RSB",
            "A instrução RSB realiza a operação de subtração do operando Z pelo operando Y, armazenando o valor em X (X = Z - Y)",
            "0011",
            "RSB X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador (Subtraendo)",
                "Z: Registrador ou valor imediato (Minuendo)",
            ],
        ],
        [
            "ADD",
            "A instrução ADD realiza a operação de adição entre os operandos Y e Z, armazenando o resultado em X",
            "0100",
            "ADD X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "ADC",
            "A instrução ADC (add with carry) soma os operandos Y e Z juntamente com o valor da flag de carry, armazenando o resultado em X",
            "0101",
            "ADC X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "SBC",
            "A instrução SBC (subtract with carry) subtrai o operando Z de Y, levando em consideração a flag de carry, e armazena o resultado em X",
            "0110",
            "SBC X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "RSC",
            "A instrução RSC (reverse subtract with carry) subtrai Y de Z, considerando a flag de carry, e armazena o resultado em X",
            "0111",
            "RSC X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "TST",
            "A instrução TST testa os bits dos operandos X e Y realizando uma operação AND bit a bit, mas não armazena o resultado, apenas atualiza as flags",
            "1000",
            "TST X, Y",
            [
                "X: Registrador",
                "Y: Registrador ou valor imediato",
            ],
        ],
        [
            "TEQ",
            "A instrução TEQ compara os operandos X e Y realizando uma operação XOR bit a bit, sem armazenar o resultado, apenas atualiza as flags",
            "1001",
            "TEQ X, Y",
            [
                "X: Registrador",
                "Y: Registrador ou valor imediato",
            ],
        ],
        [
            "CMP",
            "A instrução CMP compara os operandos X e Y realizando uma subtração, sem armazenar o resultado, mas atualizando as flags",
            "1010",
            "CMP X, Y",
            [
                "X: Registrador",
                "Y: Registrador ou valor imediato",
            ],
        ],
        [
            "CMN",
            "A instrução CMN compara os operandos X e Y realizando uma adição, sem armazenar o resultado, mas atualizando as flags",
            "1011",
            "CMN X, Y",
            [
                "X: Registrador",
                "Y: Registrador ou valor imediato",
            ],
        ],
        [
            "ORR",
            "A instrução ORR realiza a operação lógica OR bit a bit entre os operandos Y e Z, armazenando o resultado em X",
            "1100",
            "ORR X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BIC",
            "A instrução BIC (bit clear) realiza uma operação AND bit a bit entre Y e o complemento de Z, armazenando o resultado em X",
            "1110",
            "BIC X, Y, Z",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "MVN",
            "A instrução MVN (move not) copia o complemento do operando Y para X",
            "1111",
            "MVN X, Y",
            [
                "X: Registrador destino",
                "Y: Registrador ou valor imediato",
            ],
        ],
    ],
    [
        "Instruções de controle de fluxo:",
        [
            "B",
            "A instrução B (branch) desvia a execução para um novo endereço especificado",
            "",
            "B LABEL",
            [
                "LABEL: Endereço ou etiqueta de destino",
            ],
        ],
        [
            "BEQ",
            "A instrução BEQ (branch if equal) desvia a execução para um novo endereço se a condição de igualdade for verdadeira",
            "",
            "BEQ LABEL_EQUAL",
            [
                "LABEL_EQUAL: Endereço ou etiqueta de destino quando a condição for satisfeita",
            ],
        ],
        [
            "BNE",
            "A instrução BNE (branch if not equal) desvia a execução para um novo endereço se a condição de igualdade for falsa",
            "",
            "BNE LABEL_NOT_EQUAL",
            [
                "LABEL_NOT_EQUAL: Endereço ou etiqueta de destino quando a condição não for satisfeita",
            ],
        ],
        [
            "BL",
            "A instrução BL (branch with link) desvia a execução para um novo endereço e armazena o endereço de retorno no link register",
            "",
            "BL FUNCTION_CALL",
            [
                "FUNCTION_CALL: Endereço ou etiqueta da função ou rotina a ser chamada",
            ],
        ],
        [
            "BX",
            "A instrução BX (branch and exchange) desvia a execução para um novo endereço e muda o modo de execução (ARM ou Thumb)",
            "",
            "BX rX",
            [
                "rX: Registrador contendo o endereço de destino",
            ],
        ],
    ],
]

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
        ["LDR", "", "0000", "", ["", ""]],
        ["STR", "", "0000", "", ["", ""]],
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
            "",
            "0100",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "ADC",
            "",
            "0101",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "SBC",
            "",
            "0110",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "RSC",
            "",
            "0111",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "TST",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "TEQ",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "CMP",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "CMN",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "ORR",
            "",
            "1100",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BIC",
            "",
            "1100",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "MVN",
            "",
            "1100",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
    ],
    [
        "Instruções de controle de fluxo:",
        [
            "B",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BEQ",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BNE",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BL",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
        [
            "BX",
            "",
            "0000",
            "",
            [
                "X: Registrador destino",
                "Y: Registrador",
                "Z: Registrador ou valor imediato",
            ],
        ],
    ],
]


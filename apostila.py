from instrucoes import instructions
from funcoes import formattedPrint, bodyPrint


# Função que converte uma letra do alfabeto para o index correspondente
def adaptLetterToIndex(letter):
    return ord(letter.capitalize()) - ord("A")


def apostila():
    formattedPrint("Modo 1 - Apostila", True)

    runApostila = True
    while runApostila:
        print("Lista de instruções disponíveis para consulta")
        print()
        for i in range(len(instructions)):
            print(f"Conjunto {chr(i + ord('A'))} - {instructions[i][0]}")
            for j in range(1, len(instructions[i])):
                print(f"{j} - {instructions[i][j][0]}")
            formattedPrint()

        lastSectionLetter = chr(ord("A") + len(instructions) - 1)
        isInvalidLetter = True

        while isInvalidLetter:
            groupCode = str(
                input(
                    f"Selecione o código do conjunto de instruções [A - {lastSectionLetter}]: "
                )
            )
            isInvalidLetter = not (
                groupCode.isalpha() and groupCode.capitalize() <= lastSectionLetter
            )
            if isInvalidLetter:
                print("Código inválido. Tente novamente...")

        groupIndex = adaptLetterToIndex(groupCode)
        lastInstructionNumber = len(instructions[groupIndex]) - 1
        isInvalidNumber = True
        while isInvalidNumber:
            instructionCode = str(
                input(
                    f"Selecione o código da instrução [1 - {lastInstructionNumber}]: "
                )
            )
            if instructionCode.isdigit():
                instructionCode = int(instructionCode)
                isInvalidNumber = instructionCode > lastInstructionNumber
            if isInvalidNumber:
                print("Código inválido. Tente novamente...")

        selectedInstruction = instructions[groupIndex][instructionCode]
        formattedPrint(f"Informações sobre a função {selectedInstruction[0]}", True)
        bodyPrint(selectedInstruction[1])
        print()
        if selectedInstruction[2] != "":
            print(f"OPCode: {selectedInstruction[2]}")
        print(f"Sintaxe: {selectedInstruction[3]}")
        print()
        for operando in selectedInstruction[4]:
            print(operando)
        formattedPrint()

        while True:
            print("1 - Consultar informações sobre outra instrução")
            print("2 - Voltar para o menu inicial")
            userChoice = str(input("O que você deseja fazer agora? "))
            if userChoice == "1":
                break
            elif userChoice == "2":
                runApostila = False
                break
            else:
                print("Entrada inválida. Tente novamente!")

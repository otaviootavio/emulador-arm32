from funcoes import formattedPrint
from apostila import apostila
from playground import playground


def main():
    formattedPrint("PCS3732 - Laboratório de Processadores", True)
    print("Emulador ARM - Desenvolvido por")
    print("11322900 | Lucas Alexandre Tavares")
    print("11808130 | Otávio Vacari Martins ")
    print("11262233 | Silas Lima e Silva")
    formattedPrint()

    isClosing = False
    while not (isClosing):
        print("Modos disponíveis:")
        print("1 - Apostila")
        print("2 - Playground")
        print("X - Encerrar execução do programa")
        mode = str(input("Selecione o modo de execução: "))
        if mode == "1":
            apostila()
        elif mode == "2":
            playground()
        elif mode.capitalize() == "X":
            isClosing = True
        else:
            print("Modo inválido. Tente novamente!")


main()

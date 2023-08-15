### DEFINIÇÃO FUNÇÕES ###


# Função para imprimir formatado
def formattedPrint(text="=" * 140, containerMode=False):
    if containerMode:
        print("=" * 140)
        print(f"{text:^140}")
        print("=" * 140)
    else:
        print(f"{text:^140}")


# Função para imprimir textos longos no container definido
def bodyPrint(syntax: str):
    syntaxWords = syntax.split()
    charactersCount = 0
    for word in syntaxWords:
        charactersCount += len(word) + 1
        if charactersCount > 140:
            charactersCount = len(word) + 1
            print()
        print(word, end=" ")
    print()

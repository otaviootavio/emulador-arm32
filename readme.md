## 1. Objetivo
Nosso projeto tem como principal objetivo facilitar o aprendizado básico do usuário sobre as instruções ARM32. Para isso, nosso grupo buscou abordar tanto a parte teórica, quanto a parte prática. Na próxima seção, detalharemos cada abordagem.

## 2. Implementação
O desenvolvimento do projeto foi feito inteiramente em Python3, buscando principalmente aproveitar a praticidade da linguagem para que a implementação do nosso projeto e eventuais updates sejam feitos de maneira simples e eficiente. 

A execução do projeto é feita diretamente no terminal, onde buscamos atingir um visual mais semelhante ao que geralmente é encontrado quando vamos programar em assembly. Apesar de representar uma simplificação (comparado a um eventual desenvolvimento de telas), pensamos na experiência do usuário neste caso, criando um menu com inputs para selecionar dentre as opções disponíveis e tratamento de erros para evitar inputs inválidos.

### 2.1. Modo 1 - Apostila
Neste primeiro modo, listamos as principais instruções de ARM32, tais como as seguintes informações que julgamos necessárias:

- Mnemônico da instrução
- Descrição da instrução
- OPCode (quando aplicável)
- Sintaxe da instrução
- Explicação de cada operando utilizado na instrução

Como próximos passos para nosso projeto, vemos tanto a possibilidade de adicionar novas instruções dentro do nosso arquivo instrucoes.py, como também adicionar mais informações a respeito das instruções.

#### 2.1.1. Instruções disponíveis para consulta
Instruções de transferência de dados
- MOV
- LDR
- STR

Instruções aritméticas e lógicas

- AND
- EOR
- SUB
- RSB
- ADD
- ADC
- SBC
- RSC
- TST
- TEQ
- CMP
- CMN
- ORR
- BIC
- MVN

Instruções de controle de fluxo
- B
- BEQ
- BNE
- BL
- BX

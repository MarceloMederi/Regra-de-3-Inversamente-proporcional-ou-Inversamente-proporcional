#A regra de três, na matemática, é uma forma de se descobrir uma quantidade 
#que tenha para outra conhecida a mesma relação que têm entre si entre outros dois valores numéricos conhecidos.
# O codigo a seguir ajudara a calcular Grandezas diretamente proporcionais simples 
# e "Grandezas inversamente proporcionais simples "

import time

def opcao():
    print (" REGRA DE TRÊS DIRETAMENTE PROPORCIONAL SIMPLES             REGRA DE TRÊS INVERSAMENTE PROPORCIONAL SIMPLES")
    print("-" * 110)
    print("  A   B         Multiplica Cruzado                  |         A   B          Multiplica na mesma ")
    print(" -- X --         os valores.                        |         --> --         linha na horizontal.")
    print("  C   X                                             |         C   X                              ")
    print("-" * 110)

def regra1():

    A = float(input("Informe o valaor de A : \n"))
    B = float(input("Assim A esta B. Informe o Valor de B: \n"))
    C = float(input("Informe o valor de C: \n"))
    print("Vamos calcular o valor de X.")
    print("\n")

    time.sleep(3)

    print(A, "X", "=", B ,".", C)
    valor4 =(float(B * C))
    print(A, "X = " , valor4)
    X = float(valor4 / A)
    print("O valor de X é = ", X)
    time.sleep(4)

def regra2():
    A = float(input("Informe o valaor de A : \n"))
    B = float(input("Assim A esta B. Informe o Valor de B: \n"))
    C = float(input("Informe o valor de C: \n"))
    print("Vamos calcular o valor de X.")
    print("\n")

    time.sleep(3)

    print(A * B , C , "." , "X")
    valor4 =(float(A * B))
    print(C, "X = " , valor4)
    X = float(valor4 / C)
    print("O valor de X é = ", X)
    time.sleep(4)

escolha = 0

while escolha != "1" and "2":
    opcao()
    escolha = str(int(input("Escolha qual regra de Três voce gostaria de Usar'\n'[1- DIRETAMENTE PROPORCIONAL SIMPLES / 2- INVERSAMENTE PROPORCIONAL SIMPLES]:")))
    if escolha == 1:
        print("")
        regra1()
        print("")
    elif escolha == 2:
        print("")
        regra2()
        print("")
    else:
        print("Opção Invalida! Escolha entre as opçôes acima.")
        print("")


lista = []

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero >= 0:
            lista.append(numero)
        else:
            print ("Não é permitido números negativos, finalizando código...")
            break
        print ("Deseja continuar inserindo números? (Não = 0 | Sim = 1)")
        pergunta = int(input("Digite sua escolha: "))
        if pergunta == 0:
            print ("Finalizando código...")
            break
        elif pergunta == 1:
            print ("Que bom que continua a inserir números dentro da lista.")
            print (f"Quantidade de números na lista: {len(lista)}")
            print (f"{lista}")
            pass
        else:
            print (f"Opção {pergunta} desconhecida, finalizando código...")
            break
    except Exception:
        print ("Apenas números inteiros são permitidos, refaça a operação.")
        
print (f"A quantidade de números dentro da lista é {len(lista)}.")
print (lista)

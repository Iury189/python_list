# Criando uma lista vazia
lista = []
# Enquanto o loop for True sempre estará funcionando
while True:
    try:
        print ("Deseja inserir números na lista? (Não = 0 | Sim = 1)")
        comecar = int(input("Digite sua resposta: "))
        # Caso o usuário encerre o código sem inserir números o código se encerra
        if comecar == 0:
            print ("Se não deseja inserir números na lista o código será finalizado.\n")
            break
        # Caso digite uma opção inválida o código se encerra
        elif comecar != 1:
            print (f"Opção {comecar} inválida, o código será finalizado.\n")
            break
        # Caso o usuário queira
        else:
            numero = int(input("Digite um número inteiro: "))
            # Caso seja maior que zero o número é armazenado
            if numero >= 0:
                lista.append(numero)
            # Caso não seja o código se encerra
            else:
                print ("Não é permitido números negativos, finalizando código...\n")
                break
            # Pergunta se quer continuar a inserir números
            print ("Deseja continuar inserindo números? (Não = 0 | Sim = 1)")
            pergunta = int(input("Digite sua escolha: "))
            # Caso seja não o código se encerra
            if pergunta == 0:
                print ("Finalizando código... \n")
                break
            # Caso a resposta seja sim começa novamente o processo de inserção de números
            elif pergunta == 1:
                print ("Que bom que continua a inserir números dentro da lista.")
                print (f"Quantidade de números na lista: {len(lista)}")
                print (lista)
                pass
            # Caso digite uma opção inválida o código se encerra
            else:
                print (f"Opção {pergunta} desconhecida, finalizando código... \n")
                break
    # Caso o usuário digite uma opção inválida
    except Exception:
        print ("Apenas números são permitidos, finalizando código... \n")
        break
# Mensagem
print (f"A quantidade de números dentro da lista é {len(lista)}.")
print (lista)
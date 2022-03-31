# Criando uma lista vazia
lista = []
# Enquanto o loop for True sempre estará funcionando
while True:
    try:
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
        # Caso a resposta seja NÃO o código se encerra
        if pergunta == 0:
            print ("Finalizando código... \n")
            break
        # Caso a resposta seja SIM começa novamente o processo de inserção de números
        elif pergunta == 1:
            print ("Que bom que continua a inserir números dentro da lista.")
            print (f"Quantidade de números na lista: {len(lista)}")
            print (f"{lista}\n")
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

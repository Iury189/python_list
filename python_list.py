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
            print ("Não é permitido números negativos, finalizando código...")
            break
        # Pergunta se quer continuar a inserir números
        print ("Deseja continuar inserindo números? (Não = 0 | Sim = 1)")
        pergunta = int(input("Digite sua escolha: "))
        # Caso a resposta seja NÃO o código se encerra
        if pergunta == 0:
            print ("Finalizando código...")
            break
        # Caso a resposta seja SIM começa novamente o processo de inserção de números
        elif pergunta == 1:
            print ("Que bom que continua a inserir números dentro da lista.")
            print (f"Quantidade de números na lista: {len(lista)}")
            print (f"{lista}")
            pass
        # Caso digite uma opção inválida o código se encerra
        else:
            print (f"Opção {pergunta} desconhecida, finalizando código...")
            break
    # Caso o usuário não digite um número inteiro
    except Exception:
        print ("Apenas números inteiros são permitidos, refaça a operação.")
# Mensagem
print (f"A quantidade de números dentro da lista é {len(lista)}.")
print (lista)

tarefas = []

while True:
    print("\n1-Adicionar  2-Listar  3-Sair")
    op = input("Escolha: ")

    if op == "1":
        t = input("Tarefa: ")
        tarefas.append(t)

    elif op == "2":
        for i, t in enumerate(tarefas):
            print(i+1, "-", t)

    elif op == "3":
        break

    else:
        print("Erro")

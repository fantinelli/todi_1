class DaoAdicionarTarefa():
    def __init__(self, tarefa):
        with open("tarefas.txt", "w") as arquivo:
            arquivo.write(tarefa + "\n")
            print("Tarefa adicionada ao DAO.")

class DaoExcluirTarefa():
    def __init__(self, excluir):
         with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            linhas.pop(int(excluir) - 1)
            with open("tarefas.txt", "w") as arquivo:
                arquivo.writelines(linhas)
                print("Tarefa removida do DAO.")

class DaoListarTarefa():
    def __init__(self):
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            cont = 0
            for tarefas in linhas:
                cont += 1
                print(f"{cont}. {tarefas}")
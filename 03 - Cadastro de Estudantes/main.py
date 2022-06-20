import os


class Aluno:
    """ Classe Aluno """
    def __init__(self, nome: str, curso: str):
        """Inicialização

        Args:
            nome (str): Nome do aluno
            curso (str): Nome do curso
        """
        self.nome = nome
        self.curso = curso

# Variáveis globais
lista_estados = ["RS", "SC", "SP", "RJ", "MG"]
lista_cursos = ["ADS", "RDS", "PMM", "SPI"]

dic_estudantes = {estado: [] for estado in lista_estados}

menu = {
    0: "Sair",
    1: "Catalogar Aluno",
    2: "Imprimir Alunos por Estado",
    3: "Imprimir Alunos por Curso",
    4: "Localizar um Aluno por nome"
}


def imprimeMenu():
    """ Imprime o menu do programa """
    for key in menu.keys():
        print(f"{key} - {menu[key]}")


def catalogarAluno():
    """Cadastra um novo aluno"""
    
    limparTela()
    print("Catalogar Aluno\n")

    # Inserir nome do aluno
    nome_aluno = inputAluno()

    # Seleciona o estado
    estado_selecionado = selecionarEstado()
    if estado_selecionado == 0:
        return

    # Seleciona o curso
    curso_selecionado = selecionarCurso()
    if curso_selecionado == 0:
        return

    # Instancia um novo aluno
    novoAluno = Aluno(nome_aluno, curso_selecionado)
    
    # Adiciona o aluno na lista de alunos do estado
    dic_estudantes[estado_selecionado].append(novoAluno)

    # Imprime os dados do aluno criado
    print("\nAluno catalogado com sucesso.")
    print(f"Nome: {novoAluno.nome}")
    print(f"Estado: {estado_selecionado}")
    print(f"Curso: {novoAluno.curso}")

    teclarParaContinuar()


def imprimirAlunosEstado():
    """Imprime a lista de Alunos por Estado"""
    
    limparTela()
    print("Imprimir Alunos por Estado\n")

    # Seleciona o estado
    estado_selecionado = selecionarEstado()
    if estado_selecionado == 0:
        return

    print(f"\nAlunos do estado {estado_selecionado}:")

    # Verifica se há alunos, se sim imprime a lista de alunos
    if len(dic_estudantes[estado_selecionado]) == 0:
        print("\nNenhum aluno cadastrado.")
    else:
        # Cabeçalho
        print(f"{'-'*10:<10} | {'-'*10:<10}")
        print(f"{'Nome':<10} | {'Curso':<10}")
        print(f"{'-'*10:<10} | {'-'*10:<10}")

        # Alunos
        for aluno in dic_estudantes[estado_selecionado]:
            print(f"{aluno.nome:<10} | {aluno.curso:<10}")

    teclarParaContinuar()


def imprimirAlunosCurso():
    """Imprime a lista de Alunos por Curso"""

    limparTela()
    print("Imprimir Alunos por Curso\n")

    # Seleciona o curso
    curso_selecionado = selecionarCurso()
    if curso_selecionado == 0:
        return

    print(f"\nAlunos do curso {curso_selecionado}:")

    # Variável para armazenar os alunos encontrados
    alunos_encontrados = []

    # Percorre o dicionário de estudantes identificando o curso
    # de cada aluno
    for estado in dic_estudantes:
        for aluno in dic_estudantes[estado]:
            # Se o curso do aluno for igual ao curso selecionado
            # adiciona o aluno à lista de alunos encontrados
            if aluno.curso == curso_selecionado:
                alunos_encontrados.append(aluno)

    # Verifica se a lista possui alunos, se sim, imprime a lista de alunos
    if len(alunos_encontrados) == 0:
        print("\nNenhum aluno cadastrado.")
    else:
        # Cabeçalho
        print(f"{'-'*10:<10} | {'-'*10:<10}")
        print(f"{'Nome':<10} | {'Curso':<10}")
        print(f"{'-'*10:<10} | {'-'*10:<10}")
        
        # Alunos
        for aluno in alunos_encontrados:
            print(f"{aluno.nome:<10} | {aluno.curso:<10}")

    teclarParaContinuar()


def localizarAluno():
    """Localiza um aluno pelo Nome"""
    
    limparTela()
    print("Localizar Aluno\n")

    # Insere o nome do aluno
    nome_aluno = inputAluno()
    
    # Variável para identificar se encontrou aluno
    encontrou = False

    # Percorre o dicionário de estudantes comparando o nome de cada aluno
    # com o nome informado
    for estado in dic_estudantes:
        for aluno in dic_estudantes[estado]:
            
            if str.lower(aluno.nome) == str.lower(nome_aluno):
                encontrou = True

                # Cabeçalho
                print(f"{'-'*10:<10} | {'-'*10:<10} | {'-'*6:<6}")
                print(f"{'Nome':<10} | {'Curso':<10} | {'Estado':<6}")
                print(f"{'-'*10:<10} | {'-'*10:<10} | {'-'*6:<6}")

                # Aluno
                print(f"{aluno.nome:<10} | {aluno.curso:<10} | {estado:<8}")

                teclarParaContinuar()

    # Se não encontrou, imprime mensagem 
    if not encontrou:
        print("\nAluno não encontrado.")
        teclarParaContinuar()


def limparTela():
    """Executa o comando para limpar o terminal"""
    os.system("cls")


def teclarParaContinuar():
    """Executa o comando que pausa o terminal"""
    print("")
    os.system("pause")


def inputAluno():
    """Solicita e retorna o nome do aluno"""
    while True:
        try:
            nome_aluno = input("Digite o nome do aluno: ")
            
            if nome_aluno.strip() == "":
                print("Nome não pode ser vazio.")
            else:
                return nome_aluno
            
        except ValueError:
            print("Digite um nome válido.")


def selecionarEstado():
    """Solicita e retorna o Estado selecionado"""
    
    print("\nEscolha um Estado:")
    
    # Imprime as opções
    print("0 - Sair")
    for i in range(0, len(lista_estados)):
        print(f"{i+1} - {lista_estados[i]}")

    while True:
        try:
            escolha = int(input("Escolha: "))

            if escolha == 0:
                return escolha
            elif escolha > len(lista_estados) or escolha < 0:
                print("Estado inválido.")
            else:
                estado_selecionado = lista_estados[escolha-1]
                return estado_selecionado

        except ValueError:
            print("Estado inválido.")


def selecionarCurso():
    """Solicita e retorna o Curso selecionado"""
    
    print("\nEscolha um Curso:")
    
    # Imprime as opções
    print("0 - Sair")    
    for i in range(0, len(lista_cursos)):
        print(f"{i+1} - {lista_cursos[i]}")

    while True:
        try:
            escolha = int(input("\nEscolha: "))

            if escolha == 0:
                return escolha
            elif escolha > len(lista_cursos) or escolha < 0:
                print("Curso inválido.")
            else:
                curso_selecionado = lista_cursos[escolha-1]
                return curso_selecionado

        except ValueError:
            print("Curso inválido.")


if __name__ == '__main__':

    while True:
        limparTela()
        imprimeMenu()

        while True:
            escolha = ''
            try:
                escolha = int(input("Escolha: "))

                if   escolha == 0: exit()
                elif escolha == 1: catalogarAluno()
                elif escolha == 2: imprimirAlunosEstado()
                elif escolha == 3: imprimirAlunosCurso()
                elif escolha == 4: localizarAluno()
                else:
                    print("Opção inválida.")
                    
                break
            except ValueError:
                print("Opção inválida.")

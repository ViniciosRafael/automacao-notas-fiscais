import timeit

# Classe que implementa uma tabela hash para indexação rápida de nós
class TabelaHash:
    def __init__(self, tamanho):
        # Define o tamanho da tabela e cria uma lista de 'tamanho' posições, todas vazias
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
 
    def funcao_hash(self, valor):
        # Calcula o índice na tabela / metódo resto da divisão
        return int(valor) % self.tamanho
 
    def inserir(self, valor, no):
        # Calcula o índice para inserir o valor
        indice = self.funcao_hash(valor)
        # Tratamento de colisão por encadeamento: se a posição estiver vazia, cria uma lista
        # Caso contrário, adiciona à lista existente (permite múltiplos valores no mesmo índice)
        if self.tabela[indice] is None: # Se a posição ainda está vazia, inicializa com uma lista vazia
            self.tabela[indice] = []
        self.tabela[indice].append((valor, no))
 
    def buscar(self, valor):
        # Calcula o índice esperado para o valor buscado
        indice = self.funcao_hash(valor)
        if self.tabela[indice] is not None:
            for chave, no in self.tabela[indice]:
                if chave == valor:
                    return no # Retorna o nó correspondente à chave
        return None
 
    def remover(self, valor):
        # Calcula o índice e remove o par (chave, nó) correspondente
        indice = self.funcao_hash(valor)
        if self.tabela[indice] is not None:
            self.tabela[indice] = [(c, n) for c, n in self.tabela[indice] if c != valor]
 
 # Classe que representa um nó (filme) da lista
class No:
    def __init__(self, titulo, diretor, ano, genero):
        # Inicializa os atributos do filme
        self.id = id(self)
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.genero = genero
        self.proximo = None # Ponteiro para o próximo nó
 
    def mostrar_no(self): # Exibe os dados do filme de forma formatada
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")
 
 
class CatalogoFilmes:
    def __init__(self, tamanho_hash=1000):
        # Inicializa a lista ligada e a tabela hash
        self.primeiro = None
        self.hash = TabelaHash(tamanho_hash)
 
    def povoar_catalogo(self, quantidade=1000):
        # Preenche o catálogo com filmes de exemplo para teste
        for i in range(1, quantidade + 1):
            titulo = f"Filme Exemplo {i}"
            diretor = f"Diretor {i}"
            ano = str(1900 + (i % 125))
            genero = "Gênero de Teste"
            self.Incluir(titulo, diretor, ano, genero)
        print("Carga de dados finalizada!")
 
    def Incluir(self, titulo, diretor, ano, genero):
        # Cria um novo nó para o filme e o adiciona ao final da lista ligada
        novo_filme = No(titulo, diretor, ano, genero)
        if self.primeiro is None:
            self.primeiro = novo_filme
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_filme
        self.hash.inserir(novo_filme.id, novo_filme)
        #print("Filme incluído com sucesso!")
 
    def Excluir(self, titulo, diretor):
        # Percorre a lista para encontrar e remover o filme pelo título e diretor
        atual = self.primeiro
        anterior = None
        while atual is not None:
            if atual.titulo == titulo and atual.diretor == diretor:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.hash.remover(atual.id)
                print("Filme excluído com sucesso!")
                return
            anterior = atual
            atual = atual.proximo
        print("Filme não encontrado.")
 
    # SEM print aqui — só retorna o nó
    def Pesquisar(self, titulo, diretor):
        # Percorre a lista ligada para encontrar o filme pelo título e diretor
        atual = self.primeiro
        while atual is not None:
            if atual.titulo == titulo and atual.diretor == diretor:
                return atual
            atual = atual.proximo
        return None
 
    def Relatorio(self):
        # Exibe um relatório completo de todos os filmes no catálogo
        if self.primeiro is None:
            print("Nenhum filme cadastrado no catálogo.")
            return
        print("=" * 40)
        print("       CATÁLOGO DE FILMES")
        print("=" * 40)
        atual = self.primeiro
        contador = 1
        while atual is not None:
            print(f"\nFilme #{contador}")
            print("-" * 40)
            atual.mostrar_no()
            atual = atual.proximo
            contador += 1
        print("=" * 40)
        print(f"Total de filmes: {contador - 1}")
 
 
def menu():
    # Função principal que executa o menu interativo para gerenciar o catálogo de filmes
    catalogo = CatalogoFilmes()
    catalogo.povoar_catalogo(1000)
 
    while True:
        # Exibe o menu de opções
        print("\n" + "=" * 40)
        print("      CATÁLOGO DE FILMES")
        print("=" * 40)
        print("1 - Incluir filme")
        print("2 - Excluir filme")
        print("3 - Pesquisar filme")
        print("4 - Relatório")
        print("5 - Função Hash")
        print("0 - Sair")
        print("=" * 40)
 
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "1":
            # Opção para incluir um novo filme
            print("\n--- INCLUIR FILME ---")
            titulo = input("Título: ").strip()
            diretor = input("Diretor: ").strip()
            ano = input("Ano: ").strip()
            genero = input("Gênero: ").strip()
            tempo = timeit.timeit(lambda: catalogo.Incluir(titulo, diretor, ano, genero), number=1)
            print(f"Tempo de execução: {tempo:.6f} segundos")
 
        elif opcao == "2":
            # Opção para excluir um filme
            print("\n--- EXCLUIR FILME ---")
            titulo = input("Título do filme a excluir: ").strip()
            diretor = input("Diretor do filme: ").strip()
            tempo = timeit.timeit(lambda: catalogo.Excluir(titulo, diretor), number=1)
            print(f"Tempo de execução: {tempo:.6f} segundos")
 
        elif opcao == "3":
            # Opção para pesquisar um filme
            print("\n--- PESQUISAR FILME ---")
            titulo = input("\nTítulo: ").strip()
            diretor = input("Diretor: ").strip()
            tempo = timeit.timeit(lambda: catalogo.Pesquisar(titulo, diretor), number=1)
            no = catalogo.Pesquisar(titulo, diretor)
            if no is not None:
                print("\nFilme encontrado:\n")
                no.mostrar_no()
            else:
                print("Filme não encontrado.")
            print(f"Tempo de execução: {tempo:.6f} segundos")
 
        elif opcao == "4":
            # Opção para gerar relatório de todos os filmes
            print()
            tempo = timeit.timeit(lambda: catalogo.Relatorio(), number=1)
            print(f"Tempo de execução: {tempo:.6f} segundos")
 
        elif opcao == "5":
            # Opção para buscar filme pela tabela hash usando ID
            print("\n--- FUNÇÃO HASH ---")
            filme_id = input("Digite o ID do filme para buscar: ").strip()
            tempo = timeit.timeit(lambda: catalogo.hash.buscar(int(filme_id)), number=1)
            no = catalogo.hash.buscar(int(filme_id))
            if no is not None:
                print(f"Filme encontrado: {no.titulo}")
            else:
                print("ID não encontrado na tabela hash.")
            print(f"Tempo de execução: {tempo:.6f} segundos")
 
        elif opcao == "0":
            # Opção para sair do programa
            print("\nSaindo... Até logo!")
            break
 
        else:
            # Opção inválida
            print("\nOpção inválida. Tente novamente.")
 
 
menu()  # Inicia o programa executando o menu principal
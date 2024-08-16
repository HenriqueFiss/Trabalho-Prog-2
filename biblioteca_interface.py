class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        
    def remover_livro(self, livro):
        self.livros.remove(livro)
    
    def listar_livros(self):
        return self.livros

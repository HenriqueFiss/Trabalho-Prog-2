import json
import os
from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def mostrar_biblioteca(self):
        print("\nSistema de Gerenciamento de livros")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Listar todos os livros")
        print("4. Procurar livro")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        return escolha

    def adicionar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print(f'O livro "{titulo}" de {autor} foi adicionado à biblioteca.')

    def remover_livro(self):
        titulo = input("Digite o título do livro a ser removido: ")
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                self.livros.remove(livro)
                print(f'O livro "{titulo}" foi removido da biblioteca.')
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro foi encontrado na biblioteca.")
        else:
            print("\nLista de Livros na Biblioteca:")
            for idx, livro in enumerate(self.livros, start=1):
                print(f"{idx}. Título: {livro.titulo}, Autor: {livro.autor}")

    def procurar_livro(self):
        titulo = input("Digite o título do livro a ser procurado: ")
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                print(f'Livro encontrado: Título: {livro.titulo}, Autor: {livro.autor}')
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')


    def salvar_livros(self, arquivo):
        livros_dict = [livro.to_dict() for livro in self.livros]
        with open(arquivo, 'w') as f:
            json.dump(livros_dict, f, indent=4)

    def carregar_arquivo(self, arquivo):
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as f:
                livros_dict = json.load(f)
            self.livros = [Livro.from_dict(d) for d in livros_dict]

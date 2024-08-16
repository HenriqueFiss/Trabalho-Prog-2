from biblioteca import Biblioteca

def main():
    bib = Biblioteca()
    bib.carregar_arquivo("livros.json")
    while True:
        escolha = bib.mostrar_biblioteca()
        if escolha == '1':
            bib.adicionar_livro()
        elif escolha == '2':
            bib.remover_livro()
        elif escolha == '3':
            bib.listar_livros()
        elif escolha == '4':
            bib.procurar_livro()
        elif escolha == '5':
            bib.salvar_livros("livros.json")
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
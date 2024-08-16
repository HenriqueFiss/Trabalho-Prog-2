# interface.py

import tkinter as tk
from tkinter import ttk, messagebox
from livro import Livro
from biblioteca_interface import Biblioteca

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("800x600")
        self.root.configure(bg="#2e2e2e")

        self.biblioteca = Biblioteca()

        self.frame_principal = tk.Frame(root, bg="#2e2e2e")
        self.frame_principal.pack(pady=20, fill=tk.BOTH, expand=True)

        self.frame_busca = tk.Frame(self.frame_principal, bg="#2e2e2e")
        self.frame_busca.pack(side=tk.TOP, pady=10, fill=tk.X)

        self.entry_busca = tk.Entry(self.frame_busca, width=50)
        self.entry_busca.pack(side=tk.LEFT, padx=10)
        self.btn_buscar = ttk.Button(self.frame_busca, text="Buscar", command=self.buscar_livro)
        self.btn_buscar.pack(side=tk.LEFT, padx=10)

        self.btn_add_livro = ttk.Button(self.frame_principal, text="Adicionar Livro", command=self.abrir_formulario)
        self.btn_add_livro.pack(side=tk.TOP, pady=10)

        self.listar_livros()

    def listar_livros(self):
        for widget in self.frame_principal.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.frame_busca and widget != self.btn_add_livro.master:
                widget.destroy()

        for livro in self.biblioteca.listar_livros():
            frame_livro = tk.Frame(self.frame_principal, bg="#3e3e3e")
            frame_livro.pack(fill=tk.X, pady=5, padx=20)

            lbl_titulo = tk.Label(frame_livro, text=livro.titulo, fg="#ffffff", bg="#3e3e3e", anchor="w")
            lbl_titulo.pack(side=tk.LEFT, padx=10, pady=5)

            btn_detalhes = ttk.Button(frame_livro, text="Detalhes", command=lambda l=livro: self.exibir_detalhes(l))
            btn_detalhes.pack(side=tk.RIGHT, padx=10)

    def exibir_detalhes(self, livro):
        detalhes_window = tk.Toplevel(self.root)
        detalhes_window.title(f"Detalhes do Livro - {livro.titulo}")
        detalhes_window.geometry("400x300")
        detalhes_window.configure(bg="#2e2e2e")

        detalhes = f"Título: {livro.titulo}\nAutor: {livro.autor}\n"
        lbl_detalhes = tk.Label(detalhes_window, text=detalhes, fg="#ffffff", bg="#2e2e2e", justify=tk.LEFT)
        lbl_detalhes.pack(pady=20)

        def remover_livro():
            self.biblioteca.remover_livro(livro)
            self.listar_livros()
            detalhes_window.destroy()

        btn_remover = ttk.Button(detalhes_window, text="Remover", command=remover_livro)
        btn_remover.pack(pady=10)

    def abrir_formulario(self):
        form_window = tk.Toplevel(self.root)
        form_window.title("Adicionar Livro")
        form_window.geometry("400x300")
        form_window.configure(bg="#2e2e2e")

        lbl_titulo = tk.Label(form_window, text="Título:", fg="#ffffff", bg="#2e2e2e")
        lbl_titulo.pack(pady=10)
        entry_titulo = tk.Entry(form_window, width=40)
        entry_titulo.pack()

        lbl_autor = tk.Label(form_window, text="Autor:", fg="#ffffff", bg="#2e2e2e")
        lbl_autor.pack(pady=10)
        entry_autor = tk.Entry(form_window, width=40)
        entry_autor.pack()

        def salvar_livro():
            titulo = entry_titulo.get()
            autor = entry_autor.get()

            if titulo and autor:
                novo_livro = Livro(titulo, autor)
                self.biblioteca.adicionar_livro(novo_livro)
                self.listar_livros()
                form_window.destroy()
            else:
                messagebox.showwarning("Campos Incompletos", "Por favor, preencha todos os campos.")

        btn_salvar = ttk.Button(form_window, text="Salvar", command=salvar_livro)
        btn_salvar.pack(pady=20)

    def buscar_livro(self):
        titulo_busca = self.entry_busca.get()
        livro_encontrado = next((livro for livro in self.biblioteca.listar_livros() if livro.titulo.lower() == titulo_busca.lower()), None)
        
        if livro_encontrado:
            self.exibir_detalhes(livro_encontrado)
        else:
            messagebox.showinfo("Busca", "Livro não encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()

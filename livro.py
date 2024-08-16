class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def __str__(self):
        return f"{self.titulo} ({self.autor})"

    def to_dict(self):
        return {
            "título": self.titulo,
            "autor": self.autor
        }

    @staticmethod
    def from_dict(d):
        return Livro(d['título'], d['autor'])
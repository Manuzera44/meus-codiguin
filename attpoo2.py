
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class Biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo} Autor:{livro.autor} Ano:{livro.ano}")

livro1 = Livro("borracueca", "cuecaborrada", 2000)
livro2 = Livro("borracueca o legado", "cuecaborrada", 2001)
livro3 = Livro("borracueca caga tronco", "cuecaborrada", 2002)
livro4 = Livro("borracueca o medo de calcinhas", "cuecaborrada", 2003)
livro5 = Livro("borracueca a cueca lendária", "cuecaborrada", 2004)


biblioteca1 = Biblioteca()
biblioteca1.adicionar_livro(livro1)
biblioteca1.adicionar_livro(livro2)
biblioteca1.adicionar_livro(livro3)
biblioteca1.listar_livros()
biblioteca2 = Biblioteca()
biblioteca2.adicionar_livro(livro1)
biblioteca2.adicionar_livro(livro4)
biblioteca2.adicionar_livro(livro5)
biblioteca2.listar_livros()
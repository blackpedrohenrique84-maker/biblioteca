# feito com amor e carinho: samuel augusto e pedro henrique

class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            print('livro entregue!')
            self.disponivel = False

        else:
            print('Livro indisponvel no momento!')

    def devolver(self):
        if self.disponivel == False:
            print('Livro delvolvido com sucesso!')
            self.disponivel = True

        else:
            print('Livro já disponivel!')

    def ficha(self):
        print('Título: ', self.titulo)
        print('Autor: ', self.autor)
        print('Está disponível: ', self.disponivel)

livro1 = Livro('Auto da compadecida', 'Ariano Suassuna', True)
livro2 = Livro('Fui abduzido pot um alien CEO', 'Flavio Bolsonaro', True)
livro3 = Livro('A fanzendeira e o boi leiteiro', 'Luis Inacio Lula', True)

# mostrar a ficha do livro, pegar o livro, pegar dnv(vai avisar a indisponibilidade), mostrar a ficha e depois devolver
livro3.ficha()
livro3.emprestar()
livro3.emprestar()
livro3.ficha()
livro3.devolver()

# devolver o livro(mas já está devolvido), pegar o livro, ver a ficha do livro, devolver o livro, ver a ficha
livro1.devolver()
livro1.emprestar()
livro1.ficha()
livro1.devolver()
livro1.ficha()

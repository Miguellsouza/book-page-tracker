from rich import print



class Livro:

    def __init__(self, titulo="", totP=0):
        self.obra = titulo
        self.totaldepaginas = totP
        self.pagina_atual = 1

        print(f":open_book:[blue] Você acabou de abrir o livro [/]'{self.obra}'[blue] que tem[/] [yellow]{self.totaldepaginas} páginas[/] [blue]no total.[/]\n[blue]Você agora está na[/] [yellow]página {self.pagina_atual}[/]")


    def avançar_paginas(self, qtd):
        avancar = qtd
        faltam = self.totaldepaginas - self.pagina_atual

        if avancar <= faltam:
            for c in range(avancar):
                    if self.pagina_atual < self.totaldepaginas:
                        self.pagina_atual += 1
                        print(f"Pág{self.pagina_atual}:right_arrow:", end=" ")

            print(f"Você avançou {avancar} páginas e agora está na página {self.pagina_atual}")
        else:
            for c in range(faltam):
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual}:right_arrow:", end=" ")
            
            print(f"Você avançou {faltam} páginas e agora está na página {self.pagina_atual}")

            print(f":rotating_light: [red]Você chegou ao final do livro '{self.obra}'")




l1 = Livro("10 coisas que eu aprendi", 20)
l1.avançar_paginas(5)
l1.avançar_paginas(10)
l1.avançar_paginas(200)
l1.avançar_paginas(5)
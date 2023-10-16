"""
Arquivo que utiliza a biblioteca `turtle` para criar simples funçōes em gráficos
"""
import turtle


class MyTurtle(turtle.Turtle):
    def plot_linear_func(self, a: float, b: float):
        self.penup()
        if a * 500 + b * 20 > 500:
            self.goto((500 - b * 20) / a, 500)
            self.pendown()
            self.goto((-500 - b * 20) / a, -500)
        else:

            self.goto(500, (a * 500 + b * 20))
            self.pendown()
            self.goto(-500, (a * (-500) + b * 20))
        self.penup()
        self.goto(0, 0)


def initialize_graph():
    """
    Inicializa o gráfico na janela turtle
    """
    # Configuração da Tela
    scrn = turtle.Screen()
    scrn.screensize(500, 500)
    scrn.bgcolor('black')

    # Configuração da Turtle
    ttl = MyTurtle()
    ttl.shape('circle')
    ttl.shapesize(stretch_wid=0.25, stretch_len=0.25)
    ttl.hideturtle()
    ttl.speed(0)

    # Eixos Secundários
    ## Escala: 20px -> 1unidade no gráfico
    ## Colunas
    ttl.pensize(1)
    ttl.color(0.3, 0.3, 0.3)
    for i in range(-500, 501, 20):
        ttl.penup()
        ttl.goto(i, 500)
        ttl.pendown()
        ttl.goto(i, -500)
    ## Linhas
    for j in range(-500, 501, 20):
        ttl.penup()
        ttl.goto(500, j)
        ttl.pendown()
        ttl.goto(-500, j)

    # Eixos Principais
    ttl.color(0.9, 0.9, 0.9)
    ttl.penup()
    ttl.pensize(2)
    ttl.goto(-500, 0)
    ttl.pendown()
    ttl.goto(500, 0)

    ttl.penup()
    ttl.goto(0, 500)
    ttl.pendown()
    ttl.goto(0, -500)

    ttl.penup()
    ttl.goto(0, 0)
    ttl.showturtle()

    return scrn, ttl


main, pen = initialize_graph()

# # Cria um ambiente interativo
# console = code.InteractiveConsole(locals=locals())
#
# # Executa o console interativo
# console.interact()
# main.mainloop()

import turtle

screen = turtle.getscreen()
turtle.bgcolor('#201e25')
t = turtle.Turtle()
t.color('#cddbdd', '#cddbdd')
t.speed(5)


def move_fd():
    t.fd(20)


def move_bk():
    t.bk(20)


def turn_lt():
    t.lt(90)


def turn_rt():
    t.rt(90)


commands = {
    'w': move_fd,
    's': move_bk,
    'a': turn_lt,
    'd': turn_rt,
}

text_commands = ('Comandos:\n'
                 'w = andar para frente\n'
                 's = andar para trás\n'
                 'a = virar 90° à esquerda\n'
                 'd = virar 90° à direita\n'
                 'quit = sair')
print(text_commands)
while True:
    command_input = input(' > ')
    if command_input == 'quit':
        break
    for c in command_input:
        # comand = commands.get(command_input)
        comand = commands[c]
        comand()

turtle.bye()

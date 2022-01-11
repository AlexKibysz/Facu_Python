from turtle import *

def tree(i):
    if i < 12:
        tree(120)
    else:
        hr.forward(i)
        hr.left(20)
        tree(2 * i / 3)
        hr.right(15)
        tree(2 * i / 3)
        hr.left(20)
        hr.backward(i)


def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def principal(iterations, axiom, rules, angle, length=8, size=2, y_offset=0,
              x_offset=0, offset_angle=0, width=450, height=450):
    inst = create_l_system(iterations, axiom, rules)

    t = Turtle()
    wn = Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()


if __name__ == '__main__':
    axiom = " -X--X"
    rules = {"X":"XFX--XFX-XXXX"}
    iterations = 3 # TOP: 9
    angle = 45
    principal(iterations, axiom, rules, angle)

from citam_pydraw import *

clicked = [
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
]


CELL = 80
N = 5

@animation(False)
def draw():
    for i in range(N):
        for j in range(N):
            x = CELL * j
            y = CELL * i

            if clicked[i][j]:
                Rectangle(x, y, CELL, CELL).fill('red')
            else:
                Rectangle(x, y, CELL, CELL).fill("white")
        mousereleased()




@mouseReleased
def mousereleased():
    mx = mouse.X
    my = mouse.Y
    print(f"X:{mx}, Y:{my}")

    if 0 <= mx < CELL * N and 0 <= my < CELL * N:
        j = mx // CELL
        i = my // CELL

 
        toggle(i, j)
        toggle(i - 1, j)
        toggle(i + 1, j)
        toggle(i, j - 1)
        toggle(i, j + 1)

        draw()


def toggle(i, j):
    if 0 <= i < N and 0 <= j < N:
        clicked[i][j] = not clicked[i][j]


if __name__ == "__main__":
    window = Window(CELL * N, CELL * N).title("Lights Out 5x5")
    mouse = Mouse()
    draw()
    window.show()
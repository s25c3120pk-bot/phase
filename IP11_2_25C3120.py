from citam_pydraw import *
import random

heroSize = 1.0
def drawHeroFace(cx, cy):
    global heroSize
    s = heroSize
    Ellipse(cx, cy, 300*s, 300*s).fill("yellow").outlineWidth(5)

    Ellipse(cx - 40*s, cy - 40*s, 40*s, 80*s).fill("black").outlineWidth(5)
    Ellipse(cx + 40*s, cy - 40*s, 40*s, 80*s).fill("black").outlineWidth(5)

    Arc(cx - 40*s, cy - 40*s, 100*s, 150*s, 50, 130).outlineStyle("arc").outlineWidth(5).noFill()
    Arc(cx + 40*s, cy - 40*s, 100*s, 150*s, 0, 130).outlineStyle("arc").outlineWidth(5).noFill()

    Ellipse(cx, cy + 30*s, 90*s, 90*s).fill("red").outlineWidth(5)

    Ellipse(cx - 90*s, cy + 30*s, 95*s, 95*s).fill("red").outlineWidth(5)
    Ellipse(cx + 90*s, cy + 30*s, 95*s, 95*s).fill("red").outlineWidth(5)

    Arc(cx, cy + 80*s, 120*s, 60*s, 200, 140).outlineStyle("arc").outlineWidth(5).noFill()



def drawHeroBody(cx, cy):
    Rectangle(cx - 100, cy - 20, 200, 10).fill("blue")


def checkCatch(face_x, face_y, mouse_x, ground_y):
    in_y = (ground_y - 60) <= face_y <= (ground_y - 20)
    in_x = (mouse_x - 50) <= face_x <= (mouse_x + 50)
    return in_y and in_x


heroPosX = 0
heroPosY = 0
heroSpeed = 5
bataco = True

@animation(True)
def draw():
    global heroPosX, heroPosY, bataco

    clear()

    if bataco:
        heroPosX = random.randint(100, window.width - 100)
        heroPosY = 50
        bataco = False

    else:
        heroPosY += heroSpeed

        if heroPosY > window.height:
            bataco = True

    drawHeroFace(heroPosX, heroPosY)
    drawHeroBody(mouse.X, window.height - 40)


    #if checkCatch(heroPosX, heroPosY, mouse.X, window.height):
        #txt = Text(window.width // 2, window.height // 2, "Catch!")
        #txt.size(40)
        #print(txt)


if __name__ == "__main__":
    window = Window(1000, 600).title("IP11_EX2")
    mouse = Mouse()
    draw()
    window.show()
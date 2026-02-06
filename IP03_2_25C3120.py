from citam_pydraw import *
import math

@animation(False)
def draw():
    x = cx + r * math.cos(math.radians(360))
    y = cy + r * math.sin(math.radians(360))
    Ellipse(x, y, r, r).noFill()

if __name__ == "__main__":
    window = Window(400, 400, color(255,255,255)).title("IP_03_EX2S")
    cx = 200 #ウィンドウの中心X座標
    cy = 200 #ウィンドウの中心Y座標
    r = 100.0 #回転半径＆円半径
    draw()
    window.show()
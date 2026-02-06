from citam_pydraw import *
import random

def draw():
    colorMode("HSV")
    for i in range(10):              # 段数（0〜9）
        for j in range(10 - i):      # 下が広く上が狭い
            x = 200 - ((10 - i) * 20) + (j * 40)
            y = 400 - (i + 1) * 40   # 下から上に
            Rectangle(x, y, 40, 40).fill(color(random.randint(0, 100), 89, 99))

if __name__ == "__main__":
    window = Window(400, 400).title("IP07_EX02_25C3119")
    draw()
    window.show()
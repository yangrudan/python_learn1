"""
Copyright (c) Zhejiang Lab. All right reserved.
"""
import pyxel


class Mary:
    def __init__(self):
        pyxel.init(200, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)  # 涂掉画面
        for i in range(16):
            x = i * 10
            pyxel.text(x, 10, str(i), 7)
            pyxel.pset(x, 20, i)  # 点
            pyxel.line(x, 30, x+8, 40, i)  # 线
            pyxel.rect(x, 50, x+8, 60, i)
            pyxel.circ(x+4, 80, 8, i)


Mary()

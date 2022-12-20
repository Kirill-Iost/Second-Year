import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog
from PIL import Image, ImageQt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.name = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.jpeg);;Все файлы (*)')[0]
        self.pixmap = QPixmap(self.name)
        self.img1 = Image.open(self.name)
        self.img_color = Image.open(self.name)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('PIL 2.0')

        self.r_button = QPushButton("R", self)
        self.r_button.resize(80, 30)
        self.r_button.move(30, 30)
        self.r_button.clicked.connect(self.rb)

        self.g_button = QPushButton("G", self)
        self.g_button.resize(80, 30)
        self.g_button.move(30, 100)
        self.g_button.clicked.connect(self.gb)

        self.b_button = QPushButton("B", self)
        self.b_button.resize(80, 30)
        self.b_button.move(30, 170)
        self.b_button.clicked.connect(self.bb)

        self.all_button = QPushButton("ALL", self)
        self.all_button.resize(80, 30)
        self.all_button.move(30, 240)
        self.all_button.clicked.connect(self.allb)

        self.rotate1_button = QPushButton("Против часовой стрелки", self)
        self.rotate1_button.resize(150, 30)
        self.rotate1_button.move(30, 310)
        self.rotate1_button.clicked.connect(self.r1b)

        self.rotate2_button = QPushButton("По часовой стрелки", self)
        self.rotate2_button.resize(150, 30)
        self.rotate2_button.move(220, 310)
        self.rotate2_button.clicked.connect(self.r2b)

        self.label = QLabel(self)
        self.label.move(120, 0)
        self.label.resize(280, 280)
        self.label.setPixmap(self.pixmap)

    def rb(self):
        x, y = self.img.size
        pix1 = self.img.load()
        pix2 = self.img_color.load()
        for i in range(x):
            for j in range(y):
                r, g, b = pix2[i, j]
                pix1[i, j] = r, 0, 0
        self.pixmap = self.toqpixmap()

    def gb(self):
        x, y = self.img.size
        pix1 = self.img.load()
        pix2 = self.img_color.load()
        for i in range(x):
            for j in range(y):
                r, g, b = pix2[i, j]
                pix1[i, j] = 0, g, 0
        self.pixmap = self.toqpixmap(self.img)


    def bb(self):
        x, y = self.img.size
        pix1 = self.img.load()
        pix2 = self.img_color.load()
        for i in range(x):
            for j in range(y):
                r, g, b = pix2[i, j]
                pix1[i, j] = 0, 0, b

        self.pixmap = self.toqpixmap(self.img)

    def allb(self):
        x, y = self.img.size
        pix1 = self.img.load()
        pix2 = self.img_color.load()
        for i in range(x):
            for j in range(y):
                pix1[i, j] = pix2[i, j]
        self.pixmap = self.toqpixmap(self.img)


    def r1b(self):
        self.img_color = self.img_color.transpose(Image.ROTATE_270)
        self.img = self.img.transpose(Image.ROTATE_270)
        self.pixmap = self.toqpixmap(self.img)

    def r2b(self):
        self.img_color = self.img_color.transpose(Image.ROTATE_90)
        self.img = self.img.transpose(Image.ROTATE_90)
        self.img = self.img.transpose(Image.ROTATE_90)
        self.pixmap = self.toqpixmap(self.img)

    def toqpixmap(self, im):
        im_data = ImageQt._toqclass_helper(im)
        result = QPixmap(im_data["size"][0], im_data["size"][1])
        result.loadFromData(im_data["data"])
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

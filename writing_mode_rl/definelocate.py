from PyQt5.QtGui import QPainter, QFont, QPen, QPixmap
from PyQt5.QtCore import Qt


class DefineLocate:
    @staticmethod
    def characterWidth(part, fontFamily):
        virtualCanvas = QPixmap(10, 10)
        canvas = QPainter(virtualCanvas)
        width = virtualCanvas.width()
        height = virtualCanvas.height()
        canvas.setRenderHint(QPainter.Antialiasing, False)
        canvas.fillRect(-width, -height, width * 2, height * 2, Qt.white)
        canvas.setPen(QPen(Qt.gray))
        writeFont = QFont(fontFamily)
        pixelSize = width
        writeFont.setPixelSize(pixelSize)
        canvas.setFont(writeFont)
        canvas.drawText(0, pixelSize, part)
        canvas.end()
        img = virtualCanvas.toImage()
        minx = width
        maxx = 0
        y = 0
        while y < height:
            x = 0
            while x < width:
                if not (0xffffffff == img.pixel(x, y)):
                    if minx > x:
                        minx = x
                    if maxx < x:
                        maxx = x
                x += 1
            y += 1
        space = (1.0 - (float(maxx + minx)/float(width))) / 2.0
        if space < 0.1:
            space = 0
        space *= 1.2
        return space

    @staticmethod
    def __editedText(part):
        if part in "っゃゅょぁぃぅぇぉッャュョァィゥェォ":
            return 1
        elif part in "。、,.":
            return 2
        return 0

    @staticmethod
    def getEditedX(part, fontFamily):
        typeNumber = DefineLocate.__editedText(part)
        if typeNumber == 1:
            pass
        elif typeNumber == 2:
            return 0.7
        return DefineLocate.characterWidth(part, fontFamily)

    @staticmethod
    def getEditedY(part, fontFamily):
        typeNumber = DefineLocate.__editedText(part)
        if typeNumber == 1:
            return -0.1
        elif typeNumber == 2:
            return -0.7
        return 0

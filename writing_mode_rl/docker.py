from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QColorDialog,\
    QPushButton, QVBoxLayout, QPlainTextEdit, QComboBox, QHBoxLayout,\
    QFontComboBox
from krita import Krita, DockWidget, DockWidgetFactory, DockWidgetFactoryBase
import copy


class WritingModeRLDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Vertical Writing")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        convertButtons = QWidget(mainWidget)
        buttonCopyToClipboard = QPushButton(
            "Copy to Clipboard",
            convertButtons
        )
        buttonCopyToClipboard.clicked.connect(self.copyToClipboard)
        buttonOutputSVG = QPushButton("Output SVG", convertButtons)
        buttonOutputSVG.clicked.connect(self.outputSVG)
        buttonBoth = QPushButton("Both", convertButtons)
        buttonBoth.clicked.connect(self.both)

        convertTexts = QWidget(mainWidget)
        self.inputText = QPlainTextEdit(convertTexts)
        self.outputText = QPlainTextEdit(
            "text converted by \"Output SVG\" from left input textarea",
            convertTexts
        )
        self.outputText.setReadOnly(True)

        fontOptionDatas = QWidget(mainWidget)
        self.fontSelector = QFontComboBox(fontOptionDatas)
        self.fontColorDialog = QColorDialog(fontOptionDatas)
        fontSizeLabel = QLabel("font size(pt)", fontOptionDatas)
        self.fontSizeCombo = QComboBox(fontOptionDatas)
        self.fontSizeCombo.setEditable(True)
        self.fontSizeCombo.addItems(
            [
               "6",
               "7",
               "8",
               "9",
               "10",
               "11",
               "12",
               "14",
               "16",
               "18",
               "20",
               "22",
               "24",
               "26",
               "28",
               "36",
               "48",
               "72"
            ]
        )
        self.fontSizeCombo.setEditText("8")

        fontOptionDatas.setLayout(QHBoxLayout())
        fontOptionDatas.layout().addWidget(self.fontSelector)
        fontOptionDatas.layout().addWidget(fontSizeLabel)
        fontOptionDatas.layout().addWidget(self.fontSizeCombo)

        convertTexts.setLayout(QHBoxLayout())
        convertTexts.layout().addWidget(self.inputText)
        convertTexts.layout().addWidget(self.outputText)

        convertButtons.setLayout(QHBoxLayout())
        convertButtons.layout().addWidget(buttonOutputSVG)
        convertButtons.layout().addWidget(buttonCopyToClipboard)
        convertButtons.layout().addWidget(buttonBoth)

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(fontOptionDatas)
        mainWidget.layout().addWidget(convertButtons)
        mainWidget.layout().addWidget(convertTexts)

    def canvasChanged(self, canvas):
        pass

    def both(self):
        self.outputSVG()
        self.copyToClipboard()

    def copyToClipboard(self):
        ccText = self.outputText.toPlainText()
        QApplication.clipboard().setText(ccText)

    def outputSVG(self):
        putText = self.__transSVG(self.inputText.toPlainText())
        self.outputText.setPlainText(putText)

    def __transSVG(self, originText):
        beforeText = copy.deepcopy(originText)
        width = len(beforeText.split("\n"))
        editingText = ""
        outChars = list(beforeText)
        y = 0
        x = (width-1)*1.2
        for part in outChars:
            if part == "\n":
                y = 0
                x -= 1.2
            else:
                editedType = self.__editedText(part)
                editedTextX = 0
                editedTextY = 0
                if editedType == 1:
                    editedTextX = 0.2
                    editedTextY = -0.2
                elif editedType == 2:
                    editedTextX = 0.7
                    editedTextY = -0.7
                resultX = x + editedTextX
                resultY = y + editedTextY
                editingText = editingText + "  <tspan x=\"" + \
                    str(resultX) + "em\" y=\"" + str(resultY) + "em\">" + \
                    part + "</tspan>\n"
                y += 1.2
        outText = "<text style=\"font-family:" + \
            self.fontSelector.currentText() + \
            ";font-size:"+self.fontSizeCombo.currentText() + \
            ";fill:" + "#000000"+"\">\n" + \
            editingText + "</text>"
        print(self.fontSizeCombo.currentText())
        print(self.fontSelector.currentText())
        return outText

    def __editedText(self, part):
        if part in "っゃゅょぁぃぅぇぉッャュョァィゥェォ":
            return 1
        elif part in "。、,.":
            return 2
        return 0


Krita.instance().addDockWidgetFactory(
    DockWidgetFactory(
        "Text to SVG",
        DockWidgetFactoryBase.DockRight,
        WritingModeRLDocker
    )
)

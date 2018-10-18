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
        buttonOutputSVG = QPushButton(
            "Output SVG",
            convertButtons
        )
        buttonOutputSVG.clicked.connect(self.outputSVG)
        buttonBoth = QPushButton("Both", convertButtons)
        buttonBoth.clicked.connect(self.both)

        convertTextLabels = QWidget(mainWidget)
        inputTextLabel = QLabel("Input Text", convertTextLabels)
        outputTextLabel = QLabel("Output SVG", convertTextLabels)

        convertTexts = QWidget(mainWidget)
        self.inputText = QPlainTextEdit(convertTexts)
        self.outputText = QPlainTextEdit(
            "text converted by \"Output SVG\" from left input textarea",
            convertTexts
        )
        self.outputText.setReadOnly(True)

        fontNames = QWidget(mainWidget)
        fontSelectorLabel = QLabel("font family", fontNames)
        self.fontSelector = QFontComboBox(fontNames)

        fontOptionDatas = QWidget(mainWidget)
        fontColorParts = QWidget(mainWidget)
        fontColorParts.setLayout(QHBoxLayout())
        fontColorLabel = QLabel("font color", fontColorParts)
        self.fontColorButton = QPushButton("■", fontColorParts)
        self.fontColorButton.clicked.connect(self.openTextColorDialog)
        self.fontColorDialog = QColorDialog(mainWidget)
        self.fontColorDialog.colorSelected.connect(self.selectedColor)
        self.fontColorCombo = QComboBox(fontOptionDatas)
        self.fontColorCombo.setEditable(True)
        self.fontColorCombo.addItems(
            [
                "#000000",
                "#7f7f7f",
                "#ffffff",
                "#ff0000",
                "#ffff00",
                "#00ff00",
                "#00ffff",
                "#0000ff",
                "#ff00ff"
            ]
        )
        self.fontColorCombo.editTextChanged.connect(self.colorChanged)
        fontColorParts.layout().addWidget(fontColorLabel)
        fontColorParts.layout().addWidget(self.fontColorButton)
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

        fontNames.setLayout(QHBoxLayout())
        fontNames.layout().addWidget(fontSelectorLabel)
        fontNames.layout().addWidget(self.fontSelector)

        fontOptionDatas.setLayout(QHBoxLayout())
        fontOptionDatas.layout().addWidget(fontColorParts)
        fontOptionDatas.layout().addWidget(self.fontColorCombo)
        fontOptionDatas.layout().addWidget(fontSizeLabel)
        fontOptionDatas.layout().addWidget(self.fontSizeCombo)

        convertTextLabels.setLayout(QHBoxLayout())
        convertTextLabels.layout().addWidget(inputTextLabel)
        convertTextLabels.layout().addWidget(outputTextLabel)

        convertTexts.setLayout(QHBoxLayout())
        convertTexts.layout().addWidget(self.inputText)
        convertTexts.layout().addWidget(self.outputText)

        convertButtons.setLayout(QHBoxLayout())
        convertButtons.layout().addWidget(buttonOutputSVG)
        convertButtons.layout().addWidget(buttonCopyToClipboard)
        convertButtons.layout().addWidget(buttonBoth)

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(fontNames)
        mainWidget.layout().addWidget(fontOptionDatas)
        mainWidget.layout().addWidget(convertButtons)
        mainWidget.layout().addWidget(convertTextLabels)
        mainWidget.layout().addWidget(convertTexts)

    def canvasChanged(self, canvas):
        pass

    def openTextColorDialog(self):
        self.fontColorDialog.open()

    def selectedColor(self, color):
        self.fontColorCombo.setEditText(color.name())

    def colorChanged(self, text):
        self.fontColorButton.setStyleSheet(
            "color:" + text + ";"
        )

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
                editedType = WritingModeRLDocker.__editedText(part)
                editedTextX = WritingModeRLDocker.__getEditedX(editedType)
                editedTextY = WritingModeRLDocker.__getEditedY(editedType)
                resultX = x + editedTextX
                resultY = y + editedTextY
                editingText = editingText + "  <tspan x=\"" + \
                    str(resultX) + "em\" y=\"" + str(resultY) + "em\">" + \
                    part + "</tspan>\n"
                y += 1.2
        outText = "<text style=\"font-family:" + \
            self.fontSelector.currentText() + \
            ";font-size:"+self.fontSizeCombo.currentText() + \
            ";fill:" + self.fontColorCombo.currentText() + "\">\n" + \
            editingText + "</text>"
        return outText

    @staticmethod
    def __editedText(part):
        if part in "っゃゅょぁぃぅぇぉッャュョァィゥェォ":
            return 1
        elif part in "。、,.":
            return 2
        return 0

    @staticmethod
    def __getEditedX(typeNumber):
        if typeNumber == 1:
            return 0.2
        elif typeNumber == 2:
            return 0.7
        return 0

    @staticmethod
    def __getEditedY(typeNumber):
        if typeNumber == 1:
            return -0.2
        elif typeNumber == 2:
            return -0.7
        return 0


Krita.instance().addDockWidgetFactory(
    DockWidgetFactory(
        "Text to SVG",
        DockWidgetFactoryBase.DockRight,
        WritingModeRLDocker
    )
)

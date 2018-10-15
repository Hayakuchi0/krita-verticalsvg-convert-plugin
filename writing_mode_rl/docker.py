from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QVBoxLayout, QPlainTextEdit
from krita import Krita, DockWidget, DockWidgetFactory, DockWidgetFactoryBase
import copy


class WritingModeRLDocker(DockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Vertical Writing")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        buttonCopyToClipboard = QPushButton("Copy to Clipboard", mainWidget)
        buttonCopyToClipboard.clicked.connect(self.copyToClipboard)
        buttonOutputSVG = QPushButton("Output SVG", mainWidget)
        buttonOutputSVG.clicked.connect(self.outputSVG)
        self.inputText = QPlainTextEdit(mainWidget)
        self.outputText = QPlainTextEdit(
            "text converted by \"Output SVG\" from input textarea",
            mainWidget
        )
        self.outputText.setReadOnly(True)
        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(buttonOutputSVG)
        mainWidget.layout().addWidget(buttonCopyToClipboard)
        mainWidget.layout().addWidget(self.inputText)
        mainWidget.layout().addWidget(self.outputText)

    def canvasChanged(self, canvas):
        pass

    def copyToClipboard(self):
        self.outputSVG()
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
                editingText = editingText + "  <tspan x=\"" + str(x) + \
                    "em\" y=\"" + str(y) + "em\">" + part + "</tspan>\n"
                y += 1.2
        outText = "<text>\n" + editingText + "</text>"
        return outText


Krita.instance().addDockWidgetFactory(
    DockWidgetFactory(
        "Text to SVG",
        DockWidgetFactoryBase.DockRight,
        WritingModeRLDocker
    )
)

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


def GUI():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    styleComboBox = QComboBox()
    styleComboBox.addItems(["fusion"])

    styleLabel = QLabel("&Style:")
    styleLabel.setBuddy(styleComboBox)

    useStylePalette = QCheckBox("&Use style's standard palette")
    disableWidgets = QCheckBox("&Disable widgets")

    ################################################################################
    tlg = QGroupBox("Group 1")

    radioButton1 = QRadioButton("Radio button 1")
    radioButton2 = QRadioButton("Radio button 2")
    radioButton3 = QRadioButton("Radio button 3")
    radioButton1.setChecked(True)

    checkBox = QCheckBox("Tri-state check box")
    checkBox.setTristate(True)
    checkBox.setCheckState(Qt.PartiallyChecked)

    layout_tlg = QVBoxLayout()
    layout_tlg.addWidget(radioButton1)
    layout_tlg.addWidget(radioButton2)
    layout_tlg.addWidget(radioButton3)
    layout_tlg.addWidget(checkBox)
    layout_tlg.addStretch(1)
    tlg.setLayout(layout_tlg)
    ################################################################################

    trg = QGroupBox("Group 2")

    defaultPushButton = QPushButton("Default Push Button")
    defaultPushButton.setDefault(True)

    togglePushButton = QPushButton("Toggle Push Button")
    togglePushButton.setCheckable(True)
    togglePushButton.setChecked(True)

    flatPushButton = QPushButton("Flat Push Button")
    flatPushButton.setFlat(True)

    layout_trg = QVBoxLayout()
    layout_trg.addWidget(defaultPushButton)
    layout_trg.addWidget(togglePushButton)
    layout_trg.addWidget(flatPushButton)
    layout_trg.addStretch(1)
    trg.setLayout(layout_trg)
    ################################################################################

    bl = QTabWidget()
    bl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)

    tab1 = QWidget()
    tableWidget = QTableWidget(10, 10)

    tab1vbox = QVBoxLayout()
    tab1vbox.addWidget(tableWidget)
    tab1.setLayout(tab1vbox)

    tab2 = QWidget()
    textEdit = QTextEdit()

    textEdit.setPlainText("hy, my name is sulaiman \n"
                          "do you know me?\n"
                          "if you know me, please give me some money\n"
                          "i have to paid my debt\n"
                          "love you <3")

    tab2vbox = QVBoxLayout()
    tab2vbox.addWidget(textEdit)
    tab2.setLayout(tab2vbox)

    bl.addTab(tab1, "&Table")
    bl.addTab(tab2, "Text &Edit")
    ################################################################################

    brg = QGroupBox("Group 3")
    brg.setCheckable(True)
    brg.setChecked(True)

    lineEdit = QLineEdit('sulaiman')
    lineEdit.setEchoMode(QLineEdit.Password)

    spinBox = QSpinBox(brg)
    spinBox.setValue(90)

    dateTimeEdit = QDateTimeEdit(brg)
    dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    slider = QSlider(Qt.Horizontal, brg)
    slider.setValue(60)

    scrollBar = QScrollBar(Qt.Horizontal, brg)
    scrollBar.setValue(90)

    dial = QDial(brg)
    dial.setValue(90)
    dial.setNotchesVisible(True)

    layout_brg = QGridLayout()
    layout_brg.addWidget(lineEdit, 0, 0, 1, 2)
    layout_brg.addWidget(spinBox, 1, 0, 1, 2)
    layout_brg.addWidget(dateTimeEdit, 2, 0, 1, 2)
    layout_brg.addWidget(slider, 3, 0)
    layout_brg.addWidget(scrollBar, 4, 0)
    layout_brg.addWidget(dial, 3, 1, 2, 1)
    brg.setLayout(layout_brg)
    ################################################################################

    ps = QProgressBar()
    ps.setRange(0, 1000)
    ps.setValue(400)
    ################################################################################

    disableWidgets.toggled.connect(tlg.setDisabled)
    disableWidgets.toggled.connect(trg.setDisabled)
    disableWidgets.toggled.connect(bl.setDisabled)
    disableWidgets.toggled.connect(brg.setDisabled)

    widget = QWidget()
    tl = QHBoxLayout()
    tl.addWidget(styleLabel)
    tl.addWidget(styleComboBox)
    tl.addStretch(1)
    tl.addWidget(useStylePalette)
    tl.addWidget(disableWidgets)

    l = QGridLayout()
    l.addLayout(tl, 0, 0, 1, 2)
    l.addWidget(tlg, 1, 0)
    l.addWidget(trg, 1, 1)
    l.addWidget(bl, 2, 0)
    l.addWidget(brg, 2, 1)
    l.addWidget(ps, 3, 0, 1, 2)
    l.setRowStretch(1, 1)
    l.setRowStretch(2, 1)
    l.setColumnStretch(0, 1)
    l.setColumnStretch(1, 1)

    widget.setLayout(l)
    widget.show()
    app.exec_()


GUI()

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QCheckBox, QRadioButton, QVBoxLayout, QPushButton, QLineEdit, QGridLayout


def input_data():
    app = QApplication(sys.argv)

    # membuat label dari tulisan 'Input Biodata' dan style dari label tersebut
    label = QLabel('Input Biodata')
    label.setStyleSheet(
        "font-size: 30pt; background-color: #98adb8; font-weight: bold; color: red"
    )

    # membuat label dari nama, address, hobby, dan status
    name = QLabel("Name")
    address = QLabel("Address")
    hobby = QLabel("Hobby")
    status = QLabel("Status")

    # membuat kolom isian dari nama dan address
    name_input = QLineEdit()
    address_input1 = QLineEdit()
    address_input2 = QLineEdit()

    # membuar cekbox
    cekbox1 = QCheckBox("Makan")
    cekbox2 = QCheckBox("Tidur")
    cekbox3 = QCheckBox("Main")

    # membuat radiobutton
    radio1 = QRadioButton("Pelajar")
    radio2 = QRadioButton("Pegawai")
    radio3 = QRadioButton("Wiraswasta")

    # membuat GridLayout dan hubungkan dengan label nama, address, hobby, status, cekbox, dan radio button
    grid_widget = QWidget()
    grid = QGridLayout()
    # memberikan spasi antar garis yang dikenai fungsi gridlayout
    grid.setSpacing(10)

    # menambahkan label ke fungsi grid dengan fitur addwidget ('nama label', letak grid "x", letak grid "y", ukuran grid "x", ukuran grid "y")
    grid.addWidget(name, 1, 0)
    grid.addWidget(name_input, 1, 1)

    grid.addWidget(address, 2, 0)
    grid.addWidget(address_input1, 2, 1)
    grid.addWidget(address_input2, 3, 1)

    grid.addWidget(hobby, 4, 0)
    grid.addWidget(cekbox1, 4, 1)
    grid.addWidget(cekbox2, 5, 1)
    grid.addWidget(cekbox3, 6, 1)

    grid.addWidget(status, 7, 0)
    grid.addWidget(radio1, 7, 1)
    grid.addWidget(radio2, 8, 1)
    grid.addWidget(radio3, 9, 1)

    # setelah semua label yang diinginkan sudah dikenai grid, kita setkan grid layout kedalam widget layoutnya
    grid_widget.setLayout(grid)

    # menyusun semua fungsi secara vertikal dengan qvboxlayout
    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(grid_widget)
    widget.setLayout(layout)

    # mengatur tata letak dan ukuran dari windows yang kita run
    widget.setGeometry(50, 50, 500, 320)
    widget.setWindowTitle("Latihan Mandiri")

    # menampilkan semua widget kita
    widget.show()
    app.exec_()


input_data()

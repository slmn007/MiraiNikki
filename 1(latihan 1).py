import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

# membuat fungsi utk menentukan layout window


def window_go():
    # inisialisasi pyqt
    app = QApplication(sys.argv)
    window = QWidget()

    # menyiapkan label, menempelkan label ke window
    # settext, dan posisi
    label = QLabel('Hasil Angka')
    button_widget = QWidget()
    button_layout = QHBoxLayout()
    for i in range(10):
        button = QPushButton('{}'.format(i + 1))
        button_layout.addWidget(button)
        button.setStyleSheet("QPushButton { background-color: white }"
                             "QPushButton:pressed { background-color: red }")

    # combine layout with button
    button_widget.setLayout(button_layout)

    # combine layout with label and allthings
    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button_widget)
    widget.setLayout(layout)

    # Show widget
    widget.show()
    # Start event loop
    app.exec_()


if __name__ == '__main__':
    window_go()

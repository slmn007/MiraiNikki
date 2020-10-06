import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy


def num_show():
    # Initialize application
    app = QApplication(sys.argv)

    # Create label and button
    label = QLabel('Hasil Angka')
    button_widget = QWidget()
    button_layout = QHBoxLayout()
    for i in range(10):
        button = QPushButton('{}'.format(i + 1))
        button_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setStyleSheet("QPushButton:pressed { background-color: white }")

    # combine layout with button
    button_widget.setLayout(button_layout)

    # combine layout with label and allthings
    widget = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button_widget)
    widget.setLayout(layout)

    # resize the Font

    # set the windows size
    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("Latihan Mandiri")

    # Show widget
    widget.show()
    # Start event loop
    app.exec_()


num_show()

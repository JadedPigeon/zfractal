
import sys
from mandelbrot import mandelbrot_iterations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("zfractal")
    window.resize(1000, 700)

    label = QLabel("zfractal - Mandelbrot Explorer")
    label.setAlignment(Qt.AlignCenter)

    window.setCentralWidget(label)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

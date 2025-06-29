from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
import sys
def launch_gui():
    app = QApplication(sys.argv)
    w = QWidget(); w.setWindowTitle("SyncBridge")
    l = QVBoxLayout(w); l.addWidget(QLabel("SyncBridge GUI placeholder"))
    w.show(); sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from threading import Thread
from app import create_app

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insurance Predictor")
        self.setGeometry(100, 100, 1024, 768)
        
        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)
        
        # Start Flask app in a separate thread
        self.flask_thread = Thread(target=self.run_flask)
        self.flask_thread.daemon = True
        self.flask_thread.start()
        
        # Load the Flask app URL
        self.web_view.load(QUrl("http://127.0.0.1:5000"))

    def run_flask(self):
        app = create_app()
        app.run(debug=False)

if __name__ == '__main__':
    qt_app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(qt_app.exec_())


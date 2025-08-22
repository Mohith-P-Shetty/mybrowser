import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QToolBar,
    QLineEdit
)
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow) :
    def __init__(self):

        super().__init__()
        self.setWindowTitle("MyBrowser")
        self.setFixedSize(QSize(1024, 700))
        self.browser_view = QWebEngineView()
        self.setCentralWidget(self.browser_view)
        self.browser_view.setUrl( QUrl("https://www.google.com"))
        #ToolBar
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        self.browser_view.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):

        url_text = self.url_bar.text()
        if not (url_text.startswith("http://") or url_text.startswith("https://")):
            url_text = "https://" + url_text
        self.browser_view.setUrl(QUrl(url_text))

    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())

#Main Logic
if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())

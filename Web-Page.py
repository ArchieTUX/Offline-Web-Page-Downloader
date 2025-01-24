import os
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui, QtCore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import youtube_dl

class WebPageDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Offline Web Page Downloader")
        self.setGeometry(100, 100, 800, 400)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # URL Input
        self.url_label = QtWidgets.QLabel("Enter URL:", self)
        self.url_label.setGeometry(20, 20, 100, 30)
        self.url_input = QtWidgets.QLineEdit(self)
        self.url_input.setGeometry(120, 20, 600, 30)

        # Download Options
        self.option_label = QtWidgets.QLabel("Content to Download:", self)
        self.option_label.setGeometry(20, 70, 150, 30)
        self.option_combo = QtWidgets.QComboBox(self)
        self.option_combo.setGeometry(180, 70, 200, 30)
        self.option_combo.addItems(["HTML & Images", "Media Files", "Complete Page"])

        # Download Button
        self.download_button = QtWidgets.QPushButton("Download", self)
        self.download_button.setGeometry(20, 120, 120, 40)
        self.download_button.clicked.connect(self.download_page)

        # Progress Bar
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(20, 180, 760, 30)
        self.progress_bar.setValue(0)

        # Status Output
        self.status_output = QtWidgets.QTextEdit(self)
        self.status_output.setGeometry(20, 230, 760, 150)
        self.status_output.setReadOnly(True)

    def download_page(self):
        url = self.url_input.text()
        option = self.option_combo.currentText()

        if not url:
            self.status_output.append("Please enter a valid URL.")
            return

        self.status_output.append(f"Starting download for: {url}")
        self.progress_bar.setValue(10)

        try:
            if option == "HTML & Images":
                self.download_static_content(url)
            elif option == "Media Files":
                self.download_media(url)
            elif option == "Complete Page":
                self.download_full_page(url)
        except Exception as e:
            self.status_output.append(f"Error: {str(e)}")
        finally:
            self.progress_bar.setValue(100)
            self.status_output.append("Download complete.")

    def download_static_content(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Save HTML
        os.makedirs("downloads", exist_ok=True)
        with open("downloads/page.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        self.status_output.append("HTML content saved.")

        # Download Images
        os.makedirs("downloads/images", exist_ok=True)
        images = soup.find_all("img")
        for img in tqdm(images, desc="Downloading images"):
            img_url = img.get("src")
            if img_url:
                img_response = requests.get(img_url, stream=True)
                img_name = os.path.basename(img_url)
                with open(f"downloads/images/{img_name}", "wb") as f:
                    for chunk in img_response.iter_content(1024):
                        f.write(chunk)
        self.status_output.append(f"{len(images)} images downloaded.")

    def download_media(self, url):
        ydl_opts = {"outtmpl": "downloads/media/%(title)s.%(ext)s"}
        os.makedirs("downloads/media", exist_ok=True)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        self.status_output.append("Media files downloaded.")

    def download_full_page(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        driver.get(url)

        # Save Page Source
        os.makedirs("downloads", exist_ok=True)
        with open("downloads/full_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        self.status_output.append("Complete page saved.")
        driver.quit()


# Run the App
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    downloader = WebPageDownloader()
    downloader.show()
    sys.exit(app.exec())

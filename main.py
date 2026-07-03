from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import yt_dlp
import os
import sys


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyVideo Downloader Pre Release")
        self.resize(420, 300)

        # ÍCONE DA JANELA (IMPORTANTE)
        self.setWindowIcon(QIcon(self.resource_path("icon.ico")))

        # Pasta padrão
        self.download_path = os.path.join(os.path.expanduser("~"), "Downloads")

        # URL
        self.url = QLineEdit()
        self.url.setPlaceholderText("Cole o link aqui")

        # Formato
        self.format = QComboBox()
        self.format.addItems([
            "MP4 720p",
            "MP4 1080p",
            "MP3 320kbps"
        ])

        # Botão pasta
        self.btn_folder = QPushButton("Selecionar pasta de download")
        self.btn_folder.clicked.connect(self.select_folder)

        self.folder_label = QLabel(f"Pasta: {self.download_path}")

        # Botão download
        self.btn = QPushButton("Baixar agora")
        self.btn.clicked.connect(self.download)

        # Log
        self.log = QTextEdit()
        self.log.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.url)
        layout.addWidget(self.format)
        layout.addWidget(self.btn_folder)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.btn)
        layout.addWidget(self.log)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 🔥 compatível com .exe e modo normal
    def resource_path(self, relative_path):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # FFmpeg embutido
    def ffmpeg_path(self):
        return os.path.join(self.resource_path("ffmpeg"))

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Escolha a pasta")

        if folder:
            self.download_path = folder
            self.folder_label.setText(f"Pasta: {folder}")

    def log_msg(self, msg):
        self.log.append(msg)
        print(msg)

    def download(self):
        url = self.url.text().strip()

        if not url:
            QMessageBox.warning(self, "Erro", "Cole um link válido")
            return

        choice = self.format.currentText()

        ffmpeg_dir = self.ffmpeg_path()

        if "MP3" in choice:
            opts = {
                "format": "bestaudio/best",
                "outtmpl": os.path.join(self.download_path, "%(title)s.%(ext)s"),
                "ffmpeg_location": ffmpeg_dir,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }],
                "noplaylist": True,
            }

        else:
            quality = "1080" if "1080" in choice else "720"

            opts = {
                "format": f"bestvideo[height<={quality}]+bestaudio/best",
                "merge_output_format": "mp4",
                "outtmpl": os.path.join(self.download_path, "%(title)s.%(ext)s"),
                "ffmpeg_location": ffmpeg_dir,
                "noplaylist": True,
            }

        try:
            self.log_msg("🔄 Iniciando download...")

            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])

            self.log_msg("✅ Download concluído!")

            QMessageBox.information(self, "OK", "Download concluído!")

        except Exception as e:
            self.log_msg(f"❌ Erro: {str(e)}")
            QMessageBox.critical(self, "Erro", str(e))


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec()
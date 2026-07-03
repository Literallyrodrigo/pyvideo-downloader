# 🇺🇸 English

# 📖 About the Project

**PyVideo Downloader** is a desktop application developed in **Python** using **PySide6**, designed to provide a modern and intuitive graphical interface for downloading videos and audio through the **yt-dlp** library.

The application allows users to download media in different formats, choose a custom download directory, and automatically merge or convert files using **FFmpeg**.

This project was created as part of my software development portfolio to demonstrate desktop application development, GUI programming, third-party library integration and software engineering best practices.

---

# ✨ Features

✔ Modern desktop interface

✔ MP4 video downloads

✔ MP3 audio downloads

✔ 720p support

✔ 1080p support (when available)

✔ Automatic FFmpeg integration

✔ Custom download directory

✔ Download activity log

✔ Lightweight and easy to use

✔ Open-source portfolio project

---

# 🚀 How It Works

The application works as a graphical interface for **yt-dlp**, simplifying the entire media download process.

The workflow consists of:

1. Enter the media URL.
2. Select the desired output format.
3. Choose the destination folder.
4. Start the download.
5. FFmpeg automatically converts or merges media when required.
6. The application displays the operation status and completion message.

All processing is performed locally on the user's computer.

---

# 🖥 Interface

The application includes:

* URL input field;
* Output format selector;
* Download folder selection;
* Download button;
* Status log;
* Simple and responsive desktop interface.

---

# 📸 Screenshots

## Main Window

![](screenshots/home.png)

---

## Folder Selection

![](screenshots/folder-selection.png)

---

## Options

![](screenshots/options.png)

---

## Download Complete

![](screenshots/downloading.png)

---


# 🛠 Built With

* Python 3
* PySide6
* yt-dlp
* FFmpeg

---

# 📂 Project Structure

```text
pyvideo-downloader/
│
├── screenshots/
│   ├── home.png
│   ├── folder-selection.png
│   ├── downloading.png
│   └── options.png
│
├── icon.ico
├── main.py
├── README.md
├── README.pt-BR.md
├── DISCLAIMER.md
├── NOTICE.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Literallyrodrigo/pyvideo-downloader.git
```

Enter the project folder:

```bash
cd pyvideo-downloader
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# 🏗 Building the Executable

Using **PyInstaller**:

```bash
pyinstaller ^
--onefile ^
--windowed ^
--icon icon.ico ^
main.py
```

---

# 📋 Requirements

### Operating System

* Windows 10 or later

### Python

* Python 3.11 or higher

### Dependencies

* PySide6  
* yt-dlp  

### External Components

* FFmpeg (required)

FFmpeg must be installed and available in the system PATH for the following features to work properly:

- audio conversion to MP3  
- audio and video merging  

🔗 Official download: https://ffmpeg.org/download.html  

### Internet Connection

* Internet access is required to retrieve the requested content.

---

# 📦 Dependencies

Python dependencies can be installed automatically using the `requirements.txt` file.

Expected contents:

```text
PySide6
yt-dlp
```

FFmpeg must be available for operations such as audio conversion and merging audio and video streams to work correctly.

---

# 💡 Compatibility

The code was developed in Python and, with minor packaging adjustments, can be run on different operating systems compatible with the used libraries.

Currently, the main focus of the project is the Windows environment.

# ⚖ Legal Notice

**PyVideo Downloader** is an open-source desktop application created for educational and portfolio purposes.

The software provides a graphical interface for the **yt-dlp** project and does not host, distribute or provide copyrighted media.

Users are solely responsible for ensuring that their use of the application complies with applicable laws, copyright regulations and the Terms of Service of the platforms they access.

The author **does not encourage or endorse copyright infringement.**

---

# 📈 Roadmap

Future versions may include:

* Real-time progress bar;
* Download speed indicator;
* Download queue;
* Playlist support;
* Download history;
* Automatic yt-dlp updates;
* Dark mode;
* Linux support;
* macOS support;
* Additional output formats.

---

# ❓ Frequently Asked Questions

### Does the application collect personal data?

No.

All processing happens locally.

---

### Is FFmpeg required?

Yes.

FFmpeg is required for media conversion and audio/video merging.

---

### Can I choose where downloads are saved?

Yes.

Any folder on your computer can be selected as the destination.

---

### Is the application free?

Yes.

It is an open-source project distributed free of charge.

---

# 🤝 Contributions

Contributions are always welcome.

If you would like to contribute to the project:

1. Fork the repository;
2. Create a new branch for your changes;
3. Implement the desired improvements;
4. Run the necessary tests;
5. Submit a Pull Request.

The following are also highly appreciated:

* Bug fixes;
* Interface improvements;
* Performance optimizations;
* Documentation improvements;
* Suggestions for new features.

---

# 📄 License

This project is distributed under the terms of the **MIT License**.

Please refer to the **LICENSE** file for the full license text.

All third-party libraries and tools used in this project remain subject to their respective authors’ licenses.

---

# ❤️ Acknowledgements

This project uses technologies developed by the open-source community.

Special thanks to the maintainers and contributors of:

* Python
* PySide6
* yt-dlp
* FFmpeg

The work of these communities makes it possible to build modern, accessible, and high-quality applications.

---

# ⭐ Support the Project

If this project was helpful to you or contributed to your learning, please consider leaving a ⭐ on the repository.

This simple gesture helps the project reach more people, encourages its evolution, and values the work invested in its development.

---

# 👨‍💻 Author

## Rodrigo Teixeira

**Computer Scientist**

Graduated in Computer Science.

I am a software developer passionate about technology, software engineering, and building applications that combine simplicity, performance, and good user experience.

I have a particular interest in the following areas:

* Python Development;
* Desktop Development;
* Software Engineering;
* REST APIs;
* Process Automation;
* Artificial Intelligence;
* Computer Vision.

**PyVideo Downloader** was developed as part of my professional portfolio, aiming to demonstrate skills in desktop development, library integration, code organization, technical documentation, and software engineering best practices.

---

## 📬 Contact

### GitHub and LinkedIn

[GitHub](https://github.com/Literallyrodrigo)

[LinkedIn](https://www.linkedin.com/in/rodrigoteixeira-dev/)

---

<p align="center">

Built with ❤️ using Python.  
Thank you, God and Jesus, for everything.

**© 2026 Rodrigo Teixeira**

</p>
# Offline Web Page Downloader

The **Offline Web Page Downloader** is a user-friendly tool designed to download web pages for offline use. It fetches page content, including text, images, and embedded media (audio and video), and stores them locally in a neat folder structure.  

With its sleek and interactive GUI powered by PyQt5, this app is perfect for users who want to access web content without an internet connection.  

---

## Features

- **Download web pages**: Save complete web pages, including text and images, to your local machine.
- **Media support**: Download embedded media such as videos and audio files (if available).
- **Interactive GUI**: Intuitive interface for entering URLs, viewing download progress, and managing saved content.
- **Batch mode**: Enter multiple URLs to download pages in bulk.
- **Progress tracking**: Real-time progress updates with a clean and modern design.

---

## Prerequisites

- Python 3.8 or higher installed on your system.
- Google Chrome browser installed.
- ChromeDriver added to your system PATH (ensure the version matches your Chrome browser).  
  [Download ChromeDriver here](https://sites.google.com/chromium.org/driver/).

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/offline-web-downloader.git
   cd offline-web-downloader
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up ChromeDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Add the downloaded ChromeDriver to your system PATH.  

   Example for Linux/Mac:
   ```bash
   export PATH=$PATH:/path/to/chromedriver
   ```
   Example for Windows:
   Add the path to ChromeDriver in System Environment Variables.

---

## Usage

1. **Run the Application**:
   ```bash
   python offline_downloader.py
   ```

2. **Using the App**:
   - Enter a single URL or multiple URLs (comma-separated).
   - Click **Download** to save the web pages offline.
   - The app will save each web page in a neatly organized folder in the `downloads` directory.

3. **View Progress**:
   - The app displays the download progress in real-time, including text, images, and media.
   - Upon completion, you’ll receive a confirmation.

4. **Access Saved Pages**:
   - Navigate to the `downloads` folder in the application directory.
   - Each URL will have its own folder containing all the downloaded resources.

---

## Technologies Used

- **PyQt5**: For the interactive graphical interface.
- **BeautifulSoup4**: For parsing and extracting HTML content.
- **Requests**: For fetching page content and resources.
- **Selenium**: For advanced page rendering and handling JavaScript-heavy pages.
- **youtube-dl**: For downloading embedded video and audio content.
- **tqdm**: For displaying progress bars in the console (optional).

---

## Contribution

Feel free to contribute to this project by submitting issues or feature requests. Fork the repository and send a pull request with your improvements!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

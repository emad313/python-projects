# 📂 File Crawler with Generator (Advanced++)

A powerful, pluggable file crawler built in Python that scans through `.txt` and `.log` files inside any directory and yields lines containing a specific keyword. Uses:

- ✅ Abstract Base Classes (`ABC`)
- ✅ Python Generators (`yield`)
- ✅ Decorators for performance logging
- ✅ CLI interface (`argparse`)
- ✅ Clean modular file-by-file structure

---

## 🚀 Features

- Crawl directories recursively for `.txt` and `.log` files
- Search for specific keywords (case-insensitive)
- Yield matching lines with file path and line number
- Log performance using a decorator
- Simple command-line usage

---

## 📁 Project Structure

file_crawler/
├── base_crawler.py # Abstract class for pluggable crawlers
├── keyword_crawler.py # Keyword search implementation
├── decorators.py # Performance logger
├── utils.py # Print helpers
├── main.py # CLI interface


---

## 📦 Requirements

- Python 3.7+
- No external dependencies

---

## 💻 Usage

### Run from terminal:

```bash
python main.py <directory_path> <keyword>

```
## Example

python main.py ./logs error

## Output

./logs/server.log [Line 42]: Unexpected error occurred
./logs/server.log [Line 79]: Connection error with database

[INFO] Finished in 0.11 seconds.


## 🧠 Concepts Covered
- Abstract Classes: Easily extendable crawlers using BaseCrawler

- Generators: Efficient memory usage with yield for large file scans

- Decorators: Reusable performance logger

- File I/O: Safe reading with encoding fallback

- CLI Tools: Built with argparse for flexibility

## 🧰 Extend This Project
You can add more crawlers by subclassing BaseCrawler:

class RegexCrawler(BaseCrawler):
    def crawl(self, pattern: str):
        ...

## 📜 License
MIT License — Free to use and modify.

## ✍️ Author
Built as an advanced Python exercise on abstract design and generators.
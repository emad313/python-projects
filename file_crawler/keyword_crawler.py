from base_crawler import BaseCrawler
from decorators import log_performance

class KeywordCrawler(BaseCrawler):

    @log_performance
    def crawl(self, keyword: str):
        for file_path in self.root_path.rglob('*'):
            if file_path.suffix in ['.txt', '.md', '.log'] and file_path.is_file():
                with file_path.open('r', encoding='utf-8', errors='ignore') as file:
                    for lineno, line in enumerate(file, start=1):
                        if keyword.lower() in line.lower():
                            yield (file_path, lineno, line.strip())
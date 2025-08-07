from abc import ABC, abstractmethod
from pathlib import Path

class BaseCrawler(ABC):
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)

    
    @abstractmethod
    def crawl(self, keyword: str):
        """
        Abstract method to be implemented by subclasses.
        This method should contain the logic to crawl the directory structure.
        """
        pass
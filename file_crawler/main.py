import argparse
from keyword_crawler import KeywordCrawler
from utils import print_match

def main():
    parser = argparse.ArgumentParser(description="Crawl files for a keyword.")
    parser.add_argument('root_path', type=str, help='Root directory to start crawling from')
    parser.add_argument('keyword', type=str, help='Keyword to search for in files')
    args = parser.parse_args()

    crawler = KeywordCrawler(args.root_path)
    matches = crawler.crawl(args.keyword)

    found = False
    for file_path, lineno, line in matches:
        found = True
        print_match(file_path, lineno, line)

    if not found:
        print(f"No matches found for keyword '{args.keyword}' in {args.root_path}")

if __name__ == "__main__":
    main()
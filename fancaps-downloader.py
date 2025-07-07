import argparse
from scraper.crawler import Crawler
from scraper.downloader import Downloader
from scraper.utils.colors import Colors
import os

parser = argparse.ArgumentParser()
parser.add_argument('url', nargs='?', help='Url to start download')
parser.add_argument('--output', type=str, default="Downloads", help='Path of folder')
parser.add_argument("--slow", action="store_true", help="Slower download(for older or smaller images that finish faster and hit the new rate limit)")
args = parser.parse_args()

if __name__ == "__main__":
    # Crawl
    crawler = Crawler()
    links = crawler.crawl(args.url)

    # Download
    downloader = Downloader()
    for item in links:
        Colors.print(f"Download to {item['subfolder']} started:", Colors.YELLOW)
        path = os.path.join(args.output, item['subfolder'])
        if not args.slow:
            downloader.downloadUrls(path, item['links'])
        else:
            downloader.downloadUrlsSlow(path, item['links'])
import requests
import pikabu_headers
import re
from collections import defaultdict

class PikabuGrabber:
    HEADERS_PAGING = pikabu_headers.HEADERS_PAGING
    HOME = "https://pikabu.ru"

    def __init__(self):
        self.session = requests.Session()
        self.post_counter = 0
        self.tags = defaultdict(int)
        self.session.headers = self.HEADERS_PAGING

    def collect_posts(self, page):
        url = f"https://pikabu.ru/?twitmode=1&of=v2&page={page}"
        paging_resp = self.session.get(url)
        paging_resp.encoding = "utf-8"
        stories = paging_resp.json()["data"]["stories"]
        for story in stories:
            print(story["id"])
            if self.post_counter < 100:
                self.post_counter += 1
                tags = re.findall(r'(data-tag=")([^"]*?)(")', story["html"])
                for tag in [i[1] for i in tags]:
                    self.tags[tag] += 1
            else:
                break

    def get_stats(self):
        i = 1
        while self.post_counter < 100:
            self.collect_posts(i)
            i += 1
            print(self.post_counter)

        tags = sorted(self.tags, key=lambda x: self.tags[x], reverse=True)
        with open("tags_stats.txt", "w", encoding="utf-8") as tags_stats:
            for tag in tags[:10]:
                tags_stats.write(f"{tag}: {self.tags[tag]}\n")


pg = PikabuGrabber()
pg.get_stats()

from collections import Counter
import csv
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        status = item['status']
        self.counter.update([status])
        return item

    def close_spider(self, spider):
        current_datetime = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )
        dir_results = BASE_DIR / 'results'
        dir_results.mkdir(exist_ok=True)
        filename = dir_results / f'status_summary_{current_datetime}.csv'
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writter = csv.writer(f)
            writter.writerow(['Статус', 'Количество'])
            for status, count in self.counter.items():
                writter.writerow([status, count])
            total_count = sum(self.counter.values())
            writter.writerow(['Total', total_count])

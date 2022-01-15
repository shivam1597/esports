# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import pandas as pd
import csv
import cloudinary.uploader


class EsportsscraperPipeline:

    def __init__(self):
        cloudinary.config(
            cloud_name="shivam1519",
            api_key="854775435856326",
            api_secret="HvYInSsrqgYDlL0t8ILlS2H-mqk"
        )
        self.header_list = ['thumbnail_url', 'video_url']

    def open_spider(self, spider):
        self.file = open('esports.csv', mode='w+', encoding='utf-8', errors='ignore', newline='')
        self.writer = csv.DictWriter(self.file, delimiter=",", fieldnames=self.header_list)
        self.writer.writeheader()


    def close_spider(self, spider):
        self.file.close()
        df = pd.read_csv('esports.csv', sep="\t or ,")
        df.drop_duplicates(subset=None, inplace=True)
        with open('esports.csv', mode='r+', encoding='utf-8', errors='ignore') as f:
            cloudinary.uploader.upload(f.name, resource_type='raw', use_filename=True, invalidate=True,
                                       unique_filename=False, version=False)
            f.close()

        if os.path.exists('esports.csv'):
            os.remove('esports.csv')

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

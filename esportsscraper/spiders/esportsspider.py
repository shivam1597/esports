import scrapy
from scrapy.http import Request
from ..items import EsportsscraperItem
import re

class UserNameSpider(scrapy.Spider):

    name = "spider"

    def start_requests(self):
        cookie = """
            mid=YcnGnAALAAEWcbzoWV2xDGmk4i8m; ig_did=89023BF5-47EE-4968-AE75-FA990E468C03; ig_nrcb=1; csrftoken=SiFf5cGaTRMR6DC0qjzpnDu5Db6DZoCr; ds_user_id=4229762617; sessionid=4229762617%3AJi0ZKoztxeUxmF%3A24; fbm_124024574287414=base_domain=.instagram.com; shbid="19445\0544229762617\0541673543793:01f7901cc43fd183d179a5bcca397d3cdda3445836d54fa584e54bca885fbcc4957c821c"; shbts="1642007793\0544229762617\0541673543793:01f70b4875129244fb1f9d296f5228213cd4522335aa501f6baa7e2dcb5d0d2f5a986729"; fbsr_124024574287414=Kdu2tFuNzyVx2Orq64QJm5Iqr3inCARGAUCN9rCFbEQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDY3NDMyMDY5IiwiY29kZSI6IkFRREI3aFBCRnh4X2JaOWU2dTFjMFo0bWY5eHhNVnlZRzVOV2EyYUNjeVZTdDhXczNiUmtCb1Z2ZGZnazU4dXQ2a1NKOUZieVhNdG80RF9LUDZmM0ItaDFBS0cwVVdpenJPZ2NnaUctNkxhMk9oWDNRcE1uYnkxeUlaOGlBcGpNS1Z5bkJYNnBVNi05aFF1X2ZHV1JxQm05SFQwVDBwVThVYnRlYjRCXzZpd08yczlnZHB4Ym03TWtYVWlaakhvTVVXZFd5MTJIN3VIYkJHLVYwNEJybzh6bEpVdXphVkVNZ3BZR2huSkJEaUYtZWVaN2pUNVdRZHBJOWtRMjlpS0FGaVh5T0V6cUpBbl9PU1F4Vm83eUNHQkR2WFJzendKVWRXU2JTSkNISDJSdGl6Zkp6ZDhaa3daUDczcklLQkQ2ZWVyLXl4bE1makpIekVlV25wSUplbUpqYjRNS3VBT3dXSnVNVFlrWVFhWFJoUSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFCb0xCS3U5cm1IUkExUmRTdlpCQzdCYnd4T1FCTXlrOWk4cXJLaTBFQ3NFUlpDTkpvZUhIUG05blVBamNEczZqb1pBV2hQV1dOWkNrYUlrZnNkRFIxRVpDdGFoT3dBWXpiRDVTYUUzVG5aQTU5QVpDQ2xxNmZlNVJYZXBuNklSbUJrYzlzM3dnNVdnRW1aQzVjOWZtbHNaQlpCVFpBeHEzVlZIUTVpNWxsTG42bWMiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY0MjE0NTI5MX0; fbsr_124024574287414=pcA9xhWo5JsyMBFwi34boX5rccKQahdvuy8Shdby0Tw.eyJ1c2VyX2lkIjoiMTAwMDM5MDY3NDMyMDY5IiwiY29kZSI6IkFRQUp3aElhdlRKUWFCM0lEWTNINjlGN2VlM3RlallGTUtYZzdMUjdudVp0SVM1aWY3WDIxb1ZxWDBKUncxQk9xZVRGbHQ3RHlfQ0xmT1F0alNkWDluMzNfN0ZNRlNhOXhpTWxCNF9FT2dkcE5ZWDhMSFRVWTRJUEpZTVRtZGE5b2tMWFhfMk81MFlOeHUxdHJIV2pYanI4VVhxamtpR0VHSlYyY0p4YUx6MjZsVlY4NHIzYVpKV0xDakowY1RRWWJNbDJGX0NHNWQ5ZUlGUHBnaWZKcjNCaFJFZ0tPRlNCWXI1ZDdaWlRqMkdFcDZiVGxGV3dOMV9oRjl5bHNVYjJnX2VweE85VHUwUzhuYk90QVBCbURqeGJHZnF5NldJR3dkSVJOVzBPYTRGZklvOGVUcTRma1lmVlVuTXNoZkI5UGtwU1J4d1NtTG5aOU1NczFJcXM1SWdyeUVEUk5zSVRrbUE1X3pMU2VnTFFRQSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFHc3VzYU5PZlZaQTBxY0swZ0JGQTQzeGROdkV0QmVIYVRBWkNlY0FrQzA0SUYzTEFnbmozNTBvSHduQlFOVnF2Mm9QNERCQ0tiNGo0QXNRTmhMckdJTEFlZmJoMDZGbUYybXVLZkUwNzFCdzVxYVhYelpBbEVaQkhUS0FBY1M2WTNiWDdHWWdTa2J4UjZDTjg3Sm5iaWo1N2lteUgySWE3TWtWZmsyRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQyMTQ3MjcxfQ; rur="PRN\0544229762617\0541673683403:01f7d3878d9a716cc217210b7421fafec49f8959c82c11627eec15c1500a072ba010c781
            """
        headers = {
            "sec-ch-ua-platform": "Windows",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "cookie": cookie,
            "x-ig-app-id": "936619743392459",
        }
        end_cursor = "}"
        url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":"32830970734","first":"12"'+end_cursor
        self.logger.info(url)
        yield Request(url=url, headers=headers)

#32830970734 for BGMI X OFFICIAL™
#8019409743 for BGMI ESPORTS INDIA

    def parse(self, response, **kwargs):
        cookie = """mid=YcnGnAALAAEWcbzoWV2xDGmk4i8m; ig_did=89023BF5-47EE-4968-AE75-FA990E468C03; ig_nrcb=1; csrftoken=SiFf5cGaTRMR6DC0qjzpnDu5Db6DZoCr; ds_user_id=4229762617; sessionid=4229762617%3AJi0ZKoztxeUxmF%3A24; fbm_124024574287414=base_domain=.instagram.com; shbid="19445\0544229762617\0541673543793:01f7901cc43fd183d179a5bcca397d3cdda3445836d54fa584e54bca885fbcc4957c821c"; shbts="1642007793\0544229762617\0541673543793:01f70b4875129244fb1f9d296f5228213cd4522335aa501f6baa7e2dcb5d0d2f5a986729"; fbsr_124024574287414=Kdu2tFuNzyVx2Orq64QJm5Iqr3inCARGAUCN9rCFbEQ.eyJ1c2VyX2lkIjoiMTAwMDM5MDY3NDMyMDY5IiwiY29kZSI6IkFRREI3aFBCRnh4X2JaOWU2dTFjMFo0bWY5eHhNVnlZRzVOV2EyYUNjeVZTdDhXczNiUmtCb1Z2ZGZnazU4dXQ2a1NKOUZieVhNdG80RF9LUDZmM0ItaDFBS0cwVVdpenJPZ2NnaUctNkxhMk9oWDNRcE1uYnkxeUlaOGlBcGpNS1Z5bkJYNnBVNi05aFF1X2ZHV1JxQm05SFQwVDBwVThVYnRlYjRCXzZpd08yczlnZHB4Ym03TWtYVWlaakhvTVVXZFd5MTJIN3VIYkJHLVYwNEJybzh6bEpVdXphVkVNZ3BZR2huSkJEaUYtZWVaN2pUNVdRZHBJOWtRMjlpS0FGaVh5T0V6cUpBbl9PU1F4Vm83eUNHQkR2WFJzendKVWRXU2JTSkNISDJSdGl6Zkp6ZDhaa3daUDczcklLQkQ2ZWVyLXl4bE1makpIekVlV25wSUplbUpqYjRNS3VBT3dXSnVNVFlrWVFhWFJoUSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFCb0xCS3U5cm1IUkExUmRTdlpCQzdCYnd4T1FCTXlrOWk4cXJLaTBFQ3NFUlpDTkpvZUhIUG05blVBamNEczZqb1pBV2hQV1dOWkNrYUlrZnNkRFIxRVpDdGFoT3dBWXpiRDVTYUUzVG5aQTU5QVpDQ2xxNmZlNVJYZXBuNklSbUJrYzlzM3dnNVdnRW1aQzVjOWZtbHNaQlpCVFpBeHEzVlZIUTVpNWxsTG42bWMiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY0MjE0NTI5MX0; fbsr_124024574287414=pcA9xhWo5JsyMBFwi34boX5rccKQahdvuy8Shdby0Tw.eyJ1c2VyX2lkIjoiMTAwMDM5MDY3NDMyMDY5IiwiY29kZSI6IkFRQUp3aElhdlRKUWFCM0lEWTNINjlGN2VlM3RlallGTUtYZzdMUjdudVp0SVM1aWY3WDIxb1ZxWDBKUncxQk9xZVRGbHQ3RHlfQ0xmT1F0alNkWDluMzNfN0ZNRlNhOXhpTWxCNF9FT2dkcE5ZWDhMSFRVWTRJUEpZTVRtZGE5b2tMWFhfMk81MFlOeHUxdHJIV2pYanI4VVhxamtpR0VHSlYyY0p4YUx6MjZsVlY4NHIzYVpKV0xDakowY1RRWWJNbDJGX0NHNWQ5ZUlGUHBnaWZKcjNCaFJFZ0tPRlNCWXI1ZDdaWlRqMkdFcDZiVGxGV3dOMV9oRjl5bHNVYjJnX2VweE85VHUwUzhuYk90QVBCbURqeGJHZnF5NldJR3dkSVJOVzBPYTRGZklvOGVUcTRma1lmVlVuTXNoZkI5UGtwU1J4d1NtTG5aOU1NczFJcXM1SWdyeUVEUk5zSVRrbUE1X3pMU2VnTFFRQSIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFHc3VzYU5PZlZaQTBxY0swZ0JGQTQzeGROdkV0QmVIYVRBWkNlY0FrQzA0SUYzTEFnbmozNTBvSHduQlFOVnF2Mm9QNERCQ0tiNGo0QXNRTmhMckdJTEFlZmJoMDZGbUYybXVLZkUwNzFCdzVxYVhYelpBbEVaQkhUS0FBY1M2WTNiWDdHWWdTa2J4UjZDTjg3Sm5iaWo1N2lteUgySWE3TWtWZmsyRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjQyMTQ3MjcxfQ; rur="PRN\0544229762617\0541673683403:01f7d3878d9a716cc217210b7421fafec49f8959c82c11627eec15c1500a072ba010c781"""
        item = EsportsscraperItem()
        response_object = response.json()
        post_response = response_object['data']['user']['edge_owner_to_timeline_media']['edges']
        for edges in post_response:
            if not edges['node']['edge_media_to_caption']['edges']:
                pass
            else:
                if edges['node']['is_video']:
                    item['thumbnail_url'] = edges['node']['display_url']
                    item['video_url'] = edges['node']['video_url']
                    yield item
        end_cursor = "}"
        headers = {
            "sec-ch-ua-platform": "Windows",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "cookie": cookie,
            "x-ig-app-id": "936619743392459",
        }
        if response_object['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']:
            end_cursor = ',"after":"' + response_object['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']+'"}'
            url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":"32830970734","first":"12"' + end_cursor
            yield Request(url=url, headers=headers, callback=self.parse)
        else:
            url = 'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables={"id":"8019409743","first":"12"' + end_cursor
            yield Request(url=url, headers=headers, callback=self.parse)

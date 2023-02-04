import requests
import json

headers = {
    "Referer": "https://m.douban.com/tv/american",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}


resp = requests.get('https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%22%E5%9C%B0%E5%8C%BA%22:%22%E5%8D%8E%E8%AF%AD%22%7D&uncollect=false&tags=%E5%8D%8E%E8%AF%AD', headers=headers)
for item in json.loads(resp.content.decode())['items']:
    print(item['title'], item['rating']['value'])
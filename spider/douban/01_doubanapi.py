import requests

page_limit = 50
page_start = 0


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

all_data = []

while True:
    print(f'get page start: {page_start}')
    # resp = requests.get(url=f'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&page_limit={page_limit}&page_start={page_start}',
    #                     headers={'User-Agent': user_agent})
    resp = requests.get(
        url=f'https://movie.douban.com/j/search_subjects?type=tv&tag=热门&page_limit={page_limit}&page_start={page_start}',
        headers={'User-Agent': user_agent})
    if resp.status_code != 200 or len(resp.json()['subjects']) == 0:
        break
    all_data += resp.json()['subjects']
    page_start += page_limit

print(len(all_data))


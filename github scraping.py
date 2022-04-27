import requests
from bs4 import BeautifulSoup
from xlwt import Workbook


cookies = {
    '_device_id': '45c2082881d049a05003cba2893c8f98',
    '_octo': 'GH1.1.576195488.1650708514',
    'user_session': 'V5BKkOvaC2BFEYxmItidg8wICkZa_DeVLzlH_t9Emgjsm_Np',
    '__Host-user_session_same_site': 'V5BKkOvaC2BFEYxmItidg8wICkZa_DeVLzlH_t9Emgjsm_Np',
    'logged_in': 'yes',
    'dotcom_user': 'thamer-ctrl',
    'tz': 'Africa%2FTunis',
    'color_mode': '%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'has_recent_activity': '1',
    '_gh_sess': '00I3ye34Ec9330mVa0U9jluJM8mkeiAo7A9W9NWWCcoWRTocO5DDm91hsDfSNfXpvQaMEjJcGxiu30AXDlySBXCwllYfZoryFtSDMkwl7%2FVrbzFuMWboLGGDrunkiMATP4pK3vR1D%2BEAqQ7qA5VYeyz5gRLNchbWypr33SYlZtSBvL7wy4g5kYqbBLthj9IuE3UlgRU4hmEnrPFnzs11SsKKOPC%2FoiU6--lElvvOqGj%2Bfh8BOY--ibJ3AunDj%2BuJfnvUaMsQOw%3D%3D',
}

headers = {
    'authority': 'github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_device_id=45c2082881d049a05003cba2893c8f98; _octo=GH1.1.576195488.1650708514; user_session=V5BKkOvaC2BFEYxmItidg8wICkZa_DeVLzlH_t9Emgjsm_Np; __Host-user_session_same_site=V5BKkOvaC2BFEYxmItidg8wICkZa_DeVLzlH_t9Emgjsm_Np; logged_in=yes; dotcom_user=thamer-ctrl; tz=Africa%2FTunis; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; has_recent_activity=1; _gh_sess=00I3ye34Ec9330mVa0U9jluJM8mkeiAo7A9W9NWWCcoWRTocO5DDm91hsDfSNfXpvQaMEjJcGxiu30AXDlySBXCwllYfZoryFtSDMkwl7%2FVrbzFuMWboLGGDrunkiMATP4pK3vR1D%2BEAqQ7qA5VYeyz5gRLNchbWypr33SYlZtSBvL7wy4g5kYqbBLthj9IuE3UlgRU4hmEnrPFnzs11SsKKOPC%2FoiU6--lElvvOqGj%2Bfh8BOY--ibJ3AunDj%2BuJfnvUaMsQOw%3D%3D',
    'if-none-match': 'W/"6cd4f0c3302bbdeb30eb0aff569f8608"',
    'referer': 'https://github.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

j = 0
sites = []
title_list = []
url_list = []
for k in range(1,11):

    # https://github.com/search?p=1&q=filename%3Awp-config.php&type=Code
    response = requests.get('https://github.com/search?p='+str(k)+'&q=filename%3Awp-config.php&type=Code', cookies=cookies,
                            headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    response

    for i in soup.findAll("div", {"class": "f4 text-normal"}):
        j += 1
        # x= i.get("title")
        title = i.a.text
        url = "https://github.com" + i.a.get('href')
        print(j, ' Title: ', title, '  url: ', url)
        title_list.append(title)
        url_list.append(url)

for i in sites:
    print(i)

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#sheet1.write(0,0, ' id')
#sheet1.write(0,1, ' url')

x = len(url_list)
y = len(title_list)

for i in range(x):
    sheet1.write(i,0,title_list[i])

for i in range(y):
    sheet1.write(i, 1, url_list[i])

wb.save('final-data-github.xls')




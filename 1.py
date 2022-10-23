import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import tqdm
import time


data = {

    'data':[]
}
for page in range(1,41):
    url = f'https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page={page}&hhtmFrom=vacancy_search_list'
    resp = req.get(url, headers={'user-agent': UserAgent().chrome,
                                 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
    soup = BeautifulSoup(resp.text, "lxml")
    tag = soup.find_all(attrs={'class': 'serp-item__title'})
    for i in tqdm.tqdm(tag):
        time.sleep(2)
        url_object = i.attrs["href"]
        resp_object = req.get(url_object, headers={'user-agent': UserAgent().chrome,
                                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
        soup_object = BeautifulSoup(resp_object.text, "lxml")
        try:
            tag_work_experience = soup_object.find(attrs={'class':'vacancy-description-list-item'}).find(attrs={'data-qa':'vacancy-experience'}).text
        except AttributeError as ae:
            print('AttributeError' + str(ae))
        try:
            tag_price = soup_object.find(attrs={'data-qa': 'vacancy-salary'}).find(attrs={'data-qa': 'vacancy-salary-compensation-type-net'}).text
        except AttributeError as ae1:
            print('AttributeError' + str(ae1))
        try:
            tag_region = soup_object.find(attrs={'data-qa':'vacancy-view-location'}).text
        except AttributeError as ae2:
            print('AttributeError' + str(ae2))
        try:
            data['data'].append({'title':i.text, 'work_experience':tag_work_experience, 'salary':tag_price, 'region':tag_region})
        except NameError as ne:
            print('NameError' + str(ne))
        with open('data.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


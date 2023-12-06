from bs4 import BeautifulSoup
import json
import requests

from .models.group import Group
from .models.lesson import Lesson

import time
import os


def get_json(html):
    parser = BeautifulSoup(html, 'html.parser')
    table = parser.find('table')

    groups = [row.text.strip() for row in table.find_all('th', {'class': 'hcenter bold-left bold-right bold bkblue'})]

    nums = [
        row.text.strip() for row in table.find_all('td', {'class': 'bold-left midgray larger'})
    ]
    names = [
        ' '.join([name.text.strip() for name in row.find_all('div', {'class': 'hlane'})])
        for row in table.find_all('td', {'class': 'left bold nowrap'})
    ]
    rooms = [
        ' '.join([room.text.strip() for room in row.find_all('div', {'class': 'hlane reight darkgray'})])
        for row in table.find_all('td', {'class': 'right bold'})
    ]

    zip_lessons = [*zip(nums, names, rooms)]
    all_groups = {}

    for i in range(len(groups)):
        group = Group(groups[i])

        for j in range(0, len(zip_lessons), len(groups)):
            lesson = Lesson()
            lesson.num = zip_lessons[j + i][0]
            lesson.name = zip_lessons[j + i][1]
            lesson.room = zip_lessons[j + i][2]

            group.append(lesson)

        all_groups[groups[i]] = group.to_dict()

    with open('file.json', 'w') as file:
        json.dump(all_groups, file)


def load_info():
    resp = requests.get('https://live.1543.msk.ru/tt/school/').text
    get_json(resp)


def get_data():
    current_time = int(time.time())
    time_interval = int(os.environ.get('TIME_INTERVAL'))

    try:
        last_time = int(os.environ.get('LAST_TIME'))
    except TypeError:
        last_time = 0

    if current_time - last_time >= time_interval:
        os.environ['LAST_TIME'] = str(current_time)
        load_info()

    with open('file.json', 'r') as file:
        data = json.load(file)

    return data

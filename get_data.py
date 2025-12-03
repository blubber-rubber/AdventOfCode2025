import sys
import datetime
import requests
import webbrowser

HEADERS = {'cookie': ''}
YEAR = 2016


def get_input(day, year=YEAR):
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    response = requests.request("GET", url, headers=HEADERS)
    with open(f"Day{day.rjust(2,'0')}/input.txt", 'w') as f:
        f.write(response.text.rstrip('\n'))


day = 'c'


if day == 'c':    
    day = str(datetime.date.today().day)
    webbrowser.open(f"https://adventofcode.com/{YEAR}/day/{day}")
    get_input(day)
elif day == 'a':
    for day in range(int(args[0]), int(args[1]) + 1):
        get_input(str(day))
else:
    get_input(str(day))
    

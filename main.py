import requests
from bs4 import BeautifulSoup

user = input("Впишите никнейм нужного пользователя: ")

profile_url = 'https://www.eolymp.com/uk/users/'+user
profile_response = requests.get(profile_url)
profile_soup = BeautifulSoup(profile_response.text, 'lxml')

numbers = profile_soup.find_all('div', class_='eo-metric__value')
rating = numbers[0].text
solved = numbers[1].text
total_submissions = numbers[2].text
submits = numbers[3].text

print(f'Рейтинг пользователя {user}: {rating}')
print(f'Количество решенных задач: {solved}')
print(f'Всего отправок: {total_submissions}')
print(f'Количество засчитанных отправок: {submits}')

problems_url = 'https://www.eolymp.com/uk/users/'+user+'/submissions'
problems_response = requests.get(problems_url)
problems_soup = BeautifulSoup(problems_response.text, 'lxml')

problems = problems_soup.find_all('tr')
last_problem = problems[1].find_all('td', class_='mdl-data-table__cell--non-numeric')
last_problem_name = last_problem[1].find('a').text
last_problem_state = last_problem[4].find('a').text

if 'Зараховано' in last_problem_state:
    print(f'''Последняя задача "{last_problem_name}" пройдена на 100%''')
elif 'Частково зараховано' in last_problem_state:
    last_problem_percent = int((last_problem_state.split()[-1])[:-1])
    print(f'''Последняя задача "{last_problem_name}" пройдена на {last_problem_percent}%''')
else:
    print('Произошли технические шоколадки')
    print(last_problem_state)
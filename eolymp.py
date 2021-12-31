import requests
from bs4 import BeautifulSoup

class parser():
    def __init__(self, user):
        self.user = user


        self.profile_url = 'https://www.eolymp.com/uk/users/'+self.user
        self.profile_response = requests.get(self.profile_url)
        self.profile_soup = BeautifulSoup(self.profile_response.text, 'lxml')


        self.numbers = self.profile_soup.find_all('div', class_='eo-metric__value')

        self.rating = self.numbers[0].text
        self.solved = self.numbers[1].text
        self.total_submissions = self.numbers[2].text
        self.submits = self.numbers[3].text

        self.photo_div = self.profile_soup.find('div', class_='eo-user-profile__photo')
        self.photo=self.photo_div.find('img')
        self.photo_link = self.photo.get('src')

        #print(f'Рейтинг пользователя {user}: {rating}')
        #print(f'Количество решенных задач: {solved}')
        #print(f'Всего отправок: {total_submissions}')
        #print(f'Количество засчитанных отправок: {submits}')

        self.problems_url = 'https://www.eolymp.com/uk/users/'+self.user+'/submissions'
        self.problems_response = requests.get(self.problems_url)
        self.problems_soup = BeautifulSoup(self.problems_response.text, 'lxml')

        self.problems = self.problems_soup.find_all('tr')
        self.last_problem = self.problems[1].find_all('td', class_='mdl-data-table__cell--non-numeric')
        self.last_problem_name = self.last_problem[1].find('a').text
        self.last_problem_state = self.last_problem[4].find('a').text

    def get_profile_url(self):
        return self.profile_url

    def get_rating(self):
        return self.rating
    def get_solved(self):
        return self.solved
    def get_total_submissions(self):
        return self.total_submissions
    def get_submits(self):
        return self.submits

    def get_photo_link(self):
        return self.photo_link

    def get_last(self):
        if 'Зараховано' in self.last_problem_state:
             return f'''Последняя задача "{self.last_problem_name}" пройдена на 100%'''
        elif 'Частково зараховано' in self.last_problem_state:
            self.last_problem_percent = int((self.last_problem_state.split()[-1])[:-1])
            return f'''Последняя задача "{self.last_problem_name}" пройдена на {self.last_problem_percent}%'''
        else:
            return 'Произошли технические шоколадки при поиске последнего решения'

#user = parser('Andrey16')
#print(user.get_last())
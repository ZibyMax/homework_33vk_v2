import requests


class Vkontakte:
    id_vk = 0
    friends_vk =[]
    service_key = '497d9bc6497d9bc6497d9bc626491f5e8e4497d497d9bc6138c218f294555fb7cc65afd'

    def __init__(self, id_vk):
        self.id_vk = id_vk
        response = requests.get('https://api.vk.com/method/friends.get', {
            'user_id': self.id_vk,
            'access_token': self.service_key,
            'v': '5.74'
        })
        self.friends_vk = response.json()['response']['items']


def homework():
    first_vk = Vkontakte(424364020)
    second_vk = Vkontakte(183833498)

    mutual_friends = list(set(first_vk.friends_vk).intersection(second_vk.friends_vk))

    if mutual_friends:
        print('\nОбщие друзья (ссылки на страницы):')
        for friend in mutual_friends:
            print('https://vk.com/id{}'.format(friend))
    else:
        print('\nОбщих друзей нет')


homework()

import requests


def get_spell_info_by_name(spell_name):
    """
    :param spell_name:
    :return:
    """
    base_url = "https://www.dnd5eapi.co/api/spells/"
    search = f"{base_url}?name={spell_name}"
    list_result = requests.get(search)
    if list_result.status_code == 200:
        spell_list = list_result.json()
        if spell_list['count'] == 1:
            spell_url_name = spell_list['results'][0]['url'].split('/')[-1]
            return get_spell_info_url(spell_url_name)


def get_spell_info_url(url_name, session=None):
    base_url = "https://www.dnd5eapi.co/api/spells/"
    spell_url = f"{base_url}{url_name}"
    if session is not None:
        spell_info = session.get(spell_url)
    else:
        spell_info = requests.get(spell_url)
    if spell_info.status_code == 200:
        info = spell_info.json()
        useful_data = {'name': info['name'],
                       'school': info['school']['name'],
                       'ritual': info['ritual'],
                       'casting_time': info['casting_time'],
                       'range': info['range'],
                       'components': info['components'],
                       'concentration': info['concentration'],
                       'duration': info['duration'],
                       'description': ' '.join(info['desc']),
                       'level': info['level']
                       }
        return useful_data

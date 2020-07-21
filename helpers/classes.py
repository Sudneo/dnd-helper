import requests
from helpers import spells


def get_class_spells(class_name, level=None):
    url = f"https://www.dnd5eapi.co/api/classes/{class_name.lower()}/spells"
    spell_list = requests.get(url)
    class_spells = list()
    if spell_list.status_code == 200:
        spell_list_iterable = spell_list.json()['results']
        http_session = requests.session()
        for spell in spell_list_iterable:
            spell_description = spells.get_spell_info_url(spell['url'].split('/')[-1], http_session)
            if level is not None:
                if spell_description['level'] == level:
                    class_spells.append(spell_description)
            else:
                class_spells.append(spell_description)
    return class_spells

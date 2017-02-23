from pyramid.view import view_config
import random

def get_random_nickname():
    adjvs = ['golden', 'ruby', 'fuzzy', 'liquid', 'sour', 'snowy', 'blazing']
    nouns = ['shores', 'keys', 'peaks', 'smiles', 'jungles', 'skies', 'forests']

    return random.choice(adjvs) + ' ' + random.choice(nouns)

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    random_nickname = get_random_nickname()

    return {'project': 'pyramid project', 'nickname': random_nickname}


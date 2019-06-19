import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

import os 

path = '/Users/tstone/Documents/School/100DaysOfWeb/'\
'100daysofweb-with-python-course/days/009-012-modern-apis-starred/my_app'

os.chdir(path)

def _load_data():
    with open('marvel-wikia-data.json') as json_file:
        data = json.loads(json_file.read())
    return data

superheros = _load_data()
SUPER_HERO_NOT_FOUND = 'Super Hero not found'

class SuperHero(types.Type):
    id = validators.Integer(allow_null=True)
    name = validators.String(allow_null = True)
    ID = validators.Any(allow_null=True)
    ALIGN = validators.Any(allow_null = True)
    ALIVE = validators.Any(allow_null = True)

def list_sh() -> List[SuperHero]:
    return [SuperHero(superhero[1]) for superhero in sorted(superheros.items())]

def create_sh(sh: SuperHero) -> JSONResponse:
    sh_id = max(superheros.keys()) + 1
    print(sh_id)
    sh.id = sh_id
    print(sh.id)
    superheros[sh_id] = sh
    print(superheros[sh_id])
    return JSONResponse(SuperHero(sh), status_code=201)

def get_sh(sh_id: int) -> JSONResponse:
    sh = superheros.get(str(sh_id))
    if not sh:
        error = {'error': SUPER_HERO_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    return JSONResponse(SuperHero(sh), status_code=200)

def update_sh(sh_id: int, sh: SuperHero) -> JSONResponse:
    pass

def delete_sh(sh_id: int) -> JSONResponse:
    pass

routes = [
    Route('/', method='GET', handler=list_sh),
    Route('/', method='POST', handler=create_sh),
    Route('/{sh_id}/', method='GET', handler=get_sh),
    Route('/{sh_id}/', method='PUT', handler=update_sh),
    Route('/{sh_id}/', method='DELETE', handler=delete_sh),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)



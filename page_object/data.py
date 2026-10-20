import uuid
from page_object.config import ASSETS_DIR

_SUFFIX = uuid.uuid4().hex[:6]

DATA_REG = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'username': f'Иван{_SUFFIX}',
    'email': f'ivan_{_SUFFIX}@yandex.ru',
    'password': f'Test_password{_SUFFIX}'
}
DATA_AUTH = {
    'email': DATA_REG['username'],
    'password': DATA_REG['password'],
}

page_auth = 'Войти на сайт'

FILE_FOR_UPLOAD = ASSETS_DIR / "blinchiki_s_abrikosami.jpg"

DATA_RECIPE = {
    'recipe_title': f'Блины_{uuid.uuid4().hex[:6]}',
    'ingredient': 'блины',
    'weight': '100',
    'time': '10',
    'description': 'Блины — это традиционное блюдо русской кухни, представляющее собой тонкую лепёшку из жидкого теста, испечённую на сковороде. Их готовят на молоке, кефире, воде или с использованием дрожжей.'
}

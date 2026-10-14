import uuid
from page_object.config import ASSETS_DIR

DATA_REG = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'username': f'Иван{uuid.uuid4().hex[:6]}',
    'email': f'ivan_{uuid.uuid4().hex[:6]}@yandex.ru',
    'password': f'Ivan{uuid.uuid4().hex[:6]}'
}

DATA_AUTH = {
        'email': 'test14102026',
        'password': '123456789Po'
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

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     "NAME": "djangodocker",
    #     "USER": "djangodocker",
    #     "PASSWORD": "djangodocker",
    #     'HOST': 'db',
    #     'PORT': '3306',
    #     'CHARSET': 'utf8',
    #     'COLLATION': 'utf8_unicode_ci',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     },
    # },
}

from django.apps import AppConfig


class WebsiteAppConfig(AppConfig):
    name = 'djangodocker.apps.website'
    label = 'website'
    verbose_name = 'Website'

default_app_config = 'djangodocker.apps.website.WebsiteAppConfig'

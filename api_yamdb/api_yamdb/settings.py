import os
from split_settings.tools import include, optional


include(
    'settings/django_settings.py',
    'settings/project_settings.py'
)

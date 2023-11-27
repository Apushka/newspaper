import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')
django.setup()
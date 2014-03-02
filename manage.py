#!/usr/bin/env python
import os
import sys

def install_django_pdb(settings):
    """ install app `django_pdb`
    """
    settings.INSTALLED_APPS += ('django_pdb',)
    settings.MIDDLEWARE_CLASSES += ('django_pdb.middleware.PdbMiddleware',)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easy_use_django_pdb.settings")

    # use `django_pdb`
    from easy_use_django_pdb import settings
    install_django_pdb(settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

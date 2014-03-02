easy_use_django_pdb
===================

Show you how to use [django-pdb][1] in the easy way (with minimal modifications).

1. Install django-pdb
---------------------

    sudo pip install django-pdb

2. Use django-pdb in Django
---------------------------

Modify `manage.py` to add app `django-pdb` into settings dynamically.

    ...
    def install_django_pdb(settings):
	    "" install app `django_pdb`
		""
		settings.INSTALLED_APPS += ('django_pdb',)
		settings.MIDDLEWARE_CLASSES += ('django_pdb.middleware.PdbMiddleware',)"

    ...
	    # use `django_pdb`
		from use_django_pdb import settings
		install_django_pdb(settings)
    ...

3. Debug with django-pdb
------------------------

1) debug by pdb for every view

    python manage.py runserver --pdb

    GET /

2) debug by pdb for the specific view

    python manage.py runserver

    GET /?pdb


[1]: https://github.com/tomchristie/django-pdb

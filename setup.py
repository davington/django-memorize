#!/usr/bin/env python

from distutils.core import setup

if __name__ == '__main__':
    setup(name='django-memorize',
          description="Memorize your Django project's items with spaced repetition theory",
          author='Cristian Esquivias',
          author_email='cristian.esquivias@gmail.com',
          version='0.5',
          packages=['memorize'],
          url='http://code.google.com/p/django-memorize/',
    )

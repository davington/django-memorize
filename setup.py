#!/usr/bin/env python

# Copyright 2010 Cristian Esquivias

# This file is part of django-memorize.

# django-memorize is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# django-memorize is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General Public License
# along with django-memorize.  If not, see <http://www.gnu.org/licenses/>.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if __name__ == '__main__':
    setup(name='django-memorize',
          description="Memorize your Django project's items with spaced repetition theory",
          long_description=open('README', 'r').read(),
          author='Cristian Esquivias',
          author_email='cristian.esquivias@gmail.com',
          version='0.5.1',
          packages=['memorize'],
          url='http://code.google.com/p/django-memorize/',
          license='GPL',
          keywords='django flashcard learning',
          classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Topic :: Education',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
    )

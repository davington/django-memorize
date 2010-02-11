#!/usr/bin/env python

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

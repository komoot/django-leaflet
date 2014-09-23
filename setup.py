import os
from setuptools import setup, find_packages
import sys

here = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(here, 'README.rst')).read()
changes = open(os.path.join(here, 'README.rst')).read()

requires = ['Django']
if sys.version_info < (2, 7):
    requires += ['ordereddict']
elif (3, 0) > sys.version_info >= (2, 7):
    readme = str(readme.encode('utf-8'))
    changes = str(changes.encode('utf-8'))


setup(
    name='django-leaflet',
    version='0.14.2.dev0',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    url='https://github.com/makinacorpus/django-leaflet',
    download_url = "http://pypi.python.org/pypi/django-leaflet/",
    description="Use Leaflet in your django projects",
    long_description=readme + '\n\n' + changes,
    license='LPGL, see LICENSE file.',
    install_requires=requires,
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers  = ['Topic :: Utilities',
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3.3'],
)

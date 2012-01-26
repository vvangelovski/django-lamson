import os, sys
from setuptools import setup, find_packages

import django_lamson
from django_lamson import VERSION, __version__

if VERSION[-1] == 'final':
    STATUS = ['Development Status :: 5 - Production/Stable']
elif 'beta' in VERSION[-1]:
    STATUS = ['Development Status :: 4 - Beta']
else:
    STATUS = ['Development Status :: 3 - Alpha']

def get_readme():
    try:
        return  open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    except IOError:
        return ''

setup(
    name = 'django-lamson',
    version = __version__,
    packages = find_packages(exclude = ['testproject']),
    author = 'Vasil Vangelovski',
    author_email = 'vvangelovski@gmail.com',
    license = 'New BSD License (http://www.opensource.org/licenses/bsd-license.php)',
    description = 'Easy integration of lamson in django projects',
    long_description = get_readme(),
    url = 'https://github.com/vvangelovski/django-lamson',
    download_url = 'https://github.com/vvangelovski/django-lamson',
    include_package_data = True,
    zip_safe = False,
    install_requires=["lamson==1.1"],
    classifiers = STATUS + [
       'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Connect Four',
    'author': 'John Broxton, Nehemiah Newell',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'johnbroxton@gmai.com, nehemiah.newell@gmail.com',
    'version': '0.1',
    'install_requires': ['python3'],
    'packages': ['Connect4'],
    'scripts': [],
    'name': 'Connect Four Assignment'
}

setup(**config)

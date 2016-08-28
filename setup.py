from distutils.core import setup

VERSION = '0.3'

setup(
    name = 'expectorant',
    packages = ['expectorant'],
    description = 'RSpec style testing framework for Python',
    author = 'Winston Wolff',
    author_email = 'winston@nitidbit.com',
    url = 'https://github.com/winstonwolff/expectorant',

    version = VERSION,
    download_url = 'https://github.com/winstonwolff/expectorant/tarball/{}'.format(VERSION),

    keywords = ['testing', 'rspec', 'tdd'],
    entry_points = { 'console_scripts': [ 'expectorant=expectorant.runner:main' ] },
    classifiers = [],
)


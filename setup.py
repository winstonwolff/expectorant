from distutils.core import setup
setup(
    name = 'expectorant',
    packages = ['expectorant'],
    description = 'RSpec style testing framework for Python',
    author = 'Winston Wolff',
    author_email = 'winston@nitidbit.com',
    url = 'https://github.com/winstonwolff/expectorant',

    version = '0.2',
    download_url = 'https://github.com/winstonwolff/expectorant/tarball/0.2',

    keywords = ['testing', 'rspec', 'tdd'],
    entry_points = { 'console_scripts': [ 'expectorant=expectorant.runner:main' ] },
    classifiers = [],
)


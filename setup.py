from distutils.core import setup

VERSION = '0.4.1' # should match git tag

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
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: POSIX',
                   'Operating System :: MacOS :: MacOS X',
                   'Topic :: Software Development :: Testing',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 3.5',
                  ]
)


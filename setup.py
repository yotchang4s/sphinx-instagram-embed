#-*- coding:utf-8 -*-

import setuptools
import sphinx_instagram_embed as pkg


setuptools.setup(
    name=pkg.__name__,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'sphinx'
    ],
    author=pkg.__author__,
    license=pkg.__license__,
    url='https://github.com/yotchang/sphinx-instagram-embed',
    description='''embedding instagram's photo in sphinx''',
    long_description=pkg.__doc__,
)
#-*- coding:utf-8 -*-
u'''
Embedding Instagram's photo in sphinx
'''

__version__ = '1.0.0'
__author__ = 'yotchang'
__license__ = 'BSD'


def setup(app):
    from . import instagram

    app.add_node(instagram.instagram, html=(instagram.visit_node, instagram.depart_node))
    app.add_directive('instagram', instagram.InstagramDirective)

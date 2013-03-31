# -*- coding: utf-8 -*-
"""
    sphinx_instagram_embed
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2031 by yotchang
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.compat import Directive


class instagram(nodes.General, nodes.Element):
    pass


class InstagramDirective(Directive):
    has_content = True
    required_argument = 1
    optional_arguments = 1
    final_argument_whitespace = False
    option_spec = {
        "size": directives.unchanged,
    }

    def run(self):
        size = "m"
        if("size" in self.options):
            options_size = self.options["size"]
            if options_size == "thumbnail":
                size = "t"
            elif options_size == "medium":
                size = "m"
            elif options_size == "large":
                size = "l"
            else:
                raise ValueError('invalid size "%s"' % options_size)
        self.options[size] = size
        return [instagram(id=self.arguments[0], size=size)]


def visit_node(self, node):
    id = node["id"]
    size = node["size"]

    url = "http://instagram.com/p/%s" % id
    image_url = url + "/media?size=%s" % size

    self.body.append('<div class="instagram">')
    self.body.append('<a href="%s">' % (url))
    self.body.append('<img class="%s" src="%s"/>' % (id, image_url))
    self.body.append('</a>')
    self.body.append('</div>')


def depart_node(self, node):
    pass

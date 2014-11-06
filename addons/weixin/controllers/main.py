#coding:utf-8

from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.tools.translate import _

import json


class Weixin(http.Controller):
    @http.route(['/weixin'], type='http',auth="public", website=True)
    def weixin_reload(self):
        print '*'*10
        return {'a':'a'}



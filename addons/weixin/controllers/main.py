#coding:utf-8

from openerp.addons.web import http
from openerp.addons.web.http import request
from openerp.tools.translate import _

import json
import hashlib
#hashlib.sha1('This is a sha1 test!').hexdigest()

class Weixin(http.Controller):
    @http.route(['/weixin'], type='http',auth="public", website=True)
    def weixin_reload(self,signature,timestamp,nonce,echostr):
        print '*'*10
        param_list=[timestamp,nonce,echostr]
        param_list.sort()
        param=[str(a) for a in param_list]
        signature_bak=''.join(param)
        if signature==hashlib.sha1(signature_bak).hexdigest:
            print 'True'
        return {'a':'a'}



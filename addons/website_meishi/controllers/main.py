#coding:utf-8
from openerp import http
from openerp.http import request
import datetime
import random

IMG_URL="/website/image/%s/%s/%s"

class Meishi(http.Controller):
    @http.route('/meishi/',auth='public')
    def index(self):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        meishi=request.env['website.meishi']
        myechan=request.env['website.myechan']

        meishi=meishi.search([])
        ids=list(meishi._ids)
        random_id=random.sample(ids,1)
        meishi_random=meishi.browse(random_id)
        return http.request.render('website_meishi.index',{
                'meishi':meishi_random,
                'myechan':myechan.search([])
                })



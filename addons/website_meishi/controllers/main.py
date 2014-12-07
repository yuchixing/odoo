#coding:utf-8
from openerp import http
from openerp.http import request

class Meishi(http.Controller):
    @http.route('/meishi/',auth='public')
    def index(self):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        meishi=request.env['website.meishi']
        print "teachers==",meishi.search([])
        return http.request.render('website_meishi.index',{
                'meishi':meishi.search([])
                })



#coding:utf-8

from openerp.osv import fields, osv
from openerp import tools, api

class Myechan(osv.Model):
    _name='website.myechan'

    _columns={
        'image':fields.binary("图片"),
        'taobao':fields.integer('淘宝成交量'),
        'erp':fields.integer('erp成交量'),
        'taobao_url':fields.char('淘宝url'),
        'erpshop_url':fields.char('erpurl'),
    }
class Meishi(osv.Model):
    _name='website.meishi'

    @api.multi
    def _get_image(self, name, args):
        return dict((p.id, tools.image_get_resized_images(p.image)) for p in self)

    @api.one
    def _set_image(self, name, value, args):
        return self.write({'image': tools.image_resize_image_big(value)})

    @api.multi
    def _has_image(self, name, args):
        return dict((p.id, bool(p.image)) for p in self)

    @api.multi
    def get_meishi_context(self):
        import requests
        from bs4 import BeautifulSoup
        url="http://home.meishichina.com/search.php?q=鹅蛋&type=all&cs=utf8&befrom=index"

        text=requests.get(url).text
        b=BeautifulSoup(text)
        c=b.find_all('div',class_='detail')

        for d in c:
            title=d.a.text
            href=d.a['href']
            text2=requests.get(href)
            bb=BeautifulSoup(text2)
            cc=bb.find('a',class_='J_photo')
            m_image=cc.img['src']
            m_text=d.find('div',id='block_txt1').text
            m_context_div=d.find_all('div',class_='recipeCategory_sub_R')
            i=1
            str=''
            for t in m_context:
                str+="%s,%s;"%(i,t.text)
                i+=1
            m_context=str




    _columns={
        'title':fields.char(u'菜名'),
        'text':fields.text(u'简介'),
        'meishi_line':fields.one2many('website.meishi.line','meishi_id',u'步骤'),
        'image':fields.binary("成品图片",help="1024x1024px"),
        #'session_id': fields.many2one('website.meishi.session', u'session', required=False, select=True,),# readonly=True),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized image", type="binary", multi="_get_image",
            store={
                'res.partner': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized image of this contact. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'context':fields.char(u'源材料'),
        #'is_push':fields.boolean('已查看')
}




class Meishiline(osv.Model):
    _name='website.meishi.line'

    _columns={
        'squene':fields.integer(u'序号'),
        'text':fields.text(u'步骤说明'),
        'image':fields.binary("图片",help="1024x1024px"),
        'meishi_id': fields.many2one('website.meishi', u'美食', required=False, ondelete='cascade', select=True),

    }

class Meishisession(osv.Model):
    _name='website.meishi.session'
    _columns={
        'name':fields.char(u'session'),
        #'meishi_id':fields.one2many('website.meishi','session_id',u'美食'),

    }

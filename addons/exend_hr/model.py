#coding:utf-8
from openerp.osv import osv,fields
from openerp import tools

class ScheduleShiftChild(osv.osv):
    _name="schedule.shift.child"
    _description='班段'

    _columns={
        'name':fields.char(u'班段名称'),
        'st':fields.time(u'开始时间'),
        'et':fields.time(u'结束时间'),
        'record':fields.text(u'备注'),
    }
class ScheduleShift(osv.osv):
    _name="schedule.shift"
    
    _inherit=['mail.thread']

    _columns={
        'name':fields.char(u"班次名称"),
        'child_shift':fields.many2one("schedule.shift.child",u'班段')

    }
    
    




#coding:utf-8
from openerp.osv import osv,fields
from openerp import tools

class ScheduleShiftChild(osv.osv):
    _name="schedule.shift.child"

    _column={
        'name':fields.char(u'班段名称'),
        'st':fields.time(u'开始时间'),
        'et':fields.time(u'结束时间'),
        'record':fields.text(u'备注')
    }
class ScheduleShift(osv.osv):
    _name="schedule.shift"

    _column={
        'name':fields.char(u"班次名称"),
        'child_shift':fields.many2one(u'班段')

    }




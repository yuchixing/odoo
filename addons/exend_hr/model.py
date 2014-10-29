#coding:utf-8
from openerp.osv import osv,fields
from openerp import tools
from openerp import api

class ScheduleShiftChild(osv.osv):
    _name="schedule.shift.child"
    _description='班段'

    _columns={
        'name':fields.char(u'班段名称'),
        'st':fields.time(u'开始时间'),
        'et':fields.time(u'结束时间'),
        'record':fields.text(u'备注'),
    }

class ScheduleConfig(osv.osv):
    _name="schedule.config"

    _inherit=['mail.thread','res.config.settings']

    _columns={


    }
class ScheduleShift(osv.osv):
    _name="schedule.shift"

    _inherit=['mail.thread']

    @api.v8
    def _get_shift_type(self):
        return (
                ('fixed',u"固定班段"),
                ('freedom',u"自由班段"),
            )

    _columns={
        'name':fields.char(u"班次名称"),
        'shift_type':fields.selection(_get_shift_type,u"班次类型"),
        'st_shift':fields.many2one("schedule.shift.child",u"上班班段"),
        'et_shift':fields.many2one("schedule.shift.child",u"下班班段"),
        'mt_shift':fields.many2one("schedule.shift.child",u"吃饭班段"),
    }






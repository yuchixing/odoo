#coding:utf-8
from openerp.osv import osv,fields
from openerp import tools
from openerp import api

class hr_employee(osv.osv):
    _inherit='hr.employee'
    
    _columns={
              'employee_no':fields.char(u"员工号"),
              }
    
class ScheduleShiftChild(osv.osv):
    _name="schedule.shift.child"
    _description=u'班段'

    _columns={
        'name':fields.char(u'班段名称'),
        'st':fields.time(u'开始时间'),
        'et':fields.time(u'结束时间'),
        'record':fields.text(u'备注'),
    }

class ScheduleConfig(osv.osv):
    _name="schedule.config"

    _inherit=['mail.thread']

    @api.v8
    def _get_week(self):
        return (
                ('one',u"星期天"),
                ('two',u"周六日")
                )
    _columns={
              'name':fields.char(u"规则名称"),
              'week':fields.selection(_get_week,u"周日"),
    }
    
    _default={
              'week':'two'
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
        'st_shift':fields.many2one("schedule.shift.child",u"上午班段"),
        'et_shift':fields.many2one("schedule.shift.child",u"下午班段"),
        'mt_shift':fields.many2one("schedule.shift.child",u"吃饭班段"),
    }

###
class ScheduleArrange(osv.osv):
    _name="schedule.arrange"
    _inherit=['mail.thread']
    
    #按人员是硬绑定，其它是软绑定
    @api.v8
    def _get_user_add_type(self):
        return (
                ('department',u"按部门"),
                ('user',u"按人员"),
                ('category',u"按标签"),
                )
        
    def onchange_type(self, cr, uid, ids, user_add_type, context=None):
        print "user_add_type=",user_add_type
        res={}
        values={
                'user_id':False,
                'category_id':False,
                'department_id':False
                }
        key="%s_id"%user_add_type
        del values[key]
        res['value']=values
        print "res=",res
        return res
        
    _columns={
              'name':fields.char(u"排班名称"),
              'st':fields.date(u"开始日期"),
              'et':fields.date(u"结束日期"),
              'user_add_type':fields.selection(_get_user_add_type,u"添加人员方式"),
              'user_id':fields.one2many("hr.employee","user_id",u"考勤人员"),
              'shift_id':fields.many2one("schedule.shift",u"班次"),
              'department_id':fields.many2one("hr.department","department_id",u"部门"),
              'category_id': fields.many2one('hr.employee.category',"category_id", u"员工标签"),
              "schedule_config":fields.many2one("schedule.config",u"考勤规则"),
              
              }


class ScheduleCatalog(osv.osv):
    _name="schedule.catalog"
    _inherit=['mail.thread']
    _columns={
              'device_no':fields.char(u"设备序列号"),
              'record_time':fields.datetime(u'打卡时间'),
              'record_employee':fields.char(u"员工号"),
              'record_cardno':fields.char(u"卡号")
        }

























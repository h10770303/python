#coding=utf-8

import calendar;  # 引入日历模块

# cal=calendar.month(2016,5,20)
# print "输出某个月份的日历："
# print  cal

#全年日历：
# calYear=calendar.calendar(2016,4,1,7,3)
# print "输出2016年的日历："
# print calYear

#输出一周的第一天默认为0 即星期一
# fristWeekDay=calendar.firstweekday();
# print fristWeekDay

# print calendar.monthrange(2016,05)





#
# import  time;  #引入模块  时间模块
# timetruck=time.time()
# print  timetruck
#
# # 本地时间‘  time.struct_time(tm_year=2016, tm_mon=5, tm_mday=10, tm_hour=16, tm_min=43, tm_sec=45, tm_wday=1, tm_yday=131, tm_isdst=0)
# s_time=time.localtime(time.time())
# print  s_time
#
# #格式化时间
# formatTime=time.asctime(s_time)
# print  formatTime
#
# #格式化日期L:
# strTime=time.strftime('%Y-%m-%d %H:%M:%S',s_time)
# print strTime
#
# #将时间转为时间戳
# timetruck2=time.mktime(s_time)
# print  timetruck2
#
# # cpu的时间’
# cpuTime=time.clock()
# print "cpu的时间：",cpuTime
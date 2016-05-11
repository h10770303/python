#coding=utf-8
i=9
#################for ---###################################
# vars="humingwei" # 循环字符串
# for letter in vars:
#     print "当前字母：",letter
# print "end"

ints=[1,2,3,4,5,6]
# for i in ints:
#     if i==3:
#         continue
#     print i
# else: print 'end'

for i in range(len(ints)):
    print "内容：",ints[i]
    print "序号：",i


#################while#######################################
# while (i>1):
#     print "当前循环的数字为：",i
#     i=i-1; # python 中没有++ --
# print "end";

# continue的使用
# while i>1:
#     i-=1;
#     if i==5:
#         continue
#     print "this is i:", i
# print "end"

#使用break 跳出循环
# while 1:
#     # print "i:",i
#     i-=1
#     if i==3:
#         break
#     print "this is i:",i
# print "end"

#whlie 与else 结合使用
# while i>0:
#     print "this is i:",i
#     i-=1
# else:print "end"


# coding=utf-8

###############return################
def functionname(a,b):
    print a+b

print  functionname(2,5)


############匿名函数######################
# sumNumber = lambda a, b, c: a + b + c
# print sumNumber(1, 2, 4)
# # print sumNumber(1,2,4,5)  报错

###############函数的参数######################
# 必须参数
# def functionname1(a,b):
#     return a+b
# # print functionname1();# 会报错
# print  "必须参数：",functionname1(2,4)
# #关键词参数
# print "关键词参数：",functionname1(b=8,a=10)

# 不定参数
# def functionname2(a,*vartuble):
#     print "第一个参数：",a
#     for var in vartuble:
#         print "不定的参数",var
#         a+=var
#     return "最后输出结果：",a
#
# print functionname2(1,2,3,4);
# print functionname2(1,2,3,4,5,6,7,8,9)

# 缺省参数
# def functioname(a,b=5):
#     return  a+b
#
# print functioname(a=2)
# print functioname(2,4)

###################函数的基本语句###########################
# #定义函数
# def addnumeber(a,b):
#     return a+b
#
# #重写print方法
# def println(str):
#     print "输出：",str
#     return
#
# #调用函数
# print addnumeber(3,4);
# println(addnumeber(3,4))

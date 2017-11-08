#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
'''
a=['1,5','2','3','4']
for i,v in enumerate(a):
   a[i].split(',')[0]='4'
#print(a)
#b='2.2'
#a[0]=b
print(a)
'''
# def person(name,age,sex,job):
#     def walk(p):
#         print("person %s is walking..." % p['name'])
#
#     data = {
#         'name':name,
#         'age':age,
#         'sex':sex,
#         'job':job,
#         'walk':walk
#     }
#
#     return data
#
# def dog(name,dog_type):
#
#
#     def bark(d):
#         print("dog %s:wang.wang..wang..."%d['name'])
#     data = {
#         'name':name,
#         'type':dog_type,
#         'bark':bark
#     }
#
#     return data
#
# d1 = dog("李磊","京巴")
# p1 = person("严帅",36,"F","运维")
# p2 = person("林海峰",27,"F","Teacher")
#
# d1['bark'](p1) #把人的对象传给了狗的方法
class dog:
    def __init__(self,role,dd):
        if role == 'aaa':
            print('xxx')
        self.role=role
        self.dd=dd
class bdog(dog):
    def __init__(self,dd):
        super(bdog,self).__init__('aaa',dd)

a=bdog('dd')
print(a)
#!/user/bin/env python3
# -*- coding: utf-8 -*-
# author:tony
def change1(file,file_dic):   #将文件转换为字典
    with open(file,'r+',encoding='utf-8') as f:
        for line in f:
            file_dic[line.split(':')[0]]=line.split(':')[1].strip()
uesrinf_dic={}
baclk_dic={}
change1('baclk',baclk_dic)
change1('uesrinf',uesrinf_dic)
print(uesrinf_dic)
count=0
while count < 3:
    username=input('用户名：')
    password=input('密码：')
    count+=1
    if username in baclk_dic:         #在黑名单内，已锁定
        print('用户已锁定,请找管理员')
        exit()
    if username in uesrinf_dic and password==str(uesrinf_dic[username]):
        print('成功登录')
        break
    if username in uesrinf_dic and password!=str(uesrinf_dic[username]):
        print('登录失败，请重新登录')
        continue
    else:
        print('用户不存在')
        count-=1
else:
    print('输入密码次数过多，用户已锁定')      #输错三次，加入黑名单，锁定用户
    with open('baclk','r+',encoding='utf-8') as f:
        f.write('%s:%s'%(username,uesrinf_dic[username]))


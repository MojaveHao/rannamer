import time
import random
mode = 0
nameshuliang = 46
name = ['苏雨涵', '甄灿豪', '刘轶玎', '曾翰轩', '曹沅沅', '梁竣杰', '李卓凡', '邹佳希', '陈政業', '周观涵', '彭梓琳', '曾凯迪', '廖梓希', '邓家明', '刘嘉琦', '刘梓鑫', '余文俊', '郭子艺', '李敏嘉', '杨子萱', '陈嘉彦', '李文杰', '吴臻郅', '王皓宁', '鄢子珊', '周致远', '高晨浩', '许可', '王贝宁', '黄佳妮', '游子轩', '孙俪铭', '李东炫', '卢嘉铭', '韩姚乐', '郝俊杰', '罗钰娴', '郭瑜萱', '唐依陶', '范利权', '黄旭瑞', '林太乙', '温金宝', '姚婧琳', '赵家康']
namelist = []
diyname = []
while True:
      if mode == 1:
            file_name = "name_list.txt"
            dataset = []
            file = open(file_name, mode='r',encoding="utf-8")
            for line in file:
                line = line.split()
                diyname.append(line)
                file.close()
      shuliang = int(input('输入1开始随机点名，输入2进入系统设置>>>'))
      if shuliang == 1:
            while True:
                  shuliang = input('请输入点名数量:')
                  a = str(random.sample(name,int(shuliang)))
                  namelist.append(a)
                  print(namelist)
                  if mode == 1:
                        name = []
                        name = diyname
                  if int(shuliang) > int(nameshuliang):
                        break
                  namelist = []
      if shuliang == 2:
            while True:
                  print("1.改变mode")
                  print("2.设置nameshuliang")
                  print("3.退出")
                  setlist = input("请输入序号：")
                  if int(setlist) == 1:
                        oldset = mode
                        mode = str(input("请输入数值："))
                        print("您改变了mode的数值，原为"+str(oldset)+"现为"+str(mode))
                  if int(setlist) == 2:
                        oldset = nameshuliang
                        nameshuliang = input("请输入数值：")
                        print("您改变了nameshuliang的数值，原为"+str(oldset)+"现为"+str(nameshuliang))
                  if int(setlist) < 1 or int(setlist) >2:
                        break
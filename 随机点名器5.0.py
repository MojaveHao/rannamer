import turtle
import time
import random
mode = 0  #如果将此项设为0，则使用默认的6（2）名库，设为1将尝试从同目录下的"name_list.txt"导入名字
diyname = []
nameshuliang = 46  #如果设置mode=1，则将此处的50改为班级学员数量，当mode=0时，此设置不生效
while True:
  if mode == 1:
    file_name = "name_list.txt"
    dataset = []
    file = open(file_name, mode='r',encoding="utf-8")
    for line in file:
      line = line.split()
      diyname.append(line)
    file.close()
  shuliang = int(input('请输入点名数量>>>'))
  if shuliang > 46:
    print("数值过大，请重新运行程序")
    time.sleep(2)
    exit()
  namelist = []
  name = ['苏雨涵', '甄灿豪', '刘轶玎', '曾翰轩', '曹沅沅', '梁竣杰', '李卓凡', '邹佳希', '陈政業', '周观涵', '彭梓琳', '曾凯迪', '廖梓希', '邓家明', '刘嘉琦', '刘梓鑫', '余文俊', '郭子艺', '李敏嘉', '杨子萱', '陈嘉彦', '李文杰', '吴臻郅', '王皓宁', '鄢子珊', '周致远', '高晨浩', '许可', '王贝宁', '黄佳妮', '游子轩', '孙俪铭', '李东炫', '卢嘉铭', '韩姚乐', '郝俊杰', '罗钰娴', '郭瑜萱', '唐依陶', '范利权', '黄旭瑞', '林太乙', '温金宝', '姚婧琳', '赵家康']
  if mode == 1:
    name = []
    name = diyname
    if shuliang > nameshuliang:
       print("数值过大，请重新运行程序")
       time.sleep(2)
       exit()
  else:
    a = str(random.sample(name,int(shuliang)))
    namelist.append(a)
  print(namelist)
time.sleep(5)
exit()

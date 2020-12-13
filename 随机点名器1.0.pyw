import turtle
import time
import random

__Pen = turtle.Pen()


__Pen.clear()
__Pen.pencolor("#ffff00")
__Pen.backward(200)
__Pen.write('python随机点名器', font = ('Arial', 35, 'normal'))
time.sleep(1)
__Pen.clear()
__Pen.pencolor("#66ffff")
name = ['苏雨涵', '甄灿豪', '刘轶玎', '曾翰轩', '曹沅沅', '梁竣杰', '李卓凡', '邹佳希', '陈政業', '周观涵', '彭梓琳', '曾凯迪', '廖梓希', '邓家明', '刘嘉琦', '刘梓鑫', '余文俊', '郭子艺', '李敏嘉', '杨子萱', '陈嘉彦', '李文杰', '吴臻郅', '王皓宁', '鄢子珊', '周致远', '高晨浩', '许可', '王贝宁', '黄佳妮', '游子轩', '孙俪铭', '李东炫', '卢嘉铭', '韩姚乐', '郝俊杰', '罗钰娴', '郭瑜萱', '唐依陶', '范利权', '黄旭瑞', '林太乙', '温金宝', '姚婧琳', '赵家康']
for i in range(10):
    a = str(random.choice(name))
__Pen.forward(100)
__Pen.write(a, font = ('Arial', 50, 'normal'))
time.sleep(5)

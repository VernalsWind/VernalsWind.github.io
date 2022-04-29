import PIL

import numpy as np
image=[]

for i in range(5,9):
    new=PIL.Image.open("{i}prec.jpg".format(i=i))
    image.append(new)
image[0].save('SST.gif',format='GIF',
     append_images=image[1: ],
     save_all=True,duration=0.5,
     loop=0)#相关参数设置可以网络搜索一下，duration是间隔速率
print('gif绘制完成')
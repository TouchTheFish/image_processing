import os
from PIL import Image
import math


def divide_big_to_small(rootdir, suffix, dsize, save_root, category_name=""):

    """
    注意，若图片不是原正方形,或者不能整除会有黑边
    将大图切成小图
    :param rootdir: 原图片路径
    :param suffix: 原图片后缀名
    :param dsize: 切割后的图片大小
    :param save_root: 结果图片保存目录
    :param category_name: 种类名称比如apple就是00001_apple.png
    """

    img_name_i = 1
    # rootdir = 'C:\\Users\\huang\\Desktop\\big_image'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if suffix in path.lower():
            # 你想对文件的操作
            img = Image.open(path)
            # plt.imshow(img)
            # plt.show()
            print('图片的大小为： {}'.format(img.size))
            if img.size[0] > img.size[1]:
                img_big_side = img.size[0]
            else:
                img_big_side = img.size[1]

            divide_num = math.ceil(img_big_side / dsize)

            left = 0  # 图片距离左边的宽度乘积值
            shang = 0  # 图片距离上边的宽度乘积值
            index = 0  # 图片名
            # 每行切成divide_num份，每列同样切成divide_num份
            for i in range(divide_num * divide_num):
                if i % divide_num == 0 and i != 0:
                    # 当循环到第divide_num个值时，需要切下一行的图片
                    shang += 1
                    left = 0
                a = dsize * left  # 图片距离左边的大小
                b = dsize * shang  # 图片距离上边的大小
                c = dsize * (left + 1)  # 图片距离左边的大小 + 图片自身宽度
                d = dsize * (shang + 1)  # 图片距离上边的大小 + 图片自身高度
                print('a= {},b= {},c= {}, d= {}'.format(a, b, c, d))
                croping = img.crop((a, b, c, d))
                temp_ = "_"
                if category_name == "":
                    temp_ = ""
                croping.save(save_root + "\\" + str(img_name_i).zfill(8) + temp_ + category_name + '.jpg')
                img_name_i = img_name_i + 1
                index += 1
                left += 1

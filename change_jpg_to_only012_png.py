import os
from PIL import Image
import numpy as np


def change_jpg_to_only012_png(root_dir, save_root, category_name=""):
    """
    该函数用于处理茶园遥感图像label，将1 2 255 和其他像素转化为0 1 2
    原图像：255代表背景，1   代表茶园，2   代表休耕茶园
    转化后：0  代表背景，1   代表茶园，2   代表休耕茶园

    :param root_dir: 原图片路径
    :param save_root: 保存结果路径
    :param category_name: 种类名称比如apple就是00001_apple.png
    """
    # root_dir = 'C:\\Users\\huang\\Desktop\\small_label'
    # 列出文件夹下所有的目录与文件
    jpg_list = os.listdir(root_dir)
    # 排序文件目录（0 1 2 3 ...）
    jpg_list.sort(key=lambda x: int(x[:-4]))
    # 打印该目录列表
    print(jpg_list)

    # 遍历文件夹
    for list_i in range(0, len(jpg_list)):
        # 读取一个文件目录
        path = os.path.join(root_dir, jpg_list[list_i])
        # 如果他是jpg文件
        if os.path.isfile(path):
            # 你想对文件的操作

            # 读取图片
            im = Image.open(path)
            # 读取图片的长和宽
            length = im.size[0]
            height = im.size[1]
            # 显示图片
            # plt.imshow(im)
            # plt.show()

            # 读成灰度图
            im = im.convert("L")
            # 获取像素点
            data = im.getdata()

            # 读成numpy，并reshape520*520
            data = np.matrix(data).reshape(length, height)

            # 获得图像的长宽
            [rows, cols] = data.shape
            # 遍历像素点
            for i in range(rows):
                for j in range(cols):
                    # 如果不是1 2 255
                    if data[i, j] != 1 and data[i, j] != 2 and data[i, j] != 255 and data[i, j] >= 127:
                        data[i, j] = 255
                    if data[i, j] != 1 and data[i, j] != 2 and data[i, j] != 255 and data[i, j] < 127:
                        data[i, j] = 1

                    # 将255转化为0，因为背景一般为0
                    if data[i, j] == 255:
                        data[i, j] = 0
                    # 遍历打印整个矩阵
                    # print(data[i, j], end="\t")
                # print()
                # print()

            # 打印矩阵
            print(data)
            # 打印
            print(data.shape)
            new_im = Image.fromarray(data.astype(np.uint8))
            # 显示图片
            # plt.imshow(new_im)
            # plt.show()

            # new_im.save("C:\\Users\\huang\\Desktop\\small_label_012\\" + str(list_i + 1) + ".png")
            temp_ = "_"
            if category_name == "":
                temp_ = ""
            new_im.save(save_root + "\\" + str(list_i + 1).zfill(8) + temp_ + category_name + ".png")
            color_arr = new_im.getcolors()
            print(color_arr)


import os
from PIL import ImageFilter
from PIL import Image
from impulse_noise import impulse_noise


def flip_horizontal(img_root, label_root, output_root_img, output_root_label):
    """
    用于图像增强
    :param img_root: 原图像目录
    :param label_root: 原label目录
    :param output_root_img: 输出增强图像目录
    :param output_root_label: 输出对应label目录
    """
    # 列出文件夹下所有的目录与文件
    img_list = os.listdir(img_root)
    # 遍历目录和文件
    for i in range(0, len(img_list)):
        # 读取原图像目录
        img_path = os.path.join(img_root, img_list[i])
        # 读取label目录
        label_path = os.path.join(label_root, img_list[i])
        label_path = label_path.replace(".jpg", ".png")
        if ".jpg" in img_path.lower():
            # 你想对文件的操作
            img = Image.open(img_path)
            label = Image.open(label_path)

            print("正在处理第%d张图片" % i)
            # 原图
            new_img = img
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_original_image" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_original_image" + ".png")

            # 高斯模糊
            new_img = img.filter(ImageFilter.GaussianBlur)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Gaussian_Blur" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Gaussian_Blur" + ".png")

            # 普通模糊
            new_img = img.filter(ImageFilter.BLUR)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Ordinary_fuzzy" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Ordinary_fuzzy" + ".png")

            # 边缘增强

            new_img = img.filter(ImageFilter.EDGE_ENHANCE)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_edge_enhancement" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_edge_enhancement" + ".png")

            # 平滑
            new_img = img.filter(ImageFilter.SMOOTH)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_smoothness" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_smoothness" + ".png")

            # 细节
            new_img = img.filter(ImageFilter.DETAIL)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_detail" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_detail" + ".png")

            # 旋转90
            new_img = img.rotate(90)
            new_img.save(output_root_img + "\\"
                         + "\\" + str(i + 1).zfill(8) + "_Rotate_it_90" + ".jpg")
            new_label = label.rotate(90)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Rotate_it_90" + ".png")

            # 旋转180
            new_img = img.rotate(180)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Rotate_it_180" + ".jpg")
            new_label = label.rotate(180)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Rotate_it_180" + ".png")

            # 旋转270
            new_img = img.rotate(270)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Rotate_it_270" + ".jpg")
            new_label = label.rotate(270)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Rotate_it_270" + ".png")

            # 水平翻转
            new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_flip_horizontal" + ".jpg")
            new_label = label.transpose(Image.FLIP_LEFT_RIGHT)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_flip_horizontal" + ".png")

            # 竖直翻转
            new_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_The_vertical_flip" + ".jpg")
            new_label = label.transpose(Image.FLIP_TOP_BOTTOM)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_The_vertical_flip" + ".png")

            # 像素矩阵转置
            new_img = img.transpose(Image.TRANSPOSE)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Pixel_matrix_transpose" + ".jpg")
            new_label = label.transpose(Image.TRANSPOSE)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Pixel_matrix_transpose" + ".png")

            # TRANSVERSE
            new_img = img.transpose(Image.TRANSVERSE)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_TRANSVERSE" + ".jpg")
            new_label = label.transpose(Image.TRANSVERSE)
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_TRANSVERSE" + ".png")

            # 胡椒噪声
            new_img = impulse_noise(img, 0.1).transpose(Image.TRANSVERSE)
            new_img.save(output_root_img + "\\"
                         + str(i + 1).zfill(8) + "_Pepper_noise" + ".jpg")
            new_label = label
            new_label.save(output_root_label + "\\"
                           + str(i + 1).zfill(8) + "_Pepper_noise" + ".png")

            print("第%d张图片处理完成" % i)
    print("全部完成！")

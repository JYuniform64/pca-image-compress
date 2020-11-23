import PIL.Image as Image
import os

IMAGES_PATH = 'image/'  # 图片集地址
IMAGES_FORMAT = ['.png']  # 图片格式
IMAGE_WIDTH = 168  # 每张小图片的大小
IMAGE_HEIGHT = 192
IMAGE_COLUMN = 10  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = 'final.png'  # 图片转换后的地址

# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]

def sort_keys(name):
    return int(name.split('.')[0].split('_')[-1])

image_names = sorted(image_names, key=sort_keys)
print(image_names)

IMAGE_ROW = len(image_names) // IMAGE_COLUMN


# 定义图像拼接函数
def image_compose():
    to_image = Image.new('L', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_HEIGHT, IMAGE_WIDTH), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_WIDTH, (y - 1) * IMAGE_HEIGHT))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


image_compose()  # 调用函数

import os

# 获取指定目录下所有图片文件的路径列表
image_dir = 'C:/Users/WCL/Desktop/新建文件夹'  # 将此处替换为存放图片的目录路径
file_list = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
i=151
for file_name in file_list:
    # 构建新的文件名（这里只是示例，根据需求自行调整）

    new_file_name = str(i) + '.jpg'

    # 重命名文件
    old_file_path = os.path.join(image_dir, file_name)
    new_file_path = os.path.join(image_dir, new_file_name)
    os.rename(old_file_path, new_file_path)
    i=i+1
print('图片文件名已成功更改！')
import os
import random

trainval_percent = 0.9
train_percent = 0.9
xmlfilepath = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/Annotations'
txtsavepath = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

# ftrainval = open('E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/ImageSets/trainval.txt', 'w')
ftest = open('E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/ImageSets/test.txt', 'w')
ftrain = open('E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/ImageSets/train.txt', 'w')
fval = open('E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        # ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

# ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

print("Done")
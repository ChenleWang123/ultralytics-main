#coding: utf-8
from ultralytics import YOLO
import matplotlib
matplotlib.use("TkAgg")
if __name__ == '__main__':
    #加载训练好的模型
    model = YOLO('E:/Programme/Python_Projects/ultralytics-main/ultralytics/runs/detect/train/v8-GAM3/weights/best.pt')
    # 对验证集进行评估
    metrics = model.val(data = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/my_dataset.yaml', name='val/val')
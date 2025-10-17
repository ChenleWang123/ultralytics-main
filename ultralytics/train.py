
from ultralytics import YOLO
if __name__ == '__main__':
    # 加载模型
    # model = YOLO("../ultralytics/cfg/models/v8/my_yolov8-GAN.yaml")  # 从头开始构建新模型
    model = YOLO("../ultralytics/cfg/models/v8/yolov8m.yaml")  # 从头开始构建新模型

    # Use the model
    results = model.train(data="E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/my_dataset.yaml"
                          , epochs=100, batch=2, workers=8, close_mosaic=0, name='train/train')  # 训练模型


    # results = model.val()  # 在验证集上评估模型性能
    # results = model("https://ultralytics.com/images/bus.jpg")  # 预测图像
    # success = model.export(format="onnx")  # 将模型导出为 ONNX 格式

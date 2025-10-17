# Ultralytics YOLO 🚀, AGPL-3.0 license

from ultralytics import RTDETR, YOLO
from ultralytics.utils import (
    ASSETS,
)

CFG = "E:/Programme/Python_Projects/ultralytics-main/ultralytics/cfg/models/v8/my_yolov8-GAM.yaml"
SOURCE = ASSETS / "bus.jpg"


def test_model_forward():
    """Test the forward pass of the YOLO model."""
    model = YOLO(CFG)
    model(source=None, imgsz=32, augment=True)  # also test no source and augment

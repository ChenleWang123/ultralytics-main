# Ultralytics YOLO 🚀, AGPL-3.0 license

from ultralytics.engine.predictor import BasePredictor
from ultralytics.engine.results import Results
from ultralytics.utils import ops, DEFAULT_CFG


class DetectionPredictor(BasePredictor):
    """
    A class extending the BasePredictor class for prediction based on a detection model.

    Example:
        ```python
        from ultralytics.utils import ASSETS
        from ultralytics.models.yolo.detect import DetectionPredictor

        args = dict(model='yolov8n.pt', source=ASSETS)
        predictor = DetectionPredictor(overrides=args)
        predictor.predict_cli()
        ```
    """

    def postprocess(self, preds, img, orig_imgs):
        """Post-processes predictions and returns a list of Results objects."""
        preds = ops.non_max_suppression(
            preds,
            self.args.conf,
            self.args.iou,
            agnostic=self.args.agnostic_nms,
            max_det=self.args.max_det,
            classes=self.args.classes,
        )

        if not isinstance(orig_imgs, list):  # input images are a torch.Tensor, not a list
            orig_imgs = ops.convert_torch2numpy_batch(orig_imgs)

        results = []
        for i, pred in enumerate(preds):
            orig_img = orig_imgs[i]
            pred[:, :4] = ops.scale_boxes(img.shape[2:], pred[:, :4], orig_img.shape)
            img_path = self.batch[0][i]
            results.append(Results(orig_img, path=img_path, names=self.model.names, boxes=pred))
        return results


def predict(cfg=DEFAULT_CFG, use_python=False):
    """Runs YOLO object detection on an image or video source."""
    model = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/runs/detect/train/v8x/weights/best.pt'
    # source = cfg.source or ASSETS
    # source = 'E:/Programme/Python_Projects/Graduation_Design/WCL/datasets/my_dataset/test.txt'
    # source = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/images'
    source = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/my_dataset/images'
    # source = 'E:/Programme/Python_Projects/ultralytics-main/ultralytics/data/cdx/images/0.jpg'

    args = dict(model=model, source=source, name='predict/predict')
    if use_python:
        from ultralytics import YOLO
        YOLO(model)(**args)
    else:
        predictor = DetectionPredictor(overrides=args)
        predictor.predict_cli()


if __name__ == '__main__':
    predict()

# yolo detect predict model=E:/Programme/Python_Projects/Graduation_Design/ultralytics-main/runs/detect/v8n-20-predict-v8x-20/weights/best.pt source=E:/Programme/Python_Projects/Graduation_Design/WCL/light.jpg save=True

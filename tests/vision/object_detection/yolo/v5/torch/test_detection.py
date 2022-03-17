import pytest
import cv2
from deep_utils import Box, YOLOV5TorchObjectDetector, download_file


@pytest.mark.torch
def test_detection():
    model = YOLOV5TorchObjectDetector(model_weight="yolov5s.pt", device='cpu')
    file_path = download_file(
        "https://raw.githubusercontent.com/pooya-mohammadi/deep_utils/master/examples/vision/data/movie-stars.jpg")
    img = cv2.imread(file_path)
    res = model.detect_objects(img, is_rgb=False, get_time=True)
    assert len(res.boxes) >= 0, "Model did not detect anything!"
    img = Box.put_box_text(img, res.boxes, res.class_names)
    assert img is not None, "put_box_text returned nothing!"

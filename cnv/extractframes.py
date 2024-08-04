import cv2


class ExtractError(Exception):
    def __init__(self, path):
        super().__init__(f"Error while extracting file: {path}")


def extract_array(path):
    vid = cv2.VideoCapture(path)
    success = True
    frame = 0
    arr = []
    while success:
        success, image = vid.read()
        if not success:
            raise ExtractError(path)
        arr.append(image.copy())
        frame += 1


def extract(path, output_folder, prefix="frame"):
    vid = cv2.VideoCapture(path)
    success = True
    frame = 0
    while success:
        success, image = vid.read()
        if not success:
            raise ExtractError(path)
        cv2.imwrite(output_folder + f"{prefix}{frame}.jpg", image)
        frame += 1

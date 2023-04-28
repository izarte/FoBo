import os
import numpy as np
import cv2
import ffmpeg


class DecordVideoIterator(object):
    """
    The default video iterator with decord: https://github.com/dmlc/decord
    There would be memory issue when the video length is too long (> 20 mins),
    in this case, we recommend use cv2.
    """
    def __init__(self, video_file, frame_idxs=None):
        """
        :param video_file: video file path
        :param frame_idxs: frame that are to be processed, a list of integers
        """

        self.vr = cv2.VideoCapture(video_file)
        self._rotation = check_rotation(video_file)

        if frame_idxs is None:
            self._frame_idxs = np.arange(len(self.vr))
        else:
            self._frame_idxs = sorted(frame_idxs)

    def __len__(self):
        return len(self._frame_idxs)

    def video_len(self):
        return len(self.vr)

    def __call__(self):
        for idx in range(self.__len__()):
            frame_idx = self._frame_idxs[idx]
            frame = self.vr[frame_idx].asnumpy()
            if self._rotation > 0:
                frame = np.rot90(frame, k=(-(self._rotation // 90)) % 4)
            yield frame_idx, frame


class CV2VideoIterator(object):
    """
    Deprecated, it is slow. It is only used for sanity check.
    """
    def __init__(self, video_file, frame_idxs=None):
        vr = cv2.VideoCapture(video_file)
        assert vr.isOpened(), "Cannot open the video file: {}".format(video_file)

        video_len = int(vr.get(cv2.CAP_PROP_FRAME_COUNT))

        self.vr = vr
        self._rotation = check_rotation(video_file)

        if frame_idxs is None:
            self._frame_idxs = np.arange(video_len)
        else:
            self._frame_idxs = sorted(frame_idxs)

    def __len__(self):
        return len(self._frame_idxs)

    def __call__(self):
        for idx in range(self.__len__()):
            frame_idx = self._frame_idxs[idx]
            self.vr.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            success, frame = self.vr.read()
            if success:
                if self._rotation > 0:
                    frame = np.rot90(frame, k=(-(self._rotation // 90)) % 4)
                # frame is bgr by default from opencv
                yield frame_idx, frame[:, :, ::-1]
            else:
                break


class ImageVideoIterator(object):
    """
    Read video as frame per frame
    """
    def __init__(self, video_file, frame_idxs=None):
        self.images = os.listdir(folder_path)
        assert os.path.isdir(dir_path), "Cannot find folder: {}".format(video_file)

        self.video_len = len(images)
        self.rotation = 0

    def __len__(self):
        return self.video_len

    def __call__(self):
        for idx, image in enumerate(self.images):
            frame = cv2.imread(image)
            if frame is not None:
                if self._rotation > 0:
                    frame = np.rot90(frame, k=(-(self._rotation // 90)) % 4)
                # frame is bgr by default from opencv
                print(frame)
                yield idx, frame[:, :, ::-1]
            else:
                break


def check_rotation(video_file):

    meta_dict = ffmpeg.probe(video_file)
    rotation = 0
    if 'rotate' in meta_dict['streams'][0]['tags']:
        rotation = int(meta_dict['streams'][0]['tags']['rotate'])

    return rotation

class ImageIterator(object):
    """
    Read video as frame per frame
    """
    def __init__(self, image, frame_idxs=None):
        self.images = image

        self.video_len = len(self.images)
        self._rotation = 0

    def __len__(self):
        return self.video_len

    def __call__(self):
        for idx, image in enumerate(self.images):
            frame = image
            if frame is not None:
                if self._rotation > 0:
                    frame = np.rot90(frame, k=(-(self._rotation // 90)) % 4)
                # frame is bgr by default from opencv
                print("Shape: ", frame.shape)
                print()
                yield idx, frame
            else:
                break


def build_video_iterator(image, video_decode='decord'):
    return ImageIterator(image)
        # if video_decode == 'decord':
        #     return DecordVideoIterator(video_path)
        # else:
        #     return CV2VideoIterator(video_path)
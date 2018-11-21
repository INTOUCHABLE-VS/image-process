# -*- coding:utf-8 -*-
import cv2
import os
def video2image(srcVideoPath, savePath, width=4):
    """
    把视频转换成图像，并存储起来，存储名字采用数字顺序表示，并用零填充
    savePath 不存在就会创建它，默认存储格式为 jpg
    例子：如果，width=4，第一帧图像名字为0001
    :param srcVideoPath: 源视频路径
    :param savePath: 图像存储路径
    :param width: 名字补零宽度，默认为4
    :return: null
    """
    frames = []
    vc = cv2.VideoCapture(srcVideoPath)
    index = 0
    rval = vc.isOpened()
    while rval:
        index = index + 1
        rval, frame = vc.read()
        if rval:
            frames.append(frame)
            cv2.waitKey(1)
    assert (10 ** width - 1) > (index - 1), "帧数比宽度最大值要多，请重新输入width"
    i = 1
    if not os.path.exists(savePath):
        os.makedirs(savePath)
        for frame in frames:
            cv2.imwrite(savePath + "/" + str(i + 1).zfill(width) + ".jpg", frame)
            i += 1
    else:
        for frame in frames:
            cv2.imwrite(savePath + "/" + str(i + 1).zfill(width) + ".jpg", frame)
            i += 1
    vc.release()




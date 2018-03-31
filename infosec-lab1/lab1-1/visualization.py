# -*- coding: utf-8 -*-
import os
import re
import matplotlib.pyplot as plt

IMAGES_DIR = './images'


def visualization(images_dir=None, gray_mode=True):
    images = os.listdir(images_dir if images_dir else IMAGES_DIR)
    if len(images) == 6:
        for index, image in enumerate(images):
            show_img = plt.imread(os.path.join(IMAGES_DIR, image))
            plt.subplot(2, 3, index+1)
            plt.imshow(show_img, cmap='gray' if gray_mode else None)
            plt.axis('off')
            # format title
            re_rst = re.findall(r'(.*)_out.bmp', image)
            plt.title(re_rst[0] if re_rst else image[:-4])
            del re_rst
        plt.tight_layout()
    elif images:
        show_img = plt.imread(images[0])
        plt.imshow(show_img)
    else:
        exit()
    plt.show()

visualization()

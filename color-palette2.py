# https://www.alessandroai.com/extract-and-analyze-colors-from-any-image/

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib import colors
import numpy as np
import cv2

img = cv2.imread('3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def preprocess(raw):
    img=cv2.resize(raw,(900, 600),interpolation=cv2.INTER_AREA)
    img=img.reshape(img.shape[0]*img.shape[1],3)
    return img

def rgb_to_hex(rgb_color):
    hex_color="#"
    for i in rgb_color:
        hex_color+=("{:02x}".format(int(i)))
    return hex_color

def analyze(img):
    # We're using K-means, a clustering technique, to bring us the main colors of the image... As the number of clusters suggests, it'll return the top 5 colors
    clf=KMeans(n_clusters=5)
    color_labels=clf.fit_predict(img)
    counts=Counter(color_labels)
    ordered_colors=[center_colors[i] for i in counts.keys()]
    hex_colors=[rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    plt.figure(flgsize=(12,8))
    plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)

    plt.saveflg("3.jpg")
    print("Found the following colrs:\n")
    for color in hex_colors:
        print(color)

# Bring it all together 
modified_img = preprocess(img)
analyze(modified_img)
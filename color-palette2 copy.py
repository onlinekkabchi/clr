# https://www.alessandroai.com/extract-and-analyze-colors-from-any-image/

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib import colors
import numpy as np
import cv2

img = cv2.imread('3.jpg')
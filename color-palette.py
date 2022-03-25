# 여기가 내가 사용한 python library
import numpy as np
import matplotlib.pyplot as plt
import PIL as pil
import extcolors
from PIL import Image

# 1. 사진 안에서 영역을 나눈다... 16x16등?


# 2. 영역 안에서 색을 뽑는다. => 지금 내가 여기 걸린 부분~
# ""안에 이미지 이름을 넣으면 되는데 반드시 같은 directory 안에 있어야함.
# extcolors이게... 색 추출해주는 라이브러리
colors, pixel_count = extcolors.extract_from_path("jin.jpg")

rgb_list = [x[0] for x in colors]


## 추출한 색깔?? 을 콘솔에 찍어주는거...
print(rgb_list)

# 3. 1x1 내지는 5x5 칸 안에 색을 채운다 => 파레트 완성
#   for (int j = 1; j < noOfPixelsPerAxis + 1; j++) {
#     for (int i = 1; i < noOfPixelsPerAxis + 1; i++) {
#       int? pixel = image?.getPixel(xChunk * i, yChunk * j);
#       pixels.add(pixel);
#       colors.add(abgrToColor(pixel!));
#     }
#   }


# 이 부분을 수정함 될거같은데 지금 정신이 업음... 
palette = np.array(rgb_list)[np.newaxis, :, :]


# 4. 저좡
plt.imshow(palette)
plt.axis('on')
plt.show()

from PIL import Image
import numpy as np

img = Image.open('windows.jpg')
ar = np.array(img)
ar_tmp = np.zeros_like(ar)
print(ar.shape)
for i in range(ar.shape[0]):
  for j in range(ar.shape[1]):
    ar_tmp[i][j][0] = ar[i][j][0]
    ar_tmp[i][j][1] = ar[i][j][2]
    ar_tmp[i][j][2] = ar[i][j][1]

output_img = Image.fromarray(ar_tmp)

output_img.save('windows_filtered.jpg')

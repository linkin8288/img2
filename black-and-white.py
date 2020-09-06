from PIL import Image # pillow 程式
import os # operating system

# 將單張圖片轉成黑白
img_file = Image.open("vampire.jpg")   # open colour image
img_file = img_file.convert("L")   # convert image to black and white
img_file.save("result1.png")   # save image

# 將資料夾裡面所有的圖片轉成黑白
for file in os.listdir('.'): # 把現在的資料夾的檔案都列出來
	if file.endswith('.jpg'): # 只把結尾有jpg的列出來
		img_file = Image.open(file)  # open colour image
		img_file = img_file.convert("L")  # convert image to black and white
		img_file.save(file[:-4] + "_grey.png")  # save image
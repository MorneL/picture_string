from PIL import Image, ImageDraw, ImageFont
from colr import color

  
input_text = "2020 "
font_size = 10
count = 0
cn = 0

im = Image.open("this_is_fine.png")
img = Image.new('RGB', (im.size[0]* font_size, im.size[1]* font_size), color = 'white')
d1 = ImageDraw.Draw(img)
font = ImageFont.truetype("ariblk.ttf", font_size)

ascii_pic = ""
for y in range(im.size[1]):
  for x in range(im.size[0]):
    if(cn == len(input_text)): cn = 0
    d1.text((x * font_size, y * font_size), input_text[cn], fill=im.getdata()[count], font=font)
    count += 1
    cn += 1

img.save('2020_is_fine.png')
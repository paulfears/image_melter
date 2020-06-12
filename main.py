import PIL, math
import requests

from PIL import Image
from io import BytesIO

def save_imgs_as_gif(sequence, name):
  sequence[0].save(
    name,
    save_all=True,
    append_images=sequence[1:],
    loop=0,
  )

def melt(img, amount):
  bytes = img.load()
  prev = False
  w, h = img.size
  for y in range(w):
    for x in range(h):
      if prev:
        if(abs(sum(bytes[y,x])-prev)>amount):
          bytes[y,x] = (255,255,255)
      try:
        prev = sum(bytes[y,x])
      except:
        print(bytes[y,x])
        pass
  return img


a= input("image to color : ")
print(dir(requests.get(a)))
a = Image.open(BytesIO(requests.get(a).content))
a.save("original.png", "PNG")


imgs = []
for i in range(765):
  if i % 24 == 0 and i>0:
    print(format((i/765)*100, ".2f")+"%")
    imgs.append(melt(a.copy(), i))



save_imgs_as_gif(imgs, 'a.gif')



melt(a, 200).save("dog/i.png", "PNG")
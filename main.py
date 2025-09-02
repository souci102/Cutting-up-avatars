from PIL import Image


image=Image.open("example.png")
rotated_image=image.rotate(45)
rotated_image.save("rotated.png")

print(image.mode)
print(image.width)
print(image.height, end="\n\n")

image1=Image.open("lenna.jpg")
print(image1.mode)
cmyk_image = image.convert("RGB")
print(cmyk_image.mode)
print(image1.mode, end="\n\n")

image=Image.open("monro.jpg")
print(image.mode)
red,green,blue=image.split()
red.save("monro_red.jpg")
green.save("monro_green.jpg")
blue.save("monro_blue.jpg")

new_image=Image.merge("RGB", (red, green, blue))
new_image.save("new_monro.jpg", end="\n\n")

image=Image.open("monro_red.jpg")
left=80
top=0
right=image.width
bot=image.height
cropped_image=image.crop((left,top,right,bot))
cropped_image.save("cropped_monro_red.jpg")


image=Image.open("monro_red.jpg")
left=40
top=0
right=image.width-40
bot=image.height
cropped_image=image.crop((left,top,right,bot))
cropped_image.save("cropped_monro_red1.jpg")

image1=Image.open("cropped_monro_red.jpg")
image2=Image.open("cropped_monro_red1.jpg")
image3=Image.blend(image1, image2, 0.5)
image3.save("blend_cropped_monro_red.jpg")

image=Image.open("monro_blue.jpg")
left=0
top=0
right=image.width-80
bot=image.height
cropped_image=image.crop((left,top,right,bot))
cropped_image.save("cropped_monro_blue.jpg")


image=Image.open("monro_blue.jpg")
left=40
top=0
right=image.width-40
bot=image.height
cropped_image=image.crop((left,top,right,bot))
cropped_image.save("cropped_monro_blue1.jpg")


image1=Image.open("cropped_monro_blue.jpg")
image2=Image.open("cropped_monro_blue1.jpg")
image3=Image.blend(image1, image2, 0.5)
image3.save("blend_cropped_monro_blue.jpg")


image=Image.open("monro_green.jpg")
left=40
top=0
right=image.width-40
bot=image.height
cropped_image1=image.crop((left,top,right,bot))
cropped_image1.save("cropped_monro_green.jpg")
print(cropped_image1.width)
print(cropped_image1.height, end="\n\n")
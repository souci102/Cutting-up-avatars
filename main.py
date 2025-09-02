from PIL import Image


image=Image.open("monro.jpg")
red,green,blue=image.split()
new_image=Image.merge("RGB", (red, green, blue))


image=red
print(red.width)
print(red.height, end="\n\n")
left=80
top=0
right=image.width
bot=image.height
cropped_image_red=image.crop((left,top,right,bot))


image=red
left=40
top=0
right=image.width-40
bot=image.height
cropped_image_red1=image.crop((left,top,right,bot))


image1=cropped_image_red
image2=cropped_image_red1
blend_cropped_monro_red=Image.blend(image1, image2, 0.5)


image=blue
left=0
top=0
right=image.width-80
bot=image.height
cropped_monro_blue=image.crop((left,top,right,bot))


image=blue
left=40
top=0
right=image.width-40
bot=image.height
cropped_monro_blue1=image.crop((left,top,right,bot))


image1=cropped_monro_blue
image2=cropped_monro_blue1
blend_cropped_monro_blue=Image.blend(image1, image2, 0.5)


image=green
left=40
top=0
right=image.width-40
bot=image.height
cropped_monro_green=image.crop((left,top,right,bot))


red=blend_cropped_monro_red
blue=blend_cropped_monro_blue
green=cropped_monro_green
merged=Image.merge('RGB', (red, blue, green))
merged.save("final_monro.jpg")


image=Image.open("final_monro.jpg")
image.thumbnail((80, 80))  
image.save("for_avatar.jpg")

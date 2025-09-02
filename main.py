from PIL import Image


image = Image.open("monro.jpg")
red, green, blue = image.split()
new_image = Image.merge("RGB", (red, green, blue))

coordinates_red = (80, 0, image.width, image.height)
cropped_monro_red = red.crop(coordinates_red)
coordinates_red = (40, 0, image.width-40, image.height)
cropped_monro_red_for_blend = red.crop(coordinates_red)
blend_cropped_monro_red = Image.blend(cropped_monro_red, cropped_monro_red_for_blend, 0.5)

coordinates_blue = (0, 0, image.width-80, image.height)
cropped_monro_blue = blue.crop(coordinates_blue)
coordinates_blue = (40, 0, image.width-40, image.height)
cropped_monro_blue_for_blend = blue.crop(coordinates_blue)
blend_cropped_monro_blue = Image.blend(cropped_monro_blue, cropped_monro_blue_for_blend, 0.5)

coordinates_green = (40, 0, image.width-40, image.height)
cropped_monro_green = green.crop(coordinates_green)

merged = Image.merge('RGB', (blend_cropped_monro_red, blend_cropped_monro_blue, cropped_monro_green))
merged.save("final_monro.jpg")

image = Image.open("final_monro.jpg")
image.thumbnail((80, 80))  
image.save("for_avatar.jpg")

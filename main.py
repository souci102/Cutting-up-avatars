from PIL import Image


image = Image.open("example.png")
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
from PIL import Image


image = Image.open("example.png")
rotated_image=image.rotate(45)
rotated_image.save("rotated.png")

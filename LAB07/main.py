from PIL import Image, ImageFilter, ImageOps

image = Image.open('noise.jpg')

min_filtered_image = image.filter(ImageFilter.MinFilter(3))

image.show()
min_filtered_image.show()

max_filtered_image = image.filter(ImageFilter.MaxFilter(3))

# image.show()
max_filtered_image.show()

gray_scale_image = ImageOps.grayscale(image)

gray_scale_image.show()

kernel = ImageFilter.Kernel((3,3), [-1, -1, -1, -1, 3, -1, -1, -1, -1])

image_edges = gray_scale_image.filter(kernel)

image_edges.show()
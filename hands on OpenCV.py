import cv2
image = cv2.imread('image.jpg')

# h,w = image.shape[:2]

# print(f"height is = {h} and width is = {w}")

# (B, G, R) = image[100, 100]
# print(f"{B},{G},{R}")


roi = image[100:500,200:600]

print(roi)
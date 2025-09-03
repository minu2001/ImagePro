import cv2

img_file = "./img/HM.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('There is no image file.')
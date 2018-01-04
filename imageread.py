#! ~/usr/bin/env python
# conding=utf-8


from PIL import Image,ImageFilter

img=Image.open('img1121.PNG');
w,h=img.size;
print "size width",w
print "size heigh",h

img.save('1.jpg','jpeg');

imgcopy=Image.open('1.jpg');
# imgContour=imgcopy.filter(ImageFilter.CONTOUR);
# imgContour.save('contour.jpg','jpeg');
# imgContour.show();

imgEdge=imgcopy.filter(ImageFilter.SHARPEN);
imgEdge=imgEdge.filter(ImageFilter.SHARPEN);
imgEdge.save('edge.jpg','jpeg');

imgContour=imgEdge.filter(ImageFilter.CONTOUR);

imgContour.show();

# imgEdge.show();

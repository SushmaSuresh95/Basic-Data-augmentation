# Basic-Data-augmentation

This code uses image processing techniques to generate multiple copies of the input Image file with a size of 256*256.
Data augmentation is a method of increasing the data points. It is difficult to collect infinite amount of data but Machine learning models perform better with increased datasets. Every data collection process is associated with a cost. Therefore, we must augment the available data to increase the data size that we feed to our ML classifiers and compensate for the cost involved in further data collection.

An image must be downloaded and its path should be specified in the code.

The various operations performed on the image are:
1) Grayscale Image
2) Thresholding
3) Inverted/Negative Image
4) Gaussian adaptive Thresholding
5) Thresholding by OTSU Method
6) Blurred Image
7) Morphological operations such as Erosion, Dilation, Opening and Closing
8) Rotation by 90 and 180 Degrees/Flipping

With the above methods, the given image is augmented to multiple similar size images and stored in the directory.

The Libraries used for this code are: OpenCV and Numpy
https://opencv.org/releases.html


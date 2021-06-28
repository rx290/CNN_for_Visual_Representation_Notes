# Lecture 2 Notes

## Image Classification Pipelines

### Assignment

1. K-Nearest Neighbor
2. Linear Classification: SVM, Softmax
3. Two-Layer Neural Network
4. Image Features

#### Assignment Requirement

1. Python 3.0
2. Numpy

## K-Nearest Neighbor Algorithm

K-N Algo is not a smart algorithm what it usually does is, it takes the data and memorize each bit of it and then when we parse in an image it just finds the most resembling image and then it'll predict or show the label of that image.

Train Complexity O(1)
Predict Complexity O(N)

We want classifiers to be fast at prediction and slow for training but K-nth Neighbor is totally opposite of that.

Dataset to use CIFAR10

L1 / manhattan distance is a comparison method what it does is it creates a difference of two images in pixels values.

L2 / Eculidean Distance which calculates by taking a square root of the sum of squares of the elements as the distance

Hyperparameters are choices about the algorithm that we set rather than we learn

like what value of k should we use or what distance method should we use?

do's and don't:
1. Don't set k = 1 
2. Don't Divide DS into two parts train and test
3. Always Divide DS into Three parts Train, Validation and Test

cross validation is used for smaller data set

## Linear Classification

CNNs are basically like lego blocks and one of the foundational lego block for CNN is Linear Classification

### Algorithm Approach

so LC uses Parametric approach we takes in both data and parameters then it'll allocate a score out of 10 for the class it resembles.

sometimes we will need some bias data which is a constant vector of 10 elements

cons of LC:

it can only train one template per classifier


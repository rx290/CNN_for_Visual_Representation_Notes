# Lecture 5 Notes

## Convolutional Neural Network

input : wx * input : neuron

### Convolution Layer

Convolve means the filter with the image i.e. slide over the image spatially computing dot products

#### Convolution Filter Layer

Filter always extend the full depth of the input volume.

This filter is placed on the image and compute the dot product of the pixels on that particular region

note: this filter has same depth but a portion of the actual layer

#### Activation maps

are set of layers which deals with the convolutional layers and each layer then parse the processed data to the activation function and that activated data is later fed to the pooling layer and then to other connecting layer

### How does CNN work?

image is parsed in

low-level layer  : low level features
mid-level layer  : Mid level Features
high-level layer : High Level Features

Linearly Separable Classifiers -> results

## Summarize Conv Layer 

it accepts the volume of size W * H * D

Requires 4 hyperparameter:
    1. Number of filters K
    2. Spatial Extent F
    3. Stride S
    4. amount of zero Padding P

so layer 2 would be:

W2 * H2 * D2:

W2 = (W1 - F + 2P) / S + 1
H2 = (H1 - F + 2P) / S + 1
D2 = K

### Pooling Layer

A layer which makes the data being represented smaller and more manageable

It gets activated over every compute done by activation map independently

it also has filter size 


#### Pooling Layer Working

it accepts the volume of size W1 * H1 * D1

Requires 4 hyperparameter:
    1. Spatial Extent F
    2. Stride S

produces a volume of W2 * H2 * D2:

W2 = (W1 - F) / S + 1
H2 = (H1 - F) / S + 1
D2 = D1


### Fully Connected Layer

This layer is going to take all the data parsed from the layers and stretch it out as a vector

Typical Convolutional Neural Network looks like this:

[(Conv-Relu)*N-pool?]*M-(FC-Relu)*K,softmax


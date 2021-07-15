# Lecture 10 Notes

Recurrent Neural Network

Batch Normalization was introduced in 2014 and that is why we see 16-20 layers convolutional Neural Network

with Batch normalization we can now get rid of the ugly hacks like extra layers in GoogleNet and ResNet to inject more parameters at the lower layer to help model get converged

ResNet has these cool properties:
    1. Block can compete identity if we set the weights to zero
    2. L2 Regularization
    3. gradient flow in backward path (which increase both speed and accuracy)

Sequential Processing of Non sequence Data helps us to cater these relations:
    1. one to many
    2. many to one
    3. many to many

in sequential processing we take certain portion of the images and detect some patterns which are later used to generate the output.

even if we have a single frame picture we can have different models to run sequential processing on them to identify different objects present in them.

RNN:
    A Recurrent model which takes in an input and parses it to a hidden state which updates itself every time a new input is parsed later this internal hidden state will be fed to the same model when new input is parsed.
    An RNN also produces a prediction when the data / input is parsed to the internal hidden states

RNN are used for Language Modeling 

for LM we add one hot softmax at the output feed

## backprapogation through time vs Truncated Backprapogation Through Time

code:
    https://gist.github.com/karpathy/d4dee566867f8291f086

To generate a image caption generator we use CNN and RNN

How it works:
    1. image input
    2. convolutional feature extraction
    3. RNN with attention over the image
    4. word by word generation
    5. 

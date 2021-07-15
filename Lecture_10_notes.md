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

improved model of the aboves mentioned program works like this:
    1. image input
    2. convolutional feature extraction
    3. RNN with attention over the image
    4. word by word generation

Another example is Visual Question Answering program
how it works?

    1. Use CNN to detect chunks or features of image
    2. parse those chunks and a NLP question to the RNN
    3. RNN will generate a prediction as an answer

Another type of RNN is Multilayer RNN

Rnn has these problems:
    1. Exploding Gradient -> Gradient Clipping
    2. Vanishing Gradients -> Change RNN Architecture i.e. LSTM

## Long Short Term Memory (LSTM)

It generate four gates:
    1. i -> Input Gate > Whether to write to cell
    2. f -> Forget Gate > Whether to erase cell
    3. o -> Outside / Output Gate > How much to reveal
    4. g -> Gate Gate > How much to write to cell

Uninterpreted Gradient Flow in LSTM

Other RNN:

1. GRU
2. LSTM: A search space odyssey



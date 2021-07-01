# Lecture 6 Notes

a network of linear layers stack on each other

## Training CNN

it has three steps:

1. One time setup
2. Training Dynamics
3. Evaluations

We will learn these today:

1. Activation Functions
2. Data Preprocessing
3. Weight Initialization
4. Batch Normalization
5. Babysitting the learning Process
6. Hyperparameter Optimization

Sigmoid:
    d(x) = 1 / (1 + e^-x )

    problems with sigmoid:
        1. squashes number to range[0,1]
        2. Saturated Neurons can kill the gradient
        3. Sigmoid outputs are not zero-centered
        4. Exp() methods are expensive in terms of compute

tanh(x):

    problems with tannh(x):
        1. squashes number to range[-1,1]
        2. Are zero-centered
        3. Kills gradients when saturated

ReLU:
f(x) = max(0,x)

    1. Does not saturate in +ve region
    2. cheap in terms of computation
    3. Converges much faster than sigmoid and tanh
    4. biologically plausible than sigmoid

    problems with sigmoid:
            1. Outputs are not zero-centered
            2. has an annoyance dead ReLU will never get activate i.e. won't update

used with positive bias (0.001)

Variations:

Leaky ReLU:
    f(x): max(0.01x,x)

parametric Rectifier PReLU:
    f(x)= max(@x, x)
    backpropogation into alpha parameter


ELU:
f(x) = x if x > 0 and @(exp(x)-1) if x <= 0
    pros:
        1. All benefits of  ReLU
        2. closer to zero mean output
        3. Negative saturation Regime compared with leaky ReLU adds some robustness to Noise

    Cons:
        1. Exp() are expensive in terms of computation

Maxout Neuron:
    max(w1^T x + b1, w2^T x + b2)
pros:
    1. doesnot have the basic form of dot product -> nonlinearity
    2. Generalizes ReLU and Leaky ReLU
    3. Linear Regime! Does not saturate and does not die

cons:
    1. doubles the number of parameters

## Data preprocessing

1. zero centered data by np.mean(x,axis = 0)
2. normalized data by x /= np.std(x, axis = 0)

Decorated data
whitened data

calculate mean m 
then  subtract m from the data

d - m = 3 num vec

small random numbers:
    w = 0.01 * np.random.randn(D,H)
    works with small network

Batch normalization

1. improves gradient flow through the network
2. Allow higher learning rates
3. Reduces the strong dependence of initialization
4. acts as a form of regularization in a funny way and slightly reduces the need for dropout maybe

## Chose Architecture

## Double check loss is reasonable

## random search vs grid search


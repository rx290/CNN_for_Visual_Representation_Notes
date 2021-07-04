# Lecture 7 Notes

We should stick with ReLU as default

never set weight too high or too low or the model won't train that good

batch-normalization is when we add a layer to force all activations to be zero mean

to avoid noise/friction and fluctuation of local minima we use a two pram equation i.e. SGD + momentum

SGD = Small Gradient Descend 

we actually calculate average of momentum and gradient to find out the actual step

Nesterov Momentum is when you actually go with the momentum / velocity and after that you find gradient and move toward actual step

AdaGrad
so this op-algo keeps a track of all sums of suqares of gradients that we are training

beneficial for convex case and non beneficial for non convex cases 

RMSProp is a slight variation of AdaGrad where we let the sum of square gradients get decayed 

Adam
is an op-algo which is based on both adaGrad and RmsProp.
we use two steps here fisrt we calculate momentum
second we calculate sum of all squared gradient

then we calculate the learning rate by first moment / second movement

we also use Bias correction in Adam to estimate start at zero

Adam is one of the default and generic algo for most of the problems.


Secon-order optimization

L-BFGS

regularization -> Dropout -> to set some random batch of neurons to zero so that it resemble a small NN of the same version

regularization -> dropout -> Test time, common pattern , data augmentation 

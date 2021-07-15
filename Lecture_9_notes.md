# Lecture 9 Notes

GoogLe Net
    22 layers
    Efficient Inception Module
    No fc layers
    12x less params than AlexNet
    ILSVRC'14 Classification Winner
    6.7% top 5 error

We add 1x1 convolution Layer to different Convolution network to reduce dimension / depth this process is known as dimension reduction

ResNet
    152 layer model for ImageNet
    Stack Residual Blocks
    Every Residual block has 2 3x3 conv layers
    Periodically dobule # of filters and downsample spatially using stride 2 (/2 in each dimension)
    Additional conv layer at the beginning
    no FC Layers at the end only FC 1000 to output classes
    Uses bottleneck layers to improve efficiency
    ILSVRC'15 Classification Winner
    Swet all classification and detection competitions in ILSVRC'15 and COCO'15

Training Resnet in practices:
    Batch Normalization after every Conv Layer
    Xavier/2 initialization from He et al
    SGD + momentum (0.9)
    Learning rate 0.1 divided by 10 when validation error plateaus
    mini batch size 256
    weight decay of 1e-5
    no dropout used

We can't stack deeper layers on a plain convolution neural network because of Optimization

Other Networks:

    Network in Network (NiN)
        Mlpconv layer with micro network within each conv layer to compute more abstract features for local patches
        Micro network uses multilayer perceptron (FC i.e. 1x1 conv layers)
        precursor to GoogleNet and ResNet bottleneck layers
        Philosophical insipiration for GoogleNet

    Identity Mappings in Deep Residual Networks:
        Improved ResNet Block Design from Creators of ResNet
        Creates a more direct path for propagating information throughout network (Moves activation to residual mapping pathway)
        Gives better performance

    Wide Residual networks
        Argues that residuals are the important factor not depth
        User Wider residual blocks (F x K) filters instead of F Filters in each layer
        50-layer wide ResNet outperforms 152-layer original Resnet
        Increasing Width Instead of depth more computationally efficient

    Aggregated Residual Transformations for Deep Neural Networks (ResNeXt):
        Increases widht of residual block through multiple pralllel pathways (cardinality)
        parallel pathways similar in spirit to inception module 

    Deep Networks with Stochastic Depth
        Motivation: Reduce Vanishing Gradients and training time through short networks durning training
        Randomly drop a subset of layers during each training pass
        Bypass with identity funcion
        Use full deep network at the test time

    FractalNet: Ultra-Deep neural networks without Residuals
        Argues that key is transitioning effectively from shallow to deep and residual representations are not necessary
        fractal architecture with both shallow and deep paths to output 
        trained with dropping out sub paths
        full network at test time

    Desnely Connected Convolutional networks
        Dense Block where each layer sis connected to every other layer in feedforward fashion
        alleviates vanishing gradient strengthens feature propagation, encourages feature reuse

    SqueezeNet: AlexNet-level Accuracy with 50x fewer parameters and <0.5Mb model size>
        Fire modules consisting of a Squeeze layer with 1x1 filters feeding an expand layer with 1x1 3x3 and  filters
        Alexnet level accuracy on Imagenet with 50x fewer parameters
        can compress to 510x smaller than AlexNet 0.5mb
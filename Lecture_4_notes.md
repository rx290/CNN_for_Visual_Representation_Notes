# Lecture 4 Notes

## Gradient Descent

### Computational Graphs

A representation of any arbitrary complex function such that each node of the graph represent the steps we go through.

### Backpropogation

a technique which uses chain rule recursively to compute every variable.

#### patterns

1. add gate: gradient distributor
2. max gate: gradient router
3. mul gate: gradient switcher

### Sigmoid function

#### Sigmoid gate

### jacobian matrix

size?: x * x
looks? a diagonal matrix
scaling? 100 times

### Neural Training Machine

### Graph Pseudo Code

class ComputationalGraph(object):
    def forward(inputs):
        # pass in the values
        # forward the computational graph
        for gate in self.graph.nodes_topologically_sorted():
            gate.forward()
        return loss # the final gate in the graph outputs the loss

    def backward():
        for gate in reversed(self.graph.nodes_topologically_sorted()):
            gate.backward() # little piece of backprop (chain rule applied)
            return inputs_gradients

#### Multiply Gate

class MultiplyGate(object):
    def forward(x.y):
        z = x*y
        return z
    
    def backward(dz):
        dx = self.y * dz # [dz/dx * dL/dz]
        dy = self.x * dz # [dz/dy * dL/dz]
        return [dx,dy]

eg: caffe layers

## Neural Network

so in terms of functions 

linear score function: f = Wx

2-layer Neural Network: f = W2 max(0,W1x)

3-layer Neural Networks: W3 max(0, W2 max(0,W1x))

### Linear vs Non Linear Functions

## Implementation of a 2-layer Neural Network

### activation functions

1. Sigmoid
2. tanh
3. leaky ReLU
4. Maxout
5. ReLU
6. ELU


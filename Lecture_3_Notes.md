# Lecture 3

Loss Function:
    an algorithm which takes in w and the number of Dataset then tells the program what bias value will be best for the training set is known as loss function

    Equation:
        L = 1/n E

hinge loss is used for multiple SVM

min/max loss:
    min loss is ideally zero
    max is infinity

loss for multiclasses svm is c - 1

we implement loss function to reduce linearity of the function

Regularization is used when we need a simple path i.e most common type of regularization is l2 or weight decay

Softmax Classifier (Multinomial Logistic Regression)

so in softmax classifier we put more weight on the scores and use them to compute a probability distribution among the classes

 Li in softmax = - log(e^syi / Ej e^sj)
 min/max loss:
    min loss is zero
    max loss is infinity

Optimization:
    1. Random Search (bad algorithm)
    2. Follow the slope (f(x+h)-f(x))/h (Algorithm is super slow and bad to use)
    3. Analytic gradient (is super fast, exact but error-prone)
    4. so we use a combo of analytic gradient and check them with slope / numerical analytic i.e. a gradient check.

Gradient Descent
Learning Rate (Hyper Parameter, very important)

stochastic Gradient Descent is something where we create some random set of data from training data rather than the complete dataset

image features are mapping of some of the features in numerical form to feed to the classifier 

histogram oriented gradients

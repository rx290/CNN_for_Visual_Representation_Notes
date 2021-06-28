# Lecture 1

## Introduction to CV and its History

What is computer vision?
The field of computer science which deals with the study of visual data is known as Computer Vision.

History:

    Ever 1 second 5 GB of video data is being uploaded

    Humans use 50% of the cortex and neurons just for vision

    Pinhole cameras were there in 5th Century which were one of the first mechanical CV instruments ever created

    electrophysiology by hubel and wiesel in 50s-60s.

How does brain work with visual data?
simple cells responds to oriented edges when they move in certain direction which is the foundation of Visual Information.

It start with simple structure of visual words i.e. oriented edges as more and more information is gathered the brain builds up complexity and patterns of that visual information until it can recognize the complex visual world.

First educational program?
The first PHD done in CV was back in 1963 by Larry Roberts where we simplified everything into simple geometric shapes and goal was to reconstruct them.

later in 1966 a summer vision project was proposed and created. Which was a great hit. This event is known as the founding stone of the CV which has been now a community of more than 100k researchers over a span of 50 years.

Another prominent name for CV is David Marr as he described the OPen CV in 4 steps back in 1970s which are as follows:

    1. Input Image
    2. Primal Sketch (Edges, anchor points, curves and boundaries)
    3. 2.5 D Sketch (layering system, depth of field etc)
    4. 3-D Model Representation (3D Model)

Other Contributions by stanford and SRI scientists are as follows:

1. Picorial Structure by Fischler and Elschlager in 1973.
2. Generalized Cylinder by Brooks ^ Binford in 1979
3. David Lowe in 1987 tried to create a set of razors by edges, straight lines and their combinations

In 1997 there came a process by Jishetendra Malik and Jianbo Shi from berkeley which uses graph theory algorithm. it is known as Image Segmentation which says that one should group pixels into meaningful areas
i.e. we don't know what a person is in CV but we can extract all the pixels from the person's background

the years 1999 and 2000 were the period where machine learning and statistical machine learning gained a momentum and things like SVM, Boosting Graphical Models and first gen NN were developed

After years of progressing in 2001 the most awaited tech came into existence i.e. the Face Detection which was done by Viola & Jhones using AdaBoost Algorithm.

This contribution paved path for fuji's first Face Detecting Digital Camera in 2006.

Till 2001 Feature based object recognition was done and it was introduced by David Lowe in 1999 known as SIFT and Object Recognition

Spatial Pyramid Matching was introduced by Lazebnik, Schmid & ponce in 2006 the idea was there are some sort of wave patterns in different pictures which can be mapped in featured vector and carried out to a SVM and then these wave patterns can help us determine the landscape of the pictures themselves.

Human body detection was done by two technologies which are as follows:
1. Histogram of Gradients by Dalal And Triggs in 2005
2. Deformable Part Model by Felzenswalb, McAllester and Ramanan in 2009

All of this progress laid foundation to a grand dataset which was there to measure how far we(researchers) have come in terms of Object Recognition and Computer Vision i.e. a benchmark it had 20 different objects to classify and detect.

This test is known as Pascal Visual Object Challenge.

in 2009 a team from stanford took 2 challenges to overcome overfitting of ML and to recognize all things on earth and they created a dataset of 14 m pictures with 22k Categories known as Imagenet
image-net.org 

in 2012 CNN dropped the error rate by 10% which is a significant drop rate.

## Deep Learning

what is image Classification?
When an algorithm reads a image and based on some features it tends to classify it to some known classes then it is known as classification.

What is object Detection?
Detection of multiple objects within the image.

What is object Captioning?
When an object is detected we now need to produce a Natural Language Processing Label to show what it is.

What are CNNS or Convents?


lecun and collaborators at bell labs in 1998 built a network of layers to recognize digits so that OCR can be a thing and handwritten checks can be recognized.

That's how CNN were invented.

Since 1998 there are global innovationsw which made CNN popular again:

1. Computation
2. GPU
3. DATA

Visual Genome





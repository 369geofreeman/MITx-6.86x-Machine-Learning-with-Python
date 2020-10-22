# Problem set four


# Hidden Layer Models


For the following set of problems, let's consider a simple 2-dimensional classification task. The training set is made up of  4  points listed below:

 	 𝑥(1)=(−1,−1) 	 , 	 𝑦(1)=1 	 	 
 	 𝑥(2)=(1,−1) 	 , 	 𝑦(2)=−1 	 	 
 	 𝑥(3)=(−1,1) 	 , 	 𝑦(3)=−1 	 	 
 	 𝑥(4)=(1,1) 	 , 	 𝑦(4)=1 	 	 
The dataset is illustrated below (blue - positive, red - negative)


For simplicity, assume that we are only interested in binary classification problems for now. That is,  𝑦(𝑖)  can be either  1  or  −1 .

### Linear Separability After First Layer

For this problem, let us focus on a network with one hidden layer and two units in that layer:


Let  𝑓(𝑖)1,𝑓(𝑖)2  denote the output of the two units in the hidden layer corresponding to the input  𝑥(𝑖)  respectively, i.e.

 	 𝑓(𝑖)1 	 = 	 𝑓(𝑤01+(𝑤11𝑥(𝑖)1+𝑤21𝑥(𝑖)2)) 	 	 
 	 𝑓(𝑖)2 	 = 	 𝑓(𝑤02+(𝑤12𝑥(𝑖)1+𝑤22𝑥(𝑖)2)) 	 	 
Consider the set  𝐷′={([𝑓(𝑖)1,𝑓(𝑖)2],𝑦(𝑖)),𝑖=1,2,3,4} .

Assume that f is the linear activation function given by  𝑓(𝑧)=2𝑧−3 .

For which of the following values of weights would the set  𝐷′  be linearly separable? (Select all that apply.)

Answer = None of the above

Solution:

First of all note that from the figure in the text above that  𝐷  is clearly not linearly separable.
Also,  𝑓(𝑧)=2𝑧−3  is a linear activation function.
Any linear transformation of the feature space of a linearly in-separable classification problem would still continue to remain linearly inseparable. For this question, one can compute the feature representations of all the data points and verify visually.
For example, the result of the second answer is plotted here:



### Non-linear Activation Functions

Again, let's focus on a network with one hidden layer with two units and use the same training set as above. The weights of the network are given as follows:

 	 𝑤11=1,𝑤21=−1,𝑤01=1 	 	 
 	 𝑤12=−1,𝑤22=1,𝑤02=1 	 	 
Let  𝑓1,𝑓2  be the outputs of the first and second unit respectively.

Consider the set  𝐷′={([𝑓(𝑖)1,𝑓(𝑖)2],𝑦(𝑖)),𝑖=1,2,3,4} 

For which of the following functions  𝑓 , would the set  𝐷′  be linearly separable? (Select one or more that apply.)

Answer = f(z) = ReLu(z)
Answer = f(z) = tanh(z)

Solution:

From the above problem, we note that any linear transformation of the feature space of a linearly in-separable classification problem would still continue to remain linearly inseparable. Hence we rule out the two linear functions.
For all of the parts below, note that

 	𝑓(𝑖)1	=	𝑓(𝑤01+(𝑤11𝑥(𝑖)1+𝑤21𝑥(𝑖)2))	 	 
 	𝑓(𝑖)2	=	𝑓(𝑤02+(𝑤12𝑥(𝑖)1+𝑤22𝑥(𝑖)2))	 	 
𝑓(𝑧)=ReLU(𝑧): Substituting for ReLU into 𝑓 in the above equation gives the following results:

(1,1),(3,0),(0,3),(1,1)

### Neural Network Learned parameters

Given a neural network with one hidden layer for classification, we can view the hidden layer as a feature representation, and the output layer as a classifier using the learned feature representation.

There're also other parameters that will affect the learning process and the performance of the model, such as the learning rate and parameters that control the network architecture (e.g. number of hidden units/layers) etc. These are often called hyper-parameters.

Which of the following is/are optimized during a single training pass? (Note that cross-validation is tuned before this point.) Check all that apply.



Answer = The weights that control the feature representation
Answer = The weights for the classifier

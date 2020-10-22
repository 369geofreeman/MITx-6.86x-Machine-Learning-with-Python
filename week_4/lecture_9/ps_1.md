# Problem set 1


### Back-propagation Algorithm


Once we set up the architecture of our (feedforward) neural network, our goal will be to find weight parameters that minimize our loss function. We will use the stochastic gradient descent algorithm (which you learned in Lecture 4 and revisited in lecture 5) to carry out the optimization.

This involves computing the gradient of the loss function with respect to the weight parameters.

Since the loss function is a long chain of compositions of activation functions with the weight parameters entering at different stages, we will break down the computation of the gradient into different pieces via the chain rule; this way of computing the gradient is called the back-propagation algorithm.

In the following problems, we will explore the main step in the stochastic gradient descent algorithm for training the following simple neural network from the video:


This simple neural network is made up of  𝐿 hidden layers, but each layer consists of only one unit, and each unit has activation function  𝑓 .
As usual,  𝑥  is the input,  𝑧𝑖  is the weighted combination of the inputs to the  𝑖𝑡ℎ  hidden layer. In this one-dimensional case, weighted combination reduces to products:

 	 𝑧1 	 = 	 𝑥𝑤1 	 	 
 	 for 𝑖=2…𝐿:𝑧𝑖 	 = 	 𝑓𝑖−1𝑤𝑖where 𝑓𝑖−1=𝑓(𝑧𝑖−1). 	 	 
We will use the following loss function:

 	 (𝑦,𝑓𝐿)=(𝑦−𝑓𝐿)2 	 	 
where  𝑦  is the true value, and  𝑓𝐿  is the output of the neural network.


### Gradient Descent Update

Let  𝜂  be the learning rate for the stochastic gradient descent algorithm.

Recall that our goal is to tune the parameters of the neural network so as to minimize the loss function. Which of the following is the appropriate update rule for the paramter  𝑤1  in the stochastic gradient descent algorithm?


Answer =  𝑤1←𝑤1−𝜂⋅∇𝑤1(𝑦,𝑓𝐿)


### Recursive Expression - Part I


As above, let  (𝑦,𝑓𝐿)  denote the loss function as a function of the predictions  𝑓𝐿  and the true label  𝑦 . Recall

 	 𝑧1 	 = 	 𝑥𝑤1 	 	 
 	 for 𝑖=2…𝐿:𝑧𝑖 	 = 	 𝑓𝑖−1𝑤𝑖where 𝑓𝑖−1=𝑓(𝑧𝑖−1). 	 	 
Let  𝛿𝑖=∂∂𝑧𝑖 .

The first step to updating any weight  𝑤  is to calculate  ∂∂𝑤 .

Which of the following option(s) is/are correct expression(s) for  ∂∂𝑤1 ?
(Choose all that apply.)

Answer = ∂∂𝑤1=∂𝑧1∂𝑤1⋅∂∂𝑧1
Answer = ∂∂𝑤1=𝑥⋅𝛿1



### Recursive Expression - Part II

As above, let  (𝑦,𝑓𝐿)  denote the loss function as a function of the predictions  𝑓𝐿  and the true label  𝑦.  Let  𝛿𝑖=∂∂𝑧𝑖 .

In this problem, we derive a recurrence relation between  𝛿𝑖  and  𝛿𝑖+1 

Assume that  𝑓  is the hyperbolic tangent function:

 	 𝑓(𝑥) 	 = 	 tanh(𝑥) 	 	 
 	 𝑓′(𝑥) 	 = 	 (1−tanh2(𝑥)). 	 	 
Which of the following option is the correct expression for  𝛿1  in terms of  𝛿2 ?

Answer =  𝛿1=(1−𝑓21)⋅𝑤2⋅𝛿2

### Final Expression of the Gradient

As above, let  (𝑦,𝑓𝐿)  denote the loss function as a function of the predictions  𝑓𝐿  and the true label  𝑦.  Let  𝛿𝑖=∂∂𝑧𝑖 .

In this problem, we unroll the recurrence expression for  ∂∂𝑤1 . We will use the loss function

 	 (𝑦,𝑓𝐿)=(𝑦−𝑓𝐿)2. 	 	 
Compute  ∂∂𝑤1  and select the correct option from below.


Answer = ∂∂𝑤1=𝑥(1−𝑓21)(1−𝑓22)⋯(1−𝑓2𝐿)𝑤2𝑤3⋯𝑤𝐿(2(𝑓𝐿−𝑦))


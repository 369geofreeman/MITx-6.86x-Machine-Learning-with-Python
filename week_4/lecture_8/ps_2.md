# Problem set two

### Neural Network Units


A neural network unit is a primitive neural network that consists of only the “input layer", and an output layer with only one output. It is represented pictorially as follows:


A neural network unit computes a non-linear weighted combination of its input:

 	 𝑦̂  	 = 	 𝑓(𝑧)where 𝑧=𝑤0+∑𝑖=1𝑑𝑥𝑖𝑤𝑖 	 	 
where  𝑤𝑖  are numbers called weights ,  𝑧  is a number and is the weighted sum of the inputs  𝑥𝑖,  and  𝑓  is generally a non-linear function called the activation function .

The above equation in vector form is:

 	 𝑦̂  	 = 	 𝑓(𝑧)where 𝑧=𝑤0+𝑥⋅𝑤, 	 	 
where  𝑥=[𝑥1,…,𝑥𝑑]  and  𝑤=[𝑤1,…,𝑤𝑑]𝑇 .


### Numerical Example - Neural Network Unit


In this problem, you will compute the output  𝑦̂ =𝑓(𝑧)  in the following neural network unit with 2 inputs  𝑥1  and  𝑥2 .


Let

 	 𝑥 	 = 	 [1,0] 	 	 
 	 𝑤0 	 = 	 −3 	 	 
 	 𝑤 	 = 	 [1−1] 	 	 
First, compute  𝑧 .

Answer z = -2

The rectified linear function (ReLU) is defined as:

𝑓(𝑧)=max{0,𝑧}. 
 
Using the ReLU function as the activiation function  𝑓(𝑧) , compute  𝑦̂  :

Answer y = 0


### Hyperbolic Tangent Activation Function

In this problem, we will recall and refamiliarize ourselves with hyperbolic tangent function, which is commonly used as an activation function in a neural network.

Recall the hyperbolic tangent function is defined as

 	 tanh(𝑧) 	 = 	 𝑒𝑧−𝑒−𝑧𝑒𝑧+𝑒−𝑧=1−2𝑒2𝑧+1. 	 	 
What is the domain of  tanh(𝑧) , i.e. for what values of  𝑧  is  tanh(𝑧)  defined?


Answer = All real numbers

Find  tanh(0) . (Enter e for  𝑒 .)

Answer tanh(0) = 0

Is  tanh  odd, even, or neither?

Answer = odd

What is the range of  tanh ? Answer by giving the tightest lower bound, and a tightest upper bound of the set of all possible values of  tanh(𝑧) .

Answer = Lower bound -1
Answer = Upper bound = 1








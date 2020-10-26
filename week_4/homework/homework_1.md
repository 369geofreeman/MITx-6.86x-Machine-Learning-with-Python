# Nerual Networks


In this problem we will analyze a simple neural network to understand its classification properties. Consider the neural network given in the figure below, with ReLU activation functions (denoted by 𝑓) on all neurons, and a softmax activation function in the output layer:


Given an input 𝑥=[𝑥1,𝑥2]𝑇, the hidden units in the network are activated in stages as described by the following equations:

 	𝑧1	=𝑥1𝑊11+𝑥2𝑊21+𝑊01	𝑓(𝑧1)	=max{𝑧1,0}	 	 
 	𝑧2	=𝑥1𝑊12+𝑥2𝑊22+𝑊02	𝑓(𝑧2)	=max{𝑧2,0}	 	 
 	𝑧3	=𝑥1𝑊13+𝑥2𝑊23+𝑊03	𝑓(𝑧3)	=max{𝑧3,0}	 	 
 	𝑧4	=𝑥1𝑊14+𝑥2𝑊24+𝑊04	𝑓(𝑧4)	=max{𝑧4,0}	 	 
 	𝑢1	=𝑓(𝑧1)𝑉11+𝑓(𝑧2)𝑉21+𝑓(𝑧3)𝑉31+𝑓(𝑧4)𝑉41+𝑉01	𝑓(𝑢1)	=max{𝑢1,0}	 	 
 	𝑢2	=𝑓(𝑧1)𝑉12+𝑓(𝑧2)𝑉22+𝑓(𝑧3)𝑉32+𝑓(𝑧4)𝑉42+𝑉02	𝑓(𝑢2)	=max{𝑢2,0}.	 	 
The final output of the network is obtained by applying the softmax function to the last hidden layer,

 	𝑜1	=𝑒𝑓(𝑢1)𝑒𝑓(𝑢1)+𝑒𝑓(𝑢2)	 	 
 	𝑜2	=𝑒𝑓(𝑢2)𝑒𝑓(𝑢1)+𝑒𝑓(𝑢2).	 	 
In this problem, we will consider the following setting of parameters:

⎡⎣⎢⎢⎢⎢𝑊11𝑊12𝑊13𝑊14𝑊21𝑊22𝑊23𝑊24𝑊01𝑊02𝑊03𝑊04⎤⎦⎥⎥⎥⎥=⎡⎣⎢⎢⎢⎢10−10010−1−1−1−1−1⎤⎦⎥⎥⎥⎥,
 
[𝑉11𝑉12𝑉21𝑉22𝑉31𝑉32𝑉41𝑉42𝑉01𝑉02]=[1−11−11−11−102].


###  Feed Forward Step


Consider the input  𝑥1=3 ,  𝑥2=14 . What is the final output  (𝑜1,𝑜2)  of the network?

Important: Numerical outputs from the softmax function are sometimes extremely close to 0 or 1. We recommend you enter you answer as a mathematical expression, such as e∧2+1. If you choose to enter your answers as a decimal, you must enter the decimal accurate to at least 9 decimal places .


Answer = 

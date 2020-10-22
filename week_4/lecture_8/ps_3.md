# Introduction to Deep Neural Networks

A deep (feedforward) neural network refers to a neural network that contains not only the input and output layers, but also hidden layers in between. For example, below is a deep feedfoward neural network of 2 hidden layers, with each hidden layer consisting of 5 units:


One of the main advantages of deep neural networks is that in many cases, they can learn to extract very complex and sophisticated features from just the raw features presented to them as their input. For instance, in the context of image recognition, neural networks can extract the features that differentiate a cat from a dog based only on the raw pixel data presented to them from images.

The initial few layers of a neural networks typically capture the simpler and smaller features whereas the later layers use information from these low-level features to identify more complex and sophisticated features.


### Representation Power of Neural Networks: 1

In these two problems, we are going to explore how a neural network can represent any given binary functions. We will start in this problem by building the logic NAND function using a simple neural network.

The logic NAND function is defined as

 	 𝑦 	 = 	 NOT(𝑥1 AND 𝑥2) 	 	 
where  𝑥1  and  𝑥2∈{0,1}  are binary inputs (and  1  denotes  True  and  0  denotes  False ).


We will use the above simple neural network with  𝑧=𝑤1𝑥1+𝑤2𝑥2+𝑤0  and the activation function  𝑓 chosen to be the unit step function  𝑈(𝑧) :

𝑈(𝑧)={01𝑧≤0𝑧>0. 
 
Find  𝑤0 ,  𝑤1 , and  𝑤2  such that the output of the neural network  𝑦=𝑈(𝑧)  gives the NAND function as a function of  𝑥1  and  𝑥2 .
(Different correct answers will be accepted.)

Answer w0 = 20 
Answer w1 = -5
Answer w2 = -5


**Explination**

The NAND function is defined as y=NOT(x1 AND x2).

Step 1: The truth table of NAND gate is

X1	X2	Y
0	0	1
0	1	1
1	0	1
1	1	0
If we consider w0=20,w1=-15,w2=-15

We know that z=w1*x1+w2*x2+w0

f(z)=0 if z<=0

=1 if z>=0

For 1st row z=-15*0-15*0+20=20,so f(z)=1

For 2nd row z=-15*0-15*1+20=5,so f(z)=1

For 3rd row z=-15*1-15*0+20=5,so f(z)=1

For 4th row z=-15*1-15*1+20=-10,so f(z)=0

Step 2: So we can see that the value of w1,w2,w0 satisfies the condition of NAND gate. W1=-15,w2=-15,w0=20.This are one of the many possible values .we can say that w1=-20,w2=-20,w0=30 may be one of the many possible values.

Summary:This way we can find the values of weight of each possible path in neural network.



### Representation Power of Neural Networks: 2

Using the NAND function only as the basic neural network unit, we can build larger neural networks to implement other logic functions. For example, the follow neural network implements the logic  AND  function:


Note: Here, each pair of edges of the same color along with the nodes they are connected to form a neural network unit that represents the NAND function. (They do not represent values of inputs or outputs). In the example above,  𝑥1  and  𝑥2  are inputs to two NAND units, and are connected to output of respective units by the blue and orange arrows.

(Check that these output the correct values.)

Which logic function does each of the following neural networks implement?

(Choose one for each column.)


Answer = NOT function

Answer = OR function

NAND function is known as a universal logic function, which can be used to implement any boolean functions, including also XOR, without the use of any other type of function (except for the identity and zero function). Use De Morgan's law in boolean algebra.

NOT(𝑥1 AND 𝑥1)=NOT 𝑥1,
 
and

NOT( NOT (𝑥1) AND NOT(𝑥2))=NOT( NOT(𝑥1 OR 𝑥2))=𝑥1 OR 𝑥2.

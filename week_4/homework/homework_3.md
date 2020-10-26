# Backpropagation


One of the key steps for training multi-layer neural networks is stochastic gradient descent. We will use the back-propagation algorithm to compute the gradient of the loss function with respect to the model parameters.

Consider the  𝐿 -layer neural network below:


In the following problems, we will the following notation:  𝑏𝑙𝑗  is the bias of the  𝑗𝑡ℎ  neuron in the  𝑙𝑡ℎ  layer,  𝑎𝑙𝑗  is the activation of  𝑗𝑡ℎ  neuron in the  𝑙𝑡ℎ  layer, and  𝑤𝑙𝑗𝑘  is the weight for the connection from the  𝑘𝑡ℎ  neuron in the  (𝑙−1)𝑡ℎ  layer to the  𝑗𝑡ℎ  neuron in the  𝑙𝑡ℎ  layer.

If the activation function is  𝑓  and the loss function we are minimizing is  𝐶 , then the equations describing the network are:

 	 𝑎𝑙𝑗 	 =𝑓(∑𝑘𝑤𝑙𝑗𝑘𝑎𝑙−1𝑘+𝑏𝑙𝑗) 	 	 
 	 Loss 	 =𝐶(𝑎𝐿) 	 	 
Note that notations without subscript denote the corresponding vector or matrix, so that  𝑎𝑙  is activation vector of the  𝑙𝑡ℎ  layer, and  𝑤𝑙  is the weights matrix in  𝑙𝑡ℎ  layer.

For  𝑙=1,…,𝐿 .


### Computing the Error

Let the weighted inputs to the  𝑑  neurons in layer  𝑙  be defined as  𝑧𝑙≡𝑤𝑙𝑎𝑙−1+𝑏𝑙 , where  𝑧𝑙∈ℝ𝑑 . As a result, we can also write the activation of layer  𝑙  as  𝑎𝑙≡𝑓(𝑧𝑙) , and the “error" of neuron  𝑗  in layer  𝑙  as  𝛿𝑙𝑗≡∂𝐶∂𝑧𝑙𝑗 . Let  𝛿𝑙∈ℝ𝑑  denote the full vector of errors associated with layer  𝑙 .

Back-propagation will give us a way of computing  𝛿𝑙  for every layer.

Assume there are  𝑑  outputs from the last layer (i.e.  𝑎𝐿∈ℝ𝑑 ). What is  𝛿𝐿𝑗  for the last layer?

Answer = 


What is  𝛿𝑙𝑗  for all  𝑙≠𝐿 ?

Answer = ∑𝑘𝑤𝑙+1𝑘𝑗𝛿𝑙+1𝑘𝑓′(𝑧𝑙𝑗)


### Parameter Derivatives

During SGD we are interested in relating the errors computed by back-propagation to the quantities of real interest: the partial derivatives of the loss with respect to our parameters. Here that is  ∂𝐶∂𝑤𝑙𝑗𝑘  and  ∂𝐶∂𝑏𝑙𝑗 .

What is  ∂𝐶∂𝑤𝑙𝑗𝑘 ? Write in terms of the variables  𝑎𝑙−1𝑘 ,  𝑤𝑙𝑗 ,  𝑏𝑙𝑗 , and  𝛿𝑙𝑗  if necessary.

Example of writing superscripts and subscripts:

𝑑𝑒𝑙𝑡𝑎_𝑗\^𝑙  for  𝛿𝑙𝑗 

𝑤_(𝑗𝑘)\^𝑙  for  𝑤𝑙𝑗𝑘

Answer = a_k^(l-1)**delta_j^l 

What is  ∂𝐶∂𝑏𝑙𝑗 ? Write in terms of the variables  𝑎𝑙−1𝑘 ,  𝑤𝑙𝑗 ,  𝑏𝑙𝑗 , and  𝛿𝑙𝑗  if necessary.

Answer = delta_j^l


### Activation Functions: Sigmoid


Recall that there are several different possible choices of activation functions  𝑓 . Let's get more familiar with them and their gradients.

What is the derivative of the sigmoid function,  𝜎(𝑧)=11+𝑒−𝑧 ? Please write your answer in terms of  𝑒  and  𝑧 :


Answer = 1-(1/(1+e^(-z)))

Which of the following is true of  𝜎′(𝑧)  as  ||𝑧||  gets large?

Answer = Its magnitude becomes small.

What is the derivative of the ReLU function,  ReLU(𝑧)=max(0,𝑧)  for  𝑧>0 ?

Answer = 1

For  𝑧<0 ?

Answer = 0

### Simple Network


Consider a simple 2-layer neural network with a single neuron in each layer. The loss function is the quadratic loss:  𝐶=12(𝑦−𝑡)2 , where  𝑦  is the prediction and  𝑡  is the target.

Starting with input  𝑥  we have:

𝑧1=𝑤1𝑥 

𝑎1=ReLU(𝑧1) 

𝑧2=𝑤2𝑎1+𝑏 

𝑦=𝜎(𝑧2) 

𝐶=12(𝑦−𝑡)2 

Consider a target value  𝑡=1  and input value  𝑥=3 . The weights and bias are  𝑤1=0.01 ,  𝑤2=−5 , and  𝑏=−1 .

Please provide numerical answers accurate to at least three decimal places.

What is the loss?


Answer = 0.288

What are the derivatives with respect to the parameters?

Answer = 2.080

Answer = -0.004

Answer = -0.1387


### SGD


Referring to the previous problem, what is the update rule for  𝑤1  in the SGD algorithm with step size  𝜂 ? Write in terms of  𝑤1 ,  𝜂 , and  ∂𝐶∂𝑤1 ; enter the latter as (partialC)/(partialw_1), noting the lack of space in the variable names:


Answer next w1 = w_1-eta*(partialC)/(partialw_1)









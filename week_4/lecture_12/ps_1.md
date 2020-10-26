# Convolutional Neural Networks


### Motivation for CNN


Let's suppose that we wish to classify images of  1000×1000  dimensions.

We wish to pass the above input through a feed-forward neural network with a single hidden layer made up of  1000×1000  hidden units each of which is fully connected to the full image.

If the number of connections that exist between the first hidden layer and the input image is given by x, then enter below the value of  𝑙𝑜𝑔10(𝑥) , i.e. the logarithm of  𝑥  to the base  10 :

Answer = 12

Instead of a fully-connected layer, now suppose that we use a convolutional layer with  1  filter of shape  11×11  instead. Enter below the number of parameters in the first layer (ignoring the bias terms):

Answer = 121


### Second Motivation for CNN

Suppose a feed-forward, non-convolutional neural network is learning how to classify images. Then, it can classify images even if the relevant object is in a different part of the image.

Answer = False


### Convolution: Continuous Case

In the lecture we saw the example of using the convolution operation to create a feature map. Here we formally define the convolution as an operation between 2 functions  𝑓  and  𝑔 :

(𝑓∗𝑔)(𝑡)≡∫+∞−∞𝑓(𝜏)𝑔(𝑡−𝜏)𝑑𝜏 
 
In this integral,  𝜏  is the dummy variable for integration and  𝑡  is the parameter. Intuitively, convolution 'blends' the two function  𝑓  and  𝑔  by expressing the amount of overlap of one function as it is shifted over another function.

Now, suppose we are given two rectangular function  𝑓  and  𝑔  as shown in the figures below.


What is the shape of of  𝑓∗𝑔 ?

Answer = 1st image

What is the area under the convolution:  ∫+∞−∞(𝑓∗𝑔)𝑑𝑡

Answer = The product of the areas under  𝑓  and  𝑔


### Convolution: 1D Discrete Case


Similarly, for discrete functions, we can define the convolution as:

(𝑓∗𝑔)[𝑛]≡∑𝑚=−∞𝑚=+∞𝑓[𝑚]𝑔[𝑛−𝑚] 
 
Here, we give an example of convolution on 1D discrete signal.
Let  𝑓[𝑛]=[1,2,3] ,  𝑔[𝑛]=[2,1]  and suppose  𝑛  starts from  0 . We are computing  ℎ[𝑛]=𝑓[𝑛]∗𝑔[𝑛] .
As  𝑓  and  𝑔  are finite signals, we just put  0  to where  𝑓  and  𝑔  are not defined. This is usually called zero padding. Now, let's compute  ℎ[𝑛]  step by step:

 	 ℎ[0] 	 = 	 𝑓[0]⋅𝑔[0−0]+𝑓[1]⋅𝑔[0−1]+⋯=𝑓[0]⋅𝑔[0]=2 	 	 
 	 ℎ[1] 	 = 	 𝑓[0]⋅𝑔[1−0]+𝑓[1]⋅𝑔[1−1]+𝑓[2]⋅𝑔[1−2]+⋯=𝑓[0]⋅𝑔[1]+𝑓[1]⋅𝑔[0]=5 	 	 
 	 ℎ[2] 	 = 	 𝑓[0]⋅𝑔[2−0]+𝑓[1]⋅𝑔[2−1]+𝑓[2]⋅𝑔[2−2]+𝑓[3]⋅𝑔[2−3]+⋯=𝑓[1]⋅𝑔[1]+𝑓[2]⋅𝑔[0]=8 	 	 
 	 ℎ[3] 	 = 	 𝑓[0]⋅𝑔[3−0]+𝑓[1]⋅𝑔[3−1]+𝑓[2]⋅𝑔[3−2]+𝑓[3]⋅𝑔[3−3]+𝑓[4]⋅𝑔[3−4]+⋯=𝑓[2]⋅𝑔[1]=3 	 	 
The other parts of  ℎ  are all  0 .

Intuitively, we can get this result by first flipping g[n] and shift it over f[n] and compute the inner product at each step, as shown in the figures below:



n practice, it is common to call the flipped  𝑔′  as filter or kernel, for the input signal or image  𝑓 .

As we forced to pad zeros to where the input are not defined, the result on the edge of the input may not be accurate. To avoid this, we can just keep the convolution result where  𝑔′  has operated exclusively on where the input  𝑓  is actually defined. That is  ℎ[𝑛]=[5,8] .

Now suppose the input  𝑓=[1,3,−1,1,−3] , and the filter  𝑔′=[1,0,−1] , what is the convolutional output of  𝑓∗𝑔  without zero padding on  𝑓 ? Enter your answer as a list below (e.g. [0,0,0])


Answer = [ 2, 2, 2 ]

What is the convolutional output of  𝑓∗𝑔  if we pad a  0  on both edges of  𝑓  so that the output dimension is the same as the input? Enter your answer as a list below (e.g. [0,0,0,0,0])

Answer = [ -3, 2, 2, 2, 1 ]



### Convolution: 2D Discrete Case


Now, let's apply the same idea on images, which are 2D discrete signals. Suppose we had an image  𝑓  and a filter  𝑔′  as shown below. Calculate the sum of the elements in the output matrix after passing the image through the convolutional filter, without zero padding.

𝑓=⎡⎣⎢⎢121211111⎤⎦⎥⎥ 
 
𝑔′=[10.50.51]


Answer = 15


### Pooling Practice


A pooling layer's purpose is to pick up on a feature regardless of where it appears in the image.


Answer = true











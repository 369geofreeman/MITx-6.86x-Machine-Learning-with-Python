# CNN - Continued


### CNN - Numerical Example


In this problem, we are going to work out the outputs of a tiny toy example of CNN that is made up of just one conv layer consisting of just one filter  𝐹  of shape  2×2  followed by a max-pooling layer of shape  2×2 . The input image is of shape  3×3 

The output of the CNN is calculated as  Pool(ReLU(Conv(𝐼)))  where ReLU is the rectified linear activation function given by:

ReLU(𝑥)=max(0,𝑥) 
 
Also assume that the stride for the convolution and pool layers is  1 

For the following values of the image  𝐼  and filter weights  𝐹  enter below the value of the output of the CNN (hint - it will be a single integer):

𝐼=⎡⎣⎢⎢130010204⎤⎦⎥⎥ 
 
𝐹=[1001]


Answer = 5



### CNN Meaning


If you are trying to recognize a large number of features, you should have a small number of filters.

Answer = False




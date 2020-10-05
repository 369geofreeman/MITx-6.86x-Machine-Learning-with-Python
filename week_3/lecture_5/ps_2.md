# Problem set two


### Compute Hinge Loss


The empirical risk 𝑅𝑛 is defined as

𝑅𝑛(𝜃)=1𝑛∑𝑡=1𝑛Loss(𝑦(𝑡)−𝜃⋅𝑥(𝑡))
 
where (𝑥(𝑡),𝑦(𝑡)) is the 𝑡th training example (and there are 𝑛 in total), and Loss is some loss function, such as hinge loss.

Recall from a previous lecture that the definition of hinge loss:

Lossℎ(𝑧)={01−𝑧,if 𝑧≥1 otherwise.
 
In this problem, we calculate the empirical risk with hinge loss when given specific 𝜃 and {(𝑥(𝑡),𝑦(𝑡))}𝑡=1,...,𝑛. Assume we have 4 training examples (i.e. 𝑛=4), where 𝑥(𝑡)∈ℝ3 and 𝑦(𝑡) is a scalar. The training examples {(𝑥(𝑡),𝑦(𝑡))}𝑡=1,2,3,4 are given as follows:

 	𝑥(𝑡)	𝑦(𝑡)
(𝑥(1),𝑦(1))	[1,0,1]𝑇	2
(𝑥(2),𝑦(2))	[1,1,1]𝑇	2.7
(𝑥(3),𝑦(3))	[1,1,−1]𝑇	−0.7
(𝑥(4),𝑦(4))	[−1,1,1]𝑇	2
Also, we have 𝜃=[0,1,2]𝑇.

Compute the value of

𝑅𝑛(𝜃)=14∑𝑡=14Lossℎ(𝑦(𝑡)−𝜃⋅𝑥(𝑡)).


Answer = 0.8525 <- wrong


### Compute Squared Error Loss


Now, we will calculate the empirical risk with the squared error loss. Remember that the squared error loss is given by Loss(𝑧)=𝑧22.

The 4 training examples are as in the previous problem:

 	𝑥(𝑡)	𝑦(𝑡)
(𝑥(1),𝑦(1))	[1,0,1]𝑇	2
(𝑥(2),𝑦(2))	[1,1,1]𝑇	2.7
(𝑥(3),𝑦(3))	[1,1,−1]𝑇	−0.7
(𝑥(4),𝑦(4))	[−1,1,1]𝑇	2
As in the problem above, we have 𝜃=[0,1,2]𝑇.

Compute the value of

𝑅𝑛(𝜃)=14∑𝑡=14Loss(𝑦(𝑡)−𝜃⋅𝑥(𝑡))


Answer = 0.1475


### Geometrically Identifying Error

What type of error does the figure below depict? The blue dots are the training examples, and the red line is the predictor  𝑓̂ (𝑥)

Answer = Structual error

### Increasing the Number of Training Examples

Answer = Estimation error



### Empirical Risk and Model Performance

If we are given a large amount of training data and successfully obtain 0 empirical risk, is the model we learned guaranteed to perform well on the test data? (Assume training and test data are drawn from the same distribution.)

Answer = no



(Optional) Error decomposition and the bias-variance trade-off
(Optional) Error decomposition and the bias-variance trade-off

In the lecture, we intuitively defined the structural and estimation mistakes. Here we provide a more formal definition of these ideas for a regression problem.

Suppose we want to learn the relationship between random variables  𝑥∈ℝ𝑑  and  𝑦∈ℝ , where the ground truth relationship is  𝑦=𝑓(𝑥) . Of course  𝑓  is unkown to us, but we observe a training set  (𝑥1,𝑦1) ,  (𝑥2,𝑦2) , ...,  (𝑥𝑛,𝑦𝑛)  and we hope to find a function  𝑓̂   to approximate the true funtion  𝑓 .

However, our observed data might not be  100%  accurate as there can be many kinds of noise and uncertainty containing in the data. Thus, we further assume a random noise variable  𝜖  is added on top of  𝑦 :

𝑦=𝑓(𝑥)+𝜖 
 
where  𝜖∼(0,𝜎2) 

We learned from the lecture that we can find  𝑓̂   by minimizing the empirical risk on the training set. As we know the training set is a random observation of the underlying relationship and contains noise, different training set will give us different estimator  𝑓̂ (𝑥) . Hence, we can define  𝔼[𝑓̂ (𝑥)]  to be the expected estimator over all possible training sets.

Now let's look at when we have a new  𝑥  with unkonwn  𝑦 , what is the expected prediction error looks like for our estimator given all possible training sets:

 	 𝔼[(𝑦−𝑓̂ (𝑥))2] 	 =𝔼[(𝑓(𝑥)+𝜖−𝑓̂ (𝑥))2] 	 	 
 	 	 =(𝑓(𝑥)−𝔼[𝑓̂ (𝑥)])2+𝔼[(𝑓̂ (𝑥)−𝔼[𝑓̂ (𝑥)])2]+𝔼[𝜖2] 	 	 
We skip some derivations of this result, can you get this result on your own?

As we can see, there are three terms in this error decomposition:

The first term is the square of the difference between the true  𝑓(𝑥)  and the expected estimation over all possible training sets. This term is usually called bias and it describes how much the average estimator fitted over all datasets deviates from the underlying true  𝑓(𝑥) . This corresponds to the structural mistake in the lecture.

The second term is the variacne of the estimator (recall variance definition in statistics). It describes on average how much a single estimator deviates from the expected estimator over all data sets. This corresponds to the estimation error in the lecture.

The thrid term  𝔼[𝜖2]=𝜎2  is the error from the inherent noise of the data and we can do nothing to minimize it, thus it is sometimes called irreducible error. The irreducible error gives a lower bound on the expected prediction error.

Question for you to think: Apparently, the empricial risk is just an approximation of the true risk (i.e.  𝔼[(𝑓(𝑥)−𝑓̂ (𝑥))2] ). If we were able to learn the model by minimizing the true risk, which part of the error decomposition will become 0?

The task of supervised learning is to reduce the bias and variance at the same time, but because of the noise in the training data, it is not possible to simultaneously minimize these two sources of errors. This is known as the bias-variance trade-off.


To reduce bias, we can assume a more complex hypothesis space and fit a more powerful model. The model will be able to fit even the noise in the training set. However, this increases the error from variance becuase given another training set, the randomness of the noise will results in a very different model. This situation is often called 'overfitting'. On the other hand, we can have a more simple model to reduce the variance, but this can make the bias very large. For example, in the extreme case, let our model be  𝑓̂ (𝑥)=𝑐 , where  𝑐  is a constant. This will give us  0  variance but you can imagine it can hardly make any correct predictions. This situation is known as 'underfitting'.

In a few pages, you will see how regularization can be used to restrict the complexity for linear regression so that we will be able to search for a sweet spot where the total error from variance and bias is the minimum.

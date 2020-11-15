# Recap of Maximum Likelihood Estimation for Multinomial and Gaussian Models


So far, in clustering we have assumed that the data has no probabilistic generative model attached to it, and we have used various iterative algorithms based on similarity measures to come up with a way to group similar data points into clusters. In this lecture, we will assume an underlying probabilistic generative model that will lead us to a natural clustering algorithm called the EM algorithm .

While a “hard" clustering algorithm like k-means or k-medoids can only provide a cluster ID for each data point, the EM algorithm, along with the generative model driving its equations, can provide the posterior probability (“soft" assignments) that every data point belongs to any cluster.

The EM algorithm will also form the basis for a portion of Project 4 in which we explore collaborative filtering via Gaussian mixtures.



## MLE under Gaussian Noise I

Let  𝑌𝑖=𝜃+𝑁𝑖,𝑖=1,…,𝑛 , where  𝜃  is an unknown parameter and  𝑁𝑖  are iid Gaussian random variables with zero mean. Upon observing  𝑌𝑖 's, what is the maximum likelihood estimate of  𝜃 ?

Choose the correct expression from options below.

Hint: For this problem, think of the distributional property of the random variables  𝑌𝑖  and how they are derived from  𝑁𝑖 's. Also, remember that  𝑁𝑖  are iid Gaussian random variables.


Answer =  𝜃̂ =∑𝑛𝑖=1𝑌𝑖𝑛  correct 



## MLE under Gaussian Noise II


Would the ML estimator of  𝜃  change if the  𝑁𝑖 's are independent Gaussians with possibly different variances  𝜎21,…,𝜎2𝑛  but same zero mean? Assume that  𝜎2𝑖  are known constants.


Answer = YES


## MLE under Gaussian Noise III

Now, let  𝑌𝑖=𝜃+𝑁𝑖,𝑖=1,…,𝑛 , where  𝜃  is an unknown parameter. This time, let  𝑁𝑖  for all  𝑖=1,…,𝑛  each be a linear combination of  ℓ  zero-mean, independent Gaussian random variables with possibly different variances. That is, let  𝑁𝑖=𝑁𝑖,1+⋯+𝑁𝑖,ℓ , where  𝑁𝑖,𝑗  for a given  𝑖  are independent with possibly different variances. Let  {𝑁𝑖,𝑗:𝑖=1,…,𝑛 and 𝑗=1,…,ℓ}  be independent random variables, but with the condition that for a given  𝑗  the variance of  𝑁𝑖,𝑗  is the same for  𝑖=1,…,𝑛 .

Is the ML estimator of  𝜃  the same as the one we found in the problem "MLE under Gaussian Noise I"?


Answer = YES





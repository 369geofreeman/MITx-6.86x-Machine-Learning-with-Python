##  EM Algorithm


Consider the following mixture of two Gaussians:

𝑝(𝑥;𝜃)=𝜋1(𝑥;𝜇1,𝜎21)+𝜋2(𝑥;𝜇2,𝜎22) 
 
This mixture has parameters  𝜃={𝜋1,𝜋2,𝜇1,𝜇2,𝜎21,𝜎22} . They correspond to the mixing proportions, means, and variances of each Gaussian. We initialize  𝜃  as  𝜃0={0.5,0.5,6,7,1,4} .

We have a dataset    with the following samples of  𝑥 :  𝑥(0)=−1 ,  𝑥(1)=0 ,  𝑥(2)=4 ,  𝑥(3)=5 ,  𝑥(4)=6 .

We want to set our parameters  𝜃  such that the data log-likelihood  𝑙(;𝜃)  is maximized:

argmax𝜃 ∑𝑖=04log𝑝(𝑥(𝑖);𝜃). 
 
Recall that we can do this with the EM algorithm. The algorithm optimizes a lower bound on the log-likelihood, thus iteratively pushing the data likelihood upwards. The iterative algorithm is specified by two steps applied successively:

E-step: infer component assignments from current  𝜃0=𝜃  (complete the data)

𝑝(𝑦=𝑘∣𝑥(𝑖)):=𝑝(𝑦=𝑘∣𝑥(𝑖);𝜃0), for 𝑘=1,2, and 𝑖=0,…,4. 
 
M-step: maximize the expected log-likelihood

𝑙̃ (𝐷;𝜃):=∑𝑖∑𝑘𝑝(𝑦=𝑘∣𝑥(𝑖))log𝑝(𝑥(𝑖),𝑦=𝑘;𝜃)𝑝(𝑦=𝑘∣𝑥(𝑖)) 
 
with respect to  𝜃  while keeping  𝑝(𝑦=𝑘∣𝑥(𝑖))  fixed.

To see why this optimizes a lower bound, consider the following inequality:

 	 log𝑝(𝑥;𝜃) 	 =log∑𝑦𝑝(𝑥,𝑦;𝜃) 	 	 
 	 	 =log∑𝑦𝑞(𝑦|𝑥)𝑝(𝑥,𝑦;𝜃)𝑞(𝑦|𝑥) 	 	 
 	 	 =log𝔼𝑦∼𝑞(𝑦|𝑥)[𝑝(𝑥,𝑦;𝜃)𝑞(𝑦|𝑥)] 	 	 
 	 	 ≥𝔼𝑦∼𝑞(𝑦|𝑥)[log𝑝(𝑥,𝑦;𝜃)𝑞(𝑦|𝑥)] 	 	 
 	 	 =∑𝑦𝑞(𝑦|𝑥)log𝑝(𝑥,𝑦;𝜃)𝑞(𝑦|𝑥) 	 	 
where the inequality comes from Jensen's inequality . EM makes this bound tight for the current setting of  𝜃  by setting  𝑞(𝑦|𝑥)  to be  𝑝(𝑦∣𝑥;𝜃0) .

Note: If you have taken 6.431x Probability–The Science of Uncertainty, you could review the video in Unit 8: Limit Theorems and Classical Statistics, Additional Theoretical Material, 2. Jensen's Inequality.


## Likelihood Function

What is the log-likelihood of the data  𝑙(;𝜃)  given the initial setting of  𝜃 ? Please round to the nearest tenth.

Note: You will want to write a script to calculate this, using the natural log (np.log) and np.float64 data types.


Answer = -24.5


## E-Step


What is the formula for  𝑝(𝑦=𝑘∣𝑥,𝜃) ? Write in terms of  𝜋𝑘 ,  𝜋1 ,  𝜋2 ,  𝑁𝑘 ,  𝑁1 , and  𝑁2  (where  𝑁𝑘=(𝑥∣𝜇𝑘,𝜎2𝑘) ).


Answer = pi_k * N_k) / (pi_1 * N_1 + pi_2 * N_2)
 


## E-Step Weights


For each of the given data points say which Gaussian (1 or 2) they are given more weight towards in the first E-step using the given setting of  𝜃0 . This is, answer 2 if  𝑝(𝑦=2∣𝑥,𝜃0)>𝑝(𝑦=1∣𝑥,𝜃0)  and 1 otherwise.


Answer = 2

Answer = 2

Answer = 2

Answer = 1

Answer = 1




## M-Step


Fixing  𝑝(𝑦=𝑘∣𝑥,𝜃0) , we want to update  𝜃  such that our lower bound is maximized.

What is the optimal  𝜇̂ 𝑘 ? For simplicity, assume we only have two data points  𝑥(1)  and  𝑥(2)  for this particular question. Answer in terms of  𝑥(1) ,  𝑥(2) , and  𝛾𝑘1 ,  𝛾𝑘2 , which are defined to be  𝛾𝑘𝑖=𝑝(𝑦=𝑘∣𝑥(𝑖);𝜃0) 

(For ease of input, use subscripts instead superscripts, i.e. type x_i for  𝑥(𝑖) . Type gamma_ki for  𝛾𝑘𝑖 .)


Answer = (gamma_k1 * x_1 + gamma_k2 * x_2) / (gamma_k1 + gamma_k2)

What is the optimal  𝜎̂ 2𝑘 ? Answer in terms of  𝑥(1) ,  𝑥(2) ,  𝛾𝑘1  and  𝛾𝑘2 , which are defined as above to be  𝛾𝑘𝑖=𝑝(𝑦=𝑘∣𝑥(𝑖);𝜃0) , and  𝜇̂ 𝑘 .

(Type hatmu_k for  𝜇̂ 𝑘 . As above, for ease of input, use subscripts instead superscripts, i.e. type x_i for  𝑥(𝑖) . Type gamma_ki for  𝛾𝑘𝑖 .)


Answer = (gamma_k1 * (x_1 - hatmu_k)^2 + gamma_k2 * (x_2 - hatmu_k)^2) / (gamma_k1 + gamma_k2)


What is the optimal 𝜋̂ 𝑘? Answer in terms of 𝛾𝑘1 and 𝛾𝑘2, which are defined as above to be 𝛾𝑘𝑖=𝑝(𝑦=𝑘∣𝑥(𝑖);𝜃0),

(As above, type gamma_ki for 𝛾𝑘𝑖.)

Note: that you must account for the constraint that 𝜋1+𝜋2=1 where 𝜋1,𝜋2≥0.

Note: If you know that some aspect of your formula equals an exact constant, simplify and use this number, i.e. 𝛾11+𝛾21=1.


Answer = (gamma_k1 + gamma_k2) / 2
 
## Training 1


In the first M-step, which Gaussian will shift to the left more (relatively)?

Answer = Gaussian 2



## Training 2


In the first M-step, which Gaussian's variance will increase more (relatively)?

Answer = Gaussian 2


## Training 3


After convergence, which variance will be larger?

Answer =  𝜎21




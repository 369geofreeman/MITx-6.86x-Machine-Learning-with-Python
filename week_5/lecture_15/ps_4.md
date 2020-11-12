# Maximum Likelihood Estimate]


## Number of Parameters


For the following set of questions, let us consider generating documents that are English letter sequences (assume no spaces or punctuation), i.e. the vocabulary  𝑊={𝑎,𝑏,𝑐...,𝑧}  is made up of all the letters in the English alphabet.

We would like to generate documents using this vocabulary using a multinomial model  𝑀 . As described in the lecture, what is the minimal number of parameters that the model  𝑀  should have? Enter your answer below.


Answer = 25




## Maximum Likelihood Estimate


Let  𝜃∗=𝜃∗𝑎,𝜃∗𝑏,…,𝜃∗𝑧  be the parameters of the multinomial model  𝑀∗  that maximize the likelihood of generating a document  𝐷 .

Further, it is known that the letter 'e' is twice as likely to occur as the letter 'z' in document  𝐷 .

Which of the following options is a correct expression relating  𝜃∗𝑒  and  𝜃∗𝑧 ?



Answer = 𝜃∗𝑒=2𝜃∗𝑧


## Maximum Likelihood Estimate for Poisson Distribution


Maximum Likelihood Estimate (MLE) is a very general method that can be applied to both continuous and discrete distributions. In this problem, we assume we have a training data  𝑥1,𝑥2…,𝑥𝑛  that are drawn from a Poisson distribution, with probability mass function (pmf)

𝑃(𝑋=𝑥)=𝜆𝑥𝑒−𝜆𝑥!. 
 
We want to use MLE to fit the parameter  𝜆  with the training data. To do so, we first compute the log likelihood of our training data, or in other words, log of the probability of obtaining the sample  𝑥1,𝑥2,…,𝑥𝑛  given the model and where  𝑥𝑖  are independent. The log likelihood is...

Answer = log𝜆∑𝑖𝑥𝑖−𝑛𝜆−∑𝑖log(𝑥𝑖!)  


In the next step, we maximize this log likelihood function by taking the derivative. What is the resulting estimate for  𝜆 ?

Answer =  1𝑛∑𝑖𝑥𝑖


Is it in accordance with the definition of  𝜆  in Poisson distribution? (There is no answer box for this question.)





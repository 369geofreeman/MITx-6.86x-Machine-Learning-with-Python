# Homework part 6


A univariate Gaussian or normal distributions can be completely determined by its mean and variance.

Gaussian distributions can be applied to a large numbers of problems because of the central limit theorem (CLT). The CLT posits that when a large number of independent and identically distributed ((i.i.d.) random variables are added, the cumulative distribution function (cdf) of their sum is approximated by the cdf of a normal distribution.

# Probability review: PDF of Gaussian distribution

## 1) 

In practice, it is not often that you will need to work directly with the probability density function (pdf) of Gaussian variables. Nonetheless, we will make sure we know how to manipulate the (pdf) in the next two problems.

The pdf of a Gaussian random variable  𝑋  is given by:
```
			 n       (  n²(x-2)²  )
		fx(x) = ---- exp |  --------  |
			3√2π     (    18      )
```


then what is the mean  𝜇  and variance  𝜎2  of  𝑋 ?
(Enter your answer in terms of  𝑛 .)

𝜇= 2

𝜎2 = 2⋅𝜋


# Probability review: PDF of Gaussian distribution

## 1)

Let  𝑋∼(𝜇,𝜎2) , i.e. the pdf of  𝑋  is:

```
        1     (  (x-μ)² )
p(x) = --- exp|- -----  |
      σ√2π    (  2σ²    )

```

Let  𝑌=2𝑋 . Write down the pdf of the random variable  𝑌 . (Your answer should be in terms of  𝑦 ,  𝜎  and  𝜇 . Type mu for  𝜇 , sigma for  𝜎 .)

𝑓𝑌(𝑦) =  



# Argmax

Let  𝑓𝑋(𝑥;𝜇,𝜎2)  denote the probability density function of a normally distributed variable  𝑋  with mean  𝜇  and variance  𝜎2 . What value of  𝑥  maximizes this function?

(Enter mu for the mean  𝜇 , and sigma^2 for the variance  𝜎2 .)

Answer = 


# Maximum of pdf

As above, let  𝑓𝑋(𝑥;𝜇,𝜎2)  denote the probability density function of a normally distributed variable  𝑋  with mean  𝜇  and variance  𝜎2 .

What is the maximum value of  𝑓𝑋(𝑥;𝜇,𝜎2)  ?
(Enter mu for the mean  𝜇 , and sigma^2 for the variance  𝜎2 .)


Answer = 



# Quantiles

The quantile of order  1−𝛼  of a variable  𝑋 , denoted by  𝑞𝛼  (specific to a particular  𝑋 ), is the number such that  𝐏(𝑋≤𝑞𝛼)=1−𝛼 .

Graphed below is the pdf of the normal distribution with generic/unknown (but fixed) variance  𝜎2 . If the total area of the two shaded regions is  0.03 , then what is  𝑥 ?
(Choose all that apply.)


Answer = 




# Probability 

Let 𝑋∼(1,2), i.e., the random variable 𝑋 is normally distributed with mean 1 and variance 2. What is the probability that 𝑋∈[0.5,2]?

(Enter your answer accurate to at least 4 decimal places.)

𝑃(𝑋∈[0.5,2]) =  















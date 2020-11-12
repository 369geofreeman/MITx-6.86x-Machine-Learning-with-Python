# MLE for Gaussian Distribution


## MLE for the Gaussian Distribution

In this problem, we will derive the maximum likelihood estimates for a Gaussian model.

Let  𝑋  be a Gaussian random variable in d-dimensional real space ( 𝑅𝑑 ) with mean  𝜇  and standard deviation  𝜎 .

Note that  𝜇,𝜎  are the parameters of a Gaussian generative model.

Recall from the lecture that, the probability density function for a Gaussian random variable is given as follows:

𝑓𝑋(𝑥|𝜇,𝜎2)=1(2𝜋𝜎2)𝑑/2𝑒−‖𝑥−𝜇‖2/2𝜎2 
 
Let  𝑆𝑛={𝑋(1),𝑋(2),...𝑋(𝑛)}  be i.i.d. random variables following a Gaussian distribution with mean  𝜇  and variance  𝜎2 .

Then their joint probability density function is given by

∏𝑡=1𝑛𝑃(𝑥(𝑡)|𝜇,𝜎2)=∏𝑡=1𝑛1(2𝜋𝜎2)𝑑/2𝑒−‖𝑥(𝑡)−𝜇‖2/2𝜎2 
 
Taking logarithm of the above function, we get

 	 log𝑃(𝑆𝑛|𝜇,𝜎2)=log(∏𝑡=1𝑛1(2𝜋𝜎2)𝑑/2𝑒−‖𝑥(𝑡)−𝜇‖2/2𝜎2) 	 = 	 ∑𝑡=1𝑛log1(2𝜋𝜎2)𝑑/2+∑𝑡=1𝑛log𝑒−‖𝑥(𝑡)−𝜇‖2/2𝜎2 	 	 
 	 	 = 	 ∑𝑡=1𝑛−𝑑2log(2𝜋𝜎2)+∑𝑡=1𝑛log𝑒−‖𝑥(𝑡)−𝜇‖2/2𝜎2 	 	 
 	 	 = 	 −𝑛𝑑2log(2𝜋𝜎2)−12𝜎2∑𝑡=1𝑛‖𝑥(𝑡)−𝜇‖2. 	 	 
Compute the partial derivative  ∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜇  using the above derived expression for  log𝑃(𝑆𝑛|𝜇,𝜎2) .

Choose the correct expression from options below.


Answer = ∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜇=1𝜎2∑𝑛𝑡=1(𝑥(𝑡)−𝜇)


## MLE for the Mean

Use the answer from the previous problem in order to solve the following equation

∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜇=0 
 
Compute expression for  𝜇̂   that is a solution for the above equation.

Choose the correct expression from options below

Answer = 𝜇̂ =∑𝑛𝑡=1𝑥(𝑡)𝑛


## MLE for the Variance I


Compute the partial derivative  ∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜎2  using the above derived expression for  log𝑃(𝑆𝑛|𝜇,𝜎2)  which is restated below as well:

log𝑃(𝑆𝑛|𝜇,𝜎2)=−𝑛𝑑2log(2𝜋𝜎2)−12𝜎2∑𝑡=1𝑛‖𝑥(𝑡)−𝜇‖2 
 
Choose the correct expression from options below.


Answer = ∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜎2=−𝑛𝑑2𝜎2+∑𝑛𝑡=1‖𝑥(𝑡)−𝜇‖22(𝜎2)2


## MLE for the Variance II


Using the answer from the previous problem in order to solve the equation

∂log𝑃(𝑆𝑛|𝜇,𝜎2)∂𝜎2=0 
 
Compute expression for  𝜎̂ 2  that is a solution for the above equation.

Choose the correct expression from options below


Answer = 𝜎̂ 2=∑𝑛𝑡=1‖𝑥(𝑡)−𝜇‖2𝑛𝑑







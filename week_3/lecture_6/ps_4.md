# Problem set 4


## The Kernel Perceptron Algorithm



### How the Kernel Perceptron Algorithm Works: Initalization

Recall that the original Perceptron Algorithm is given as the following:


Perceptron ({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛},𝑇): 
  initialize  𝜃=0  (vector);
    for  𝑡=1,...,𝑇 ,
      for  𝑖=1,...,𝑛 ,
        if  𝑦(𝑖)(𝜃⋅𝑥(𝑖))≤0 ,
        then update  𝜃=𝜃+𝑦(𝑖)𝑥(𝑖). 

In the lecture, it was introduced that we can always express  𝜃  as

 	 𝜃=∑𝑗=1𝑛𝛼𝑗𝑦(𝑗)𝜙(𝑥(𝑗)) 	 	 
where values of  𝛼1,…,𝛼𝑛  may vary at each step of the algorithm. In other words, we can reformulate the algorithm so that we somehow initialize and update  𝛼𝑗 's, instead of  𝜃 .

The reformulated algorithm, or kernel perceptron , can be given in the following form:


Kernel Perceptron ({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛,𝑇}) 
  Initialize  𝛼1,𝛼2,...,𝛼𝑛  to some values;
  for  𝑡=1,...,𝑇 
    for  𝑖=1,...,𝑛 
      if  (Mistake Condition Expressed in 𝛼𝑗) 
        Update  𝛼𝑗  appropriately

Look at the initialization statement of the algorithm. Which of the following is an equivalent way to initialize  𝛼1,𝛼2,...,𝛼𝑛 , if we want the same result as initializing  𝜃=0 ?

Answer =  𝛼1=...=𝛼𝑛=0


### How the Kernel Perceptron Algorithm Works: The Update

As in the previous problem, our goal is to correctly reformulate the original perceptron algorithm. In other words, we want the algorithm to be about updating  𝛼𝑗 's instead of  𝜃 .


Kernel Perceptron ({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛,𝑇}) 
  initialize  𝛼1,𝛼2,...,𝛼𝑛  to some values;
  for  𝑡=1,...,𝑇 
    for  𝑖=1,...,𝑛 
      if  (Mistake Condition Expressed in 𝛼𝑗) 
        Update  𝛼𝑗  appropriately

Now look at the line "Update  𝛼𝑗  appropriately" in the above algorithm. Remember that we express  𝜃  as

𝜃=∑𝑗=1𝑛𝛼𝑗𝑦(𝑗)𝜙(𝑥(𝑗)) 
 
Assuming that there was a mistake in classifying the  𝑖 th data point i.e.

𝑦(𝑖)(𝜃⋅𝑥(𝑖))≤0 
 
which of the following conditions about  𝛼1,...,𝛼𝑛  is equivalent to

𝜃=𝜃+𝑦(𝑖)𝜙(𝑥(𝑖)), 
 
the update condition of the original algorithm?


Answer = 𝛼𝑖=𝛼𝑖+1

### How the Kernel Perceptron Algorithm Works: The Mistake Condition


Kernel Perceptron({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛,𝑇})
  initialize 𝛼1,𝛼2,...,𝛼𝑛 to some values;
  for 𝑡=1,...,𝑇
    for 𝑖=1,...,𝑛
      if (Mistake Condition Expressed in 𝛼𝑗)
        Update 𝛼𝑗 appropriately

Now look at the line "Mistake Condition Expressed in 𝛼𝑗" in the above algorithm. Remember that we express 𝜃 as

𝜃=∑𝑗=1𝑛𝛼𝑗𝑦(𝑗)𝜙(𝑥(𝑗))
 
Which of the following conditions is equivalent to 𝑦(𝑖)(𝜃⋅𝜙(𝑥(𝑖)))≤0? Remember from the video lecture above that given feature vectors 𝜙(𝑥) and 𝜙(𝑥′), we define the Kernel function 𝐾 as

𝐾(𝑥,𝑥′)=𝜙(𝑥)𝜙(𝑥′).

Answer = 𝑦(𝑖)∑𝑛𝑗=1𝛼𝑗𝑦(𝑗)𝐾(𝑥𝑗,𝑥𝑖)≤0



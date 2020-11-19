# Maximum Likelihood Estimation




Consider a general multinomial distribution with parameters 𝜃. Recall that the likelihood of a dataset  is given by:

𝑃(;𝜃)=∏𝑖=1|𝜃|𝜃𝑐𝑖𝑖
 
where 𝑐𝑖 is the occurrence count of the 𝑖-th event.

The MLE of 𝜃 is the setting of 𝜃 that maximizes 𝑃(;𝜃). In lecture we derived this to be

𝜃∗𝑖=𝑐𝑖∑|𝜃∗|𝑗=1𝑐𝑗



## Unigram Model

Consider the sequence:

A B A B B C A B A A B C A C
A unigram model considers just one character at a time and calculates  𝑝(𝑤)  for  𝑤∈{𝐴,𝐵,𝐶} .

What is the MLE estimate of  𝜃 ? Give your result to three decimal places.



Answer = 𝜃∗𝐴 0.429

Answer = 𝜃∗𝐵 0.357

Answer = 𝜃∗c 0.214


Using the MLE estimate of  𝜃  on   , which of the following sequences is most likely?


Answer = ABB


## Bigram Model 1

A bigram model computes the probability  𝑝(;𝜃)  as:

𝑝(;𝜃)=𝑝(𝑤0)∏𝑤1,𝑤2∈𝑝(𝑤2|𝑤1) 
 
where  𝑤0  is the first word, and  (𝑤1,𝑤2)  is a pair of consecutive words in the document.

This is also a multinomial model. Assume the vocab size is  𝑁 . How many parameters are there?


Answer = N^2-1


## Bigram Model 2

Which of the following represents the MLE for the conditional probability  𝑝(𝑤2∣𝑤1) ?


Answer = count(𝑤1,𝑤2)∑𝑤1,𝑤′2∈count(𝑤1,𝑤′2)

## Bigram Model 3


Consider the same sequence from the unigram model:

A B A B B C A B A A B C A C
If you estimate  𝜃  on this, what probability will be assigned to the following test sequence? Assume the starting probabilities of all characters  𝑝(𝑤∣null)  is uniform. Give your answer to three decimal places.

A A B C B A B


Answer = 0














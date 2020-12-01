# Estimating Inputs for RL algorithm

## Estimating Transition Probabilities and Rewards


What might be some issue(s) with trying to estimate  𝑇̂ ,𝑅̂   in the following manner?

 	 𝑇̂  	 = 	 count(𝑠,𝑎,𝑠′)∑𝑠′count(𝑠,𝑎,𝑠′) 	 	 
 	 𝑅̂  	 = 	 ∑𝑡=1count(𝑠,𝑎,𝑠′)𝑅𝑡(𝑠,𝑎,𝑠′)count(𝑠,𝑎,𝑠′) 	 	 
Select one or more options from below that are correct:



Answer = Certain states might not be visited at all while collecting the statistics for  𝑇̂ ,𝑅̂ 

Answer = Certain states might be visited much less often than others leading to very noisy estimates of  𝑇̂ ,𝑅̂ 


## Model Free vs Model Based Approaches


Say we want to estimate the expectation of a function  𝑓(𝑥) .

𝔼[𝑓(𝑥)]=∑𝑥𝑝(𝑥)⋅𝑓(𝑥) 
 
We have access  𝐾  samples in order to compute our estimation. Select one or more statement(s) from the options below that are correct about model free or model based approaches



Answer = Model Based Approach first tries to estimates the probability distribution before estimating the expectation 

Answer = Model Free Approach estimate would be given by  ∑𝐾𝑖=1𝑓(𝑋𝑖)𝐾  







# Utility Function



## Finite Horizon vs Discounted Reward


The main problem for MDPs is to optimize the agent's behavior. To do so, we first need to specify the criterion that we are trying to maximize in terms of accumulated rewards. We will define a utility function and maximize its expectation.

We consider two different types of utility functions:

Finite horizon based utility : The utility function is the sum of rewards after acting for a fixed number  𝑛  steps. For example, in the case when the rewards depend only on the states, the utility function is

𝑈[𝑠0,𝑠1,…,𝑠𝑛]=∑𝑖=0𝑛𝑅(𝑠𝑖)for some fixed number of steps𝑛. 
 
In particular  𝑈[𝑠0,𝑠1,…,𝑠𝑛+𝑚]=𝑈[𝑠0,𝑠1,…,𝑠𝑛]  for any positive integer  𝑚 .

(Infinite horizon) discounted reward based utility : In this setting, the reward one step into the future is discounted by a factor  𝛾 , the reward two steps ahead by  𝛾2 , and so on. The goal is to continue acting (without an end) while maximizing the expected discounted reward. The discounting allows us to focus on near term rewards, and control this focus by changing  𝛾 . For example, if the rewards depend only on the states, the utility function is

𝑈[𝑠0,𝑠1,…]=∑𝑘=0∞𝛾𝑘𝑅(𝑠𝑘). 
 
How do these two types of utility function depend on the time steps?
(Choose all that apply.)


Answer = The action at state  𝑠  that maximizes a finite horizon based utility can depend on how many steps have been taken.


Answer = The action at state  𝑠  that maximizes a discount reward based utility does not depend on how many steps have been taken.


## Discounted Reward

Recall that the discounted reward in the case when  𝑅(𝑠,𝑎,𝑠′)=𝑅(𝑠)  is given by:

𝑅(𝑠0)+𝛾𝑅(𝑠1)+𝛾2𝑅(𝑠2)…=𝑅(𝑠0)+∑𝑡=1∞𝛾𝑡𝑅(𝑠𝑡)where 0≤𝛾<1. 
 
Which of the following is true about discounted reward?
(Choose all that apply.)


Answer = For  𝛾=0 , maximizing for discounted reward boils down to greedily maximizing for the immediate reward.

Answer = Discounted reward is guaranteed to be finite when the maximum reward is finite.







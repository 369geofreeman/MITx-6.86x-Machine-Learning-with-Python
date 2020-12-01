#  Q value iteration by sampling


Let us consider a toy example which might not be very realistic but which neverthless can help delineate the Q-value iteration for RL using sampling approach.

For this example, assume that there are only two states,  𝑠1,𝑠2  and only one action possible from each of these states. Let  𝑎𝑠1 ,  𝑎𝑠2  be the actions that could be taken from  𝑠1  and  𝑠2  respectively.


The state transition probabilities are listed below and are also shown in the figure above.

 	 𝑇(𝑠1,𝑎𝑠1,𝑠1)=0.1 	 	 
 	 𝑇(𝑠1,𝑎𝑠1,𝑠2)=0.9 	 	 
 	 𝑇(𝑠2,𝑎𝑠2,𝑠2)=0.1 	 	 
 	 𝑇(𝑠2,𝑎𝑠2,𝑠1)=0.9 	 	 
The rewards for these actions are given by

 	 𝑅(𝑠1,𝑎𝑠1,𝑠1)=1 	 	 
 	 𝑅(𝑠1,𝑎𝑠1,𝑠2)=−1 	 	 
 	 𝑅(𝑠2,𝑎𝑠2,𝑠2)=−1 	 	 
 	 𝑅(𝑠2,𝑎𝑠2,𝑠1)=1 	 	 
Note that we resort to finding optimal  𝑄∗  function by sampling for tasks where we don't have access to the exact  𝑇,𝑅  functions. However, for this toy example we will assume that the Q-value iteration algorithm isn't directly provided with the above specified values of  𝑇,𝑅  and has to resort to sampling to estimate the  𝑄  function.

Let's say that the agent starts out from state  𝑠1  and collects few samples. Each sample can be described by the following tuple  (𝑠,𝑎,𝑠′,𝑅(𝑠,𝑎,𝑠′))  which indicates that the agent received a reward of  𝑅(𝑠,𝑎,𝑠′)  when it reached state  𝑠′  by taking action  𝑎  from the state  𝑠 .

The collected samples are described as follows in the order in which they are presented to the Q-value iteration algorithm.

 	 (𝑠1,𝑎𝑠1,𝑠1,+1) 	 	 
 	 (𝑠1,𝑎𝑠1,𝑠2,−1) 	 	 
 	 (𝑠2,𝑎𝑠2,𝑠1,+1) 	 	 
Let  𝑆𝑄(𝑠,𝑎)𝑘  be used to denote the  𝑘𝑡ℎ  sample of  𝑄(𝑠,𝑎)  ( 𝑘=𝑖+1 ). Then recall that

𝑄̂ 𝑖+1(𝑠,𝑎)=𝛼𝑆𝑄(𝑠,𝑎)𝑘+(1−𝛼)∗𝑄̂ 𝑖(𝑠,𝑎) 
 
For all of the following problems, assume that the discount factor  𝛾=0.5 ,  𝛼=0.75  and that all the  𝑄  values are initialized to  0  to start with. That is,

𝑄̂ 0(𝑠,𝑎)=0 for all 𝑠,𝑎


## Numerical Example

Answer = Enter below the value of  𝑄(𝑠1,𝑎𝑠1)  after the first sample is processed by the Q-value iteration algorithm








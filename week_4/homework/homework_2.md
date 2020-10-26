#  LSTM


The diagram below shows a single LSTM unit that consists of Input, Output, and Forget gates.


The behavior of such a unit as a recurrent neural network is specified by a set of update equations. These equations define how the gates, “memory cell"  𝑐𝑡  and the “visible state"  ℎ𝑡  are updated in response to input  𝑥𝑡  and previous states  𝑐𝑡−1 ,  ℎ𝑡−1 . For the LSTM unit,

 	 𝑓𝑡 	 =sigmoid(𝑊𝑓,ℎℎ𝑡−1+𝑊𝑓,𝑥𝑥𝑡+𝑏𝑓) 	 	 
 	 𝑖𝑡 	 =sigmoid(𝑊𝑖,ℎℎ𝑡−1+𝑊𝑖,𝑥𝑥𝑡+𝑏𝑖) 	 	 
 	 𝑜𝑡 	 =sigmoid(𝑊𝑜,ℎℎ𝑡−1+𝑊𝑜,𝑥𝑥𝑡+𝑏𝑜) 	 	 
 	 𝑐𝑡 	 =𝑓𝑡⊙𝑐𝑡−1+𝑖𝑡⊙tanh(𝑊𝑐,ℎℎ𝑡−1+𝑊𝑐,𝑥𝑥𝑡+𝑏𝑐) 	 	 
 	 ℎ𝑡 	 =𝑜𝑡⊙tanh(𝑐𝑡) 	 	 
where symbol  ⊙  stands for element-wise multiplication. The adjustable parameters in this unit are matrices  𝑊𝑓,ℎ ,  𝑊𝑓,𝑥 ,  𝑊𝑖,ℎ ,  𝑊𝑖,𝑥 ,  𝑊𝑜,ℎ ,  𝑊𝑜,𝑥 ,  𝑊𝑐,ℎ ,  𝑊𝑐,𝑥 , as well as the offset parameter vectors  𝑏𝑓 ,  𝑏𝑖 ,  𝑏𝑜 , and  𝑏𝑐 . By changing these parameters, we change how the unit evolves as a function of inputs  𝑥𝑡 .

To keep things simple, in this problem we assume that  𝑥𝑡 ,  𝑐𝑡 , and  ℎ𝑡  are all scalars. Concretely, suppose that the parameters are given by

 	 𝑊𝑓,ℎ 	 =0 	 𝑊𝑓,𝑥 	 =0 	 𝑏𝑓 	 =−100 	 𝑊𝑐,ℎ 	 =−100 	 	 
 	 𝑊𝑖,ℎ 	 =0 	 𝑊𝑖,𝑥 	 =100 	 𝑏𝑖 	 =100 	 𝑊𝑐,𝑥 	 =50 	 	 
 	 𝑊𝑜,ℎ 	 =0 	 𝑊𝑜,𝑥 	 =100 	 𝑏𝑜 	 =0, 	 𝑏𝑐 	 =0 	 	 
We run this unit with initial conditions  ℎ−1=0  and  𝑐−1=0 , and in response to the following input sequence: [0, 0, 1, 1, 1, 0] (For example,  𝑥0=0 ,  𝑥1=0 ,  𝑥2=1 , and so on).


### LSTM states


Calculate the values  ℎ𝑡  at each time-step and enter them below as an array  [ℎ0,ℎ1,ℎ2,ℎ3,ℎ4,ℎ5] .

(Please round  ℎ𝑡  to the closest integer in every time-step. If  ℎ𝑡=±0.5 , then round it to  0 .
For ease of calculation, assume that  sigmoid(𝑥)≈1  and  tanh(𝑥)≈1  for  𝑥≥1 , and  sigmoid(𝑥)≈0  and  tanh(𝑥)≈−1  for  𝑥≤−1 .)


Answer = [0, 0, 1, -1, 1, -0]

### LSTM states 2


Now, we run the same model again with the same parameters and same initial conditions as in the previous question. The only difference is that our input sequence in now: [1, 1, 0, 1, 1].

Calculate the values  ℎ𝑡  at each time-step and enter them below as an array  [ℎ0,ℎ1,ℎ2,ℎ3,ℎ4] .

(Please round  ℎ𝑡  to the closest integer in every time-step. If  ℎ𝑡=±0.5 , then round it to  0 .
For ease of calculation, assume that  sigmoid(𝑥)≈1  and  tanh(𝑥)≈1  for  𝑥≥1 , and  sigmoid(𝑥)≈0  and  tanh(𝑥)≈−1  for  𝑥≤−1 .)


Answer = [1,-1,0,1,-1]

### LSTM info

What information is carried in the state  ℎ𝑡 ?


Answer = Whether the number of consecutive ones is odd.






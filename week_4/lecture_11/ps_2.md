# problem set 2

## Markov Models to Feedforward Neural Nets


### Markov Transitions

Suppose we represent a Markov model as a feedforward neural network, as described in the lecture. Given a word, let the probability that word j occurs next be  𝑝𝑗 . Which of the condition(s) below must hold true? Let  𝐾  be the set of words. (Choose all that apply.)


 Answer =  ∑𝑘∈𝐾𝑝𝑘=1

Answer = 𝑝𝑘  is greater than or equal to zero for all 𝑘∈𝐾 


How do we satisfy the conditions you marked above? (Choose all that apply.)


Answer = take the softmax activation of the outputs



### Markov As Feedforward

When representing a first-order Markov model as a feedforward network, what is the number of non-zero values in a single input vector?

Answer = 1



### Markov vs Feedforward


What are some advantages of the feedforward NN as described in the lecture versus Markov models? (Choose all that apply.)

Answer = They contain a fewer number of parameters

Answer = We can easily control the complexity of feedforward NN by introducing hidden layers

Suppose you have a word vocabulary of size 10 (including <beg> and <end>), and you were using a trigram language model to predict the next word.

How many parameters would you need for a Markov Model?

Answer = 1000


How many parameters would you need for a feedforward neural network that contained biases and no hidden units?

Answer = 210

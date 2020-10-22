# Problem set one

## Markov Models


### Markov Symbols


To specify a Markov language model, what additional symbols do we need to add to our set of possible symbols?
(Choose all that apply.)

Answer = A start symbol
Answer = An end symbol
Answer = A symbol for unknown words


### Transition Probabilities

Using a first order Markov model specified above, what is the probability of generating the following sentence <beg> ML course UNK <end>?


Answer = 0.007


Which of the following sentences are probable to generate?

Answer = <beg> ML course <end>



### Maximum Likelihood

Suppose our training examples are the following three sentences.

ML courses are cool.

Humanities courses are cool.

But some courses are boring.

Using a bigram model, what is the maximum likelihood estimate for the probability that the next word is 'cool', given that the previous word is 'are'?


Answer = 2/3

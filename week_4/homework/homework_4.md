# Word Embeddings


Training a neural network using back-propagation and SGD moves the network weights in a direction that minimizes the loss function. If the network contains a bottleneck, a layer in which many inputs are reduced to only a few outputs, training will adjust the weights to maximize the useful information contained in the layer's output. In this way, a sparse input representation can be embedded in a lower-dimensional space to become a dense, distributed representation. Embeddings often have interesting properties like transforming semantic or visual similarity into geometric proximity.

For example, imagine you have the words "cat", "lion", "car", "bridge". You could have a possible dense representation like: "cat" : [0.9, 0.2], "lion" : [0.9, 0.5], "car" : [0.01, 0.8], "bridge" : [0.01, 1.0]. In this representation, the first component give (not exactly) a measure of "animalness" and the second, size. In addition, the vectors for similar or related words may be close together in space. In this question, we will examine the utility of (the highly popular) word embeddings.

Consider two neural networks for classifying sequences of words that differ only in their input representation:

The first of which uses a sparse one-hot encoding of each word in which word  𝑖  is identified by a vector that contains a  1  in position  𝑖  and  0 s elsewhere. For instance, a dictionary containing the words word and embedding might be represented as  [0 1]  and  [1 0] , respectively. You may assume that the dictionary used contains all words in both the training and testing sets.

The second neural network, instead, uses a pre-trained embedding of the dictionary that you may assume represents every word in the dictionary.

Assuming that both networks use  tanh  activations and have randomly initialized weights, and they are trained using the same training set, but different input representation.

Now, at test time, each network is presented with a sequence of words not seen during training. Which of the following statement(s) is/are true about the output of the network for this sequence?




Answer = The first network cannot classify the sequence correctly

Answer = The second network has a fighting chance at classifying the sequence

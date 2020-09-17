# Lecture 2: Linear Classifiers and Perceptron Algorithm

**At the end of this lecture, you will be able to**

* Understand the concepts of Feature vectors and labels, Training set and Test set, Classifier, Training error, Test error, and the Set of classifiers

* Derive the mathematical presentation of linear classifiers

* Understand the intuitive and formal definition of linear separation

* Use the perceptron algorithm with and without offseti


## Review of basic concepts

Lets start this lecture by briefly revising concepts from teh previous lecture


### Feature Vector: 𝒳

Foe each and every case that we had, we had some propertie staht were inherent to the case. Like for eg. Every movie that we had earlier had a genre, Imdb rating, budget, cast etc.

We, for our purpose, wanted to redict something on the basis iof these features. Hence for each case we chose 'd' features taht we were characteristic of that case and stacked them in a vector with each entry being a number (because taht's what machines understand).

This vector for the ith movie/case was called the feature vector:
```

	𝒳⁽ⁱ⁾ = | 𝒳₁⁽ⁱ⁾ |	∈ ℝᵈ (Generally)
	       | 𝒳₂⁽ⁱ⁾ |
	       |   ┇   |
 	       | 𝒳𝑑⁽ⁱ⁾ | dx1

	𝒳ｊ⁽ⁱ⁾ : jth feature of the ith case
``` 


### Label : 𝕐⁽ⁱ⁾

This was the thing that we wanted to predict

we are talking about supervised learning here, which means we will have labelled data. (At least training data will be labelled)

To each case from the traning data we will have a label associated and for each case in the test data we want to predict the label.

For the movie example we are studying each vector which could have one of two labels.
```
		/ : Indicating viewer would watch ith movie
	𝕐⁽ⁱ⁾ = 
		\ : Indicating viewer would not watch ith movie
```


### Traning Set : Sn

Its the set of examples we feed our algorithm in order to train it. Again we are doing supervised learning which means teh traning data that we have will be labelled and we will have n examples to feed. Therefore mathmatically we write:
```
	Sn = {(𝒳⁽ⁱ⁾, 𝕐⁽ⁱ⁾), i = 1,2,3.....n}
```
Ie, set all pairs (feature vector i, label i) for all n cases

### Classifier : h()

It is simply a function or mapping from 𝒳 : ie, the space of feature vectors to the space of labels. For the movie example we had
```
	h : ℝ² --> {-1, +1} 
```

The idea was simple

We will habe a function h() that will take as input any feature vector 𝒳 and give us out a corrisponding label of +1 or -1. In order to do that we will first need to train the model. This function h() we have will infact depend on parameter 𝜣 (which can be multi-dimentional), and using the traning data, we will estimate 𝜣's to fins an optimal h().

Then we will predict lables using this optimal h().


### Traning Error En(h)

In order to see how our classifier performed with the traning data, we needed some sort of metric. The idea we had was pretty simple : Just look at what fraction of points in the traning set are misclassified by h()

So we introduced the double bracket notation:
```
	[[ Expression ]] = 1 if Expression is True
			   2 if Expression is False
```

If for the ith case in traning data
```
	h(𝒳⁽ⁱ⁾) ≠ 𝕐⁽ⁱ⁾ : Then h commited an error
	h(𝒳⁽ⁱ⁾) = 𝕐⁽ⁱ⁾ : Then h did not commit an error
```

So in order to find the fraction of the error commited we have
```
		    n
	En(h) = 1/n ∑ [[h(𝒳⁽ⁱ⁾) ≠ 𝕐⁽ⁱ⁾]]
		   i=1
```

### Test Error and test Set

Now we know what the Test Set is. it is the set of examples of cases for which we want to predict the labels. the feature vectors are as discussed earlier only a property / characteristic of the examples / cases alone. it does not matter whether the example is from the traning set or the test set, the example will always have a feature vector.

The label is the tricky part

Up untill now, we have assumed that the test data we have is unlablled. This may or may not be true.

Usually what we do while traning models is something like this:
	* We have a lot of **LABELLED** data
	* We split it into two parts **RANDOMLY**
Usually:
	* 80% is the testing data
	* 20% is the traning data

	* With the 20% traning data we train the model
	* Then we check how our trained model preforms on the test data

Here we have two things for a case in the **TEST SET** 
```
For 𝒳⁽ⁱ⁾ in the TEST SET

	The predicted label : h(𝒳⁽ⁱ⁾)
	The truth	    : 𝕐⁽ⁱ⁾ 
```

	* We can then compare these two values to finnd an error, Similar to our traning error
```
		        m
Test Error :En(h) = 1/m ∑ [[h(𝒳⁽ⁱ⁾) ≠ 𝕐⁽ⁱ⁾]]
		       i=1

	𝒳⁽ʲ⁾ : jth feature vector in TEST SET
	m    : Total cases in TEST SET
	𝕐⁽ʲ⁾ : Label of the jth case in TEST SET 

```

Now note that this will only be the possible to calculate when we have actual labels for the cases in the **Test DATA SET**, which may not  always be the case.



### Set of Calssifiers : 𝑯 

This was the set of choices we had for our function h(). Ie, h ∈ 𝑯 

We saw that the more choices we allowed for h(), the less generalised the model become. Ie, although we got perfect classifiers for the traning set with En(h) = 0; they failed miserably when applied to the test data

Lets also revise the geometric picture we had in mind while doing all this


### Geometric Picture

In order to anaalyse what happened geoetrically, we took
```
	n = 4  (examples in the traning set)
	𝒳 ∈ ℝ² (The feature vector was 2 dimensional)
	𝕐⁽ʲ⁾ ∈ {+1 or -1}
```

<img src="img/img1.png" alt="future events  img" width="600"/>

<img src="img/img2.png" alt="future events  img" width="600"/>

<img src="img/img3.png" alt="future events  img" width="600"/>


### Linear Classifiers

Althought we have talked a lot about how we plan to classify or predict teh labels, we haven't yet proposed any mathmatical form for the function h(), that is our classifier. In our lecture now, we plan to do exactly that, and we will start with the simplest family called the **Linear Classifier**. But in order to clearly understand them, we will need a mathmatical concept called hyperplane, so....


## HYPERPLANE


### Lets begin with a simple case

```
	----------()--------------->
		 𝒳₀               𝒳₁ axis
```

We have a straight line above called a 𝒳₁ axis. And we have some point at 𝒳₀

what is the equasion of this point?

Thats a rather silly question but if we had to answer it, the answer would be 
```
	𝒳₁ = 𝒳₀
```
Now note what this point is doing. It's dividing the 𝒳₁ axis or line into two regions.
	* Region 1: To the right of 𝒳₀
	* Region 2: To the left of 𝒳₀
```
x : Points to the right of 𝒳₀
o : Points to the left of 𝒳₀

	--o--oo----o----o-()---x--xxx-xx--x-x-->
			  𝒳₀                 𝒳₁ axis
```

Good, now lets move on to the next case


### Lets complicate this a little 


Now we have two axis 𝒳₁ and 𝒳₂. ie, we have a second plane. We also have a line thats passes through this plane

We again ask the question, what is the equasion of this line.

<img src="img/img4.png" alt="future events  img" width="600"/>

We already know the equasion of a line looks like 
```
	𝒳₂ = m𝒳₁ + c

Where m is the slope and c is the intercept
```

We can write this as 
```
	𝒳₂ + m𝒳₁ -c = 0
```


But we again note a pattern here.  The Blue line divides the 2nd plane into two regions

	* Region 1 : Above the line
	* Region 2 : Below the line


<img src="img/img4.png" alt="future events  img" width="600"/>


<img src="img/img5.png" alt="future events  img" width="600"/>

	* x : Points above the line
	* o : Points below the line

Note that there will also be points exactly on the line


Good now lets us move on to the next case


### Let's complicate this a little more


Now we have 3 axis here, 𝒳₁, 𝒳₂ and 𝒳₃. This is what we call a 3rd plane. We also have a plane (in blue) And we again can ask the question what is the equasion of this plane.

<img src="img/img6.png" alt="future events  img" width="600"/>

The equasion of the plane is of form
```
	a𝒳₂ + b𝒳₂ + c𝒳₃ = d
```

And we can again see the pattern continued here

The plane divides the 3rd region into two parts

	* Region 1 : Above the plane points
	* Region 2 : Below the plane points

<img src="img/img7.png" alt="future events  img" width="600"/>


	x : Points above the plane
	0 : Points below the plane

Note that there will also be points that tie exactly on the plane and will satify the planes equasion



### So Now we cant go visually further







































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


## HYPERPLANE  (Then back to the lecture)


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
	a𝒳₁ + b𝒳₂ + c𝒳₃ = d
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


Because there's no way we can draw a 4d plot, But we can mathmatically translate this idea forward. before doinf that lets look at the similarites we had for our 3 examples above

Equation of:
	* Point in one dimension:    𝒳₁ - 𝒳₂ = 0 
	* Line in two dimensions:    𝒳₂ - m𝒳₁ - c = 0
	* Plane in three dimensions: a𝒳₃ + b𝒳₂ + c𝒳₁ - d = 0

So we can say if we have a dimensional sopace in general, the equasion we are looking for is off the form
```
	𝜣₁𝒳₁ + 𝜣₂𝒳₂ + 𝜣₃𝒳₃ + ........ + 𝜣ⅾ𝒳ⅾ + 𝜣ｏ = 0
``` 

Also note the following:

	in 1 dimension : dimension of point is 0
	in 2 dimension : dimension of point is 1
	in 3 dimension : dimension of point is 2

So if we are in a d dimensional space we will have the above equation as a 'd-1' dimensional thing / obgect

**Now a finall thing to note ie**

No matter which dimension d, we choose, teh equasion we wrote before divides the d dimensional space into **TWO** seperate regions and there are also points taht lie on the object that satisfy the equasion we wrote earlier. Ie, 𝜣₁𝒳₁ + 𝜣₂𝒳₂ + 𝜣₃𝒳₃ + ........ + 𝜣ⅾ𝒳ⅾ + 𝜣ｏ = 0

We are now ready to understand the concept of:


### Hyperplane


* A hyperplane in n dimensions is a n-1 dimensional subspace.
* A hyperplane seperates the space into two sides
* The equasion of a hyperplabe is:
```
	𝜣ｏ+ 𝜣₁𝒳₁ + 𝜣₂𝒳₂ + 𝜣₃𝒳₃ + ........ + 𝜣n𝒳n = 0
```

𝜣ｏ: is called the offset term

Linear algebra  provides us a great way to write the equation:
```
If we take

	    |𝜣₁ |	   |𝒳₁ |
	𝜣 = |𝜣₂ |  And 𝒳 = |𝒳₂ |
	    | ┊ |          | ┊ |
	    |𝜣∩ |nx1       |𝒳∩ |nx1
```

Then we use the dot product (𝜣ᵀx or 𝜣﹒x) to write the eqation of the hyperplane as
```
	𝜣ｏ+ 𝜣﹒x = 0
```


Now in light of this new formulation, lets look at our old examples

	* Point in one dimension:    𝒳₁ - 𝒳₂ = 0 ; 𝜣₁𝒳₁ + 𝜣ｏ= 0  ⟹  𝜣₁ = 1. 𝜣ｏ= -𝒳₀
	* Line in two dimensions:    𝒳₂ - m𝒳₁ - c = 0  ; 𝜣₂𝒳₂ + 𝜣₁𝒳₁ + 𝜣ｏ = 0 ⟹  𝜣₁ = -m, 𝜣ｏ= -c
	* Plane in three dimensions: a𝒳₃ + b𝒳₂ + c𝒳₁ - d = 0 ; 𝜣₃𝒳₃ + 𝜣₂𝒳₂ + 𝜣₁𝒳₁ + 𝜣ｏ= 0
					ie, 𝜣₁ = c, 𝜣₂ = b, 𝜣₃ = a. 𝜣ｏ= -d


Now one more thing before we end this topic


Lets first see the case of line in 2d 


The eqation of line is 𝜣₁𝒳₁ + 𝜣₂𝒳 + 𝜣₂ = 0


<img src="img/img8.png" alt="future events  img" width="600"/>


<img src="img/img9.png" alt="future events  img" width="600"/> 


Which menas any vector thats along the direction of AB is pependicular 𝜣 vector.

Similary for the case of plane in 3d we have

<img src="img/img10.png" alt="future events  img" width="600"/>

Therefore we can conclude for a hyperplane in n dimensions with equation
```
	𝜣ｏ+ 𝜣₁𝒳₁ + 𝜣₂𝒳₂ + ..... +  𝜣n𝒳n = 0

Or

	𝜣ｏ+ 𝜣﹒x = 0
```

The vector 𝜣 will be orthagonal to any vector that lies on this hyperplane, ie lives in the subspace defined by the hyperplane



Now back to the lecture



## Linear Classifiers

Ok now we are ready to study our first linear classifier mathmmatically. And the problem we had in  mind is the movie recommender, where a movie from a test data set will be assigned either a +1 or -1 label.

We already know what a classifier does for our problem. It divides the space where 𝒳 ∈ ℝᵈ live into two regions. (For our example we had the blue region and the white region)

But the study of hyperplanes earlier, revealed that it too does the same thing. A hyperplane in n dimensionsis a n-1 dimensional subspace that divides the n dimensional space into two regions.

So as our first classifier, why don't we use the help of a hyperplane in order to find our classifier h()?

And we will indeed do exactly that. We will now tackle the movie recommender problem, using hyperplane's help in forming a classifier.

Now note that a hyperplane is actually just a line, when we are in 2 dimensional space. We decided earlier to keep things simple, that the feature vector for the ith movie 𝒳⁽ⁱ⁾ will have two features ie, 𝒳⁽ⁱ⁾ ∈ℝ² so our hyperplane will be a line in our example.

However the mathmatical formulation that we will use or derive will be applicable for any problem of two-class classification, with a general feature vector 𝒳⁽ⁱ⁾ ∈ ℝᵈ

We may not be able to visualise it when d > 3 but the mathematical ideas will remain the same




## The idea

we have 𝒳⁽ⁱ⁾ ∈ ℝ². Ie, the feature vectors are 2 dimensional. So we need to divide the ℝ² plane in 2 regions, using a line


<img src="img/img11.png" alt="future events  img" width="600"/>

Now the general equation of a line is 
```
	𝜣₁𝒳₁ + 𝜣₂𝒳₂ + 𝜣₀ = 0
```

This line here is called the **DECISION BOUNDRY**. A common machine learning term.

In general d dimensions of the hyperplane will be called the decision boundry.

Ok, now in order to carry our analysis forward, we will first simplify the math a bit. We will let the desision boundry pass through the origin.


 <img src="img/img12.png" alt="future events  img" width="600"/>

We will later see the general case but first lets see this one

If that is the case then point (0,0) should satisfy the equation. 
```
	Ie, 𝜣₁﹒0 + 𝜣₂﹒0 + 𝜣₀ = 0

	⟹  𝜣₀ = 0
```
So the odffset term 𝜣₀ is 0

The equation of the line becomes
```
	𝜣₁𝒳₁ + 𝜣₂𝒳₂ = 0
```

Decission boundry passing through the origin


###  Now lets move a step further

Now we want to look at the vector 𝜣. As we know that vector 𝜣 is orthagonal to the hyperplane (line in this case).
The real direction of 𝜣 will become clear when we actually know the numerical values of its components. But for nowwe have two choices, we can either choose option A or option B. We choose option A (either A or B it doesn't matter).

<img src="img/img13.png" alt="future events  img" width="500"/>

But note that these two directions are the only choices we have as these are the only directions orthagonal to the lline.

<img src="img/img14.png" alt="future events  img" width="700"/>


**Img 1**

Here we see two vectors that lie on region. By definition of the dot product

	0﹒x = ||0|| ||x|| cos(< bw the two)
	0﹒x = ||0|| ||x⁽¹⁾|| cos 1
	0﹒x = ||0|| ||x⁽²⁾|| cos 2

As long as the vector x lies in region. The angle between will be between 0 to ∏/2 therefore
```
	𝜣﹒x > 0 for all x in region 1
```

<hr/>

**Img 2**

Here we see two vectors that lie on region 1. By definition of the dot product

	0﹒x = ||0|| ||x|| cos(< bw the two)
	0﹒x⁽³⁾ = ||0|| ||x⁽³⁾|| cos 3
	0﹒x⁽⁴⁾ = ||0|| ||x⁽⁴⁾|| cos 4

As long as the vector  x lies in region 2. The angle between will be between ∏/2 to ∏ therefore
```
	𝜣﹒x < 0 for all x in region 2
```


So now we have a new insight

We had the decission boundry 𝜣﹒x = 0 passing through origin and we know that it derives the space into two regions.















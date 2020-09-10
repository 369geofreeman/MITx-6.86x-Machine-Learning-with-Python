# Homework part 3


A list of  𝑛  numbers can be thought of as a point or a vector in  𝑛 -dimensional space. In this course, we will think of  𝑛 -dimensional vectors 
```
	 				   ⎡𝑎1⎤
 we will think of  𝑛 -dimensional vectors  |𝑎2|  flexibly as points and as vectors.
	 				   | ⋮|
	 				   ⎣𝑎𝑛⎦ 
```

<hr />

## Dot Products and Norm

Notation: In this course, we will use regular letters as symbols for numbers, vectors, matrices, planes, hyperplanes, etc. You will need to distinguish what a letter represents from the context.

Recall the dot product of a pair of vectors  𝑎  and  𝑏 :
```
					⎡𝑎1⎤         ⎡b1⎤
 𝑎⋅𝑏 = 𝑎1𝑏1 + 𝑎2𝑏2 + ⋯ + 𝑎𝑛𝑏𝑛 where 𝑎 = |𝑎2| and b = |b2|
					| ⋮|         | ⋮|
					⎣𝑎𝑛⎦         ⎣b𝑛⎦
```

When thinking about  𝑎  and  𝑏  as vectors in  𝑛 -dimensional space, we can also express the dot product as:
```
		𝑎⋅𝑏 = ‖𝑎‖‖𝑏‖cos𝛼,
```
where  𝛼  is the angle formed between the vectors  𝑎  and  𝑏  in  𝑛 -dimensional Euclidean space. Here,  ‖𝑎‖  refers to the length, also known as norm, of  𝑎 :
```
		‖𝑎‖ = √a2/1 + a2/2 + ... + a2/n
```

# 1)
 
```
				  ⎡0.4⎤
What is the length of the vector: ⎣0.3⎦ L = 0.5
```
```
				  ⎡-0.15⎤
What is the length of the vector: ⎣ 0.2 ⎦ L = 0.25
```

```
				        ⎡0.4⎤     ⎡-0.15⎤
What is the angle (in radians) between  ⎣0.3⎦ and ⎣ 0.2 ⎦ ? Choose the answer that lies between 0 and 𝜋.

Angle = 1.5707963
```

# Dot Products and Orthogonality

# 2) 

```
				     ⎡𝑎1⎤         ⎡ 𝑎1 ⎤
Given  3 -dimensional vectors  𝑥(1)= |a2|  x(2) = |-a2 |  
				     ⎣𝑎3⎦	  ⎣ 𝑎3 ⎦ 

when is  𝑥(1)  orthogonal to  𝑥(2) , i.e. the angle between them is  𝜋/2 ?

Answer = when  𝑎21−𝑎22+𝑎23=0
```

# Unit Vectors

# 3)

A unit vector is a vector with length  1 . The length of a vector is also called its norm.

Given any vector  𝑥,  write down the unit vector pointing in the same direction as  𝑥 ?

(Enter x for the vector  𝑥 , and norm(x) for the norm  ‖𝑥‖  of the vector  𝑥 .)

Answer = x/norm(x)

# Projections

# 4)

Recall from linear algebra the definition of the projection of one vector onto another. As before, we have  3 -dimensional vectors:
```
       ⎡𝑎1⎤         ⎡ 𝑎1 ⎤
x(1) = |a2|  x(2) = |-a2 |  
       ⎣𝑎3⎦	    ⎣ 𝑎3 ⎦ 
```
Which of these vectors is in the same direction as the projection of  𝑥(1)  onto  𝑥(2) ?

Answer = x(2)

What is the signed magnitude  𝑐  of the projection  𝑝𝑥(1)→𝑥(2)  of  𝑥(1)  onto  𝑥(2) ? More precisely, let  𝑢  be the unit vector in the direction of the correct choice above, find a number  𝑐  such that  𝑝𝑥(1)→𝑥(2)=𝑐𝑢 .

(Enter a_1 for  𝑎1 , a_2 for  𝑎2 , and a_3 for  𝑎3 .)

𝑐 = (a_1^2-a_2^2+a_3^2)/sqrt(a_1^2+a_2^2+a_3^2)




























# Problem set 3



## Motivation for Kernels: Computational Efficiency


### Kernels as Dot Products 1

Let us go through the computation in the video above. Assume we map  𝑥  and  𝑥′∈ℝ2  to feature vectors  𝜙(𝑥)  and  𝜙(𝑥′)  given by

 	 𝜙(𝑥) 	 =[𝑥1,𝑥2,𝑥12,2‾√𝑥1𝑥2,𝑥22] 	 	 
 	 𝜙(𝑥′) 	 =[𝑥′1,𝑥′2,𝑥′12,2‾√𝑥′1𝑥′2,𝑥′22]. 	 	 
Which of the following equals the dot product  𝜙(𝑥)⋅𝜙(𝑥′) ?

Answer = 𝑥⋅𝑥′+(𝑥⋅𝑥′)2


### Kernels as Dot Products 2

Which of the following feature vectors 𝜙(𝑥) produces the kernel

𝐾(𝑥,𝑥′)=𝜙(𝑥)⋅𝜙(𝑥′)=𝑥1𝑥′1+𝑥2𝑥′2+𝑥3𝑥′3+𝑥2𝑥′3+𝑥3𝑥′2


Answer = 𝜙(𝑥)=[𝑥1,𝑥2+𝑥3]

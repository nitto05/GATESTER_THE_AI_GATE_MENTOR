GATE O PEDIA

**COMPUTER SCIENCE &**

**INFORMATION TECHNOLOGY**

Published By:

**Physics Wallah**

ISBN: 978 - 93 - 94342 - 51 - 4

Mobile App: Physics Wallah (Available on Play Store)

Website: [http://www.pw.live](http://www.pw.live)

Email: support@pw.live

Rights

All rights will be reserved by Publisher. No part of this book may be used or reproduced in any manner
whatsoever without the written permission from author or publisher.

In the interest of student's community:

Circulation of soft copy of Book(s) in PDF or other equivalent format(s) through any social media channels,
emails, etc. or any other channels through mobiles, laptops or desktop is a criminal offence. Anybody
circulating, downloading, storing, soft copy of the book on his device(s) is in breach of Copyright Act. Further
Photocopying of this book or any of its material is also illegal. Do not download or forward in case you come
across any such soft copy material.

Disclaimer

A team of PW experts and faculties with an understanding of the subject has worked hard for the books.

While the author and publisher have used their best efforts in preparing these books. The content has been
checked for accuracy. As the book is intended for educational purposes, the author shall not be responsible for
any errors contained in the book.

The publication is designed to provide accurate and authoritative information with regard to the subject matter
covered.

This book and the individual contribution contained in it are protected under copyright by the publisher.

```
(This Module shall only be Used for Educational Purpose.)
```

## Design Against Static Load

- 1. Engineering Mathematics (EM) 1.1 – 1.
- 2. Discrete Mathematics 2.1 – 2.
- 3. Digital Logic 3.1 – 3.
- 4. Computer Organization & Architecture 4.1 – 4.
- 5. Programming & Data Structures 5.1 – 5.
- 6. Algorithms 6.1 – 6.
- 7. Theory of Computation 7.1 – 7.
- 8 Compiler Design 8.1 – 8.
- 9 Operating System 9.1 – 9.
- 10 Database Management Systems 10.1 – 10.
- 11 Computer Networks 11.1 – 11.
- 12 General Aptitude 12.1 – 12.

**EngineeringEngineering**

**MathematicsMathematics**

**Engineering**

**Mathematics**

```
Design Against Static Load
```

1. Basic Calculus ...................................................................................................................... 1.1 – 1.1 6
2. Linear Algebra ...................................................................................................................... 1 .1 7 – 1.2 8
3. Probability and Statistics ..................................................................................................... 1.2 9 – 1. 40

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Design Against Static Load
```

1

**BASIC CALCULUS**

**1.1. Introduction**

**1.1.1 Limits, Continuity and Differentiability**

(a) As x tends to a (x → a)  x is moving towards a

A value l is said to be limit of a function f(x) at x → a if f(x) → l as x → a.

It is mathematically defined as

𝑙𝑖𝑚𝑥→𝑎𝑓(𝑥)=𝑙=𝑥𝑙𝑖𝑚→𝑎−𝑓(𝑥)=𝑥𝑙𝑖𝑚→𝑎+𝑓(𝑥)

That is, Limit exist at any point, if LHL = RHL

A function f(x) is said to be continuous at x = a, if

(^) 𝑥𝑙𝑖𝑚→𝑎𝑓(𝑥)=𝑙=𝑓(𝑎)=𝑓(𝑥)|𝑥=𝑎
That is, for a function to be continuous at any point, RHL = LHL = Value of function at point x = a.
Note: • For 𝑙𝑖𝑚𝑥→𝑎 𝑓(𝑥) to exist, the function need not be continuous at x = a.

- But for f(x) to be continuous at x = a, 𝑙𝑖𝑚𝑥→𝑎𝑓(𝑥) should exist.
- Continuity from Left :lim ( ) ( )
  xa
  −f x f a
  →

```
=
```

- Continuity from Right : If lim ( ) ( )
  xa
  +f x f a
  →

```
=
```

Continuity in an Open Interval

A function ‘f ’ is said to be continuous in open interval (a, b), if it is continuous at each point of open interval.

Continuity in a Closed Interval

Let ‘f ’ be a function defined on the closed interval (a, b) then ‘f _’_ is said to be continuous on the closed interval [a, b], if
it is :

1. Continuous from the right at a and
2. Continuous from the left at b and
3. Continuous on the open interval (a, b).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 2
Engineering Mathematics**
Fig. 1.
(b) Concept of differentiability
A continuous function f(x) is said to be differentiable at x = a, if 𝑥𝑙𝑖𝑚→𝑎𝑓(𝑥𝑥)−−𝑓𝑎(𝑎) exists, that is, RHL and LHL exist at a point
under consideration in 𝑓 _′_ (𝑥).
𝑓 _′_ (𝑥)|𝑥=𝑎=𝑓 _′_ (𝑎)=𝑙𝑖𝑚𝑥→𝑎𝑓(𝑥𝑥)−−𝑓𝑎(𝑎)
𝑓 _′_ (𝑎)=𝑡𝑎𝑛𝜃, where 𝜃 is the angle made by the tangent to the curve at x=a with x – axis.
(c) Some Standard Derivatives
(i) (^) 𝑑𝑥𝑑(𝑥𝑛)=𝑛.𝑥𝑛−^1
(ii) (^) 𝑑𝑥𝑑(𝑠𝑖𝑛𝑥)=𝑐𝑜𝑠𝑥
(iii) (^) 𝑑𝑥𝑑(𝑐𝑜𝑠𝑥)=−𝑠𝑖𝑛𝑥
(iv) (^) 𝑑𝑥𝑑(𝑡𝑎𝑛𝑥)=𝑠𝑒𝑐^2 𝑥
(v) (^) 𝑑𝑥𝑑(𝑐𝑜𝑡𝑥)=−𝑐𝑜𝑠𝑒𝑐^2 𝑥
(vi) (^) 𝑑𝑥𝑑(𝑠𝑒𝑐𝑥)=𝑠𝑒𝑐𝑥.𝑡𝑎𝑛𝑥
(vii) (^) 𝑑𝑥𝑑(𝑐𝑜𝑠𝑒𝑐 𝑥)= – 𝑐𝑜𝑠𝑒𝑐 𝑥𝑐𝑜𝑡𝑥
(viii) (^) 𝑑𝑥𝑑(𝑠𝑖𝑛−^1 𝑥)=√ 1 −^1 𝑥 2 ;− 1 <𝑥< 1
(ix) (^) 𝑑𝑥𝑑(𝑐𝑜𝑠−^1 𝑥)=√ 1 −−^1 𝑥 2 ,− 1 <𝑥< 1
(x) (^) 𝑑𝑥𝑑(𝑡𝑎𝑛−^1 𝑥)= 1 +^1 𝑥 2

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 3
Engineering Mathematics**
(xi) (^) 𝑑𝑥𝑑(𝑐𝑜𝑡−^1 𝑥)= 1 −+^1 𝑥 2
(xii) (^) 𝑑𝑥𝑑(𝑠𝑒𝑐−^1 𝑥)=|𝑥|√^1 𝑥 (^2) − 1
(xiii) (^) 𝑑𝑥𝑑(𝑐𝑜𝑠𝑒𝑐−^1 𝑥)=|𝑥|√−𝑥^12 − 1 ; |x| > 1
(xiv) (^) 𝑑𝑥𝑑(𝑙𝑜𝑔𝑎𝑥)=𝑥𝑙𝑜𝑔^1 𝑒𝑎
(xv) (^) 𝑑𝑥𝑑(𝑙𝑜𝑔𝑒𝑥)=^1 𝑥
(xvi) (^) 𝑑𝑥𝑑(𝑎𝑥)=𝑎𝑥.𝑙𝑜𝑔𝑒𝑎
(xvii) (^) 𝑑𝑥𝑑(𝑒𝑥)=𝑒𝑥
(xviii) (^) 𝑑𝑥𝑑(|𝑥|)=|𝑥𝑥|, (𝑥≠ 0 )
(xix) (^) 𝑑𝑥𝑑(𝑥𝑥)=𝑥𝑥( 1 +𝑙𝑜𝑔𝑒𝑥)
(xx) (^) 𝑑𝑥𝑑(𝑠𝑖𝑛 _ℎ_ 𝑥)=𝑐𝑜𝑠 _ℎ_ 𝑥
(d) Product rule of differentiation
(i) (^) 𝑑𝑥𝑑(𝑓(𝑥).𝑔(𝑥))=𝑓(𝑥).𝑔 _′_ (𝑥)+𝑓 _′_ (𝑥).𝑔(𝑥)
(ii) 𝑑(𝑢𝑣𝑤)=𝑢𝑣𝑤 _′_ +𝑢𝑣 _′_ 𝑤+𝑢 _′_ 𝑣𝑤
(e) Quotient rule of differentiation
(^) 𝑑𝑥𝑑(𝑓𝑔((𝑥𝑥)))=𝑔(𝑥).𝑓 _′_ ((𝑥𝑔)(−𝑥𝑓))( 2 𝑥).𝑔 _′_ (𝑥),(𝑔(𝑥)≠ 0 )
(f) Logarithmic differentiation:
Taking log might help in differentiation of a function. For example if yv= u then we can take log both side and
differentiable to get
dy
dx
(g) Differentiation in parametric from :
If we write x and y in term of find variable ‘t’ that is x = f(t), y = (t), then
/
/
dy dy dt
dx dx dt
========

(h) Greatest Integer function / step function / integer part function
𝑓(𝑥)=[𝑥]=𝑛,∀ 𝑛≤𝑥<𝑛+ 1 where, 𝑛∈𝑍
𝑙𝑖𝑚𝑥→𝑎[𝑥]=∄ if a is an integer ( ∄ = do not exist)
L.H.L. = 𝑥𝑙𝑖𝑚→𝑎−[𝑥]=𝑎− 1
R.H.L. = 𝑥𝑙𝑖𝑚→𝑎+[𝑥]=𝑎

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 4
Engineering Mathematics**
Fig.1. 2. Greatest Integer
(i) Properties of Limits
(i) 𝑙𝑖𝑚𝑥→𝑎(𝑓(𝑥)±𝑔(𝑥))=𝑥𝑙𝑖𝑚→𝑎𝑓(𝑥)±𝑙𝑖𝑚𝑥→𝑎𝑔(𝑥)
(ii) 𝑙𝑖𝑚𝑥→𝑎(𝑓(𝑥).𝑔(𝑥))=𝑙𝑖𝑚𝑥→𝑎𝑓(𝑥).𝑙𝑖𝑚𝑥→𝑎𝑔(𝑥)
(iii) 𝑙𝑖𝑚𝑥→𝑎𝑓𝑔((𝑥𝑥))=
𝑥𝑙𝑖𝑚→𝑎𝑓(𝑥)
𝑙𝑖𝑚𝑥→𝑎𝑔(𝑥),(𝑥𝑙𝑖𝑚→𝑎𝑔(𝑥)≠^0 )^
(iv) If 𝑙𝑖𝑚𝑥→𝑎𝑓(𝑥) exists and 𝑙𝑖𝑚𝑥→𝑎𝑔(𝑥)=∄, then 𝑥𝑙𝑖𝑚→𝑎𝑓(𝑥).𝑔(𝑥) may exist
Example: Let 𝑓(𝑥)=𝑠𝑖𝑛𝑥, 𝑔(𝑥)=^1 𝑥, 𝑙𝑖𝑚𝑥→ 0 𝑓(𝑥)= 0 , 𝑙𝑖𝑚𝑥→ 01 𝑥=∄
But 𝑙𝑖𝑚𝑥→ 0 𝑠𝑖𝑛𝑥.^1 𝑥= 1
(v) Indeterminate form III (0^0 , 1, ^0 )
If lim ( )()x
xa
y f x 
→
==

Then, log lim ( ) log ( )
xa
y x f x
→

### =

Thus 0^0 , 1, ^0 will convert into ×0 from which can be solved easily.

(vi) If 𝑙𝑖𝑚𝑥→𝑎𝑔𝑓((𝑥𝑥))=^00 (or)∞∞, then 𝑙𝑖𝑚𝑥→𝑎𝑓𝑔((𝑥𝑥))=𝑙𝑖𝑚𝑥→𝑎𝑓𝑔 _′′_ ((𝑥𝑥))≠(^00 )

If 𝑙𝑖𝑚𝑥→𝑎𝑓𝑔 _′′_ ((𝑥𝑥))=^00 (or)∞∞, then 𝑙𝑖𝑚𝑥→𝑎𝑓𝑔 _′′_ ((𝑥𝑥))=𝑙𝑖𝑚𝑥→𝑎𝑓𝑔 _′′′′_ ((𝑥𝑥))and so on

(vii) If 𝑥𝑙𝑖𝑚→𝑎(𝑓(𝑥).𝑔(𝑥))= 0 × _∞_ ⇒𝑙𝑖𝑚𝑥→𝑎(𝑓( 1 𝑥)
𝑔(𝑥))

```
=^00 (Apply L- Hospital Rule again)
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 5
Engineering Mathematics**
(j) Some Standard Limits
(i) 𝑙𝑖𝑚𝑥→ 0 𝑠𝑖𝑛𝑥𝑥= 1
(ii) 𝑙𝑖𝑚𝑥→ 0 𝑡𝑎𝑛𝑥𝑥= 1
(iii) 𝑙𝑖𝑚𝑥→ 01 −𝑐𝑜𝑠𝑥 2 𝑎𝑥=𝑎
2
2
(iv) (^) 𝑥𝑙𝑖𝑚→ _∞_ 𝑠𝑖𝑛𝑥𝑥= 0
(v) (^) 𝑥𝑙𝑖𝑚→ _∞_ 𝑐𝑜𝑠𝑥𝑥= 0
(vi) 𝑙𝑖𝑚𝑥→ 0 ( 1 +𝑎𝑥)𝑏/𝑥=𝑒𝑎𝑏
(vii) (^) 𝑥𝑙𝑖𝑚→ _∞_ ( 1 +𝑎𝑥)
𝑏𝑥
=𝑒𝑎𝑏
(viii) 𝑙𝑖𝑚𝑥→ 0 (𝑎
𝑥+𝑏𝑥
2 )
1 /𝑥
=√𝑎𝑏
(ix) 𝑙𝑖𝑚𝑥→ 0 (^1
𝑥+ 2 𝑥+ 3 𝑥+....+𝑛𝑥
𝑛 )
1 /𝑥
=𝑛√𝑛!
(x) 𝑙𝑖𝑚𝑥→ 0 𝑎
𝑥− 1
𝑥 =𝑙𝑜𝑔𝑒𝑎;𝑙𝑖𝑚𝑥→ 0
𝑒𝑥− 1
𝑥 =^1
(xi) 𝑙𝑖𝑚𝑥→ 0 𝑥.𝑠𝑖𝑛(^1 𝑥)= 0
**1.2 Mean Value Theorems
1.2.1 Lagrange’s Mean Value Theorem (LMVT)**
If 𝑓(𝑥) is continuous in [a, b] and it is differentiable in (a, b) then ∃ at least one point ‘c’ such that c  (a, b) and
𝑓 _′_ (𝑐)=

### 𝑓(𝑏)−𝑓(𝑎)

### 𝑏−𝑎

Here 𝑓 _′_ (𝑐) slope of tangent to f(x) at x = c.

Tangent at x = c is parallel to the line connecting the points A and B

```
Fig.1. 3. LMVT
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 6
Engineering Mathematics
1.2.2 Rolle’s Mean Value Theorem**
If 𝑓(𝑥) is continuous in [a, b] and differentiable in (a, b) and f(a) = f(b) then  at least one-point c  (a, b) such that 𝑓 _′_ (𝑐)= 0.
Fig. 1. 4. **Rolle’s mean value
1.2.3 Cauchy’s Mean Value Theorem**
If f(x) and g(x) are continuous in [a, b] and differentiable in (a, b) then  at least one value of ‘c’ such that c  (a, b) and
𝑔𝑓 _′′_ ((𝐶𝐶))=𝑔𝑓((𝑏𝑏))−−𝑔𝑓((𝑎𝑎))
**1.3 Increasing and Decreasing Functions
1.3.1 Increasing Functions**
A function f(x) is said to be increasing, if 𝑓(𝑥 1 )<𝑓(𝑥 2 ) ∀ 𝑥 1 <𝑥 2
Or
A function f(x) is said to be increasing, if f(x) increases as x increases.
For a function 𝑓(𝑥) to be increasing at the point x=a, 𝑓′(𝑎)> 0.
Example:
ex, log ex → Monotonically increasing functions
sin x in (0, /2) → non-monotonic functions
**1.3.2 Decreasing Functions**
A function f(x) is said to be a decreasing function, if 𝑓(𝑥 1 )>𝑓(𝑥 2 )∀𝑥 1 <𝑥 2
A function 𝑓(𝑥) is said to be decreasing function, if 𝑓(𝑥) decreases as x increases.
Example: 𝑒−𝑥 →Monotonically decreasing function, sin𝑥 in (𝜋 2 ,𝜋)
**1.4. Concept of Maxima and Minima**
Let f(x) be a differentiable function, then to find the maximum (or) minimum of f(x).
(1) Find f (x) and equate to zero.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 7
Engineering Mathematics**
(2) Solve the resulting equation for x. Let its roots be a 1 , a 2 ,... then f(x) is stationary at x = a 1 , a 2 ,...... Thus x = a 1 , a 2 ,...

... are the only points at which f(x) can be maximum or a minimum.

(3) Find f (x) and substitute in it by terms x = a 1 , a 2 ,...... wherever f (x) is negative, we have a maximum and wherever

```
f (x) is positive, we have a minimum.
```

(4) If f (a 1 ) = 0, find f (x) put x = a 1 in it. If f (a 1 )  0, there is neither a maximum nor a minimum at x = a 1. If f (a 1 ) = 0,

```
find f iv(x) and put x = a 1 in it. If f iv(a 1 ) is negative, we have maximum at x = a 1 , if it is positive there is a minimum at
x = a 1. If f iv(a 1 ) is zero, we must find f v(x), and so on. Repeat the above process for each root of the equation f (x) = 0.
```

Example: x = 0 is a critical point of f(x) = x^3

```
Fig. 1.5. Graph of 𝒙𝟑
𝑓(𝑥)=𝑥^3
```

 𝑓 _′_ (𝑥)= 3 𝑥^2 = 0  x = 0

𝑓′′(𝑥)= 6 𝑥⇒ 𝑓 _′′_ ( 0 )= 6 ( 0 )= 0

- Global maxima and minima :
  We first find local maxima and minima and then calculate the value of ‘f’ at boundary points of interval given e.g. (a, b)
  we find f(a) and f(b) and compare it with the values of local maxima and minima. The absolute maxima and minima can
  be decided then.

**1.5. Taylor Series**

If f(x) is continuously differentiable (𝑓 _′_ (𝑥),𝑓"(𝑥),𝑓 _′′′_ (𝑥),..... exists) then the Taylor series expansion of f(x) about the

```
point x = a is given by
```

𝑓(𝑥)=𝑓(𝑎)+𝑓′ 1 (𝑎!)(𝑥−𝑎)+𝑓′′ 2 (!𝑎)(𝑥−𝑎)^2 +𝑓′′′ 3 (!𝑎)(𝑥−𝑎)^3 .+...∞

If a = 0, then 𝑓(𝑥)=𝑓( 0 )+𝑓′ 1 (!^0 )𝑥+𝑓′′ 2 (!^0 )𝑥^2 +𝑓′′′ 3 (!^0 )𝑥^3 +.....∞ (Remember that Mc-Lauren Series is same as Taylor

```
Series if a = 0)
```

The coefficient of (x – a)n in the Taylor series expansion of f(x) is 𝑓

𝑛(𝑎)
𝑛!.^
The general expansion of Taylor series is given by 𝑓(𝑥+ _ℎ_ )=𝑓(𝑥)+ _ℎ_ .𝑓 _′_ 1 (𝑥!)+ _ℎ_^2 .𝑓 _′′_ 2 (𝑥!)+ _ℎ_^3 .𝑓 _′′′_ 3 (!𝑥)+...... _∞_

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 8
Engineering Mathematics**

- Finding the expansion of ex about x = 0

𝑓(𝑥)=𝑒𝑥⇒𝑓( 0 )=𝑒^0 = 1

𝑓′(𝑥)=𝑒𝑥⇒𝑓′( 0 )=𝑒^0 = 1 ;𝑓"( 0 )=𝑓′′′( 0 )=𝑓′′′′( 0 )=.....= 1

𝑓(𝑥)=𝑒𝑥= 1 +(𝑥− 0 ) 11 !+(𝑥− 0 )^2. 21 !+(𝑥− 0 )^3. 31 !+......

 𝑒𝑥= 1 + 1 𝑥!+𝑥

```
2
2 !+
```

```
𝑥^3
3 !+.....^
```

**1.6 Integral Calculus**

If F(x) is anti-derivative of f(x). That is, continuous and differentiable in (a, b), then we write (^) ∫𝑥𝑥==𝑎𝑏𝑓(𝑥)𝑑𝑥=𝐹(𝑏)−
𝐹(𝑎). Here f(x) is integrand
If 𝑓(𝑥)> 0 ∀𝑎≤𝑥≤𝑏,𝑡ℎ𝑒𝑛 (^) ∫𝑎𝑏𝑓(𝑥) 𝑑𝑥 represents the shaded area in the given figure.
y = f(x)
x=a x=b
Fig.1. 6. Integration of continuous function
**1.6.1 Mean Value Theorem of Integration**
If f(x) is continuous in [a, b] and differentiable in (a, b) then ‘’ atleast one-point c (a, b) such that
𝑓(𝑐)=∫
𝑎𝑏𝑓(𝑥)𝑑𝑥
(𝑏−𝑎)^
Fig. 1. 7. Mean value of integration

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 9
Engineering Mathematics
1.7. Newton-Leibnitz Rule**
If f(x) is continuously differentiable and (x), (x) are two functions for which the 1st derivative exists, then
𝑑
𝑑𝑥(∫ 𝑓

### (𝑥)𝑑𝑥

```
𝜓(𝑥)
```

```
𝜙(𝑥)
```

### )=𝑓(𝜓(𝑥)).𝜓 ′ (𝑥)−𝑓(𝜙(𝑥)).𝜙 ′ (𝑥)

Example: (^) 𝑑𝑥𝑑(∫𝑥 𝑠𝑖𝑛𝑥
2
𝑥 𝑑𝑥)=𝑠𝑖𝑛(𝑥
(^2) ). 2 𝑥−𝑠𝑖𝑛𝑥. 1 = 2 𝑥𝑠𝑖𝑛(𝑥 (^2) )−𝑠𝑖𝑛𝑥
**1.8. Some Standard Integrals**

1. (^) ∫𝑥𝑛𝑑𝑥=𝑥
   𝑛+ 1
   𝑛+ 1 +𝐶, (𝑛≠−^1 )^
2. ∫^1 𝑥𝑑𝑥=𝑙𝑜𝑔𝑒|𝑥|+𝐶
3. (^) ∫𝑠𝑖𝑛𝑥𝑑𝑥=−𝑐𝑜𝑠𝑥+𝐶
4. ∫𝑐𝑜𝑠𝑥𝑑𝑥=𝑠𝑖𝑛𝑥+𝐶
5. (^) ∫𝑓𝑓 _′_ ((𝑥𝑥))𝑑𝑥=𝑙𝑜𝑔𝑒|𝑓(𝑥)|+𝐶

### 6. ∫𝑡𝑎𝑛𝑥𝑑𝑥=−∫−𝑠𝑐𝑜𝑠𝑖𝑛𝑥𝑥𝑑𝑥=−𝑙𝑜𝑔𝑒|𝑐𝑜𝑠𝑥|+𝐶

 (^) ∫𝑡𝑎𝑛𝑥𝑑𝑥=𝑙𝑜𝑔𝑒|𝑠𝑒𝑐𝑥|+𝐶

7. ∫𝑐𝑜𝑡𝑥𝑑𝑥=∫𝑐𝑜𝑠𝑠𝑖𝑛𝑥𝑥𝑑𝑥=𝑙𝑜𝑔𝑒|𝑠𝑖𝑛𝑥|+𝐶=−𝑙𝑜𝑔𝑒|𝑐𝑜𝑠𝑒𝑐 𝑥|+𝐶
8. (^) ∫𝑠𝑒𝑐𝑥𝑑𝑥=∫𝑠𝑒𝑐(𝑠𝑒𝑐𝑥(𝑠𝑒𝑐𝑥+𝑥𝑡𝑎𝑛+𝑡𝑎𝑛𝑥)𝑥)𝑑𝑥 = 𝑙𝑜𝑔𝑒|𝑠𝑒𝑐𝑥+𝑡𝑎𝑛𝑥|+𝐶

### 9. ∫𝑐𝑜𝑠𝑒𝑐 𝑥𝑑𝑥=𝑙𝑜𝑔𝑒|𝑐𝑜𝑠𝑒𝑐 𝑥−𝑐𝑜𝑡𝑥|+𝐶

### 10. ∫𝑎𝑥𝑑𝑥= 𝑎

```
𝑥
𝑙𝑜𝑔𝑒𝑎+𝐶^
```

11. (^) ∫𝑥.𝑙𝑜𝑔^1 𝑒𝑎𝑑𝑥=𝑙𝑜𝑔𝑎𝑥+𝐶

### 12. ∫𝑥𝑥( 1 +𝑙𝑜𝑔𝑒𝑥)𝑑𝑥=𝑥𝑥+𝐶

### 13. ∫𝑓(𝑥).𝑓 ′ (𝑥)𝑑𝑥=^12 (𝑓(𝑥))

```
2
+𝐶
```

14. (^) ∫√𝑓𝑓 _′_ ((𝑥𝑥))𝑑𝑥= 2 .√𝑓(𝑥)+𝐶
15. If f(x), g(x) are two functions. that are differentiable, then

(^) ∫𝑓(𝑥) 𝑔(𝑥)𝑑𝑥=𝑓(𝑥).∫𝑔(𝑥)𝑑𝑥−∫[𝑓 _′_ (𝑥)𝑔(𝑥)]𝑑𝑥+𝐶

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 10
Engineering Mathematics**
Before integrating the product, the functions f(x) and g(x) are to be arranged according to the ILATE Principle.
Here, ILATE stands for INVERSE LOGARITHMIC ALGEBRAIC TRIGONOMETRIC EXPONENTIAL.
**1.9 Properties of Definite Integrals**

1. If f(x) is differentiable in interval (a, b), then ∫𝑎𝑏𝑓(𝑥)𝑑𝑥=−∫𝑏𝑎𝑓(𝑥)𝑑𝑥
2. If  a point c  (a, b) such that f(x) is not differentiable, then

(^) ∫𝑎𝑏𝑓(𝑥)𝑑𝑥=∫𝑎𝑐𝑓(𝑥)𝑑𝑥+∫𝑐𝑏𝑓(𝑥)𝑑𝑥

3. If f(x) is continuously differentiable function,

∫−𝑎𝑎𝑓(𝑥)𝑑𝑥= 2 ×∫ 0 𝑎𝑓(𝑥)𝑑𝑥;if 𝑓(−𝑥)=𝑓(𝑥), (“f(x) is even function”)

= 0 ; if 𝑓(−𝑥)=−𝑓(𝑥),("𝑓(𝑥) is odd function")

4. (^) ∫ 02 𝑎𝑓(𝑥)𝑑𝑥= 2 ×∫ 0 𝑎𝑓(𝑥)𝑑𝑥, if 𝑓( 2 𝑎−𝑥)=𝑓(𝑥)
5. ∫𝑎𝑏𝑓(𝑥)𝑑𝑥=∫𝑎𝑏𝑓(𝑎+𝑏−𝑥)𝑑𝑥
6. (^) ∫𝑎𝑏𝑓(𝑥)+𝑓𝑓((𝑥𝑎)+𝑏−𝑥)=(𝑏− 2 𝑎)
   Example:
   (i) (^) ∫ 0 𝜋/^2 𝑠𝑖𝑛𝑠𝑖𝑛𝑥+𝑐𝑜𝑠𝑥 𝑥=𝜋 4
   (ii) ∫ 1 +√^1 𝑡𝑎𝑛𝑥𝑑𝑥=∫^1
   1 +(√√𝑠𝑖𝑛𝑐𝑜𝑠𝑥𝑥)

### 0 𝜋/^20 𝜋/^2 𝑑𝑥=∫ 0 𝜋/^2 √𝑐𝑜𝑠√𝑥𝑐𝑜𝑠+√𝑥𝑠𝑖𝑛𝑥𝑑𝑥=𝜋 4

(iii) ∫ (^23) √𝑥+√√𝑥 5 −𝑥=(^3 − 22 )=^12
(iv) (^) ∫ 0 𝜋/^2 √𝑡𝑎𝑛√𝑡𝑎𝑛𝑥+√𝑥𝑐𝑜𝑡𝑥𝑑𝑥=𝜋 4
7. (^) ∫ 0 𝜋/^2 𝑠𝑖𝑛𝑚𝑥𝑑𝑥=∫ 0 𝜋/^2 𝑐𝑜𝑠𝑚𝑥 𝑑𝑥=(𝑚𝑚−×^1 )(×𝑚(−𝑚 2 −)×^3 )(×𝑚(−𝑚 4 −)^5 )×...(^12 )(or)^23 ×𝐾
Where K = /2 if m is even
= 1 if m is odd.
8. (^) ∫ 0 𝜋𝑎 (^2) 𝑐𝑜𝑠 (^2) 𝑥𝑑𝑥+𝑏 (^2) 𝑠𝑖𝑛 (^2) 𝑥=𝑎𝑏𝜋
9. (^) ∫ 0 𝜋/^2 𝑎 (^2) 𝑐𝑜𝑠 (^2) 𝑥𝑑𝑥+𝑏 (^2) 𝑠𝑖𝑛 (^2) 𝑥= 2 𝜋𝑎𝑏
**1.10 Length of a Curve**
(a) The length of the arc of the curve y = f(x) between the points where x = a and x = b is
2
s ab 1 dy dx
dx

### 

### =+

 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 11
Engineering Mathematics**
Fig.1. 8. Length of the curve
(b) The length of the arc of the curve x=f y() between the points where y = a and y = b, is
2
1
b
a
s dx dy
dy

### 

### =+

 

(c) The length of the arc of the curve x==f t y( ), f t( ) between the points where t = a and t = b, is

```
b^22
a
s dx dy dt
dt dt
```

### =+   

       ^

(d) The length of the arc of the curve rf=( ), between the points where  =  and  = , is
2 dr^2
s r d d

```


```

```

= + 
 
```

**1.11 Surface Area of Solid generated by revolving a curve about a fixed axis**

Elemental Surface Area
𝑑𝐴= 2 𝜋𝑦×𝑑𝑠= 2 𝜋𝑦𝑑𝑠

 Total surface area = A = ∫𝑥𝑥==𝑎𝑏 2 𝜋𝑦√ 1 +(𝑑𝑦𝑑𝑥)

```
2
𝑑𝑥
```

```
Fig.1. 9. Surface area
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 12
Engineering Mathematics
1.12 Volume of the solid**
A. The volume of the solid obtained by revolving the curve y = f (x) between the lines x = a and x = b is given by
 𝑉≈∫𝑥𝑥==𝑎𝑏𝜋𝑦^2 𝑑𝑥
Fig. 1. 10. Volume of the solid
B. Revolution about the y-axis. Interchanging x and y in the above formula, we see that the volume of the solid generated
by the revolution, about y-axis, of the area, bounded by the curve x=f y( ), the y-axis and the abscissa y = a, y = b is
b 2
ax dy.^
**1.13 Gamma Function**
The integral ∫ 0 ∞𝑒−𝑥.𝑥𝑛−^1 𝑑𝑥,(𝑛> 0 ) is called Gamma function of n. It is denoted by Γ𝑛=∫ 0 ∞𝑒−𝑥𝑥𝑛−^1 𝑑𝑥.
Note :
/
0
11
sin cos^22
2 2
2
mn
mn
x xdx
mn

 ++  
     
=====================

++

^
Where (x) is called the gamma function.
**1.13.1 Properties of Gamma Function**
(i) Γ𝑛=(𝑛− 1 )! (ii) Γ(𝑛+ 1 )=(𝑛)!
(iii) Γ(𝑛+ 1 )=𝑛Γ𝑛 (iv) Γ(^12 )=√𝜋
**1.14 Beta Function**
The function  (m, n) = ∫ 01 𝑥𝑚−^1 .( 1 −𝑥)𝑛−^1 𝑑𝑥 (m, n > 0) is called  function of m and n.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 13
Engineering Mathematics
1.14.1 Properties of**  **function**
(i) 𝛽(𝑚,𝑛)=ΓΓ(𝑚m.+Γ𝑛𝑛)
(ii) 𝛽(𝑚,𝑛)=𝛽(𝑛,𝑚)
(iii) 𝛽(𝑚,𝑛)=∫ 𝑥
𝑚− 1
( 1 +𝑥)𝑚+𝑛
_∞_
0 𝑑𝑥^
𝛽(𝑛,𝑚)=∫ 𝑥
𝑛− 1
( 1 +𝑥)𝑚+𝑛
_∞_
0 𝑑𝑥^
(iv) 𝑠𝑖𝑛𝑝𝜃.𝑐𝑜𝑠𝑞𝜃𝑑𝑥=^12 𝛽(𝑝+ 21 ,𝑞+ 21 ),(𝑝,𝑞>− 1 )
**1.15 Area between the curves**
If the function f(x) > g(x) for all values of x between x=a and x=b then
𝐴=∫𝑎𝑏𝑓(𝑥)𝑑𝑥−∫𝑎𝑏𝑔(𝑥)𝑑𝑥 ⇒ 𝐴=∫𝑎𝑏(𝑓(𝑥)−𝑔(𝑥))𝑑𝑥
Fig. 1 .1 1. Area under curve
Note : Area bounded by curve rf=() between = and  is^2
1
2
rd

 ^
**1.16 Multi Variable Calculus**
(a) Continuity of a function
A function f(x, y) is said to be continuous at (a, b), if 𝑙𝑖𝑚𝑥→𝑎
𝑦→𝑏

### 𝑓(𝑥,𝑦)=𝑓(𝑎,𝑏)

(b) Differentiation of a two-variable function

If f(x, y) is a continuous function, then the derivative of f(x, y) with respect to x treating y as constant is given by

p = 𝜕𝜕𝑓𝑥=𝑙𝑖𝑚 _ℎ_ → 0 𝑓(𝑥+ _ℎ_ ,𝑦 _ℎ_ )−𝑓(𝑥,𝑦)

The derivative of f(x, y) with respect to y treating x as constant is given by

```
𝑞=
```

### 𝜕𝑓

### 𝜕𝑦

### =𝑙𝑖𝑚𝑘→ 0

### 𝑓(𝑥,𝑦+𝑘)−𝑓(𝑥,𝑦)

### 𝑘

(c) Homogenous Function

A function f (x, y) is said to be homogenous function of degree ‘n’ if 𝑓(𝑘𝑥,𝑘𝑦)=𝑘𝑛.𝑓(𝑥,𝑦).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 14
Engineering Mathematics**
Example: 𝑓(𝑥,𝑦)=𝑥^3 − 3 𝑥^2 𝑦+ 3 𝑥𝑦^2 +𝑦^3
 𝑓(𝑘𝑥,𝑘𝑦)=(𝑘𝑥)^3 − 3 (𝑘𝑥)^2 (𝑘𝑦)+ 3 (𝑘𝑥).(𝑘𝑦)^2 +(𝑘𝑦)^3
= 𝑘^3 (𝑥^3 − 3 𝑥^2 𝑦+ 3 𝑥𝑦^2 +𝑦^3 )
= 𝑘^3 .𝑓(𝑥,𝑦)  𝑓(𝑥,𝑦) is a homogenous function of degree ‘3’.
(d) **Euler’s Theorem**
If f (x, y) is a homogeneous function of degree ‘n’ then
(i) 𝑥.𝜕𝑓𝜕𝑥+𝑦.𝜕𝑓𝜕𝑦=𝑛𝑓
(ii) 𝑥^2 .𝜕
(^2) 𝑓
𝜕𝑥^2 +^2 𝑥𝑦
𝜕^2 𝑓
𝜕𝑥𝜕𝑦+𝑦
2 𝜕^2 𝑓
𝜕𝑦^2 =𝑛(𝑛−^1 )𝑓^
If f(x, y) = g(x, y) + h(x, y) + (x, y) where g (x, y), h (x, y) and (x, y) are homogenous functions of degrees m, n and
p respectively, then
𝑥.𝜕𝑓𝜕𝑥+𝑦.𝜕𝑓𝜕𝑦=𝑚.𝑔(𝑥,𝑦)+𝑛.ℎ(𝑥,𝑦)+𝑝.𝜙(𝑥,𝑦)
𝑥^2 .𝜕
(^2) 𝑓
𝜕𝑥^2 +^2 𝑥𝑦.
𝜕^2 𝑓
𝜕𝑥𝜕𝑦+𝑦
(^2) .𝜕^2 𝑓
𝜕𝑦^2 =𝑚(𝑚−^1 ).𝑔(𝑥,𝑦)+𝑛(𝑛−^1 ).ℎ(𝑥,𝑦)+𝑝(𝑝−^1 ).𝜙(𝑥,𝑦)^
(e) Total derivative:
(i) If u = f(x, y) and if x = (t), y = v(t) then ..
du u dx u dy
dt x dt y dt

=+

(ii) If u be a function of x and y, where y is a function of x, then.
du u u dy
dx x y dx
=+

(iii) If u = f(x, y) and x=f t t1 1 2( , ) and y=f t t2 1 2( , ), then
1 1 1
u u..x u y
t x t y t
    =+
    
and
2 2 2
u u..x u y
t x t y t
    =+
    
(iv) If x and y are connected by an equation of the form f(x, y) = 0, then /
/
dy f x
dx f y
=−

(f) Concept of Maxima and Minima in Two Variables
If f(x, y) is a two-variable differentiable function, then to find the maxima (or) minima.
Step-1: Calculate 𝑝=𝜕𝑓𝜕𝑥 and 𝑞=𝜕𝜕𝑓𝑦 and equate p = 0, q = 0
Let (x 0 , y 0 ) be a stationary point.
Step- 2 : Calculate r, s, t where 𝑟=𝜕
(^2) 𝑓
𝜕𝑥^2 |(𝑥 0 ,𝑦 0 ); 𝑠=
𝜕^2 𝑓
𝜕𝑥.𝜕𝑦|(𝑥 0 ,𝑦 0 ); 𝑡=
𝜕^2 𝑓
𝜕𝑦^2 |(𝑥 0 ,𝑦 0 )^
Case (i): If 𝑟𝑡−𝑠^2 > 0 and r > 0, then the function f (x, y) has minimum at (x 0 , y 0 ) and the minimum value is f(x 0 , y 0 ).
Case (ii): If 𝑟𝑡−𝑠^2 > 0 and r < 0, then the function f (x, y) has maximum at (x 0 , y 0 ) and the maximum value is

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 15
Engineering Mathematics**
f(x 0 , y 0 ).
Case (iii): If 𝑟𝑡−𝑠^2 < 0 ; then we cannot comment on the existence of maxima and minima.
Such stationary points where 𝑟𝑡−𝑠^2 = 0 are called saddle points.
(g) **Concept of Constraint Maxima and Minima (Method of Lagrange’s unidentified multipliers).**
If f(x, y, z) is a continuous and differentiable function, such that the variables x, y and z are related/constrained by the
equation (x, y, z) = C then to calculate the extreme value of f(x, y, z) using Lagrange’s Method of unidentified multipliers.
Step-1: Form the function F(x, y, z) = f(x, y, z) + , where 𝜆 is a multiplier.
Step-2: Calculate 𝜕𝐹𝜕𝑥, 𝜕𝐹𝜕𝑦 and 𝜕𝜕𝐹𝑧 and equate them to zero
Step- 3 : Equate the values of  from the above 3 equations and obtain the relation between the variables x, y and z.
Step- 4 : Substitute the relation between x, y and z in (x, y, z) = C and get the values of x, y, z. Let they be (x 0 , y 0 , z 0 ).
Step-5: Calculate f(x 0 , y 0 , z 0 )
The value f(x 0 , y 0 , z 0 ) is the extreme value of f(x, y, z).
(h) Multiple Integrals
If f(x, y) is continuous and differentiable at every point within a region ‘R’ bounded by some curves is given by
𝐼=∫∫𝑅𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦
If there is a double integral,
𝐼=∫𝑥𝑥==𝑎𝑏∫𝑦𝑦==𝜙𝜓((𝑥𝑥))𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥 [Let (x) > (x)]
Then I = area of the region bounded by the curves, y = (x); y = (x), x = a and x = b if f(x, y) = 1
Value of x – co-ordinate of centroid of the region bounded by y = (x); y = (x); x = a, x = b if f(x, y) = x
(i) Change of Orders of Integration
𝐼=∫𝑥𝑥==𝑎𝑏∫𝑦𝑦==𝜙𝜓((𝑥𝑥))𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥 → 𝐼=∫𝑦𝑦==𝑐𝑑∫𝑥𝑥==𝑔 _ℎ_ ((𝑦𝑦))𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦
In change of order of Integration, the order of the Integrating variables changes and the limits as well.
Note : When limits are constants, the order of integration does not matter,
(^) ( , ) ( , )
y d x b x b y d
y c x a x a y c
f x y dxdy f x y dydx
=====================

= = = =
  =  ^
**1.17 Jacobian of the Transformation**
(i) The Jacobian of the transformation, x==f u v y 12 ( , ,) f u v( , ) is defined as,

### ( , )

### ( , )

```
uv
uv
```

```
xy xx
J
uv yy
```

### ==

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **1. 16
Engineering Mathematics**
(ii) The Jacobian of the transformation,
x=f u v w y 1 ( , , ), =f u v w z 2 ( , , ), =f u v w 3 ( , , ) is defined as
( , , )
( , , )
u v w
u v w
u v w
x x x
x y z
J y y y
u v w
z z z

==


**1.18 Change of Variables Formula**
(i) ( , ) ( ( , ), 12 ( , ) | |
RR
f x y dx dy=f f u v f u v J du dv^
(ii) ( , , ) ( ( , , ), ( , , ), 1 2 3 ( , , )) | |
RR
f x y z dxdydz=f f u v w f u v w f u v w J du dv dw^
**1.19 Change of Variables**
(i) Cartesian to polar co-ordinates :
(^) xr=cos
yr=sin
J = r
dx dy rdrd=
(ii) Cartesian to cylindrical polar co-ordinate :
xr=cos
yr=sin
z = z
J = r
dxdydz rdr d dz=
(iii) Cartesian to spherical polar co-ordinates :
x=  sin cos
y=  sin sin
z= cos
(^) J= ^2 sin
(^) dx dy dz=    ^2 sin d d d
❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

2

**LINEAR ALGEBRA**

 **Matrix**

An array of elements in horizontal lines (Rows) and Vertical Lines (Columns) is called a Matrix.

Example: 𝐴= [𝑖𝑗 𝑛𝑎 𝑑𝑝 𝑎𝑖 𝑎𝑛]

**2 .1.1 Size of Matrix**

If a matrix has 'm' rows and 'n' columns, then we say that the size of the matrix is m × n (read as m by n)

### 𝐴=

### [

### 𝑎 11 𝑎 12 𝑎 13 .........𝑎 1 𝑛

### 𝑎 21 𝑎 22 𝑎 23 .........𝑎 2 𝑛

### .. ..

### .. ..

### 𝑎𝑚 1 𝑎𝑚 2 𝑎𝑚 3 .........𝑎𝑚𝑛]

```
; 𝐴=[𝑎𝑖𝑗]𝑚×𝑛 such that 1 ≤𝑖≤𝑚, 1 ≤𝑗≤𝑛 and 𝑎𝑖𝑗=𝑓(𝑖,𝑗)
```

**2 .1.2 Addition of Matrices**

(i) Two matrices 𝐴=[𝑎𝑖𝑗]𝑚×𝑛 & 𝐵=[𝑏𝑖𝑗]𝑝×𝑞can be added only if m = p & n = q.

(ii) Matrix Addition is commutative (A + B = B + A)

(iii) Matrix Addition is Associative. A + (B + C) = (A + B) + C

(iv) Existence of additive identity : If O be m × n matrix each of whose elements are zero. Then, A + O = A = O + A for every
m × n matrix A.

(v) Existence of additive inverse : Let Aa=ij mn then the negative of matrix A is defined as matrix −aij mn and is

```
denoted by –A.
```

 Matrix –A is additive inverse of A. Because (–A) + A = O = A + (–A). Here O is null matrix of order m × n.

(vi) Cancellation laws holds good in case of addition of matrices, which is X = –A.

 A + X = B + X  A = B

```
 X + A = X + B  A = B
```

(vii) The equation A + X = 0 has a unique solution in the set of all m × n matrices.

**2 .1.3 Multiplication of Matrices**

The multiplication of two matrices 𝐴=[𝑎𝑖𝑗]𝑚×𝑛 and 𝐵=[𝑏𝑖𝑗]𝑝×𝑞 (⇒𝐴𝐵𝑚×𝑞) is feasible only if n = P.

𝐴𝑚×𝑛⋅𝐵𝑝×𝑞=𝐶

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

### A = [

### 𝑎 11 𝑎 12 𝑎 13

### 𝑎 21 𝑎 22 𝑎 23

### 𝑎 31 𝑎 32 𝑎 33

### ]

```
3 × 3
```

### 𝐵=[

### 𝑏 11 𝑏 12

### 𝑏 21 𝑏 22

### 𝑏 31 𝑏 32

### ]

```
3 × 2
```

### 𝐴 3 × 3 × 𝐵 3 × 2

### ⇒ [

### 𝑎 11 .𝑏 11 +𝑎 12 ⋅𝑏 21 +𝑎 13 .𝑏 31 𝑎 11 𝑏 12 +𝑎 12 𝑏 22 +𝑎 13 𝑏 32

### 𝑎 21 .𝑏 11 +𝑎 22 .𝑏 21 +𝑎 23 .𝑏 31 𝑎 21 𝑏 12 +𝑎 22 𝑏 22 +𝑎 23 𝑏 32

### 𝑎 31 .𝑏 11 +𝑎 32 ⋅𝑏 21 +𝑎 33 ⋅𝑏 31 𝑎 31 𝑏 12 +𝑎 32 𝑏 22 +𝑎 33 𝑏 32

### ]

```
3 × 2
```

**2 .1.4 Properties of Multiplication of Matrices**

(i) Matrix Multiplication Need not be commutative.

(ii) Matrix Multiplication is Associative (A(BC)) = ((AB)C)

(iii) Matrix Multiplication is distributive A(B + C) = (AB + AC)

(iv) The product of two Matrices 𝐴𝑚×𝑛,𝐵𝑛×𝑞 (i.e. 𝐴𝐵𝑚×𝑞) can be a zero matrix even if 𝐴≠𝑂&𝐵≠𝑂.

Example: 𝐴=[^3000 ];𝐵=[^0004 ]⇒𝐴𝐵=[^0000 ]

- For the multiplication of two matrices 𝐴𝑚×𝑛 & 𝐵𝑛×𝑞

(i) The No. of Multiplications required = m n q

(ii) The number of Additions required = m (n –1) q

**2 .2 Types of Matrices**

(1) Upper triangular Matrix: A matrix 𝐴=[𝑎𝑖𝑗]; 1 ≤𝑖,𝑗≤𝑛 is said to be an upper triangular matrix if

𝑎𝑖𝑗= 0 ∀ 𝑖>𝑗

(2) Lower Triangular Matrix: A matrix 𝐴=[𝑎𝑖𝑗]𝑛×𝑛; 1 ≤𝑖,𝑗≤𝑛 is said to be a lower Triangular Matrix

if 𝑎𝑖𝑗= 0 ∀ 𝑖<𝑗

(3) Diagonal Matrix: A matrix 𝐴=[𝑎𝑖𝑗],∀ 1 ≤𝑖,𝑗≤𝑛 is said to be a diagonal matrix if 𝑎𝑖𝑗=𝑂 ∀ 𝑖≠𝑗

Example: 𝐴=[

### 𝑑 1 0 0

### 0 𝑑 2 0

### 0 0 𝑑 3

```
]. The diagonal Matrix is also denoted as 𝐴=𝑑𝑖𝑎𝑔 [𝑑 1 ,𝑑 2 ,𝑑 3 ]
```

(4) Scalar Matrix: A Matrix 'A' = [𝑎𝑖𝑗] ; 1 ≤𝑖,𝑗≤𝑛 is said to be a scalar Matrix if 𝑎𝑖𝑗={𝐾 0 ;; 1 𝑖=≠𝑗𝑗

If K = 1, then A → Identity Matrix,

If K = 0, then A → Null Matrix.

(5) Idempotent Matrix:

A Matrix '𝐴𝑛×𝑛' is said to be an idempotent matrix if 𝐴^2 =𝐴.

Example: 𝐴=[ 124 −−^13 ]

⇒𝐴⋅𝐴=[ 124 −−^13 ][ 124 −−^13 ]=[ 124 −−^13 ]=𝐴

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

(6) Nilpotent Matrix: A matrix A is said to be nilpotent of class x or index if Ax = 0 and Ax–^1  0 i.e. x is the smallest index
which makes Ax = 0.

Example: The matrix A =

### 1 1 3

### 5 2 6

### 2 1 3

### 

### 

### 

### − − −

```
is nilpotent class 3, since A  0 and A^2  0, but A^3 = 0.
```

(7) Orthogonal Matrix: A matrix A is said to be orthogonal if A.AT=I

Example: [cossin𝜃𝜃 −cossin𝜃𝜃]

(8) Involutory Matrix: A matrix A is said to be involutory if A^2 =I

Example: [−^21 −^32 ]

**2 .3 Transpose of a Matrix**

For a given matrix =[𝑎𝑖𝑗]; 1 ≤𝑖≤𝑚, 1 ≤𝑗≤𝑛, we can say that 'B' where 𝐵=[𝑏𝑖𝑗], 𝑖≤𝑖≤𝑛 𝑖≤𝑗≤𝑚 is the
transpose of the Matrix 'A' if 𝑎𝑖𝑗=𝑏𝑗𝑖

**2 .3.1 Properties of Transpose of a Matrix**

(i) (𝐴𝑇)𝑇=𝐴

(ii) (𝐴𝐵)𝑇=𝐵𝑇⋅𝐴𝑇

(iii) (𝐾𝐴)𝑇=𝐾𝐴𝑇 where 'K' is a scalar.

**2 .4 Conjugate of a matrix**

The matrix obtained by replacing each element of matrix by its complex conjugate.

**2 .4.1 Properties of conjugate matrix**

(a) (A)=A (b) ()A B+ = +A B

(c) ()KA=K A (d) ()AB =AB

(e) AA= if A is real matrix

AA=− if A is purely imaginary matrix

**2 .5 Transposed Conjugate of a Matrix**

The transpose of conjugate of a matrix is called transposed conjugate. It is represented by A.

(a) ()AA= (b) ()A B+ = +  A B

(c) (KA) = KA (K : Complex number) (d) ()AB  =B A

**2 .6 Trace of a Matrix**

Trace is simply sum of all diagonal elements of a matrix.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2 .6.1 Properties of Trace of a matrix**

Let A and B be two square matrices of order  and  is scalar then

1. Tr( =A) Tr A( )
2. Tr A B( + =) Tr A( )+Tr B( )
3. Tr AB( )=Tr BA( ) [If both AB and BA are defined]

**2 .7 Type of Real Matrix**

(a) Symmetric matrix : (A)T = A

(b) Skew symmetric matrix : (AT) = –A

(c) Orthogonal matrix : (AT = A–^1 , AAT = I)

Note : (a) If A and B are symmetric, then (A + B) and (A – B) are also symmetric.

(b) For any matrix AAT is always symmetric.

(c) For any matrix,
2

### AA+ T

### 

### 

```
is symmetric and
2
```

### AA− T

### 

### 

```
is skew symmetric.
```

(d) For orthogonal matrices, |A| =  1

(e) We can write any matrix A as a sum of symmetric and skew symmetric matrix
22

```
A ATTA A
A=++−
```

**2 .8 Type of complex matrix**

(a) Hermitian matrix : (A = A)

(b) Skew-Hermitian matrix: A = –A

(c) Unitary matrix : (A = A–^1 , AA = I)

Note : (a)
2

```
AA+  is Hermitian and
2
```

```
AA−  is skew Hermitian matrix.
```

(b) We can write any matrix as a sum of Hermitian and skew Hermitian matrix
22

```
A=+A A+−A A
```

**2 .9 Determinant**

The summation of the product of elements of a row(or) column of a matrix with their corresponding Co-factors.
𝐴⋅𝑎𝑑𝑗(𝐴)=|𝐴|⋅I
Determinant can be calculated only if matrix is a square matrix.
Suppose, we need to calculate a 3 × 3 determinant,

```
3 3 3
1 1 2 2 3 3
1 1 1
```

```
j ( j) j ( j) j ( j)
j j j
```

```
a cof a a cof a a cof a
= = =
```

 = = =

We can calculate determinant along any row or column of the matrix.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2.9.1 Properties of Determinants**

(i) If 'A' is a Square Matrix of size ' 𝑛×𝑛 ' and 'k' is a Scalar then

|𝐾⋅𝐴𝑛×𝑛|=𝐾𝑛⋅|𝐴𝑛×𝑛|

(ii) |𝑎𝑑𝑗(𝐴)|=|𝐴|(𝑛−^1 )

(iii) |𝑎𝑑𝑗(𝑎𝑑𝑗(𝐴))|=(|𝐴|)(𝑛−^1 )^2

(iv) |𝐴𝐵|=|𝐴|⋅|𝐵|

(v) |(𝐴𝐵)𝑇|=|𝐵𝑇|⋅|𝐴𝑇|

(vi) If two rows (or) two columns of a determinant are interchanged, then the determinant changes its sign.

(vii) The determinant of an upper triangular Matrix/a lower triangular Matrix/a diagonal Matrix is the product of the

```
principal diagonal elements of the Matrix.
```

(viii) The determinant of Every Skew-Symmetric Matrix of odd order (𝐴𝑛×𝑛)( _′_ 𝑛 _′′_ 𝑖𝑠 𝑜𝑑𝑑) is zero.

(ix) The determinant of an orthogonal Matrix 𝐴𝑛×𝑛 is ± 1

(x) The determinant of an Idempotent Matrix is either 0 (or) 1.

(xi) The determinant of an Involuntary Matrix is ± 1

(xii) The determinant of a Nilpotent Matrix is always zero.

(xiii) If the product of two Non-zero Matrices 𝐴𝑛×𝑛≠ 0 ;𝐵𝑛×𝑛≠ 0 is a zero Matrix ((𝐴𝐵)𝑛×𝑛= 0 ), then both |𝐴|= 0 &

```
|𝐵|= 0.
```

(xiv) If two rows (or) two columns of a Matrix are either equal or Proportional, then the determinant of the Matrix is equal to

```
zero.
```

(xv) The number of terms in the general expansion of an 'n × n' determinant is 𝑛!

(xvi) Value of the determinant is invariant under row and column interchange i.e., AAT =

(xvii) If any row or column is completely zero, then |A| = 0.

(xviii) If any single row or column of the matrix is multiplied by k then the determinant the of new matrix = K|A|

(xix) In a determinant the sum of the product of the element of any row or column with its cofactor gives a determinant of
the matrix.

(xx) In determinant the sum of the product of the element of any row or column with a cofactor of another row or column
will give zero.

(xxi) |AB| = |A| × |B|

(xxii) Elementary operations don’t effect the determinant that is i i j

```
R R KR
AB
```

```
=+
⎯⎯⎯⎯⎯→ then |A| = |B|
```

i i j

```
C C KC
AB
```

```
=+
⎯⎯⎯⎯⎯→ then |A| = |B|
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2 .10 Minors, Cofactor and Adjoint of a Matrix**

Minor of an element is equal to the determinant of the remaining elements of the matrix, after excluding the row and column
containing the particular element. The cofactor of an element can be calculated from the minor of the element. The cofactor of
an element is equal to the product of the minor of the element, and -1 to the power of position values of row and column of the
element.

Cofactor of an Element = − ( (^1) )ij+ Minor of an Element
Here i and j are the positional values of the row and column of the element.
Example :
If
11 12 13
21 22 23
31 32 33
a a a
a a a
a a a

### =^

Minor of element a 21 : 21 12 13
32 33

```
aa
M
aa
```

### =

Co-factor of an element, aMij=−( (^1) )ij+ ij

- To design co-factor matrix, we replace each element by its co-factor.
- Adjoint of a matrix = transpose of cofactor matrix
- 1 ()
  ||

```
A Adj A
A
```

### − =

**2 .11 Inverse of a matrix**

Inverse of a matrix only exists for square matrices.

(^) (^1 )
Adj A()
A
A
− = and A 0
Properties:
(a) AA−−^11 ==A A I
(b) ()AB−^1 =B A− −^11
(c) ()ABC−^1 =C B A− − −^111
(d) (AATT)−−^11 =( )
(e) The inverse of 2 × 2 matrix should be remembered,
( )
a b^11 d b
c d ad bc c a

###  −  − 

###   =  

###   − − 

(i) Interchange the diagonal elements and put negative sign on the rest.

(ii) Divide by determinant.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2.12 Rank of a Matrix**

- The rank of the matrix refers to the number of linearly independent rows or columns in the matrix. ρ(A) is used to denote
  the rank of matrix A.
- A matrix is said to be of rank zero when all of its elements become zero.
- The rank of the matrix is the dimension of the vector space obtained by its columns.
- The rank of a matrix cannot exceed more than the number of its rows or columns. The rank of the null matrix is zero.
- The nullity of a matrix is defined as the number of vectors present in the null space of a given matrix. In other words, it
  can be defined as the dimension of the null space of matrix A called the nullity of A. Rank + Nullity is the number of all
  columns in matrix A.

A real Number 'r' is said to be the rank of a matrix '𝐴𝑚×𝑛' if

```
(1) There is at least one square sub-matrix of A of order r whose determinant is not equal to zero.
(2) If the matrix A contains any square sub-matrix of order (r + 1) and above, then the determinant of such a matrix
should be zero.
```

It is mathematically denoted by 𝜌(𝐴)=𝑟

**2 .12.1 Properties of Rank of a Matrix**

(i) 𝜌(𝐴𝑚×𝑛)≤(𝑚,𝑛)

(ii) 𝜌(𝐴𝐵)≤𝑚𝑖𝑛{𝜌(𝐴),𝜌(𝐵)}

(iii) Rank of transpose of matrix is equal to rank of matrix

(iv) Elementary operations do-not affect the rank the matrix

(v) 𝜌(𝐴+𝐵)≤ {𝜌(𝐴)+𝜌(𝐵)}

**2 .12.2 Row Echelon Form**

A Matrix 𝐴𝑚×𝑛 is said to be in row-echelon form if

(i) Number of zeroes before the 1st Non-zero element in any row is less than the number of such zeroes in its succeeding row.

(ii) Zero rows (if any) should lie at the bottom of the Matrix.

𝜌(𝐴𝑚×𝑛)= Number of non-zero rows in the Row-Echelon form of A.

 **System of Equations**

The given system of equations

𝑎 11 𝑥 1 +𝑎 12 𝑥 12 +𝑎 13 𝑥 3 =𝑏 1

𝑎 21 𝑥 1 +𝑎 22 𝑥 2 +𝑎 23 𝑥 3 =𝑏 2

𝑎 31 𝑥 1 +𝑎 32 𝑥 2 +𝑎 33 𝑥 3 =𝑏 3

can be written in Matrix form as

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

### [

### 𝑎 11 𝑎 12 𝑎 13

### 𝑎 21 𝑎 22 𝑎 23

### 𝑎 31 𝑎 32 𝑎 33

### ][

### 𝑥 1

### 𝑥 2

### 𝑥 3

### ]=[

### 𝑏 1

### 𝑏 2

### 𝑏 3

### ]

### [

### 𝑎 11 𝑎 12 𝑎 13

### 𝑎 21 𝑎 22 𝑎 23

### 𝑎 31 𝑎 32 𝑎 33

### ] [

### 𝑥 1

### 𝑥 2

### 𝑥 3

### ] = [

### 𝑏 1

### 𝑏 2

### 𝑏 3

### ]

Ax = B

Coefficient Variable Constants

Matrix Matrix Matrix

The system Ax = B is said to be a homogeneous system if B = 0.

The system of Ax = B is said to be a non-homogeneous system if 𝐵≠ 0.

**2 .13.1 Consistency of a non-homogeneous system of Equations**

For the above system of non – homogeneous equations, Ax = B; Augmented Matrix = [A/B] = [

### 𝑎 11 𝑎 12 𝑎 13 𝑏 1

### 𝑎 21 𝑎 22 𝑎 23 𝑏 2

### 𝑎 31 𝑎 32 𝑎 33 𝑏 3

### ]

(i) If 𝜌(𝐴)=𝜌(𝐴/𝐵)= Number of unknowns, then the system Ax = B has a unique solution.

(ii) If 𝜌(𝐴)=𝜌(𝐴/𝐵)< Number of unknowns, then the system has infinitely many solutions.

(iii) If 𝜌(𝐴)≠𝜌(𝐴/𝐵), then the system has no solution.

Number of linearly independent solutions for a system of 'n' equations given by Ax = B is 𝑛−𝜌(𝐴)

**2 .13.2 Consistency of Homogeneous System of Equations**

𝑎 11 𝑥+𝑎 12 𝑦+𝑎 13 𝑧= 0

𝑎 21 𝑥+𝑎 22 𝑦+𝑎 23 𝑧= 0

𝑎 31 𝑥+𝑎 32 𝑦+𝑎 33 𝑧= 0

Ax = 0⇒[

### 𝑎 11 𝑎 12 𝑎 13

### 𝑎 21 𝑎 22 𝑎 23

### 𝑎 31 𝑎 32 𝑎 33

### ][

### 𝑥

### 𝑦

### 𝑧

### ]=[

### 0

### 0

### 0

### ] [𝐴/𝐵]=[

### 𝑎 11 𝑎 12 𝑎 13 0

### 𝑎 21 𝑎 22 𝑎 23 0

### 𝑎 31 𝑎 32 𝑎 33 0

### ]

```
3 × 4
```

If 𝜌(𝐴)=𝜌(𝐴/𝐵)=𝑛 (𝑖.𝑒 |𝐴|≠ 0 ); the system has a unique solution.

(Trivial solution; x = 0, y = 0, z = 0)

If 𝜌(𝐴)=𝜌(𝐴/𝐵)<𝑛(|𝐴|= 0 ); the system has infinitely many solutions (Non-trivial solution exists for the system).

**2 .14 Linear Combination of Vectors**

If 𝑥 1 ,𝑥 2 ,𝑥 3 ,......,𝑥𝑛 are 'n' rows vectors, then the combination 𝑘 1 𝑥 1 +𝑘 2 𝑥 2 +𝑘 3 𝑥 3 +.....+𝑘𝑛𝑥𝑛 is called a linear
combination of 𝑥 1 ,𝑥 2 ,....,𝑥𝑛(𝑘 1 ,𝑘 2 ,𝑘 3 ,.....𝑘𝑛 are scalars)

(1) The linear combination 𝑘 1 𝑥 1 +𝑘 2 𝑥 2 +𝑘 3 𝑥 3 +.....+𝑘𝑛𝑥𝑛is said to be linearly dependent if 𝑘 1 𝑥 1 +𝑘 2 𝑥 2 +
𝑘 3 𝑥 3 +.....+𝑘𝑛𝑥𝑛= 0 when 𝑘 1 ,𝑘 2 ,𝑘 3 ,.....,𝑘𝑛 (NOT All zeroes).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

If 𝑥 1 =[𝑎 1 𝑏 1 𝑐 1 ];𝑥 2 [𝑎 2 𝑏 2 𝑐 2 ];𝑥 3 =[𝑎 3 𝑏 3 𝑐 3 ], then the vectors 𝑥 1 ,𝑥 2 ,𝑥 3 are said to be linearly dependent if

```
|
```

### 𝑎 1 𝑏 1 𝑐 1

### 𝑎 2 𝑏 2 𝑐 2

### 𝑎 3 𝑏 3 𝑐 3

### |= 0.

(2) The combination 𝑘 1 𝑥 1 +𝑘 2 𝑥 2 +......+𝑘𝑛𝑥𝑛is said to be linearly independent if 𝑘 1 𝑥 1 +𝑘 2 𝑥 2 +........+𝑘𝑛𝑥𝑛= 0 when
𝑘 1 =𝑘 2 =𝑘 3 =.....𝑘𝑛= 0

**2 .14.1 Eigen Values and Eigen Vectors**

For any square Matrix 𝐴𝑛×𝑛, the equation |𝐴−𝜆𝐼|= 0 where '' is a scalar is called the characteristic equation.

The roots of the characteristic equation of a Matrix are called Eigen Values.

**2 .14.2 Properties of Eigen Values**

(i) If 𝜆 1 ,𝜆 2 ,𝜆 3 ,......,𝜆𝑛are 'n' Eigen Values of 𝐴𝑛×𝑛, then

(a) Sum of Eigen Values of 'A' = 𝜆 1 +𝜆 2 +𝜆 3 +....+𝜆𝑛=∑𝑛𝑖= 1 𝜆𝑖=𝑡𝑟𝑎𝑐𝑒(𝐴) = Sum of Principal diagonal elements

(b) Product of all the Eigen Values of 'A' = 𝜆 1 ⋅𝜆 2 ⋅𝜆 3 ⋅......𝜆𝑛=∏𝑛𝑖= 1 𝜆𝑖=|𝐴|

(c) Eigen Values of 𝐴𝑚 are 𝜆 1 𝑚,𝜆𝑚 2 ,𝜆 3 𝑚,......𝜆𝑚𝑛

(d) Eigen Values of adj(A) are |𝜆𝐴 1 |,|𝜆𝐴 2 |,|𝜆𝐴 3 |,......,|𝜆𝐴𝑛|

(e) Eigen Values of A & AT are the same.

(f) Eigen Values of 𝑘 1 𝐴+𝑘 2 𝐼 (Where 𝑘 1 and 𝑘 2 are scalar) are

```
𝑘 1 𝜆 1 +𝑘 2 ,𝑘 1 𝜆 2 +𝑘 2 ,𝑘 1 𝜆 3 +𝑘 2 ,𝑘 1 𝜆 4 +𝑘 2 ,........𝑘 1 𝜆𝑛+𝑘 2
```

(ii) '0' is always an Eigen Value of an odd-order Skew-Symmetric Matrix.

(iii) Eigen Values of a Real Symmetric Matrix are always real.

(iv) Eigen Values of the Skew-Symmetric Matrix are either zero (or) purely Imaginary.

(v) The Eigen values of an Orthogonal Matrix are of unit modulus.

(vi) If the sum of all the elements in a row (or Column) is constant (= k) for all the rows (or columns) in the matrix

```
respectively, then 'k' is an Eigen Value of the Matrix.
```

Example: If 𝐴=[

### 𝑎 1 𝑏 1 𝑐 1

### 𝑎 2 𝑏 2 𝑐 2

### 𝑎 3 𝑏 3 𝑐 3

```
] and if 𝑎 1 +𝑏 1 +𝑐 1 =𝑎 2 +𝑏 2 +𝑐 2 =𝑎 3 +𝑏 3 +𝑐 3 =𝑘,
```

then 'k' is an Eigen Value of 'A'.

(vii) The Eigen Values of an upper triangular Matrix, a lower triangular Matrix, a diagonal Matrix are the Principal diagonal

```
elements of the Matrix.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

 **Eigen Vector**

A non-zero column vector 𝑋𝑛× 1 is said to be an Eigen Vector of 𝐴𝑛×𝑛 corresponding to the Eigen Value '',
if 𝐴𝑋=𝜆𝑋(𝑋≠ 0 ).

**2 .15.1 Properties of Eigen Vectors**

(i) Eigen Vectors of A & AT are not the same.

(ii) Eigen Vectors of A & AM are same.

(iii) The Eigen Vectors of a Real Symmetric Matrix are always orthogonal.

(iv) The number of linearly independent Eigen Vectors of '𝐴𝑛×𝑛' is equal to the number of distinct Eigen Values of '𝐴𝑛×𝑛'.

**2 .15.2 Cayley Hamilton Theorem**

Every Matrix satisfies its characteristic equation.

This means that, if c 0  +  + + + =n c 1 −^1 ... cnn− 1 c 0 is the characteristic equation of a square matrix A of order n, then

```
c A 0 nn+c A 1 −^1 + +... cnn− 1 A c I+ = 0 ...(i)
```

Note: When 𝜆 is replaced by A in the characteristic equation, the constant term cn should be replaced by cnI to get the result

```
of the Cayley-Hamilton theorem, where I is the unit matrix of order n.
```

Also, 0 in the R.H.S. of (i) is a null matrix of order n.

**2 .16. Subspace (Basis of Dimensions)**

**2 .16.1 Vector**

An ordered n-tuple of numbers is called an n-vector.

**2 .16.2 Linearly Independent and Dependent Vector**

Let X 1 and X 2 be the non-zero vectors:

- {x 1 , x 2 , ...., xk} are linearly independent if r 1 x 1 + r 2 x 2 + ... + rk xk = 0 only for r 1 = r 2 = ... + rk = 0.
- The vectors x 1 , r 2 , ...., xk = are linearly dependent if they are not linearly independent; that is, if there exist scalars r 1 , r 2 ,
  ... , rk which are not all zero such that

r 1 x 1 + r 2 x 2 + .... + rk xk = 0

Note: Let X 1 , X 2 .......Xn be ‘n’ vector of matrix A.

- If rank (A) = number of vectors then vector X 1 , X 2 .....Xn are linearly independent.
- If rank (A) ≠ number of vectors then vector X 1 , X 2 ..... Xn are linearly dependent.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2 .16.3 Vector Space Rn**

If n positive integer, then an ordered n-tuple is a sequence of n real numbers (α 1 , α 2 ,.... αn). the set of all ordered n-tuples is
called n-space and is denoted by ℝn.

**2 .16.4 Subspaces of an N-vector space Vn**

A non-empty set S, of vectors of Vn(F) ,is called a subspace of Vn(F), if

- 𝜉 1 , 𝜉 2 are any two members of S, then ξ 1 + ξ 2 is also a member of S; and
- 𝜉 is a member of S, and k is a scalar then kξ is also a member of S.

Briefly, we may say that a set S of vectors Vn(F) is a subspace of Vn(F) it closed w.r.t. the compositions of “addition” and
"multiplication with scalars".

Every subspace of Vn contains the zero vector; being the product of any vector with the scalar zero.

**2 .16.5 Construction of Subspaces**

- A subspace Spanned by a Set of Vectors: A subspace that arises as a set of all linear combinations of any given set of

```
vectors is said to be spanned by the given set of vectors.
```

- Basis of a subspace: A set of vectors is said to be a basis of a subspace, if

```
➢ The subspace is spanned by the set, and
```

```
➢ The set is linearly independent.
```

Note: If we have N vectors and they are independent then they span N-dimension space. But if they are dependent then they
span only a subspace of N-dimension space.

**2 .16.6 Orthogonality of Vectors**

- Two vectors are orthogonal if each is non-zero and XX 12 T = 0
- If n vectors X 1 , X 2 .... Xn each of n dimensions is orthogonal then they are surely linearly independent and form the basis
  for n-dimension space.
- The set of the vector is orthonormal if they are orthogonal and have unit magnitude.

**2.17 Similar Matrices**

- Two matrix A and B are similar if there exist a non singular matrix P such that B = P–^1 AP
- Similar matrix has same eigen valves
- If A is similar to B then B is also similar to A
- If A is similar to B and B is similar to C then A is similar to C.

**2.18 Diagonalization of a matrix**

Finding a matrix D which is a diagonal matrix and which is similar to A is called diagonalization i.e., we wish to find a non-

singular matrix M such that A = M–^1 DM where D is a diagonal matrix.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**2.18.1 Condition for a Matrix to be Diagonalizable**

1. A necessary and sufficient condition for a matrix An × n to be diagonalizable is that the matrix must have n linearly

```
independent eigen vectors.
```

2. A sufficient (but not necessary) condition for a matrix An × n to be diagonalizable is that the matrix must have n linearly

```
independent eigen values.
```

This is because if a matrix has n linearly independent eigen values then it surely has n linearly independent eigen vectors

```
(although the converse of this is not true).
```

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

3

**PROBABILITY**

**AND STATISTICS**

**3 .1 Random Experiment**

The experiment in which the outcome is uncertain is called a Random Experiment (RE).

Example: Flipping a coin, rolling a pair of dice, Picking a ball from a bag.

**3 .1.1 Sample Space**

The set contains all the possible outcomes of a random experiment. It is denoted by 'S'.

If RE is flipping a coin, S = {Head, Tail}

If RE is rolling a dice, S = {1,2,3,4,5,6}

**3 .2 Event**

Any subset of sample space 'S' is called an Event.

Example: If RE is flipping a coin, then the occurring of a Head is an Event.

If RE is rolling a dice, then getting an odd number is an Event.

**3 .2.1 Probability of an Event**

If 'A' is any event with in the sample space 'S' of a Random experiment, then the probability of event 'A' is given by

( )

```
( )
( )
```

```
No. of outcomes favouring event 'A' to happen
Total number of elements in 'S'
```

```
nA
PA
nS
```

### ==

Probability of getting an Even Number when a dice is rolled.

P(Even Number) =^36 = 0. 5

S = {1,2,3,4,5,6},

A = {2,4,6}

Note: Probability can also be expressed as odds if favour and odds against an event:

- Odds is favour of an event:

Odds in favour of an event = Number of successes : Number of failures = m: (n – m).

- Odds against an event:

Odds against an event = Number of failures : Number of successes = (n – m) : m.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3 .2.2 Axioms Probability**

(i) If 'A' is any event with in the sample space 'S' of a RE, then 0 ≤𝑃(𝐴)≤ 1

```
0 n(A) n(S)
n(S) n(S) n(S)
```

```
 
```

### 0 ≤𝑃(𝐴)≤ 1

(ii) P(S) = 1
When a RE is conducted the experiment yields a possible outcome.

**3 .2.3 Types of Events**

(i) Mutually Exclusive Events:

If A, B are two events within a sample space 'S', then A & B are said to be mutually exclusive if A∩B = .
Example: If 'A' is the event of getting a prime number when a dice is rolled and 'B' is the event of getting a composite
number when a dice is rolled then
S = {1,2,3,4,5,6}, A = {2,3,5},B = {4,6}  A  B =   P(A  B) = 0

```
Fig. 5.1. Mutually exclusive event
```

(ii) Mutually Exhaustive Events:

If 'A', and 'B' are two events within a sample space 'S', then 'A' & 'B' are said to be mutually exhaustive if A  B = S
Example: If 'A' is the event of getting an odd number when a dice is rolled and 'B' is the event of getting an Even
Number, then
   = S
S = {1,2,3,4,5,6}
A = {1,3,5}, B ={2,4,6}
   B = S

```
Fig. 5.2. Mutually exhaustive event
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

(iii) Independent Events:

Two events 'A' & 'B' within the sample space 'S' (or) within two different sample spaces 'S 1 ' & 'S 2 ' are said to be independent
if P(  ) = P(A)  P(B).

```
Fig. 5.3. Independent Event
```

(iv) Impossible Event ():

The event with zero probability is called an Impossible Event P() = 0.

**3.3 Addition Theorem of Probability**

If A, and B are two events with a sample space 'S' of a Random Experiment, then
P(  ) = P(A) + P(B) – P(  )

n(A B) n(A) n(B) n(A B)
n(S) n(S) n(S) n(S)

### =+−

```
Fig. 5.4. Addition theorem
```

 P(A  B) = P(A) + P(B) – P(A  B)

When A, and B are mutually exclusive events, A  B = .

 P(A  B) = 0

P(  ) = P(A) + P(B)

- If E 1 , E 2 , E 3 ,.......En are mutually exclusive events (Ei  j = ), then P(E 1  E 2  E 3  .......  En ) = ∑𝑛𝑖= 1 𝑃(𝐸𝑖)

= P(E 1 ) + P(E 2 ) + P(E 3 ) + ...... p(En)

**3.3.1 De Morgan’s Law**

• (^) (A = B)C ACCB
• (^) (A = B)C ACCB

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3 .3.2 Union and Intersection properties**

For any two events A and B:

(a) P A(  =B) P A( )+P B( )− P A( B)

(b) P A( cc = − B ) 1 P A B( )

For any three events A, B and C:

(a) P A(   =B C) P A( )+P B( )+P C( )−  −  −  +  P A( B) P B C( ) P C( A) P A( B C)

(b) P A( c  = −  Bc Cc) 1 P A B C( )

**3 .3.3 Conditional Probability:**

The probability of the happening of event 'A' when it is known that event 'B' has already occurred is given by P(A/B)

```
𝑃(𝐴/𝐵)=
```

### 𝑃(𝐴∩𝐵)

### 𝑃(𝐵)

### =

### 𝑛(𝐴∩𝐵)

### 𝑛(𝐵)

**3.3.4 Joint Probability:**

➢ f(x, y) is the joint probability of two RV’S x, y.
➢ If the two RV are Independent then
f(x, y) = f(x) ⋅ f(y)

➢ ( , ) ( , )

```
bd
```

```
ac
```

P a x b c    =y d f x y dydx

➢ f x( ) f x y dy( , )

```

```

```
−
```

=

➢ f y( ) f x y dx( , )

```

```

```
−
```

=

**3.3.5 Multiplication Theorem of Probability:**

If A, and B are two events within a sample space 'S', then P(A/B)  P(B) = P(B/A)  P(A)

P(A/B) = 𝑃(𝑃𝐴(∩𝐵𝐵))⇒𝑃(𝐴∩𝐵)=𝑃(𝐴/𝐵)⋅𝑃(𝐵)→( 1 )

P(B/A) = 𝑃(𝑃𝐵(∩𝐴𝐴))⇒𝑃(𝐵∩𝐴)=𝑃(𝐵/𝐴)⋅𝑃(𝐴)→( 2 )

From (1) & (2)
𝑃(𝐴/𝐵)⋅𝑃(𝐵)=𝑃(𝐵/𝐴)⋅𝑃(𝐴)

**3.3.6 Total Theorem of Probability:**

If E 1 , E 2 , E 3 ,......En are 'n' mutually exclusive (𝐸𝑖∩𝐸𝑗=𝜙;∀𝑖≠𝑗) and collectively exhaustive event (E 1  E 2  E 3

```
 ......  En = S) and 'A' is any event with in the sample space 'S', then
```

𝑃(𝐴)=𝑃(𝐸 1 )⋅𝑃(𝐴/𝐸 1 )+𝑃(𝐸 2 )⋅𝑃(𝐴/𝐸 2 )+......+𝑃(𝐸𝑛)⋅𝑃(𝐴/𝐸𝑛)

```
1
```

```
( ) ( ) ( / )
```

```
n
ii
i
```

```
P A P E P A E
=
```

=

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3.3.7 Baye's Theorem**

If E 1 ,E 2 ,E 3 ,......En are mutually exclusive (𝐸𝑖∩𝐸𝑗=𝜙∀𝑖≠𝑗) and collectively exhaustive event (𝐸 1 ∪𝐸 2 ∪𝐸 3 ∪.......∪
𝐸𝑛=𝑆) and 'A' is any event with in the sample space 'S', then

### 𝑃(𝐸𝑖/𝐴)=

### 𝑃(𝐸𝑖)⋅𝑃(𝐴/𝐸𝑖)

### ∑𝑛𝑖= 1 𝑃(𝐸𝑖)⋅𝑃(𝐴/𝐸𝑖)^

```
Fig. 5.5. Baye’s theorem
```

**3 .3.8 Use of permutation and combination**

What is combination?

A combination of ‘n’ objects taken ‘r’ at a time (r-combination of ‘n’ objects is an unordered selection of ‘r’ of the objects).

Number of ways of combining of ‘r’ object out of ‘n’ objects without repetition

!
r ( )!!
C n
n r r

###  =

### −

What is permutation?

A combination of ‘n’ objects taken ‘r’ at a time (r-combination of ‘n’ objects is an ordered selection of ‘r’ of the objects).

Number of ways of selection of r object out of n objects without repetition

!
r ( )!
P n
nr

###  =

### −

Result:

(i) nnCCr= n r−

(ii) nC 0 + + + + =nC 1 nC 2 .... nCn^2 n

(iii) nC 024 + + + +=nC nC .... 2 n−^1

(iv) nC 1 + + + +=nC 3 nC 5 .... 2 n−^1

(v) 0.nC 0 +1.nC 1 +2.nC 2 + +.... n C.n n=n.2n−^1

Permutations with Repetition

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

The number of permutations of n objects, where p objects are of one kind, q objects are of another kind and the rest, if any, are

of a different kind is
!!

```
n
Pr
pq
```

### .

Combination with Repetition

Number of combinations of ‘n’ distinct things taking ‘r’ at a time when each thing may be repeated any number of times is

given bynr−+^1 Cr.

**3.4 STATISTICS**

Statistics → Collection and Analysis of Data

**3.4.1 Analysis of Ungrouped Data**

If x 1 , x 2 , x 3 , .......,xn are 'n' observations, then

(1) The range of the data = R = max{x 1 , x 2 , .......,xn} – min{x 1 , x 2 , x 3 , ....., xn}

(2) Arithmetic mean : Mean of the data is equal to sum of observaions divided by the total number of observations.

### 𝑥̄(𝑜𝑟)𝜇=

### 𝑥 1 +𝑥 2 +......+𝑥𝑛

### 𝑛

### =

### ∑𝑛𝑖= 1 𝑥𝑖

### 𝑛

### =𝑥̄=𝜇

- The mean of 1st 'n' natural numbers =

```
(𝑛(𝑛 2 +^1 ))
𝑛 =
```

```
𝑛+ 1
2
```

- The mean of 1st 'n' odd numbers = 𝑛

```
2
𝑛 =𝑛^
```

- The mean of 1st 'n' even numbers = n +1

**3 .4.2 Median**

The middle most observation of the data (𝑥 1 ,𝑥 2 ,𝑥 3 ,.....𝑥𝑛) When the data is arranged in either ascending or descending order.

If 𝑥 1 ,𝑥 2 ,𝑥 3 ,𝑥 4 ,.......𝑥𝑛 are 'n' observations that are arranged in ascending/descending order then

(i) Median of the Data = (𝑛+ 21 )

```
𝑡 ℎ
observation, if 'n' is odd.
```

(ii) Median of the Data = Mean of (𝑛 2 )

```
𝑡 ℎ
&(𝑛 2 + 1 )
```

```
𝑡 ℎ
observations, if 'n' is even.
```

**3 .4.3 Mode**

The observation with highest frequency is called mode.

Any Data with two Modes is called → Bimodel Data

If 𝑥 1 ,𝑥 2 ,𝑥 3 ,......,𝑥𝑛 are 'n' data points, 𝑥̄=𝜇=𝑥^1 +𝑥^2 +𝑛.......+𝑥𝑛

Mean Deviation of the observation (𝑥𝑖)=𝑑𝑖=𝑥𝑖−𝑥̄

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

```
Fig. 5.6. Discrete data
```

Sum of derivations of all the observations = 𝛴𝑑𝑖=(𝑥 1 −𝑥̄)+(𝑥 2 −𝑥̄)+...... 0 +(𝑥𝑛−𝑥̄)
=𝛴𝑑𝑖=(𝑥 1 +𝑥 2 +.....+𝑥𝑛)−𝑛𝑥̄
𝛴𝑑𝑖= 0

The sum of mean deviations of all the observations is equal to zero.

**3 .4.4 Absolute Mean Deviation**

If x 1 , x 2 , x 3 ,.......,xn are 'n' data points with Mean = 𝑥̄, then the absolute mean deviation of 𝑥𝑖 about 𝑥̄ is given by |𝑑𝑖|=|𝑥−𝑥̄|
The sum of absolute mean derivations of given data is not zero.
(𝛴|𝑑𝑖|≠ 0 )⇒(|𝑥 1 −𝑥̄|+|𝑥 2 −𝑥̄|+........+|𝑥𝑛−𝑥̄|≠ 0 )

**3 .4.5 Standard Deviation**

If x 1 , x 2 , x 3 ,......,xn ('n' is very large), then the standard deviation of the data is given by

Population Standard Deviation 𝜎=√^1 𝑛𝛴(𝑥𝑖−𝑥̄)^2 , n → size of population

Sample Standard derivation: 𝜎=√(𝑛−^11 )𝛴(𝑥𝑖−𝑥̄)^2 , n→ size of sample

Generally (n > 29 → population) (n < 29 →sample)

Note: Measures of skewness (The degree of asymmetry)

A lack of symmetry is skewness.

- For symmetric distribution mean (M) = Median (Md) = Mode (Me)
- For negatively skewed distribution mean (M) < Median (Md) < Mode (Me)
- For positively skewed distribution Mean (M) > Median (Md) > Mode Me).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3 .5 Random Variables**

The variable that connects the outcome of a Random Experiment to a real number.

Example: 'x' is the value of the number that a dice shows when it is rolled.

Discrete RV → The RV whose value is obtained by counting, defined by PMF

Random Variable

Continuous RV → The RV whose value is obtained by Measuring, defined by PDF

- If a data consists of 'f 1 ' data points with value ′𝑥 1 ′,′𝑓 2 ′ data points with value ′𝑥 2 ′......′𝑓𝑛′ data point with value _′_ 𝑥𝑛 _′_ , then

(i) Expectation of 'x' =𝐸(𝑥)=∑𝑛𝑖= 1 𝑥𝑖𝑃(𝑥=𝑥𝑖)

```
(ii) Variance of ‘x’ = 𝜎^2 =𝐸(𝑥^2 )−(𝐸(𝑥))^2 and σ is the standard deviation.
```

**3 .5.1 Probability Mass Function (PMF)**

The PMF p(x) of a discrete random variable X taking values x x 12 , ,.....xn is defined such that,

(i) px( ) 0i 

(ii)
1

### ( ) 1

```
n
i
i
```

```
px
=
```

 =^

(iii) p x( )ii==p X( x)

**3 .5.2 Probability Density Function (PDF)**

The pdf f(x) of a continuous random variable X is defined such that,
(i) fx( ) 0

(ii) f x dx( ) 1

```

```

```
−
```

 =^

(iii) ( ) ( )

```
b
```

```
a
```

P a X b  =f x dx^

**3 .5.3 Expected Value**

1. Expected value of a random variable X, E [X], is defined as,  

```
( ); X is discrete rv
```

```
( ) ; X is continuous rv
```

```
xp x
EX
xf x dx
```

```

```

```
−
```

### 

### 

### 

### 

### 





2. Expected value of X^2 is,
   2
   2
   2

```
( ); X is discrete rv
[]
( ) ; X is continuous rv
```

```
x p x
EX
x f x dx
```

```

```

```
−
```

### 

### 

### =

### 

### 





Note: EX[]n is called nth moment.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3 .5.4 Mean of Random Variable ‘X’**

Mean = =EX[]

**3 .5.5 Variance of a Random Variable ‘X’**

Var ( )X =E X[( −) ]^2

Or, Var ( )X =E X[^22 ]−

**3 .5.6 Properties of Expectation**

(i) E[c] = c, c is a constant.

(ii) E[ax] = aE[X]

(iii) E(aX + b) = aE(X) + b

(iv) If X and Y are random variable E[X  Y] = E(x)  E(Y).

(v) If X and Y are random variables E(X. Y) = E(X). E(Y / X).

(vi) If X and Y independent random variables E(X. Y) = E(X). E (Y).

**3 .5.7 Properties of Variance**

(i) Var[C] = 0, C is constant.

(ii) Var (aX) = a^2 V(X) where X is random variable and ‘a’ constant.

Var(–X) = (–1)^2 Var(X) = Var(X) Variance is always positive.

(iii) Var(ax + b) = a^2 Var(X) + 0

(iv) If X and Y are independent random variables.

Var(X + Y) = Var(X) + Var(Y)

Var(X – Y) = Var(X) + Var(Y)

(v) Var(ax + by) = a^2 v(x) + b^2 v(y) + 2ab Cov (x, y)

(vi) Cov (x, y) = E(x, y) – E(x) E(y)

(vii) For independent random variables Cov(x, y) = 0

**3 .5.8 Continuous RV**

The value of the Random Variable is obtained by Measuring.

**3.6 Probability Distribution Function (PDF)**

A continuous & differentiable function P(x) is said to be a probability distribution/density function of a continuous random

variable 'x' if 𝑃(𝑎≤𝑥≤𝑏)=∫𝑎𝑏𝑃(𝑥)𝑑𝑥

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

**3 .6.1 Mean (or) Expectation**

If P(x) is a probability distribution/density function of a continuous Random Variable 'x' then the Mean of 'x' = E(x) = ∫− _∞∞_ 𝑥⋅

𝑃(𝑥)𝑑𝑥

**3 .6.2 Median**

The value of 'x' for which the total probability is exactly divided into two equal halves is called Median.

**3 .6.3 Mode**

The valueof 'x' at which P(x) is maximum is called mode.

**3 .6.4 Variance**

= 𝜎^2 =𝐸(𝑥^2 )−(𝐸(𝑥))^2

```
( ) ( ( ) )
22 2
x P x dx x P x dx
```

```

 = −  − − 
```

```
Fig. 5.7. Continuous random variables
```

**3.7 Continous RV distributions**

(1) Gaussian/Normal Distributon:

If 'x' is a continuous Random variable with mean '' and standard deviation '', then the probability distribution/density
function of normally distributed variable 'x' is given by

```
Fig. 5.8. Normal distribution
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

```
Mean = Median = Mode = 
𝑃(𝜇−𝜎≤𝑥≤𝜇+𝜎)= 0. 6828
𝑃(𝜇− 2 𝜎≤𝑥≤𝜇+ 2 𝜎)= 0. 9544
𝑃(𝜇− 3 𝜎≤𝑥≤𝜇+ 3 𝜎)= 0. 9973
𝑃(𝑥)=
```

### 1

### 𝜎⋅√ 2 𝜋

### .𝑒

```
−(𝑥−𝜇)^2
2 𝜎^2
```

(2) Standard Normal Distribution:

Assuming 𝑧=𝑥−𝜎𝜇;𝜇= 0 ;𝜎= 1 , 𝑃(𝑧)=√^12 𝜋⋅𝑒

```
−𝑧^2
```

(^2)
𝑃(− 1 ≤𝑧≤ 1 )= 0. 6828
𝑃(− 2 ≤𝑧≤ 2 )= 0. 9544
𝑃(− 3 ≤𝑧≤ 3 )= 0. 9973
Note:

1. The normal distribution curve is bell shaped curve
2. The points of infelection of the normal distribution curve are at 𝑥=𝜇+𝜎 𝑎𝑛𝑑 𝑥=𝜇−𝜎.
3. The cumulative function graph is of ‘S’ Shape.
4. For a given normal distribution, Mean = median = Mode

(3) Uniform Distribution:

If 'x' is a uniformly distrbuted random variable such that 𝑎≤𝑥≤𝑏 then the Pdf is given by

```
𝑃(𝑥)=
```

### 1

### (𝑏−𝑎)

Mean = ∫𝑎𝑏𝑥⋅𝑃(𝑥)𝑑𝑥=∫𝑎𝑏𝑥⋅𝑏−^1 𝑎𝑑𝑥=(𝑏^1 −𝑎)∫𝑎𝑏𝑥⋅𝑑𝑥

```
Mean
2
```

```
ba+ =
^
```

 𝑉𝑎𝑟𝑖𝑎𝑛𝑐𝑒=𝜎^2 =(𝑏−𝑎)

2
12
Std. deviation = 𝜎=(𝑏√− 12 𝑎)

```
Fig. 5.9. Uniform Distribution
```

**3 .7.1 Properties of Mean and Variance:**

𝐸(𝑎𝑥+𝑏𝑦)=𝑎⋅𝐸(𝑥)+𝑏⋅𝐸(𝑦)

```
𝑉(𝑎𝑥+𝑏𝑦)=𝑎^2 ⋅𝑉(𝑥)+𝑏^2 ⋅𝑉(𝑦)− 2 𝑎𝑏𝐶𝑂𝑉(𝑥,𝑦)
```

where 𝐶𝑂𝑉(𝑥,𝑦)=𝐸(𝑥𝑦)−𝐸(𝑥)⋅𝐸(𝑦)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Engineering Mathematics
Engineering Mathematics
```

If x,y are indpendent random variables, then 𝐸(𝑥𝑦)=𝐸(𝑥)⋅𝐸(𝑦)⇒𝐶𝑂𝑉(𝑥,𝑦)= 0

(1) Exponential Dirtibution:

If 'x' is a continous random variable with mean as^1 𝜆 then the exponential distribution of 'x' is

```
given by the function
```

𝑓(𝑥)={𝜆⋅𝑒

### −𝜆𝑥 ;𝑥≥ 0

### 0 :𝑜𝑡 ℎ 𝑒𝑟𝑤𝑖𝑠𝑒

Mean =^1 𝜆

𝜎^2 =𝜆^12

Mean = Standard Deviation =^1 𝜆

**3.8 Discrete Random Variable Distributions**

If a Random experiment has only two Possible outcomes, (one is Success & other is failure) and the Probability of Success
doesn't depend on time, then the probability of occuring of exactly 'r-successes' in 'n-trials' is given by
𝑃(𝑋=𝑟)=𝑛𝐶𝑟⋅𝑃𝑟⋅𝑞𝑛−𝑟
Where, P → Probability of Success,
q → Probability of Failure
p + q = 1

Mean = np,Variance = npq = ^2 , standard deviation = = npq

**3 .8.1 Poisson Distribution**

If a random experiment has only two possible outcomes, and the average number of successes in a given time 't' is , then the

probability that exactly 'r' successes occur within the same time 't' given by

𝑃(𝑥=𝑟)𝑒

```
−𝜆⋅𝜆𝑟
𝑟!^
```

Mean = .

Mean = Variance = 𝜆

⇒ 𝜎=√𝜆

```
❑❑❑
```

```
Fig. 5.10. Exponential distribution
```

**Discrete Discrete Discrete**

**MathematicsMathematicsMathematics**

```
Design Against Static Load
```

1. Graph Theory ....................................................................................................................... 2 .1 – 2 .1 0
2. Logic Handbook ................................................................................................................... 2 .1 1 – 2. 17
3. Set Theory ........................................................................................................................... 2. 18 – 2. 35
4. Combinatorics ..................................................................................................................... 2. 36 – 2. 40

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**GRAPH THEORY**

**1.1 Basics of Graphs:**

The number of vertices of odd degree in a graph is always even.

Every graph has an even number of odd vertices.

- Based on Parallel edges & self-loops graphs are classified into 3 types
  Parallel graph Self-loops
  Simple graph × ×
  Multi graph ✓^ ×
  Pseudograph ✓^ ✓^

(We mainly discuss simple graph in our syllabus)

**1.1.1 Theorem1:**

Maximum degree of a vertex, in a simple graph with n vertices, is  n – 1.

Note:

Hand Shaking Lemma: Sum of all degrees = 2  sum of all edges.

**1.1.2 Theorem2 :**

Maximum no. of edges, in a simple graph with n vertices, is  2 (^1 )
c 2

```
nn
n
```

### −

### =^

Note: No of different graphs possible with n distinct vertices is

### (^1 )

```
2 2
```

```
nn−
=
```

No. of different graphs possible with n distinct vertices and ‘e’ edges is ( )

### 1

### 2

###  − 

### 

```
Ce
```

```
nn
```

**1.1.3 Degree sequence:**

If the degrees of a graph are written in increasing order or decreasing order, we call it a degree sequence

- Not all degree sequence forms simple graph.
- The degree sequence which forms simple graph is called graphical

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**1.1.4 Theorem 3 :**

In a simple graph at least two vertices with have same degree (n  2 )
Example: {5, 4, 3, 2, 1} is not graphical

**1.1.5 Theorem 4 :**

Max degrees in a given graph G is denoted as (G) & Min degree is denoted as (G)

```
(G) 2e (G) n 1
n
```

###      −

**1.1.6 Complete Graph (kn) (n**  **1):**

Degree of every vertex is n – 1
(or)
There direct edge b/w every pair of vertices

- no. of edges is,

( )

```
n n 1
e
2
```

### −

### =

**1.1.7 Regular Graph:**

A graph in which degree of all vertices is same is called a regular graph.
n.(G) = 2e = n.(G)

**1.1.8 Cycle Graph (Cn) (n**  **3):**

If given degree sequence is all 2’s, then it’s not guaranteed that it’s a cycle graph
G: [2, 2, 2, 2, 2, 2]

```
k 1
k 2
k 3
```

```
C 3 C 4 C 5
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

Degree of all vertices is 2 in a cycle graph

- Every Cn is a regular graph
- Number of Edges = n = Number of Vertex

**1.1.9 Wheel Graph (wn) (n**  **4):**

A wheel graph wn is obtained by adding a vertex (hub) to cn – 1 (Cycle Graph) such that this vertex is adjacent to all the other
vertices.

Number of edges = 2 (n - 1)

**1.1.10 Line Graph (L(G)):**

Consider below graph, G

Step to construct L(G)
(i) define edges in G
(ii) label these edges as vertices in L(G)
(iii) Connect vertices with common number.

Line graph of every cycle graph is also a cycle.

C 3 W 4 C 4

### 1

### 2

### 3

### 4

### 5

### (12)

### (13)

### (23)

### (34)

### (35)

### (45)

```
34
```

```
35
```

```
23 45
```

```
12
```

```
13
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**1.1.11 Bipartite (L(G)):**

Note: Bi – partite graphs do not contain odd length cycle.

**1.1.12 Complete bipartite graph (km,n) :**

Each vertex in set v 1 is adjacent to all vertices in set v 2.
Example:

K 2 , 4 |v 1 | = m
| v 2 | = n

In km, n number of vertices = m + n
number of edges = mn
(km, n) = max (m, n), ( km, n) = min (m, n)

**1.1.13 Theorem 5 :**

- Maximum no. of edges passible is bipartite graph of n vertices is 
  n^2
  4

```



```

```
A
```

```
B
```

```
D C
```

```
E
```

```
A B
```

```
C D
```

```
A
```

```
B C
```

```
A B
```

```
D C
```

```
A B
```

```
C D
```

```
A B
```

V 1  V 2 V 1  V 2

```
C 4 is a bipartite graph Now adding E in either of the
sets violates the property of
bipartite graph
C 5 is not a bipartite graph
```

```
adding C is not possible
C 3 is not a bipartite graph
```

```
V 1 V 2
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**1.1.14 Star graph (k 1 ,n- 1 ) :**

It is complete bipartite graph with one vertex in one set and rest of the vertices in other set.
(or)
Star graph (k 1 , kn- 1 ) is complete bipartite graph possible with n vertices and minimum no. of edges.

Eg: Star graph of 5 vertices, k 1 , 4 is
total no of edges in k1, n- 1 = n - 1
 (k1, n – 1 ) = n - 1,  (k1, n- 1 ) = 1

**1.1.15 Complement graph** (G) **:**

For a graph G, complement of G(G) is the graph which contains all the vertices present in G and does not contain the edges

present in G.

( ) ( )

```
( )
n
```

```
n n 1
G G k e G e G
2
```

### −

###  + =  + =

If the degree of vertex v is x in graph G, then the degree of vertex v in G is [(n-1)-x]
If d 1 , d 2 ......... dn is degree sequence for G then
(n- 1 - d 1 ), (n1-d 2 ), ..... (n- 1 - dn) is degree sequence of G
Example:
consider a graph of degree sequence {5, 2, 2, 2, 2, 1}.
What is the degree sequence of complement graph?
Total vertices, n = 6

 

```
k 6 5, 5, 5, 5, 5, 5
G 5, 2, 2, 2, 2, 1
G 0, 3, 3, 3, 3, 4
```

### →

### →

### →

Isomorphic Graphs:
Let G 1 = (V 1 , E 1 ) and G 2 = (V 2 , E 2 ) be two undirected graphs. A function f: V 1 → V 2 is called a graph isomorphism if (a) f
is one-to-one and onto, and (b) for all a, b  V 1. {a, b}  E 1 if and only if {f(a), f(b)} E 2. When such a function exists, G 1
and G 2 are called isomorphic graphs.

```
(or)
```

```
3
```

```
1 2
```

(^43)
1 2
4
G G

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

(ii) Self-complement: (GG )

It is a graph which is isomorphic to-its own complement.
i.e., GG=

It is clear that above two graphs are self-complement to each other.
w.r.t

(^) e G( ) e G( ) n n 1( )
2

### −

### +=^

Let e be no. of edges in G

( )

```
n n 1
e te
2
```

### −

### =

• (^) e n n 1( )
4

### −

```
=^ i.e., no. of edges in a self-complement^ graph^
Complement of star graph k1, n- 1 gives one isolated vertex and a complete graph kn- 1
n must be congruent to 0 or 1 mod 4.
```

Hypercube (Qn):
Q 1
2’ vertices – 0, 1
Q 2
4 ’ vertices – 00, 01, 10, 11

Every cycle in hypercube B of even length (think why). So, every hypercube is bipartite graph
Q 3 : 23 vertices

Number of edges =
n2n n1
n2
2

```
 =−
```

```
G G
```

```
01
```

```
10 11
```

```
00
```

```
001
```

```
010
```

```
111
```

```
101
```

(^100000)
511
40

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**1.2 Connectivity**

```
Name Repeated Vertex
(Vertices)
```

```
Repeated Edge(s) Open Closed
```

```
Walk (open) Yes Yes Yes
Walk (closed) Yes Yes Yes
Trail Yes No Yes
Circuit Yes No Yes
Path No No Yes
Cycle No No Yes
```

**1.2.1 Connected graph:**

For every two pair of vertices, there must exist a path between them.

**1.2.2 Disconnected graph:**

If we can find at least one pair of vertices, such that there is no path available b/w these 2 verities, then the graph is said to be
disconnected graph.

- If G is connected then G may be connected or disconnected

Disconnected graph

```
G G G G
Connected Connected Connected disconnected
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**1.2.3 Theorem 6 :**

If G is disconnected, then Gis connected.
Example:

**1.2.4 Range of edges for a connected graph (k=1):**

(k is connected components)
Tree

- Minimum no of edges required to get a possibility to make graph connected with in vertices is n-1.

```
( )
Tree
```

```
n n 1
(n 1) e
2
```

### −

### −  

- The connected graph with n-1 edges is doesn’t have a cycle.
- This graph is known as minimally connected graph.
- In this kind of graph, these will be a unique path b/w any two pair of vertices.
- This kind of graph is called a tree (a connected graph with no cycles)

**1.2.5 Range of edges for a disconnected graph:**

- Edges range b/w

```
n k e (n k n k 1)( )
2
```

### − − +

### −  

Proof:
Here lets say we have k components with n 1 , n 2 ...... nk components
 n 1 + n 2 + ........ + n 2 : k
For min no. of edge, each compared must be minimally connected.
 min no of edges is
N 1 – 1 + n 2 – 1 + ...... + nk – 1
= (n 1 + n 2 + ..... nk) – k = n – k

Note:

1. Let G be a graph of order n. If
   deg u + deg v  n – 1
   nonadjacent vertices u and v of G, then G is connected and diam(G)  2.
2. If G is a graph of order n with (G)  (n – 1)/2, then G is connected.
3. A directed graph is strong connected if there is a path from a to b and from b to a whenever a and b are vertices in the
   graph.
   4.A directed graph is weakly connected if there is a path between every two vertices in the underlying undirected graph.
4. k(G)  (G)  minvv deg(v).

G G

G G

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

6. Simple graph G with n vertices is connected if it has more than (n - 1) (n - 2)/2 edges.
7. Let G = (V, E) be a loop-free graph with n (2) vertices. If deg(v)  (n - 1)/2 for all v  V, then G has a Hamilton path.
8. If G = (V, E) is a loop-free undirected graph with

```
n1
V n 3, and if E 2 2,
```

```
−
=  +

```

```
then G has a Hamilton cycle.
```

9. If G = (V, E) is a loop-free undirected graph with V n 3, and deg v=  ( )n / 2 for all   V, then G has a Hamilton cycle.

( 10 ) If G 1 , G 2 are (loop-free) undirected graphs, G 1 , G 2 are isomorphic if and only if G , G 12 are isomorphic.

(11) If G is an undirected graph or multigraph with no isolated vertices, then we can construct an Euler trail in G if and only
if G is connected and has exactly two vertices of odd degree.

(12) k G( )    −(G) (G) (G) n 1

**1.3 Planarity**

A graph (or multigraph) G is called planar if G can be drawn in the plane with its edges intersecting only at vertices of G. Such
a drawing of G is called an embedding of G in the plane.

Kuratowski’s Theorem. A graph is nonplanar if and only if it contains s subgraph that is homomorphic to either K 5 or K3.3.

Let G = (V, E) be a connected planar graph or multigraph with |V| =  and |E| = e. Let r be the number of regions in the plane
determined by a planar embedding (or, depiction) of G; one of these regions has infinite area and is called the infinite region.
Then  – e + r = 2.
Let G = (V, E) be a loop-free connected planar graph with |V| = , |E| = e > 2, and r regions. Then 3r  2e and e  3  – 6.

**1.3.1 Coloring:**

Note: Every MIS will always be MDS. But reverse need not to be true

Domination number  Independence number.

(G) =  (G

**1.3.2 Theorem 7 :**

Sum of size of minimum vertex cover and size of maximum independent set is equal to number of vertices

**1.4 Covering:**

It is set of edges such that all vertices should incident on at least one edge.

1

6 5

2 3

4

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

### ,

Set of all edge is also a covering set

- It is also known as edge covering set.

**1.4.1 Minimal Covering set:**

It is a covering set from which we can’t remove new elements(edge).
{16, 12, 53, 54}. {16, 54, 23} are MCS

**1.4.2 Covering Number (C(G)):**

It is no of edges present smallest covering set.
For above graph C(G) = 3

**1.5 Perfect Matching:**

A matching is said to be prefect matching if every vertex in the graph is matched
(or)
Induced degree of all the vertices is 1.

**1.5.1 Induced degree:**

The degree of a vertex in a matching is called indeed degree

Example:

{12, 45, 36} is perfect matching

Note: Every perfect matching is maximal, but reverse need not to be true.
If prefect matching exists, then no. of vertices will always be even but reverse need not to be true.

A graph may contain more than one perfect matching.

Total no. of prefect matching possible for a complete graph with 2n vertices is (n )

```
2n!
2 .n!
❑❑❑
```

```
1
```

```
2 3
```

```
4 5
```

```
6
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

2

**LOGIC HANDBOOK**

**2.1 Introduction**

```
p p
```

```
T
F
```

### F

### T

```
p q p  q
```

```
T
T
F
F
```

### T

### F

### T

### F

### T

### F

### F

### F

Let p and q be propositions. The conditional statement p → q is the proposition “if p, then q.”

The conditional statement p → q is false when p is true and q is false, and true otherwise. In the conditional statement

p → q, p is called the hypothesis (or antecedent or premise) and q is called the conclusion (or consequence).

“if p, then q” “p implies q”

“if p, q” “p only if q”

“p is sufficient for q” “a sufficient condition for q is p”

“q if p” “q whenever p”

“q when p” “q is necessary for p”

“a necessary condition for p is q” “q follows from p”

“q unless p” “q provided that p”

p q (^) p  q
T
T
F
F

### T

### F

### T

### F

### T

### T

### T

### F

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

```
Let p and q be propositions. The biconditional statement p  q is the proposition “p if and only if q”. The biconditional
statement p  q is true when p and q have the same truth values, and is false otherwise. Biconditional statements are also
called bi-implications.
```

```
Operator Precedence
 1


```

### 2

### 3

### →

### 

### 4

### 5

```
A compound proposition that is always true, no matter what the truth values of the propositional variables that occur in it,
is called a tautology. A compound proposition that is always false is called a contradiction. A compound proposition that
is neither a tautology nor a contradiction is called contingency.
→ Every contingency is satisfiable, but reverse need not to be true 1.
→ Every tautology is satisfiable, but revers need not to be true.
For any primitive statements p, q, r, any tautology ‘T’ and any contradiction ‘F’.
(1)   p  p Law of Double Negation
(2)  (p  q)   p   q DeMorgan’s Laws
 (p  q)   p   q
(3) p  q  q  p Commutative Laws
p  q  q  p
(4) p  (q  r)  (p  q)  r Associative Laws
```

p  (q  r)  (p  q)  r

(5) p  (q  r)  (p  q)  (p  r) Distributive Laws

p  (q  r)  (p  q)  (p  r)

(6) p  p  p Idempotent Laws

```
p q p → q
```

```
T
T
F
F
```

### T

### F

### T

### F

### T

### F

### T

### T

```
p q p  q
```

```
T
T
F
F
```

### T

### F

### T

### F

### T

### F

### F

### T

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

p  p  p

(7) p  F  p Identity Laws

p  T  p

(8) p   p  T Inverse Laws

p   p  F

(9)^ p^ ^ T^ ^ T^ Domination Laws^

p  F  F

(10)p  (p  q)  p Absorption Laws

p  (p  q)  p

```
Rule of Inference Related Logical Implications Name of Rule
```

### 1) →

### 

```
p
pq
q
```

### 2)

### →

### →

### →

```
pq
qr
pr
```

### 3)

### →

### 

### 

```
pq
q
p
```

```
[p  (p → q)] → q
```

```
[(p → q)  (q → r)] → (p → r)
```

```
[(p → q)  q] →  p
```

```
Rule of Detachment (Modus Ponens)
```

```
Law of the syllogism
```

```
Modus Tollens
```

```
p → q   p  q
p → q   q →  p
p  q   p →  q
p  q   (p →  q)
 (p → q)  p   q
(p → q)  (p → r)  p → (q  r)
(p → r)  (q → r)  (p  q) → r
(p → q)  (p → r)  p → (q  r)
(p → r)  (q → r)  (p  q) → r
p  q  (p → q)  (q → p)
p  q   p   q
p  q  (p  q)  ( p   q)
 (p  q)  p   q
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

### 4)

### 

```
p
q
pq
```

### 5)

### 

### 

### 

```
pq
p
q
```

```
6) pF
p
```

### →

### 

### 7) 

### 

```
pq
p
```

```
8)

```

```
p
pq
```

### 9) ()

### 

### →→

### 

```
pq
p q r
r
```

### 10)

### ()

### →

### →

###   →

```
pq
qr
p q r
```

### 11)

### →

### →

### 

### 

```
pq
rs
pr
qs
```

### 12)

### →

### →

###   

###   

```
pq
rs
qs
pr
```

```
[(p  q)   p] → q
```

```
( p → F 0 ) → p
```

```
(p  q) → p
```

```
p → p  q
```

```
[(p  q)  [p → (q → r)]] → r
```

```
[(p → r)  (q → r)] → [(p  q) →r]
```

```
[(p → q)  (r → s)  (p  r)] → (q  s)
```

```
[(p → q)  (r → s)  (q  s)]→( p  r)
```

```
Rules of Conjunction
```

```
Rule of Disjunctive Syllogism
```

```
Rule of Contradiction
```

```
Rule of Conjunctive simplification
```

```
Rule of Disjunctive Amplification
```

```
Rule of Conditional Proof
```

```
Rule for Proof by Cases
```

```
Rule of the Constructive Dilemma
```

```
Rule of the Destructive Dilemma
```

```
x p(x)
```

```
For some (at least one) a in
the universe, p(a) is true.
```

```
For every a in the universe,
p(a) is false.
```

```
x p(x)
```

```
For every replacement a from
The universe, p(a) is true.
```

```
There is at least one replacement a from
the universe for which p(a) is false.
```

```
x  p(x)
```

```
For at least one choice a in
The universe, p(a) is false, so
Its negation p(a) is true.
```

```
For every replacement a in the universe,
p(a) is true.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

```
x  p(x)
```

```
For every replacement a from
The universe, p(a) is false and its
negation p(a) is true
```

```
There is at least one replacement a from
the universe for which p(a) is false and
p(a) is true.
```

```
Statement When True? When False?
```

```
xyP(x, y)
yxP(x, y)
```

```
P(x, y) is true for every pair x, y There is a pair x, y for which
P(x, y) is false.
```

```
xyP(x, y) For every x^ there is a y^ for which P(x, y) is
true
```

```
There is an x such that
P(x, y) is false for every y.
xyP(x, y) There is an x^ for which P(x, y) is true for
every y.
```

```
For every x there is a y for
which P(x, y) is false.
```

```
x [P(x)  Q(x)]  x P(x)  x Q(x)
x [P(x)  Q(x)]  x P(x)  x Q(x)
x [P(x)  Q(x)] → x P(x)  x Q(x)
x [P(x)   Q(x)] → x [P(x)  Q(x)]
x [P(x) → Q(x)] → x P(x) → x Q(x)
x [P(x)  Q(x)] →  P(x)  x Q(x)
(x) P(x)  (x) Q(x)  (x) [P(x)  Q(x)]
(x) P(x)  (x) Q(x)  (x) (y) [P(x)  Q(y)]
(x) P(x)  (x) Q(x)  (x) (y) [P(x)  Q(y)]
(x) P(x)  (x) Q(x)  (x) [P(x)  Q(y)]
(x) P(x)  (x) Q(x)  (x) (y) [ P(x)  Q(y)]
(x) P(x)  (x) Q(x)  (x) (y) [ P(x)  Q(y)]
A  (x) P(x)  (x) [A  P(x)]
A  (x) P(x)  (x) [A  P(x)]
A  (x) P(x)  (x) [A  P(x)]
A  (x) P(x)  (x) [A  P(x)]
```

```
 [x p(x)]  x  p(x)
 [x p(x)]  x  p(x)
 [x  p(x)]  x  p(x)  x p(x)
 [x  p(x)]  x  p(x)  x p(x)
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

```
xyP(x, y)
yxP(x, y)
```

```
The is a pair x, y for which P(x, y) is true P(x, y) is false for every
pair x, y
```

```
Rule of Inference Name
```

```
()
()
```

```
xP x
Pc
```

### 

### 

(^) Universal instantiation
( )for an arbitary
()
P c c
xP x
(^) Universal generalization

### ()

```
for some element
```

```
xP x
c
```

### 

### 

(^) Existential instantiation
( )for some elemet
()
P c c
xP x
(^) Existential generalization
Number of non- **equivalent propositional function possible with ‘n’ propositional variable**
22 n
Nested Quantifier
xy xy yx xy
English statements Logical Expressions

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

All graphs are connected (^) x[G(x) → C(x)]
Not all graphs are connected (^) x[G(x) → C(x)]
All graphs are not connected  No graphs are
connected
x[G(x) →  C(x)]  x[G(x) →  C(x)]

### ❑❑❑

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

3

**SET THEORY**

**3 .1 Introduction**

Collection of unordered, district and well defined objects.

- {1, 2} = {2, 1} = {1, 2, 1} (order & repetition doesn’t matter)

Set representation: A {1, 2, 3} - Roaster form

A = {zzN x  3} – Set builder form

- Set with one element is known as singleton set.
- Set with zero element is known as empty set or null set.
- No of elements in a set is known as cardinality of set.
- If a set A contains an element a, it is denoted as:

a  A.

**3.1.1 Equal sets (Axiom of extension):**

Two sets A and B are said to be equal iff they have same set of elements.

A = B x (xA  xB)  A  B ^ B  A

**3.1.2 Subset:**

- A is said to be subset of B iff every element in A is also then in B. Denoted as A  B

x (x  A  x  B)

**3.1.3 Proper subset:**

- ‘A’ is said to be a proper subset of B if every element in A. exist in B and A  B. Denoted as A  B

i.e., A  B  x (xA → xB) ^ x. (x  B ^ x  A)

or

A  B  x (xA → xB) ^ (|A|  |B|)

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.1.4 Powerset:**

Powerset of a set A is set of all subsets of A. Denoted as P(A)

- if |A| = n

|P(A)| = 2n

- For any set A

  A

If A = , then

  A

**3.1.5 Operations on set:**

(i) Union:

AB = {xxA  x  B}

(ii) Intersection:

AB = {xxA  x  B}

(iii) Complement:

If A is a set,

Complement of A, A = Ac = {xx    x  A}

i.e., A = U – A = U  A

(iv) Difference:

A/B = A – B = {xx  A  x  B} = AB

AB− is also called complement of B w.r.t. to A.

“complement of B in A”

(v) Symmetric Difference:

A  B = {xxA  xB, but not both}

Since it corresponds to XOR operator, it is also denoted as AB

AB = (A – B)  (B – A) = (A  B) – (A  B)

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

- Two sets are said to be disjoint if their intersection .

**3.1.6 Loss involving set operations:**

- Idempotent law

### A A A

### A A A

### =

### =

### 

- Domination law

###  = 

### =

### 

### A

### A U U

- Indentity law

### A U A

### AA

### =

###  = 

### 

• (^) ( )
( ) ( )

### ( ) ( )

```
( ) Associative law
```

### A B C A B C

### A B C A B C

### A B C A B C

###   =   

###   =   

### 

###   =   

### 

XOR operation is associative

- ( ) ( ) ( )
  ( ) ( ) ( )

```
Distributive law
```

```
A B C A B A c
A B C A B A C
```

###   =    

###   =    

### 

- ( )
  ( )

```
absorption law
```

###   = 

###   = 

### 

### A A B A

### A A B A

- Demorgan's law

```
A B A B
A B A B
```

```
 =  

 =  
```

```
Note:
```

```
log.
```

### A B A C B C

```
The proot can be obtained by relating
A C B C A Cthis to XOR operation in ic
```

###  =   = 

###  =   = 

### ^

**3.1.7 Representation of sets using Venn diagrams:**

Rather than direct calculations we sometimes represent sets with Venn diagram and see them as regions.
Let A, B, C be 3 sets

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

The region 1 is represented by AB c

The region 2 is represented by A B c

Similarly, we have 8 regions including region outside of A, B, C

The principle of duality:

```
Let s denote a theorem dealing with the equality at two expressions which involve only operation  and . The dual of
s(sd) (i.e., expression obtained by interchanging  and ) is also a theorem.
```

Finding dual of A  B

A  B can be written as

AB = B

Dual is AB = B

i.e., B  A

 Dual of A  B is B  A

Duality principle should be applied only for general can but no for particular cases

**3.1.8 Cartesian Product:**

A × B = {(a, b) aA  be B}

- Cartesian product is associative

However

( ) ( )

(( , ,) ) ( , ,( ))

###     

### 

```
it has ordered pairs t type a b c a b c
```

### A B C A B C

### A × B  B × A

If A × B = B × A then (A = B  (A = )  (B = )

- A × (BC) = (A × B)  (A × C)

A × (BC) = (A × B)  (A × C)

A B  A B

```
A
1 2 3
4 5 6
7
C
```

B

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

### A B  A B

**3.1.9 Multisets:**

Multiset is an unordered collection of elements where on element can occur more than once.

Eg: {m 1 .a 1 , m 2 .a 2 --- mnan}

Where m 1 is called multiplicity of set

**3.1.10 Operations on multisets:**

- Union: Maximum of multiplicities is considered.
- Intersection: Minimum of multiplicities is considered
- Difference: Difference of multiplicities is considered.

If the difference is -ve, it is considered 0.

- Sum: Sum of multiplicities is considered.

It is denoted as P + Q

**3.2 Relations:**

A binary relation from set A to set B is any subset of A × B.

If |A| = M and |B| = n, then |A × B| = mn

 number of relations possible from A to B = 2mn^

If relation B from A to A we say it relation on A.

 Number of relations possible on a set A =
n^2
2 , |A| = n

Domain of relation : { x  (x, y)R}

Range of relation : {y  (x, y) R}

- (x, y) R is written as ‘xRy’ on ‘k’ relates y

**3.2.1 Inverse of relations:**

Inverse of a relation, R-^1 = {(y, x)|(x, y)R}

**3.2.2 Diagonal relation:**

Diagonal relation on set A is

 =A (a a,|) a A

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.2.3 Reflexive relations:**

Relation R defined on set A is reflexive

```
  aRa a A
```

i.e., if R is a reflexive relation then A  R

**3.2.4 Important type of relations:**

```
Type of relation
Condition No. of relatives
possible
```

```
Union Intersection
```

Reflective (^) aRa, aA (^2) nn^2 − ✓ ✓
Irreflective aA (aRa) (^2) nn^2 − ✓^ ✓^
Symmetric (^) x, yA(xRy  yRx) 2
2 .2^2
nn
n
−

### ✓ ✓

Antisymmetric (^) x, y (xRy  yRx  x = y) 2
232
nn
n
−

### × ✓

Asymmetric (^) x, y (xRy  yRx) 2
3 2
nn−

### × ✓^

Transitive (^) x, y (z(xRy  yRz  xRz) — × ✓^

- Note that all the above relations are defined on a single set.
- Also to prove any relation is not of certain type we need to P.T the logical formula for that relation is false.
- Every Asymmetric relation is antisymmetric relation.

**3.2.5 Composition of relations:**

If R is a relation from A to B, S is a relation from B to C, the composition of R & S is given by

SoR from A to C.

S.R = {(a, c)|(a, b)R and (b, c)S}

If R is relation on A, then composition is denoted as R^2 , R^3.

Note:

```
If R is any relation on set A, then
```

RoA = R and A oR = R

**3.2.6 Closure:**

Clause of a relation R under given property is smallest possible relation that contains R and Satisfy the prpperty.

(i) Reflexive Closure (R*):

Reflexive clouse of a relation R,

R# = RUA

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

(ii) Symmetric closure:

R+ = RUR–^1

(iii) Transitive closure:

- Finding transitive closure has no formula, but we have a procedure as shown below.
  Steps: Represent relation R with a directed graph such that whenever aRb draw a directed edge from a to b.

Steps: Now from each vertex, find all reachable vertices and for each reachable vertex b from a add the ordered pair (a,
b) to the closure.

- The standard procedure for finding transitive closes is
  R# = RR^2. R^3 ........ Rn-^1 Rn
  ‘n’ is a positive integer such that Rn–^1 = Rn
- when a relation is represent as a graph,
  If (a, b)  Rn, we can say that there exists an n-length path from a to b.
- when asked to find more than one closure, the order to be followed is reflexive, symmetric, transitive.
  Following any other order may give redundancy.
- The closure of a relation, if exists, under a property is intersection of the relations with that property containing R.
- If R is a transitive relation,
- Rn  R n  1
- also Rn is transitive relation.

**3.2.7 Partion:**

A partition of set s is dividing s in disjoint subsets such that

A 1 A 2  ...An = s

AiAj =  i, j  n

**3.2.8 Refinement:**

Partition P 2 is called refinement of partition p 1.

if every partitioned subset of P 2 is subset to some partitioned subset of P 1.

**3.2.9 Equivalence Relation:**

A relation which is reflexive

Symmetric

Transitive

is called an equivalence relation.

- Equivalence relation creates partition.
- Each set of the partition is called an equivalence class.
- Every element of same equivalence class are related to each other.
- No two element of different classes of related to each other

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

- Equivalence class is represented by
  [a] R

Where a is any element of the equivalence classes

- It R is an equivalence relation, the below two sentences means the same
  (i) aRb
  (ii) [a]R = [b]R

```
aRb & [a]R  [b] also mean same.
If R is an equivalence relation.
aRb is read as “a is equivalent to b”.
```

- If R 1 , R 2 are two equivalence relations
  R 1 R 2 need not to be an equivalence relation
  R 1 R 2 is an equivalence relation.

**3.2.10 Finding number of equivalence relations:**

- No of equivalence relations on a set with n elements is given by

```
Bell number ( )
1
```

### ,

```
n
n
k
```

```
B s n k
=
```

=^

```
Where sterling 2nd kind number
```

```
( ) ( ) ( )
0
```

### ,1^1

### !=

= − −

```
n im
i
i
```

```
s m n nc n i
n
```

```
The below is a shortcut to find the Bell number
B 0 → (1)
```

```
B 1 → (1) 2
B 2 → (2) 3 5
```

```
B 3 → (5) 7 10 15
```

```
B 4 → (15) 20 27 37 52
Find no. of equivalence relations is nothing but find no. of way we can partition the set.
```

**3.3 Partial Ordering Relations:**

A relation R on a set A is called a partial order if R is reflexive, antisymmetric and transitive.

**3 .3.1 Poset:**

A set ‘A’ together with a partial order R is called a poset

It is denoted as [A:R]. In a poset aRb is denoted as a  b. a < b means a  b and a  b.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.3.2 To set:**

A post [A;R] is called toset it every pair of element of set A are comparable.

Toset is also known as linearly ordered set (or) chain.

If [A, R] is a poset, then

[A ; R–^1 ] is called dual of the poset.

i.e., these diagram of [A : R–^1 ] can be obtained by turning the hasse diagram of [A, R] upside down.

**3.3.3 Hasse Diagram (Poset Diagram):**

- It is graphical representation of a poset.
  It is constructed as below:
  (i) Create vertex corresponding to every element of set A.
  (ii) All loops & Edges implied from transitivity are not shown.
- Let [A, ] be a poset
  We say yes, covers x  s, if x < y such that there doesn’t exist any z  s, x < z < y
- Thus hasse diagram shows edges b/w two elements x & y only if x covers y (or) y covers x. The set of such pairs x < y is
  called covering relation of (s, ).
- Thus applying reflexive transitive closure on covering relation of a poset gives the poset.
- Hasse Diagram of a toset is a chain.

**3.3.4 Maximum Element:**

In a poset an element is called maximal if it is not related to any other element.

**3.3.5 Greatest element (or) Maximum element:**

In a poset an element is called greatest if every element of the set relates to that element.

**3.3.6 Minimal element:**

In a poset an element is called minimal, if no other element is related to it.

**3.3.7 Least element (or) Minimum Element:**

In a poset least element is the one which relates to every other element of the set.

- Every finite, nonempty lattice has at least one minimal and one maximal element.
- Greatest or least element if exists is unique.
- Greatest and least elements may or may not exist if they exist they are the only maximal and only minimal elements
  respectively.

**3.3.8 Upper Bound:**

If [A : R] is a poset and B  A

Upper band of B = {x|bB, x  b and xA}

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.3.9 Least Upper Bound (lub or join or Supremum):**

In a poset [A : R] lub of two elemis a, b  A is least element of upper bound of {a, b}. It is denoted as ab.

i.e., ab  x x upper band of [a, b]

- If no least element exists in the upper bound, we say lub doesn’t exist.
- In other word,
  If ab = c then

aRc & bRc and

If aRd  bRd  cRd

**3.3.10 Greatest lower Bound (glb or meet or infimum)**

In a poset [A, R] glb of a, b is greatest element of lower bound of {a, b}. It is denoted as a  b

- If no such element exists we say glb doesn’t exist.
- Other way to define glb is
  If a  b = c, then

```
[eRa  cRb]  [(dRa  dRb)  dRc]
```

- For poset [Dn ; 1]
  Lub (a, b) = LCM (a, b)
  Glb (a, b) = GCD (a, b)
- For poset [P(A) ; ], where P(A) is power set of A
  lub (x, y) = xy
  lub (x, y) = xy
- The hasse diagram of [P(A); ] forms a hypercube on, where |A| = n

**3.3.11 Join Semi Lattice:**

It is a poset in which every pair of elements has lub.

**3.3.12 Meet Semi Lattice:**

It is a poset in which every pair of elements has glb.

**3.4 Lattice**

A lattice is a poset in which every pair of elements has both glb & lub.

i.e., Lattice is both join semi lattice & meet semi lattice.

A lattice L is denoted as (L, , )

- It is not needed that every lattice has greatest and least element.
- Every finite lattice has least and greatest elements.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.4.1 Properties of Lattice:**

- Idempotent

```
a a a
a a a
```

### =

### =

### 

- Commutative

```
a b a a
a v a a
```

###  =  

###  =  

### 

### •

```
( )
( )
```

### ()

```
Associative
()
```

```
a b c a b c
a b c a b c
```

###   =   

###   =   

### 

### •

### ()

```
Absorption law
()
```

```
a a b a
a a b a
```

###   = 

###   = 

### 

- a b    a c b c

a b    a c b c

If a  b and c  d then

a  c  b  d

a  c  b  d

**3.4.2 Sublattice:**

If A is a lattice B is called

Sublattice of A iff

(i) B itself is a lattice.

(ii) lub of any two element of B is same as lub of the two elements in A.

```
In above figure B is subset of A and B is a lattice still B is not a sublattice of A.
```

```
Because ( )
( )
```

### 2,3 4

### B 2,3

```
not sublat cenot equal
5
```

```
i
```

### 

### −

### 

### =

### =

```
in A glb
in glb
```

5

4

```
2 3
1
A
```

5

2 3

```
1
B
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.4.3 Types of Lattices:**

(1) Bounded Lattice:

- A lattice with greatest element and least element is called bounded lattice.
- Every finite lattice is bounded lattice.

(2) Complemented Lattice:

- Complemented lattice is a bounded in which every element has atleast one complement.
  B is said to be complement of a iff.
- glb (a, b) = greatest element and lub (a, b) = least element.

(3) Distributive Lattice:

- A lattice is said to be distributive if following distributive laws hold.
- a(bc) = (ab)  (ac).
- a(bc) = (ab)  (ac).

Note: If L is a bounded distributive lattice then complement of an element if exists, is unique. The reverse need not to be true.

Hence if we find more than one complement for an element, we can conclude that the lattice is not distributive

(4) Boolean Algebra:

- A lattice which is both distributive and complemented is known as Boolean algebra
- It is called so because it satisfises all the properties of Boolean algebra. Thus when given lattice is a Boolean algebra we
  can apply all the rules that we apply in logic.
- In Boolean algebra every element has exactly one complement.
- [Dn : 1] is a distributive lattice for any n.
- It is because distributive properties hold for lcm & gcd.
- [Dn : 1] is a Boolean lattice if n is a square free number.
- [P(s); ] is a Boolean lattice.
- Every Boolean lattice with 2n elements,   0.
  Every Boolean lattice contains 2nelements is isomorphic to the lattice (P(s); ) where s is a set with n elements.
  Also this Boolean lattice is a hypercube Qn.
- Sublattice of a complemented lattice need not to be a complemented lattice.
- Sublattice of a bounded lattice is a bounded lattice.

**3.5 Function (or) Mapping (or) Transformation**

A function F from set A to set B is an assignment of exactly in one element of B to each element of A. It is denoted as: F : A
→ B
Here A is called Domain B is called codomain
Function is a special type of relation.

- Consider f(a) = b
  b is called image of a
  a is called preimage of b.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

- Range: It is set of images of all the elements of A.

Range  Co-domain (Range need not to be equal to co-domain)

- If f 1 , f 2 are two functions
  f 1 (x) + f 2 (x) is denoted as (f 1 + f 2 ) (x)
  f 1 (x). f 2 (x) is denoted as (f 1 .f 2 ) (x)

( )

### 1

```
fx
```

```
is denoted as^1
f
```

```
(x), (^1
f
```

```
is not equal to inverse function)
```

- If A and B are two sets with
  |A| = n |B| = m then
  number of functions possible from A to B = mn

**3.6 Types of functions:**

**3.6.1 One - One function (Injection):**

f : A → B is one to one
iff
ab(f(a) = f(b)  a = b)

- It f : A → B is 1–1 then |A| ≤ |B|
- If |A| = m and |B| = n
  no of 1 – 1 function possible from A to B = nmp
- If m = n = k, then number of 1:1 function = k!

**3.6.2 Onto function (Surjection):**

f : A → B is onto iff
bB aA such that f(a) = b

- If f : A → B is onto then |A| ≥ |B|
- If |A| = m |B| = n then

( ) ( )

```
n im
i
i0
```

```
number of onto functions = 1 nc n i
=
```

  − −

- If m = n = k, then number of 1:1 function = k!

**3.6.3 One-to-One Correspondence (or) Bijection:**

A function f : A → B is Bijection iff
f is both one-one and onto

- If f : A → B is bijection, then |A| = |B|
- If f : A → B is 1 – 1 and |A| = |B|
  then f is a bijection
- If f : A → B is onto and |A| = |B|
  then f is a bijection

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

- If |A| = |B| = n then no of bijections possible from A to B are n!
- If f : A → A is a function and A is a finite set then
  A is 1– 1  A is onto

**3.6.4 Inverse of a function:**

f : A → B is invertible if its inverse relation fi is a function from B to A.
f : A → B is invertible  f is a bijection

- Inverse doesn’t exist if a function is not bijection. However, we can find inverse image of subset of codomain. If f : A →
  B is a function and S ≤ B
  Inverse image of S = {aA|f(a)  S}
- If f is a function from A to B and let S, T be subsets of A.

f S T f( ) = (S) f T( )

f S T f( ) = (S) f T( )

However, f S T f( ) = (S) f T( ) if f is a bijection

- If f is a function from A to B and let S, T be subsets of B

f−^1 (S T f) = −^1 (s f) −^1 (T)

f−^1 (S T f) = −^1 (s f) −^1 (T)

f−−^11 (s)=f (s)

**3.6.5 Identity function:**

A mapping IA : A → A is called an identity function if
IA = {(x, x)/xA}

**3.6.7 Constant function:**

A function f : A → B is said to be a constant function if
f(x) = c x A

**3.6.8 Composition of functions:**

If f : A → B and g:B → C are two function then gof: A → C is called a composition function of f & g.

gof(x) = g(f(x))

- In gof : A → C
  A is domain of gof
  C is codomain of gof

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

Range of gof is image of (range of f under g)

- If f : A → B and g : B → C are tow functions
  gof is defined for every case

But fog is defined iff
range of g ≤ domain of f
fog maps from B to B i.e., fog : B → B
fog  gof (i.e., composition is not commutative)
(fog)oh = fo(goh) (i.e., Associative)
(fog)–^1 = g–^1 of–^1 (Think why)
Let f : A → B be an invertible function then

f–^1 : B → A is a inverse of f
f–^1 of : A → A is an identity function IA
fof–^1 : B → B is an identity function IB

Note:

- f is 1–1 & g is 1– 1  gof is 1– 1
- f is onto & g is onto  gof is onto
- f is bijection & g is bijection  gof is bijection
- If gof is onto then g is onto
- If gof is 1–1 then f is 1– 1
- If gof is a bijection then f is onto  g is 1– 1

**3.6.9 Partial Functions:**

f: A → B is called partial function if ‘f’ is defined only for some of aA.
The subset of A on which f is defined is called domain definition of f.

**3.7 Groups:**

**3.7.1 Binary Operation:**

The binary operator * is said to be a binary operation on a non-empty set A if the set is closed under the operation.
i.e., (a*b) A a,bA

**3.7.2 Binary Structure (or) Algebraic Structure:**

A nonempty set A is called binary structure with respect is a binary operator *, if * is binary operation on A. it is demoted as
(A, *)

**3.7.3 Semi Group:**

(A, *) is semigroup iff
(i) is closed operation
(ii) is an associative property

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.7.4 Monoid:**

(A, *) is called monoid iff:
(i) is closed operation
(ii) is an associative property
(iii) Identity element exists

**3.7.5 Group:**

(A, *) is called monoid iff:
(i) is closed operation
(ii) is an associative property
(iii) Identity element exists in A
(iv) Every element of A has inverse

- Identity element if exists is unique.
- Inverse element if exist is unique.
- Finite Group:
  A group with finite number of elements
- Order of a group: It is number of elements in the group.
- In a group of 2 element
  a–^1 = a, aG
- ({0,1,2,3 ..... m- 1 }, m) is a group
- Let Sn be set of positive integers less than n and relatively prime to n. then
  (Sn, n) is a group.
- Abelian Group:
  A group (G,*) is called abelian if * is commutative.

**3.7.6 Properties of Groups**

- Let (G,*) be a group

if ab = ac  b = c (Left cancellation property)
ba = ca  b = c (Right cancellation property)
due to these property ever raw and column in Caley table has exactly one element

- If G is a group and a,bG
  then (ab)–^1 = b–^1 a–^1
- Group G is abelian  (ab)–^1 = b–^1 a–^1 a, bG
- aG, a° = e

**3.7.7 Homomorphism**

- If (G, *) and (G’, ) are two groups then a function f : G → G’ is called a homomorphism

if f(a*b) = f(a)  f(b)

- If f : G → G’ is a bijection, then we call the homomorphism isomorphism. It is denote as G ≅ G’
- If e 1 , e 2 are identity elements of G and G’ respectively then f(e 1 ) = e 2
- If aG, and f : G → G’ is a homomorphism f(a–^1 ) = (f(a))–^1

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

**3.7.8 Order of an element:**

The smallest positive integer n such that an = e is called of order of an element a in the group.

- The order of an element is divisor of order of the group.
- Order (a) = order (a–^1 ) aG
- a–n = bn if a–^1 = b and n is any positive integer.

**3.7.9 Subgroup:**

A non-empty subset H of a group G is called subgroup of G if (H, *) is also a group.

- For every group G, {e} and G are called trivial subgroups of G.
- Every subgroup contains identity element of its parent group.
- If H is a subgroup of G then order(H) divides order(G) (Lagrange’s theorem). The converse of Lagrange’s theorem holds
  only for abelian groups.
- If H and k are two subgroups of same group, then
  Hk is also, a subgroup

Hk need not to be a subgroup.

- If H  G, then H is called subgroup of G iff:
  (i) (a*b)H a, bH
  (ii) a–^1  H a, bH
- If H  G, and if H is finite → (applies only when H is finite) and nonempty, then H is called subgroup iff:
  (a*b)H a, bH
- If G is a subgroup of composite order, then G necessarily has non-trivial subgroup.

**3.7.10 Cyclic Groups:**

A group G is called cyclic, if aG such that every element can be written as an integral power of a such an element ‘a’ is
called generator.

- The order of generator is order of the group.
- If ‘a’ is a generator then a–^1 is also a generator.
- All subgroups of a cyclic group are cyclic.
- If G is a cyclic group of order n, then no of generator of G is given by (n) (Euler’s phi function)
- If ‘a’ is a generator of G, and let m be an integer such that 1 < m ≤ n then

order(am) =
( )

```
n
gcd n, m
```

- If G is a cyclic group with generator a and let d be divisor of |G|.
  For every d there exists exactly one subgroup of order d. this subgroup is generated by an/d where n = |G|
   No of subgroup of a cyclic group = no. of divisors of |G| each subgroup is generated by an/d. (d is divisor of |G|)

**3.7.11 Cyclic subgroup of a group:**

If (G,*) is any group and let aG.
The smallest subgroup of G containing a is <a></a> where
<a></a> = {an/nZ}
Also <a></a> is a cyclic subgroup.
order of the subgroup <a></a> = order of element ‘a’ in G.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

- If H is any subgroup of G and if H contains ‘a’ then
  <a></a>  H
- Thus if G is a group
  <a></a> is a cyclic subgroup of G, aG.
  Such subgroups are called generating sets

Note:

- Every group of prime order is cyclic in which every element (except e) is a generator element.
- Every cyclic group is abelian.
- A group is cyclic  it can’t be expressed as union of two proper subgroups.
- If (G,*) and (H,) are two groups
  (G  H, •) is a group where • is defined as
  (g 1 , h 1 ) • (g 2 , h 2 ) = (g 1 *g 2 , h 1  h 2 )
  This group is called direct product of G and H.
- Every group of order less than or equal to 5 is abelian.
- There is only one unique group for each of the order 1,2,3.

```
❑❑❑
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

4

**COMBINATORICS**

**4.1 Introduction**

Let m  ℕ. For a procedure of m successive distinct and independent steps with n 1 outcomes possible for the first step, n 2
outcomes possible for the second step, .... , and nm outcomes possible for the mth step, the total number of possible outcomes
is
n 1  n 2    nm
For a collection of m disjoint sets with n 1 elements in the first, n 2 elements in the second,.. ., and nm elements in the mth, the
number of ways to choose one element from the collection is
n 1 + n 2 +    + nm

( )
n n k n k
k0

```
n
x y x y.
nk
```

```
−
=
```

```
+=
−

```

^

( )( )

```
n i
```

```
i0
```

```
C n, i 1 0
=
```

 −=^

For n even,

(^) ( ) ( )
n / 2 n / 2 1
i 0 i 0
C n, 2i C n, 2i 1
−
==

=+^
For n odd,
( ) ( )
n / 2 n / 2 1
i 0 i 0
C n, 2i C n, 2i 1
     +
======================

=+^
(^) ni1=iC n, i( )=n2 .n1−
For positive integers n, t, the coefficient of x x x ...xnn 1122 3 nn3tt in the expansion of (x 1 + x 2 + x 3 + ... + xt)n is
1 2 3 t
n! ,
n !n !n !... n!
where each ni is an integer with 0 ≤ ni ≤ n, for all 1 ≤ i ≤ t, and n 1 + n 2 + n 3 + ··· + nt = n.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

When we wish to select, with repetition, r of n distinct objects, we are considering all arrangements of r x's and n – 1 |'s and
that their number is

```
( )
( )
```

```
n r 1! n r 1
.
r! n 1! r
```

```
+− +−
=
− 
```

Consequently, the number of combinations of n objects taken r at a time, with repetition, is C(n + r – 1, r).

**4.1.1 we recognize the equivalence of the following:**

(a) The number of integer solutions of the equation

x 1 + x 2 + ... + xn = r, xi ≥ 0, 1 ≤ i ≤ n.

(b) The number of selections, with repetition, of size r from a collection of size n.

(c) The number of ways r identical objects can be distributed among n distinct containers.

(^) n
2n 2n 1 2n
b,
n n 1 n1n

### =   − =  

###    − +  

###      

```
n ≥ 1, b 0 = 1.
```

The numbers b 0 , b 1 , b 2 **, .... are called the Catalan numbers,** after the Belgian mathematician

```
Order Is Relevant Repetitions Are Allowed Type of Result Formula
Yes No Permutation P(n, r) = n!/(n – r)!, 0 ≤ r ≤ n
Yes Yes Arrangement Nr, n, r ≥ 0
```

```
No No Combination C(n, r) = n!/[r!(n –^ r)!] =
```

```
n
r
```

### 

### 

### 

### ,

```
0 ≤ r ≤ n
```

No Yes (^) with repetitionCombination
n r 1
r

### +−

### 

### 

```
, n, r ≥ 0
```

If there are n objects with n 1 indistinguishable objects of a first type, n 2 indistinguishable objects of a second type,... and nr

indistinguishable objects of an rth type, where n 1 + n 2 +... + nr = n, then there are
1 2 r

```
n!
n !n !... n!
```

```
(linear) arrangements of the
```

given n objects.

Let A and B be subsets of a finite universal set U. Then

(a) A B= + −A B A B

(b) AB ≤ min{|A|, |B|}, the minimum of |A| and |B|

(c) |A\B| = |A| – AB≥ |A| – |B|

(d) |Ac| = |U| – |A|

(e) |A  B| = A B−A B= + −A B 2 A B=A / B+B / A

(f) |A × B| = |A| – |B|

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

Given a finite number of finite sets, A 1 , A 2 ,... , An, the number of elements in the union A 1 A 2 ... Anis

```
A 1 A 2 ... An = i Ai−i j Ai Aj+i j k Ai Aj Ak –... + (–1)
n+1
A 1 A 2 ... An,
```

where the first sum is over all i, the second sum is over all pairs i, j with i < j, the third sum is over all triples i, j, k with i < j <
k, and so forth.

The number of derangements of n ≥ 1 ordered symbol is

```
n ( )n
D n! 1^111... 1 1.
1! 2! 3! n!
```

### = − + − + + −

### ^

Let a 0 , a 1 , a 2 ,... be a sequence of real numbers. The function

```
f(x) = a 0 + a 1 x + a 2 x^2 +... = i i
i0
```

```
ax
```

```

=
```

^

is called the generating function for the given sequence.

**4.1.2 Extended Binomial coefficient**

( )( )( ) ( )

```
n n n 1 n 2... n r 1
r r!
```

### − − − − − − − − +

### =

### 

( )( )( )( ) ( )

```
1 r n n 1 n 2... n r 1
r!
```

### − + + + −

### =

( ) ( )
( )

( )

```
n
1 n r 1! 1 r n r 1
n 1 !r! r
```

### − + − +−

### = = − 

### − 

### .

For all m, n  Z+, a  R,

(1) (1 + x)n = 2n

```
n n n n
x x ... x
0 1 2 n
```

###      + + + + 

###        

###        

(2) (1 + ax)n = 2 2 n n

```
n n n n
ax a x ... a x
0 1 2 n
```

###      + + + + 

###        

###        

(3) (1 + xm)n = m 2m nm

```
n n n n
x x ... x
0 1 2 n
```

###        

###      + + + + 

###        

(4) (1 – xn+1)/(1 – x) = 1 + x + x^2 + .... + xn

(5) 1/(1 – x) = 1 + x + x^2 + x^3 + ... = i0= xi

(6) 1/(1 – ax) = 1 + (ax) + (ax)^2 + (ax)^3 + ...

= i 0==(ax)i= i 0a xii

= 1 + ax + a^2 x^2 + a^3 x^3 + ...

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

(7) 1/(1 + x)n =^2

```
n n n
x x ...
0 1 2
```

###      − − −

###      + + +

###      

= i0 i

```
n
x
i
```

```

=
```

### −

### 

### 

^

( ) ( )^22

```
n 1 1 n 2 1
1 1 x 1 x ...
12
```

###  + −   + − 

### = + −   + −   +

###    

= i0( )i i

```
n i 1
1x
i
```

```

=
```

### +−

### − 

### 

^

(8) 1/(1 – x)n = ( ) ( )^2

```
n n n
x x ...
0 1 2
```

###    − −  −

###    + − +  − +

###      

= i0 ( )i

```
n
x
i
```

```

=
```

### −

### −

### 

^

( ) ( ) ( )^22 ( )

```
n 1 1 n 2 1
1 1 x 1 x ...
12
```

###  + −  + − 

### = + −   − + −   − +

###    

= i0 i

```
n i 1
x
i
```

```

=
```

### +−

### 

### 

^

If f(x) = i 0==a x ,g xiiii( )= i 0b x , and h(x) = f(x)g(x), then

h(x) = i0= cxi i, where for all k ≥ 0,

```
ck = a 0 bx + a 1 bx– 1 + ... + ak– 1 b 1 + akb 0 =
```

```
k
j k j
j0
```

```
ab−
=
```

.^

```
Objects Are
Distinct
```

```
Containers Are
Distinct
```

```
Some Container(s)
May Be Empty Number of^ Distributions^
```

```
No Yes Yes
```

```
n m 1
m
```

### +−

### 

### 

```
No No Yes
```

```
(1) p(m), for n = m
(2) p(m, 1) + p(m, 2) + ... +
p(m, n), for n < m
```

```
No Yes No
```

```
( )
( )
```

```
n m n 1 m 1 m 1
mn m n n 1
```

###  + − −   −−  

### ==   

### −  −−  

No No No p(m, n)
Consider the nonhomogeneous first-order relation

```
an + C 1 an– 1 = krn,
```

where k is a constant and n  Z+. If rn is not a solution of the associated homogeneous relation

```
an + C1an– 1 = 0,
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Discrete Mathematics
```

then a(np) = Arn, where A is a constant. When rn is a solution of the associated homogeneous relation, then a(np)= Bnrn, for B a
constant.

Now consider the case of the nonhomogeneous second-order relation

```
an + C 1 an– 1 + C 2 an– 2 = krn,
```

Where k is a constant. Here we find that

(a) (^) a(np)= Arn, for A a constant, if rn is not a solution of the associated homogeneous relation;
(b) a(np)= Bnrn, where B is a constant, if a(nh)=+c r 1 nnc r2 n, where r 1  r; and
(c) a(np)= Cn^2 rn, for C a constant, when a(nh) = (c 1 + c 2 n)rn.
Given a linear nonhomogeneous recurrence relation (with constant coefficients) of the form C 0 an + C 1 an– 1 + C 2 an– 2 + ... + Ckan–
k^ = f(n), where C 0 ^ 0 and Ck^ ^ 0, let a(nh)denote the homogeneous part of the solution an.^
(^) a(np)
c, a constant A, a constant
n A 1 n + A 0
n^2 A 2 n^2 + A 1 n + A 0
nt, t  Z+ Atnt^ + At– 1 nt–^1 + .... + A 1 n + A 0
rn, r  R Arn^
sin n A sin n + B cos n
cos n A sin n + B cos n
nt rn rn (Atnt + At– 1 nt–^1 + ... + A 1 n + A 0 )
rn sin n Arn sin n + Brn cos n
rn cos n Arn sin n + Brn cos n

### ❑❑❑

**DigitalDigital**

**LogicLogic**

**Digital**

**Logic**

```
Design Against Static Load
```

1. Logic Gate ............................................................................................................................ 3 .1 – 3 .1 2
2. Minimization of Boolean Function ...................................................................................... 3 .1 3 – 3. 22
3. Combinational Circuits ........................................................................................................ 3. 23 – 3. 42
4. Sequential Logic Circuits ...................................................................................................... 3. 43 – 3. 67
5. Number System ................................................................................................................... 3. 68 – 3. 75

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**LOGIC GATE**

**1.1. Logic Operations**

In Boolean algebra, all the algebraic functions performed is logical. The AND, OR and NOT are the basic operations that are
performed in Boolean algebra. There are some derived operations such as NAND, NOR, EX-OR, EX-NOR that are also
performed in Boolean algebra.

**1.1. NOT Operation**

Symbol:

```
Fig. 1.1.
```

A⎯⎯⎯→NOT Aor A (Complementation law)

```
and AA=  Double complementation law
```

```
Truth table for NOT operation
Input
A
```

```
Output
Y = A
0
1
```

### 1

### 0

A NOT gate can be represented using switch whose circuit representation is shown in figure below.

Fig. 1.2.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
A buffer is a basic logic gate that passes its input, unchanged, to its output. Its behaviour is the opposite of a NOT
gate.
The main purpose of a buffer is to regenerate the input, usually using a strong high and a strong low. Buffers are
also used to increase the propagation delay of circuits by driving the large capacitive loads.
```

```
Input Output
0 0
1 1
```

**1. 1 .2. AND Operation**

Symbol:

### A.A = A, A.0 = 0, A.1 = A,AA = 0

```
Truth table for AND operation:
Input Output
A B Y = AB
0 0 0
0 1 0
1 0 0
1 1 1
```

**1.1. 3. OR Operation**

Symbol:

```
A + A = A, A + 0 = A, A + 1 = 1, A + A=1
Truth table for OR operation:
Input Output
A B Y = A+B
0 0 0
0 1 1
1 0 1
1 1 1
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: Reduce the combinational logic circuit shown figure such that the desired output can be obtained using only one

gate.

```
Fig. 1.3.
```

Solution:

```
Fig. 1.4.
```

P = A, Q = B, R = C

(^) S = A · B · C
V = U = ABC
X = U + V + D
= ABC + ABC + D
= A + B + C + D
Fig. 1.5.
Enable or Disable Input:
Fig. 1.6.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Enable:

- Allow a signal to pass when the control signal is HIGH.
- Prevent a signal from passing when the control signal is LOW.

Disable:

- Prevent a signal from passing when the control signal is HIGH.
- Allow a signal to pass when the control signal is LOW.
- Enable and Disable Functions:
- AND and OR gates can both be used to enable or disable a transmitted waveform.

For a two input AND gate:

For a two input OR gate:

- **Control ‘0’ disable**
- **Control ‘1’ enabl** e (Buffer)
- **Control ‘0’ enable (Buffer)**
- **Control ‘1’ Always enable**

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.1. 4. Switch Diagram for AND/OR gate**

```
Fig. 1.7.
```

```
Fig. 1.8.
```

**1.1. 5. Basic law applications in AND/OR gate.**

(a) Commutative Law:

The commutative law allows change in position of AND or OR variables. There are two commutative laws.

```
A + B = B + A
A× B = B × A
```

(b) Associative Law:

```
( ) ( )
( ) ( )
```

### A + B + C = A + B + C

### A× B × C = A× B × C

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.1. 6. Circuit Diagram for AND/OR gate.**

```
Fig. 1.9.
```

**1.1. 7. Switch Diagram for AND/OR Gate**

The circuit shown below shows the switch representation

of AND gate which is basically the series connection of

switches A and B.

```
Fig. 1.10.
```

```
The circuit shown below shows the switch representation
```

```
of OR gate which is basically the parallel connection of
```

```
switches A and B.
```

```
Fig. 1.11.
```

**1.1. 8. Venn Diagram:**

NOT (^)

### A

A (^) Output
0
1

### 1

### 0

AND (^)

### A.B

```
A B Output
0
0
1
1
```

### 0

### 1

### 0

### 1

### 0

### 0

### 0

### 1

### OR

(^)

### A + B

```
A B Output
0
0
1
1
```

### 0

### 1

### 0

### 1

### 0

### 1

### 1

### 1

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.2. Logic Gates**

Logic gates are the fundamental building blocks of digital systems.
Types of logic gates: There are three basic logic gates, namely

- OR gate
- AND gate
- NOT gate
  And other logic gates that are derived from these basic gates are:
- NAND gate
- NOR gate
- Exclusive OR gate
- Exclusive NOR gate

**1.2.1. NAND gate:**

The term NAND gate equivalent to AND gate followed by a NOT gate, implies NOT-AND

Symbol:

```
Fig. 1.12.
```

Truth table of 2-input NAND gate.

```
Input Output
```

```
A B Y = AB
```

```
0 0 1
```

```
0 1 1
```

```
1 0 1
```

```
1 1 0
```

Switching and Circuit Diagram for NAND gate.

```
Fig. 1.13.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

NAND gate acts as Universal Gate

Logic Gates using only NAND Gates

```
Fig. 1.14.
```

All the logic gate functions can be created using only NAND gates. Therefore, it is also known as a Universal logic gate.

**1.2.2. NOR Gate**

A NOR gate is equivalent to OR gate followed by a NOT gate.

Symbol:

```
Truth Table for 2 - input NOR gate
Input Output
```

A B (^) Y = A + B
0 0 1
0 1 0
1 0 0
1 1 0

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Switching and Circuit Diagram for NOR gate

```
Fig. 1.15.
```

NOR gate acts as Universal Gate.

Logic Gates using only NOR Gates

```
Fig. 1.16.
```

All the logic gate functions can be created using only NOR gates. Therefore, it is also known as a Universal logic gate.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.2.3. XOR Gate**

Symbol of two input XOR gate

```
Truth table for 2-input XOR gate
Input Output
A B Y = A ⨁ B
0 0 0
0 1 1
1 0 1
1 1 0
```

XOR gate using AND, OR and NOT gate

Switching diagram of XOR gate

```
Truth Table:
A B Y
0 0 0
0 1 1
1 0 1
1 1 0
```

```
Y = A + B A + B( )( )
= AB + AB
= AB
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.2.4. X-NOR gate:**

Symbol for two input X-NOR gate

```
Truth table for 2-input X-NOR gate
Input Output
A B Y = A ⨀ B
0 0 1
0 1 0
1 0 0
1 1 1
```

Boolean expression for EX-NOR gate is Y= AB

Apply De-Morgan's theorem:

AB = AB + AB = AB AB = (A + B A + B = AB + AB)( )

The output of a two input EX-NOR gate is logic '1' when the inputs are same and a logic '0' when they are different.

X-NOR gate using AND OR and NOT gate

Switching Diagram of X-NOR gate

```
Truth Table:
```

```
A B Y
```

```
0 0 1
```

```
0 1 0
```

```
1 0 0
```

```
1 1 1
```

```
Y (A B A B) ( )
AB AB
AB
```

```
= + +
=+
=
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**1.3. Alternate Logic Gate Representation**

Example: In the following circuit, the find the output Z?

Solution: From the given circuit, we can observe that input to last XNOR is same, so, the
XNOR output is given by (let input is X)
Z = X. X + X. X = X + X = 1

i.e. the output will be high [logic 1] irrespective of the inputs A and B.
Example: The gate G 1 and G 2 in figure shown below have propagation delays of 10ns and 20ns respectively.

If input Vi makes an abrupt change from logic 0 to 1 at t = t 0 , then find the output waveform V 0?
Here, t 1 = t 0 + 10 ns, t 2 = t 1 + 10ns, t 3 = t 2 + 10 ns.
Solution: Let the output of G 1 = X

The output waveform will be as shown in figure below.

```

```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

2

**MINIMIZATION OF**

**BOOLEAN FUNCTION**

**2.1. Boolean Algebra**

Boolean algebra is a system of mathematical logic. It is an algebraic system consisting on the set of elements (0, 1) two binary
operators called OR, AND and one unary operator NOT. It is the basic mathematical tools in the analysis and the synthesis of
switching circuits. It is a way to express logic functions algebraically.

Note: Any functional relation in Boolean algebra can be provided by the method of perfect induction perfect inductions the
method of proof, where by a function relation is verified for every possible combination of values that the value may
assume.

**Axioms of Boolean Algebra:**

Axioms of Boolean algebra are a set of logical expressions that we accept without proof and upon which we can build a set of
useful theorem.

```
AND operator OR operator NOT operators
```

Axioms 1: 0.0 = 0 0 + 0 = 0 (^1) = 0
Axioms 2: 0.1 = 0 0 + 1 = 1 (^0) = 1
Axioms 3: 1.0 = 0 1 + 0 = 1
Axioms 4: 1.1 = 1 1 + 1 = 1
Logic operations: In Boolean Algebra all the algebraic function performed is logical. These actually represents logic
operations. The AND, OR and NOT are the basic operations that are performed in Boolean Algebra. In addition to these
operations, there are some derived operations such as NAND, NOR, EX-OR and EX-NOR that are also performed in Boolean
Algebra.
**1.1.1. NOT Operation**
The NOT operation in Boolean algebra is similar to inversion in ordinary algebra
================================================================================

=
1 : 0 1
2 : 1 0
3 : if A = 0 then A1=
4 : A = A (Double inversion)
**1.1.2. AND Operation**
It is a logical operation that are performed by AND gate. The AND operation in Boolean Algebra is similar to
multiplication in ordinary algebra.
1: A 0 0= (Null Law)

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

2: A 1 A= (Identity law)
3: A A A=
4: A A 0=

**1.1.3. OR Operation**

It is the logical operation that are performed by OR gate. The OR operation in Boolean Algebra is similar to addition in
ordinary algebra.
1: A + 0 = A (Null law)
2: A + 1 = 1 (Identity law)
3: A + A = A
4: A + A = 1

**1.1.4. NAND Operation:**

The NAND operation in Boolean Algebra is performed by AND operation followed by NOT operation i.e., the negation
of AND operation is performed by NAND gate.

**1.1.5. NOR Operation:**

The NOR operation in Boolean Algebra is performed by OR operation followed by NOT operation i.e., the negation of
OR operation is performed by NOR gate.

**2.2. Laws of Boolean Algebra**

**2.2. 1. Commutative Law**

1. A + B = B + A

A + B + C = B + C + A = C + A + B = B + A + C

2. AB = BA

ABC = BCA = CAB = BAC

Violation: Inhibition (1) for Example x/y (x but not y) is not commutative law it means x/y ≠ y/x

**2.2. 2. Associative law:**

This law arrows grouping of variables

1. (A + B) + C = A + (B + C)

A + (B + C + D) = (A + B + C) + D

= (A + B) + (C + D)

2. (AB)C = A(BC)

A (BCD) = (ABC)D

A (BCD) = ABCD

Note:- NAND and NOR gates are not Associative

**2.2. 3. Distributive Law**

1: A(B + C) = AB + AC

A + BC = (A + B) (A + C)

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**2. 2. 4. Redundant Literal Rule**

1. A + AB = A + B
2. A A + B( ) = AB

**2.2.5. Idempotent Law**

1. AA= A
2. A + A = A

**2.2. 6. Absorption Law**

1. A + AB = A
2. A(A + B) = A

**2.2. 7. Involutionary Law**

The law that for any variable A.

A = (A’)’ = A

**2.2. 8. Consensus theorem:**

There are two consensus theorems

AB + AC + BC = AB + AC

(^) (A + B A + C B + C = A + B A + C)( )( ) ( )( )

**2. 3. De-Morgan's theorem:**

De-Morgan’s theorem represents two of the most important rules of Boolean algebra.

I. (^) A. B = A + B
II. A + B = A. B
The above two laws can be extended for 'n' variables as,
A .A .A ... + A = A + A + ...A (^123) n 1 2 n and A + A + ... + A = A .A ...A (^12) n 1 2 n
**2.3.1 Duality theorem:**
Duality Theorem states that,
(a) Change each OR sign by an AND sign and vice versa.
(b) Compliment any '0' or '1' appearing in expression
(c) Keep literals as it is.
Note: With n variables, maximum possible distinct logic function =
2 n
2

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example : If a function is given as f = AB A B+ then find its complement.

Solution : Given f = (AB+AB)

Complement of f = AB + AB = AB AB

(^) = A + B A + B( )( )
(^) = AA + AB + BA + BB = AB + AB
Example : Show that
AB + BC + AC = AC + BC
Solution : LHS = AB + BC + AC
= AB C + C + BC A + A + A B + B C( ) ( ) ( )
= ABC + ABC + ABC + ABC + ABC + ABC
= ABC + ABC + ABC + ABC
(^) = AC B + B + BC A + A = AC + BC( ) ( )
= RHS
**2.4. Minimization of Boolean function:**
Every Boolean function expression must be reduced to as simple form as possible before realization because every logic
operation in the expression represents a corresponding elements of hardware. Realization of digital circuit with minimal
expression has several advantages as:

1. The number of logic gates will reduced.
2. The speed of operation will increase
3. power dissipation will decrease
4. The FAN IN may reduced
5. The complexing of the circuit reduces
   The simple method of minimization of Boolean function using certain Algebraic rules which results in the reduction of
   number of term and/or number of arithmetic operations the various theorem and rules that are already discussed are very
   useful for the simplification of Boolean expression.
   A function of n Boolean variables denoted by f(A 1 , A 2 .... An) is another variable of Algebra and takes one of the two
   possible values either 0 or 1. The various way of representing a given function are discussed below.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

All the terms contain all the variable either in complementary or in uncomplimentary form

The literal means the Binary variable either in complementary or in uncomplimentary form.

**2.4.1. Minimization of Boolean function using k-map**

- Using K-map: The Boolean function can be simplified Algebraically but being not a symmetric method, we can never
  be sure that whether the minimal expression obtained is the real minimal or not.
- Karnaugh Map (k-map): A k-map is a graphical representation of Boolean expression, A two variable k-map will
  have four cell or squares 3-variable k-map will have 8-cells, n-variable k-map will have 2n cells.

Note: Adjacent cells differ by 1 bit to maintain adjacently property gray code sequence is used in k-maps (Any two adjacent

cells will differ by only one bit)

Min terms & Max terms:

1. n-binary variable have 2n possible combinations.
2. Min term is a product term, it contains all the variables either complementary or un complementary form for that
   combination the function output must be ‘1’.

- Max term is a sum term, it contains all the variables either complementary or uncomplimentary form for that
  combination the function output must be ‘0’.
  For two variable
  x y Min terms Max terms
  0 0 m 0 =x y^ M = x + y 0

```
0 1 m = x y 1 M = x + y 1
1 0 m = x y 2 M = x + y 2
```

(^1 1) m = x y 3 M = x + y 3

- In min terms we assigns ‘1’ to each uncomplemented variables and ‘0’ to each complemented variable.
- In Max terms we assign ‘0’ to each uncomplemented variable and ‘1’ to each complemented variables.
  **2. 5. Representation of Boolean Functions**

Any Boolean expression can be expressed in two forms

- Sum of Product form (SOP)
- Product of Sum form (POS)
  **2. 5 .1. SOP Form**

The SOP expression usually takes the forms of two or more variables OR together.

```
Y = ABC + AB + AC
```

```
Y = AB + BC
```

SOP forms are used to write logical expression for the output becoming logic '1'.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example:

```
Input (3-variables) Output (Y)
A B C Y
0 0 0 0 1 1 1 1
0 0 1 1 0 0 1 1
0 1 0 1 0 1 0 1
0 0 0 1 0 1 1 1
```

∴ Notation of SOP expression is:

f(A, B, C) = Σm(3, 5, 6, 7)

Y = m 3 + m 5 + m 6 + m 7

Also, Y= ABC + ABC + ABC + ABC

**2. 5 .2. POS Form**

The POS expression usually takes the form of two or more OR variables within parentheses, ANDed with two or more such

terms.

Example: (^) Y=(A+B+C BC+D)( )
Each individual term in standard POS form is called maxterm.
POS forms are used to write logical expression for output be coming logic '0'.
we get f(A, B, C) = πM(0, 1, 2, 4)
Y = M 0 .M 1 .M 2 .M 4
Y = A + B + C A + B + C A + B + C A + B + C( )( )( )( )
∴ We can also conclude from Table 2 and from above equations:
if Y = Σm(3, 5, 6, 7) or Y = πM(0, 1, 2, 4)

**2. 6. Karnaugh Map (K-MAP)**

The K-map is a graphical method which provides a systematic method for simplifying the Boolean expressions. In n variable

K-map, there are 2n cells.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**2. 6 .1. Two variable K-map
2. 6 .2. Three variable K-map
2. 6 .3. Four Variable K-map**

```
(AB)  00
(AB)  01
(AB)  11
(AB)  10
```

```
AB
```

```
CD
```

```
(CD)(CD)(CD)(CD)
00 01 11 10
m 0 m 1 m 3 m 2
m 4 m 5 m 7 m 6
m 12 m 13 m 15 m 14
m 8 m 9 m 11 m 10
```

```
M 0 M 1 M 3 M 2
M 4 M 5 M 7 M 6
M 12 M 13 M 15 M 14
```

```
(A+B)  10 M 8 M 9 M 11 M 10
```

```
(A+B)  11
```

```
(A+B)  01
```

```
(A+B)  00
```

```
AB
```

```
AB 00 01 11 10
```

```
(C
```

```
+D
```

```
)
(C
```

```
+D
```

```
)
(C
```

```
+D
```

```
)
(C
```

```
+D
```

```
)
```

```
For SOP For POS
```

**2. 6 .4. Five variable K-map**
    - 32 cells
    - 32 Minterms (Maxterms)
Here, we have f(A, B, C, D, E)

```
m 0 m 1 m 3 m 2
m 4 m 5 m 7 m 6
m 12 m 13 m 15 m 14
m 8 m 9 m 11 m 10
```

### BC

### DE

### DEDEDEDE

### BC

### BC

### BC

### BC

### BC

### DE

### DEDEDEDE

### BC

### BC

### BC

### BC

### M 0 M 1 M 3 M 2

### M 4 M 5 M 7 M 6

### M 12 M 13 M 15 M 14

### M 8 M 9 M 11 M 10

```
(From 0 - 16) (From 16 - 31)
(For Sop)
```

```
For A = 0 For A = 1
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**2. 7. Simplification Rules**

1. Construct the K-map and place 1's in those cells corresponding to the 1's in the truth table. Place the 0's in the other cells.
2. Examine the map for adjacent 1's and loop those 1's which are not adjacent to any other 1's. These are called isolated 1's.
3. Next, look for those 1's which are adjacent to only one other 1. Loop any pair containing such a 1.
4. Loop any octet even if it contains some 1's that have already been looped.
5. Loop any quad that contains one or more 1's which have not already been looped, making sure to use the minimum number

```
of loops.
```

6. Form the OR sum of all the terms generated by each loop.

Example: Simply a four variable logic function using K-map

f(A, B, C, D) = Σm(0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14) also implement the simplified expression with AND-OR logic.
Solution:

```
1 1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
1
```

```
0
```

```
0
```

```
0
```

```
0
```

```
→ Quad I
```

```
Quad II → → Quad II
```

```
AB
```

```
CD 00 01 11 10
```

```
CD CD CD CD
```

```
 
```

```
 
```

```
 
```

```
 
Quad I
Octet
```



```
∴
```

```
= C + A D + BD
```

```
octet quad - II quad - I
```

```
f
  
```

```
⇒ Gate implementation:
```

**2. 8. Redundant Group**

If all the 1's in a group are already involved in some other groups, then that group is caused as a redundant group. A redundant

group has to be eliminated, because it increases the no of gates required.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**2. 9. Don't Care Condition**

The combinations for which the values of the expression are not specified are called don't care conditions.

Example: Simply the given equation in part (i) and (ii)

(i) In terms of SOP. and don't care conditions

f (A, B, C, D) = Σm(1, 3, 7, 11, 15) + d(0, 2, 5)

(ii) In terms of POS and don't care conditions.

f(A, B, C, D) = πM(4, 5, 6, 7, 8, 12) + d(1, 2, 3, 9 , 11, 14)

Solution:

(i) (ii)

**2. 10. Implicants, Prime Implicants and Essential Prime Implicants**

**2.10.1. Implicants**

Implicants is a product term on the given function for that combination the function output must be 1.

**2.10.2. Prime Implicant (PI)**

Prime implicant is a smallest possible product term of the given function,

**2. 10 .3. Essential Prime Implicants (EPI)**

EPI is a prime implicant it must cover at least one minterms, which is not covered by other PI.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: Reduce the expression using mapping F = Σm(2, 3, 6, 7, 8, 10, 11, 13, 14)

Solution :

### F = ABCD + ABD + AC + BC + CD

Example : Reduce the following expression using k-map and identify PI’s and EPI

F = Σm(0, 1, 2, 3, 6, 7, 13, 15)

Solution :

### EPI = AB, AC, ABD

### PI = BCD

Minimal F = AB + AC + ABD

Example: Given the following Karnaugh map, which one of the following represents the

minimal sum of products of the map.

A. xy + yz

B. _ωx y+xy+xz_

C. _ωx+yz+xy_

D. xy + y
Solution :

= xy + yz

```

```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

3

**COMBINATIONAL CIRCUITS**

**3. 1. Combinational Circuits**

The combinational circuit has ‘n’ input variables and ‘m’ output variables. Since, the number of input variables is n, there are

2 n possible combinations of bits at the input. Each output can be expressed in terms of input variables by a Boolean expression.

```
Fig. 3.1. Block diagram of a Combinational Circuit
```

**3. 2. Adders**

The most basic arithmetic operation is the addition of two binary digits. A combinational circuit that performs the addition of

two 1-bit numbers is called as half adder, and the logic circuit that adds three 1-bit numbers is called as full adder.

**3.2.1. Half Adder**

The logic circuit that performs the addition of two 1-bit numbers is called as half adder. It is the basic building block for addition

of two single bit numbers. This circuit has two outputs namely carry (C) and sum (S).

```
Fig. 3.2. Block Diagram of a 2-bit Half Adder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The truth table of half adder: where A and B are the inputs and sum and carry

```
Table 1: Truth Table of Half Adder
Inputs Outputs
A B Sum (S) Carry (C)
0 0 0 0
0 1 1 0
1 0 1 0
1 1 0 1
```

K **–** map simplification for Carry and Sum: Boolean expressions for the sum (S) and carry (C) outputs from K – maps:

```
Sum, S AB AB (A B)
Carry, C AB
```

```
= + = 
=
```

Logic Diagram:

```
Fig. 3.3. Logic Diagram of Half Adder
```

**3.2.2. Full Adder**

A full adder circuit is an arithmetic circuit block that can be used to add three bits to produce a sum and a carry output. Let us
consider A and B as two 1-bit inputs & Cin is a carry generated from the previous order bit additions. Let S (sum) and Cout
(carry) are the outputs of the full adder.

```
Fig. 3.4. Block Diagram of a Full Adder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The Truth Table for Full Adder is given as:

```
Table: Truth Table for Full Adder
Inputs Outputs
A B Cin Sum (S) Carry Cout
0 0 0 0 0
0 0 1 1 0
0 1 0 1 0
0 1 1 0 1
1 0 0 1 0
1 0 1 0 1
1 1 0 0 1
1 1 1 1 1
```

K **–** map Simplification for Carry and Sum:

```
Fig. 3.5.
```

Simplified Boolean expressions for the sum (S) and carry (Cout) output from K-maps is

```
( ) ( )
( ) ( )
```

( ) ( )

```
in in in in in in
```

```
in in
```

```
in in
in
out in in
```

```
Sum, S ABC ABC ABC ABC C AB AB C AB AB
C A B C A B
```

```
C A B C A B
Sum, S C A B
Carry, C AB AC BC
```

```
= + + + = + + +
= + 
```

```
=  + 
=  
= + +
```

Logic Diagram:

We can realize logic diagram of a full adder using gates as shown in below figure:

```
Fig. 3.6. Logic Diagram of Full Adder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: A full adder is implemented using two input OR gate and two half adders. Half adder is implemented using two
input XOR and two input AND gate. The propagation delays of XOR gate, AND gate and OR gate respectively are 2ns, 1.5ns.
and 1ns. The propagation delay of full adder is ..... ns.

Solution:

```
Fig. 3.7.
```

**3. 3. Subtractors**

**3.3.1. Half subtractor**

A half subtractor is a combinational logic circuit, which performs the subtraction of two 1-bit numbers. It subtracts one binary
digit from another to produce a DIFFERENCE output and a BORROW output.

```
Fig. 3.8. Block diagram of a half subtractor
```

The truth table of half **–** subtractor, where A, B are the inputs, and difference (D) and borrow (B) are the outputs.

```
Table: Truth table of Half – Subtractor
Inputs Outputs
A B D Bout
0 0 0 0
0 1 1 1
1 0 1 0
1 1 0 0
```

K **–** map Simplification for Difference and Borrow:

```
out
```

```
Difference, D = AB + AB = A B
Borrow, B = AB
```



GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Logic Diagram:

```
Fig. 3.9. Logic Diagram of a Half subtractor
```

**3.3.2. Full Subtractor**

A full subtractor performs subtraction operation on two bits, a minuend and a subtrahend.

```
Fig. 3.10. Block Diagram of a Full subtractor
```

Truth table of Full subtractor:

ble: Truth table of Full subtractor
Inputs Outputs
A B Bin D Bout
0 0 0 0 0
0 0 1 1 1
0 1 0 1 1
0 1 1 0 1
1 0 0 1 0
1 0 1 0 0
1 1 0 0 0
1 1 1 1 1
K **–** map simplification for Difference and Borrow:

( ) ( )

( ) ( )

```
in in in in
in in
```

```
in in
in
in in in
```

```
Difference, D = ABB + ABB + ABB + ABB
= B AB + AB + B AB + AB
```

```
= B AÅB + B AÅB
D = A B B
Borrow, B = AB + AB + BB
```

```

```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Logic Diagram

```
Fig. 3.11. Logic Diagram of a Full Subtractor
```

**3. 4. Binary Parallel Adder**

An n-bit parallel adder can be constructed using n number of full adders are connected in parallel and hence; it is also known
as parallel adder such that the previous carry or carry input for adder 0 is set to zero. The carry output of each adder is connected
to the carry input of the next higher order adder. Hence, it is also known as carry propagate adder.

```
Fig. 3.12. n-bit Binary Adder
```

**3.4.1. Propagation Delay in Parallel Adder:**

Parallel adders suffer from propagation delay problem because higher bit additions depend on the carry generated from
lower bit addition. In effect, carry bits must propagate or ripple through all stages before the most significant sum bit is valid.
Thus, the total sum (the parallel output) is not valid until after the cumulative delay of all the adder.

**3. 5. Carry Look Ahead Adder**

The look ahead carry adder speeds up the operation by eliminating this ripple carry delay. It examines all the input bits
simultaneously and also generates the carry in bits for all the stages simultaneously. The method of speeding up the addition
process is based on the two additional functions of the full adder called the carry generate and carry propagate functions.

**3.5.1. Carry Generation**

Carry is generated only if both the input bits are 1, that is, if both the bits A and B are 1’s, a carry has to be generated in
this stage regardless of whether the input carry Cin is a 0 or a 1. Let G as the carry generation function,
G = A  B
Consider the present bit as the nth, then
Gn = AnBn

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 3.13. Carry Look – ahead Generator Circuit
```

**3.5.2. Carry Propagation**

A carry is propagated if any one of the two input bits A or B is 1. If both A and B are 0, a carry will never be propagated.
On the other hand, if both A and B are 1, then will not propagate the carry but will generate the carry. Let P as the carry –
propagation function, then
Pn = An  Bn

**3.5.3. Look ahead Expressions**

Let nth bit adder, the sum (S) and the carry out (C) for the nth bit may be expressed in terms of the carry generation
function (G) and the carry propagation function (P) as
Sn = Pn  Cn
Cn+1 = Gn + PnCn

```
Fig. 3.14. 4 - bit Full Adder with a look Ahead Carry Generator
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: A full adder can be realized using half adder? Explain it in detail.

Solution: A full adder realization using half adder is given by:

```
Fig. 3.15.
```

**3. 6. Comparator**

The comparator is a combinational logic circuit. It compares the magnitude of two n-bit numbers and provides the relative
result as the output. Let A and B are the two n-bit inputs. The comparator has three outputs namely A > B, A = B and A < B.
Depending upon the result of comparison, one of these outputs will go high.

```
Fig. 3.16. Block diagram of digital comparator
```

**3.6.1. 1 - bit Magnitude Comparator**

The 1-bit comparator is a combinational logic circuit with two inputs A and B and three outputs namely A < B, A= B and
A > B.
Table : Truth Table of a 1-bit Comparator
Inputs Outputs
A B X (A < B) Y (A = B) Z (A > B)
0 0 0 1 0
0 1 1 0 0
1 0 0 0 1
1 1 0 1 0

Design of 1-bit Magnitude Comparator: We can write the expressions for the three outputs as under:

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
( )
( )
```

```
00
0 0 0 0 0 0
00
```

```
For (A < B), X = A B
For A = B , Y = A B + A B = A B
For A > B , Z = A B
```

```
^
```

Logic Diagram of 1-bit Comparator:

```
Fig. 3.17. Logic Diagram of 1-bit Comparator
```

Example: The circuit shown in given figure is:

```
Fig. 3.18.
```

Solution: From the logic circuit shown in the figure, we obtain the following results,
X = AB
Y = (AB)(AB) = AB + AB = A B
Z = AB
So, we obtain the truth table for the above function as shown below.
From truth table, we deduce the following results.
It A > B, then x = 1
It A = B, the y = 1
It A < B, then z = 1

Therefore, it is a comparator circuit.

**3. 7. Multiplexer**

A multiplexer, abbreviated as MUX, is a digital switch which selects one of the many inputs to a single output. A number of
control lines determine which input data is to be routed to the output. If there are n select lines, then the number of maximum
possible input lines is 2n and the multiplexer is referred to as a 2n–to-1 multiplexer or 2n × 1 multiplexer.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 3.19. Block diagram of a 2 n to 1 multiplexer
```

**3.7.1. 2 × 1 MUX**

A 2 to 1 multiplexer has 2 inputs. Since 2 = 2^1 , this multiplexer will have one control (select) line. It has two data inputs I 0 and
I 1 , one select input S, and one output.

```
Fig. 3.20. Schematic block diagram of 2:1 Multiplexer
```

The truth table of this MUX is given below,

```
Select Line
(S)
```

Output
Y
0 I 0
1 I 1
Thus, the SOP expression for the output Y is,

```
Y=+I S 0 0 I S1 0
```

Realization of a 2:1 MUX using Logic Gates:

```
Fig. 3.21. Logic Diagram of a 2 x 1 Multiplexer
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**2.7.2. 4 × 1 MUX**

A 4-to-1 multiplexer has 4 inputs and two select lines, where I 0 to I 3 are the four inputs to the multiplexer, and S 0 and S 1 are
the select lines.

```
Fig. 3.22. Schematic block diagram of 4 x 1 MUX
```

Truth Table of a 4-to- 1 Multiplexer

```
Select Inputs
S 1 S 0
```

Output
Y
0 0 I 0
0 1 I 1
1 0 I 2
1 1 I 3
Output Y for a 4-input multiplexer is

Y = I S S + I S S + I S S + I S S 0 1 0 110 2 1 (^0) 3 1 0
**3.8. Implementation of Higher Order Mux Using Lower Order MUX**
The methods for implementing higher order MUX using lower order MUX are
Step 1: If 2n is the number of input lines in the available lower order multiplexer and 2N is the number of input lines in the
desired multiplexer, then the number of lower order multiplexers required to construct the desired multiplexer circuit
would be 2N – n.
Step 2: From the knowledge of the number of selection inputs of the available multiplexer and that of the desired multiplexer,
connect the less significant bits of the selection inputs of the desired multiplexer to the selection inputs of the available
multiplexer.
Step 3: The most significant bits of the selection inputs of the desired multiplexer circuit are used to enable or disable the
individual multiplexers so that their outputs when OR produce the final output.
Example: In realization of 32 : 1 MUX using 2 : 1 MUX, the required number of 2 : 1 MUX is?
Solution: In realization of 2 n : 1 MUX using 2 : 1 MUX, the required number of 2 : 1 MUX is 2n - 1, since, we have to realize
32 : 1 MUX, so we have
n = 5
Hence, the required number of 2 : 1 MUX is
2 n− = − =1 2^5 1 31

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**3. 9. Applications of Multiplexers**

1. It is used as a data selector to select one out of many data inputs.
2. They are used in designing the combinational circuits.
3. They are used in digital-to-analog and analog-to-digital converters.
4. They can be used for simplification of logic design.
5. Multiplexers are also used in data acquisition systems.
   **3. 10. Demultiplexer**

The demultiplexer is a combinational logic circuit that performs the reverse operation of a multiplexer. The demultiplexer has
one input line and m output lines. Again m = 2n, so it requires n select lines. A demultiplexer with one input and m output is
called a 1-to-m demultiplexer.

```
Fig. 3.23. Block Diagram of m-output Demultiplexer
```

The demultiplexer has one input line and m output lines. Again m = 2n, so it requires n select lines. A demultiplexer with one

input and m outputs is called a 1-to-m demultiplexer.

**3.10.1. 1 × 2 Demultiplexer**

A 1 to 2 demultiplexer has one input and two outputs. Since 2 = 2 × 1, it requires only one control (select) line.

```
Fig. 3.24. Logic Diagram of 1 x 2 De-MUX
```

Truth table of a 1-to-2 demultiplexer

```
Table: Truth table of a 1-to-2 demultiplexer
Input Select input
S S 0
```

```
Output
Y 1 Y 0
D 0 0 D
D 1 D 0
```

Thus, the Boolean expressions for the outputs can be written as

```
Y = DS 0 0 & Y = DS 10
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Realization of a 1 x 2 Demultiplexer using Logic Gates:

```
Fig. 3.25. Logic Diagram of 1 × 2 Demultiplexer
```

**3. 1 0.2. Applications of Demultiplexers**

Demultiplexers are used in

1. Data transmission
2. Implementation of Boolean Functions
3. Combinational logic circuit design
4. Generate enable signals (enable one out of many). The application of enable signals in microprocessor systems are:
   (a) Selecting different banks of memory
   (b) Selecting different input/output devices for data transfer
   (c) Enabling different functional units
   (d) Enabling different rows of memory chips depending on address

**3.11. Comparison Between Multiplexer and Demultiplexer**

```
Table : Comparison between Multiplexer and Demultiplexer
```

```
S.No. Parameter of comparison Multiplexer Demultiplexer
```

1. Type of logic circuit Combinational Combinational
2. Number of data inputs m 1
3. Number of select inputs n N
4. Number of data output 1 M
5. Relation between input/output lines and select lines m = 2n M = 2N
6. Operation principle Many to 1 or as data selector 1 to many or data distributor
   **3. 12. Decoder**

A decoder is a combinational circuit that converts an n-bit binary input data into 2n output lines, such that each output line will
be activated for only one of the possible combinations of inputs. Decoders are usually represented as n-to- 2 n line decoders,
where n is the number of input lines and 2n is the number of maximum possible output lines.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 3.26. Block Diagram of n-to- 2 n Decoder
```

If there are some unused or ‘don’t care’ combinations in the n-bit code, then there will be less than 2n output lines. In general,

if n and m are respectively the numbers of input and output lines, then m ≤ 2n.

**3.12.1. 2 to 4 Line Decoder**

Consider a 2 to 4-line decoder, where A and B are two inputs whereas Y 0 through Y 3 are the four outputs.

```
Fig. 3.27. Block Diagram of a 2 to 4 Line Decoder
```

Truth Table of a 2 to 4 Line Decoder
Table : Truth Table of a 2 to 4 Line Decoder
Inputs
A B

Outputs
Y 0 Y 1 Y 2 Y 3
0 0 1 0 0 0
0 1 0 1 0 0
1 0 0 0 1 0
1 1 0 0 0 1
The Boolean expressions for the four outputs is given as:

```
Y = A B and Y = AB 01
```

```
Y = AB and Y = AB 23
```

Realization of a 2 to 4 Line Decoder using Logic Gates

```
Fig. 3.28. Logic Diagram of a 2 to 4 Line Decoder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**3.12.2. Applications of Decoder**

Some of important applications of decoder are as follows:

1. When the decoder inputs come from a counter which is being continually pulsed, the decoder outputs will be activated

```
sequentially. Hence, they can be used as timing or sequencing signals to turn devices on or off at specific times.
```

2. Decoder are use in memory system of a computer where they respond to the address code generated by the microprocessor

```
to activate a particular memory location.
```

3. They are also used in computers for selection of external devices that include printers, modems, scanners, internal disk

```
drives, keyboard, video monitor etc.
```

**3. 13. Encoders**

An encoder is a combinational logic circuit that performs the inverse operation of a decoder. An encoder has 2n (or fewer) input
lines and n output lines.

```
Fig. 3.29. Block Diagram of Encoder
```

**3. 13 .1. Octal to Binary Encoder**

```
Fig. 3.30. Octal to Binary Encoder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Truth Table of an Octal to Binary Encoder:
Table: Truth Table of an Octal to Binary Encoder
Inputs
D 0 D 1 D 2 D 3 D 4 D 5 D 6 D 7

```
Outputs
A B C
1 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 1
0 0 1 0 0 0 0 0 0 1 0
0 0 0 1 0 0 0 0 0 1 1
0 0 0 0 1 0 0 0 1 0 0
0 0 0 0 0 1 0 0 1 0 1
0 0 0 0 0 0 1 0 1 1 0
0 0 0 0 0 0 0 1 1 1 1
```

The logical expressions for the outputs as follows:
A = D 4 + D 5 + D 6 + D 7
B = D 2 + D 3 + D 6 + D 7
C = D 1 + D 3 + D 5 + D 7

**3. 13 .2. Octal to Binary Encoder**

```
Fig. 3.31. Logic Diagram of Octal-to Binary Encoder
```

**3. 13 .3. Decimal to BCD Encoder**

This type of encoder has 10 inputs one for each decimal digit and 4 outputs corresponding to the BCD code.

```
Fig. 3.32. Block Diagram of a Decimal-to-BCD Encoder
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Truth Table of a Decimal to Binary Encoder:

```
Table : Truth Table of a Decimal to Binary Encoder
Input
0 1 2 3 4 5 6 7 8 9 Output^
D 0 D 1 D 2 D 3 D 4 D 5 D 6 D 7 D 8 D 9 A B C D
1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0 0 0 0 1
```

```
0 0 1 0 0 0 0 0 0 0 0 0 1 0
0 0 0 1 0 0 0 0 0 0 0 0 1 1
0 0 0 0 1 0 0 0 0 0 0 1 0 0
0 0 0 0 0 1 0 0 0 0 0 1 0 1
0 0 0 0 0 0 1 0 0 0 0 1 1 0
0 0 0 0 0 0 0 1 0 0 0 1 1 1
0 0 0 0 0 0 0 0 1 0 1 0 0 0
0 0 0 0 0 0 0 0 0 1 1 0 0 1
```

```
Fig. 3.33. Logic Diagram of Decimal-to-BCD encoder
```

The outputs of a decimal-to-BCD encoder:

```
A = D 8 + D 9
B = D 4 + D 5 + D 6 + D 7
C = D 2 + D 3 + D 6 + D 7
D = D 1 + D 3 + D 5 + D 7 + D 9
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**3. 14. Priority Encoder
3. 14 .1. Truth Table of a Four Input Priority Encoder: (Taking LSB as priority)**

```
Table: Truth Table of a Four Input Priority Encoder
Inputs
D 0 D 1 D 2 D 3
```

```
Outputs
A B
0 0 0 0 X X
1 0 0 0 0 0
X 1 0 0 0 1
X X 1 0 1 0
X X X 1 1 1
```

According to the truth table, the higher the subscript number, the higher the priority of the input.
The X’s are don’t care conditions indicating that the binary values they represent may be equal to 0 or 1.

**3. 15. Code Converters**

A code converter is a combinational logic circuit which accepts the input information in one binary code, converts it and

produces an output into another binary code.

**3. 15 .1. The truth table for 4-bit Binary and its Equivalent BCD**

```
Table: Truth table for 4-bit Binary and its Equivalent BCD
```

Decimal (^) A Binary InputB C D B 4 B 3 BCD Output B 2 B 1 B 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 1 0 0 0 0 1
2 0 0 1 0 0 0 0 1 0
3 0 0 1 1 0 0 0 1 1
4 0 1 0 0 0 0 1 0 0
5 0 1 0 1 0 0 1 0 1
6 0 1 1 0 0 0 1 1 0
7 0 1 1 1 0 0 1 1 1
8 1 0 0 0 0 1 0 0 0
9 1 0 0 1 0 1 0 0 1
10 1 0 1 0 1 0 0 0 0
11 1 0 1 1 1 0 0 0 1
12 1 1 0 0 1 0 0 1 0
13 1 1 0 1 1 0 0 1 1
14 1 1 1 0 1 0 1 0 0
15 1 1 1 1 1 0 1 0 1

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The minimized expression of outputs are as follows:
B 4 = AB + AC
B = AC + ABC 1

```
B = AB + BC 2
```

```
B = AB C 3
B 0 = D
```

### .

```
Fig. 3.34. Logic Diagram of a Binary-to-BCD Code Converter
```

**3. 16. Parity Generator**

Parity generators are circuits that accept an (n-1) bit data stream and generate an extra bit that is transmitted with the bit stream.
This extra bit is referred to as the parity bit. The parity added in binary message is such that the total number of 1’s in the
message can be either odd or even according to the type of parity used.

**3. 16 .1. Even Parity Generator**

The even parity generator is a combinational logic circuit that generates the parity bit such that the number of 1’s in the
message becomes even. The parity bit is ‘1’ if there are odd number of 1’s in the data stream and the parity bit is ‘0’ if there
are even number of 1’s in the data stream.
Truth table for 4-bit data with Even Parity:

```
Table: Truth table for 4-bit data with Even Parity
4 - bit data
A B C D
```

```
Even Parity
P
0 0 0 0 0
0 0 0 1 1
0 0 1 0 1
0 0 1 1 0
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

### 0 1 0 0 1

### 0 1 0 1 0

### 0 1 1 0 0

### 0 1 1 1 1

### 1 0 0 0 1

### 1 0 0 1 0

### 1 0 1 0 0

### 1 0 1 1 1

### 1 1 0 0 0

### 1 1 0 1 1

### 1 1 1 0 1

### 1 1 1 1 0

The minimized expression for even parity generator is
P = A ⨁ B ⨁ C ⨁ D
The logic diagram for the even parity generator is given as

```
Fig. 3.35. Logic diagram of even parity generator
```

**3. 16 .2. Odd Parity Generator**

The odd parity generator is a combinational logic that generates the parity bit such that the number of 1’s in the message

becomes odd. The parity bit is ‘0’ for odd number of 1’s and ‘1’ for even number of 1’s in the bit stream.

Example: A parity generation circuit required to generator on odd parity bit may use ————?

Solution: Odd parity generation circuit consists of combination of EX-OR and EX-NOR gates, whereas even priority generator

consists only EX-OR gates.

```
Fig. 3.36
 It is combination of EX-OR and EX-NOR gates.
```

```

```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

4

**SEQUENTIAL**

**LOGIC CIRCUITS**

**4. 1. Sequential Logic Circuits**

In sequential logic circuits, the output is a function of the present inputs as well as the inputs and outputs. Sequential circuit
include memory elements to store past data. The flip-flop is a basic element of sequential logic circuits.

```
Fig. 4.1. General Block diagram of Sequential Logic Circuit
```

There are two types of sequential circuits:

**4.1.1. Synchronous Circuits**

The sequential circuits which are controlled by a clock are called synchronous sequential circuits. These circuits get activated
only when clock signal is present.

**4.1.2. Asynchronous Circuits**

The sequential circuits which are not controlled by a clock are called asynchronous sequential circuits, i.e. the sequential circuits
in which events can take place any time the inputs are applied are called asynchronous sequential circuits.

**4.2. Difference Between Synchronous and Asynchronous Sequential Circuits**

```
S.No. Synchronous Sequential Circuits Asynchronous Sequential Circuits
```

```
1.
```

```
In synchronous circuits, the change in input signals
can affect memory elements upon activation of
clock signal.
```

```
In asynchronous circuits, change in input signals can affect
memory elements at any instant of time.
```

2. In synchronous circuits, memory elements are
   clocked FF’s.

```
In asynchronous circuits, memory elements are either
unlocked FF’s or time delay elements.
```

```
3.
```

```
The maximum operating speed of the clock depends
on time delays involved.
```

```
Since the clock is not present, asynchronous circuits can
operate faster than synchronous circuits.
```

4. They are easier to design. More difficult to design.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

### 5.

**4. 3. Latches**

Flip-flop is an electronic circuit or device which is used to store a data in binary form. Actually, flip-slop is a one-bit memory

device and it can store either 1 or 0. Flip-flops is a sequential device that changes its output only when a clocking signal is

changing. On the other hand, latch is a sequential device that checks all its inputs continuously and changes its outputs

accordingly at any time independent of a clock signal. It refers to non-clocked flip-flops, because these flip-flops, because these

flip-flops ‘latch on’ to a 1 or a 0 immediately upon receiving the input pulse.

**4.3.1. General Block Diagram of a Latch or Flip-flop**

Figure shown below is the general type of symbol used for a latch. In case of a flip-flop, a clock signal must be shown at input

side. It has many inputs and two outputs, labelled Q and Q. The Q output is the normal output of the latch and Qis the inverted

output.

Note: A flip-flop is said to be in HIGH state or logic 1 state or SET state when Q = 1, and in LOW state or logic 0 state or

RESET state or CLEAR state when Q = 0.

**4.3.2. Difference between Latches and Flip-flops**

```
S.No. Latch Flip-flop
```

1. A latch is an electronic sequential logic circuit used to store information in an asynchronous arrangement.

```
A flip-flop is an electronic sequential logic circuit used to
store information in a synchronous arrangement. It has
two stable states and maintains its states for an indefinite
period until a clock pulse is applied.
```

2. One latch can store onechanges only in response to data input.-bit information, but output state One flipchanges w-flop can store oneith clock pulse only.-bit data, but output state
3. Latch is an asynchronous device and it has no clock input. Flipwith clock pulse.-flop has clock input and its output is synchronised
4. Latch holds a bit value and it remains constant until new inputs force it to change. Flipclock pulse is received.-flop holds a bit value and it remains constant until a

### 5.

```
Latches are level-sensitive, and the output tracks the input
when the level is high. Therefore, as long as the level is
logic level 1, the output can change if the input changes.
```

```
Flip-flops are edge sensitive. They can store the input
only when there is either a rising or falling edge of the
clock.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 4. Latch**

A latch is a type of bistable logic device or multivibrator that is most often used in applications that require data storage. The
main characteristics of latch is that the output is not dependent solely on the on the present state of the input but also on the
proceeding output state.
Latches are sometimes used for multiplexing data onto a bus. For example, data being input to a computer from a external
source have to share the data bus with data from other sources. When the data bus becomes unavailable to external source, the
existing data must be temporarily stored, and hence the latches are placed between the external source and data bus.

**4.4.1. SR Latch**

For the SR latch (S stands for set and R for reset). The logic circuit for SR latch is shown in figure below:

```
Fig. 4.1. Logic circuit of SR latch.
```

The state table for the SR latch is:

S R Q Q+ (^) Q+
0 0 0 0 1
0 0 1 1 0
0 1 0 0 1
0 1 1 0 1
1 0 0 1 0
1 0 1 1 0
1 1 0 0 1
1 1 1 0 0
The symbol for SR Latch is:
Fig. 4.2.
Obtaining the characteristic equations of the NOR gate based latch are; we get
Q = R × S + R × Q = R × (S + Q)+ and Q = S × R + S × Q = S × (S + Q)+
Note: It must be noted that the complementing Q+ does not yield Q.+

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Hence, the truth table for SR latch is

However, the forbidden state (S = R = 1) is considered a don't care state.

Consider a Timing diagram for SR latch

```
Fig. 4.3.
```

**4. 4.2. SR Latch:**

An SR latch can be implemented using NAND gates, as shown in figure below

```
Fig. 4.4. Logic circuit for SR Latch
```

The SR latch is said to be set-dominant 1,
The symbol for SR latch is shown below:

```
Fig. 4.5.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The truth table for SR latch is given as:

Application of SR latch: The application of SR latch is in switch bouncing i.e. contact bounces of a push-button
switch during its opening or closing can be eliminated by using SR latch.

**4.4.3. Gated SR Latch on Enable SR Latch or clocked SR Latch**

A gated or level-sensitive SR latch uses a control signal C that can be used as a clock signal or can be used as enable input.
The logic circuit diagram, symbol and truth is given as

```
Fig. 4.6. Logic circuit of clocked SR latch.
```

```
Fig. 4.7. Symbol for clocked SR latch
```

**4.4.4. Gated SRLatch or enable SR Latch or clocked SRLatch**

Gated SR latch is implemented using two NAND gates and an SRlatch.
The logic circuit diagram, symbol and truth is given as

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Fig. 4.8. Logic diagram of clocked SRlatch. Fig. 4.9.

The truth table of the gated SR latch based on a SR latch:

C J K Q (^) Q+
O X X Q Q^
1 0 0 Q Q^
1 0 1 0 1
1 1 0 1 0
1 1 1 1 1
The characteristic equation for SR flip-flop is given as
Q = Q+ n +1= S + RQ = S + RQn

**4. 5. Flip-Flops**

Flip-flops are synchronous bistable devices also known as bistable multivibrator. Its output change its state only at a verified
paint (i.e. leading or trailing edge) on the triggering input called the clock (CLK), i.e. changes in the output occur in
synchronization with the clock.
Flip-flops are edge-triggered or edge-sensitive whereas gated latches are level-sensitive.

**4.5.1. Edge-triggered flip-flop**

An edge-triggered flip-flop changes its state either at positive edge (rising edge) or at negative edge (falling edge) of the check
pulse.
There are two type of edge-triggered flip-flops. The key to identify an edge-triggered flip-flop is by its logic symbol by
small triangle inside the block at the clock input C. This triangle is called the dynamic input indicator.
Positive edge triggered has no bubble at input C whereas negative edge triggered has bubble at input C.

```
Fig. 4. 10. Positive edge triggered flip-flop. Fig. 4.1 1. Negative edge-triggered flip-flop.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4.5.2. Basic JK flip-flop**

JK Flip-flop (J as a set input and K as a reset input) is the most versatile of the basic flip-flops.

The logic circuit of the gated JK flip-flop is shown in figure below:

```
Fig. 4.12. Logic circuit diagram of clocked JK flip-flop.
```

The state table for the JK flip-flop is given as

C J K Q Q+
O X X X Q
1 0 0 0 0
1 0 0 1 1
1 0 1 0 0
1 0 1 1 0
1 1 0 0 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
Hence, the truth table becomes,

```
C S R Q+ Q+
0
1
1
1
1
```

### 1

### 1 1

### 1

### 1

### 1

### 0 0

### 0

(^00)

### 0

### 0

### Q

### X X Q

### Q

```
Q No change state
```

```
 Reset
 Set
 Forbidden state
```

### 0

Note: The forbidden state, inherent to SR flip-flop is eliminated by adding two feedback loops such that the output becomes 1

only if Q = 0 and reset to only if Q = 1.

It should also be noted that when the inputs (J & K) are set to 1 and clock signal change to 1, then the feedback value of Q &
Q forced the flip-flop is toggle its value.
(i.e. to switch its state to its logical complement) hence, to ensure this operation in smooth fashion, the pulse width of
the clock must be smaller than the propagation delay of the flip-flop.
The characteristic equation of the JK flip-flop

```
Qn 1+ =+JQn KQn or Q+=+JQ KQ
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4.5.3. T-flip-flop**

A JK flip-flop can be transformed into a T- flip-flop (T stands for Toggle). When T flip-flop is activated, its output changes its
state at every time a pulse is applied to the input T.
The logic circuit of the gated T flip-flop is.

```
Fig. 4.13.
```

The state or characteristic table for T flip-flop is

```
C T Q Q+
```

```
O X X Q
```

```
1 0 0 0
```

```
1 0 1 1
```

```
1 1 0 1
```

```
1 1 1 0
```

As J = K = T, we obtain the characteristic equation as
Q = T × Q × C + (T + C) × Q+

If C = 1, the characteristic the equation is reduced to

Q = T+ Q

If C = 0, Q = Q+
Hence, the truth table of the T-flip flop is given as

```
Fig. 4.14.
```

**4.5.4. D Flip-Flop**

D-flip-flop can be obtained by use of only two combinations of S-R or J-K flip-flop. It has only one input i.e. D-input or data
input.
The logic symbol for D- flip-flop is given as

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 4.15.
The truth table for D-flip-flop is
Input Output
D Qn+1
0 0
1 1
```

The characteristic equation of D-flip-flop is:

```
Qn+1 = D
```

**4.5.5. Excitation table of Flip-flops**

The truth table of a flip-flop is sometimes referred as characteristic table as it specifies the operational characteristics of the
flip-flop there may occurs some situations in which the present state and the next state of the circuit is desired and known. Then
the designing of input conditions to as to fulfil the requirements of the circuit, there is a table called excitation table.
It is very important and useful design aid for sequential circuit.

The excitation table for flip-flops:

**4. 6. Operating Characteristics of Flip-Flops**

**4.6.1. Propagation Delay Time:**

Propagation delay time is the time interval required after an input signal has been applied for the resulting output change to
occur.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

There are four categories of propagation delay times which are as follows:
A. Propagation delay tPLH, it is measured from the triggering edge of the clock pulse to Low-to-High transition of the output.

```
Fig. 4.16.
```

B. Propagation delay tPHL, it is measured from the triggering edge of the clock pulse to HIGH-to-LOW transition of the
output.

```
Fig. 4.17.
```

C. Propagation delay tPHL, it is measured from the leading edge of the PRESET input to LOW-to-HIGH transition of the

output.

```
Fig. 4.18.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

D. Propagation delay tPHL, it is measured from the leading edge of the clear input to the HIGH-to-LOW transition of the
output.

```
Fig. 4.19.
```

**4.6.2. Set-up time (** **_ts_** **)**

It is the minimum time interval required for the logic levels (0 or 1) to be maintained constantly on the inputs (J, K or D)
prior to the triggering edge of the clock pulse in order for the levels to be reliably clocked into the flip-flop.

```
Fig. 4.20.
```

**4.6.3. Hold time (** **_th_** **)**

It is the time for which the data must remain stable after the triggering edge of the clock.

**4.6.4. Clock-pulse width**

The minimum time duration for which the clock pulse must remain HIGH and LOW which are designed by manufacturers.

Failure to clock pulse width results in unreliable triggering.

**4.6.5. Maximum clock frequency**

The maximum clock frequency (fmax) is the highest rate at which flip-flop can be reliably operated.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 7. Applications of Flip-Flops**

Some of the common applications of flip-flops are as follows:

1. Switch bouncing.
2. Registers.
3. Counters.
4. Memory elements.
   **4. 8. Race Around Condition**

JK flip flop suffers from the problem of race around condition. When J = 1 & K = 1, is applied to the JK flip flop and JK flip
flop is level triggered then output of the JK flip flop toggles so many times during the pulse width of the clock and output of
the flip flop settled either at 1 or 0 depending upon the pulse width of the clock and propagation delay of the flip flop is called
race around condition.

```
Fig. 4.21. Race Around Condition in JK Flip Flop
```

To avoid Race Around condition:

• (^) Tpulse-widthTpd Tclock

- Master Slave flip flop
  **4. 8 .1. Master Slave Flip flop:**

```
Fig. 4.22. Logic Diagram for Master Slave JK Flip Flop
(a) In master slave flip flop, inverted clock is given to the slave.
(b) Master slave flip flop is used to store single bit because output is taken only from slave flip flop.
(c) Here, master flip flop is level triggered while slave is negative edged triggered.
Note: JK flip flop is also known as Universal flip flop.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 9. Designing of One Flip Flop by Other Flip Flop**

The steps for designing of one flip flop or new flip flop using existing or same existing flip flop.

Step 1: Write the characteristic table for the designed flip flop.

Step 2: Write the excitation table for the available flip flop.

Step 3: Write the logical expression.

Step 4: Minimize the logical expression.

Step 5: Circuit Implementation.

**4. 10. Shift Registers**

An array of flip-flops in required to store binary information, and the number of flip-flops required is equal to the number of
bits used to store is referred as registers.
Examples of registers are general purpose registers flags, etc.

Now, the information or data can be stored or entered in serial form (one-bit at a time) or in parallel form (all the bits
simultaneously) and can be retrieved like this manner too. The data will be entered or retrieved in serial form is known as
temporal code and which is in parallel form is called special code.
Hence, registers can be classified into four categories depending upon the data being entered or retrieved.

**4. 10 .1. SISO (serial-in, serial-out) Shift Register:**

In serial-in, serial-out shift register, data input is in serial form and common clock pulse is applied to each of the flip-flop. After
each clock pulse, data moves by one position. The output can be obtained in serial form, as shown in figure below:

```
Fig. 4.23. SISO Shift Register
```

- It is the slowest shift register among all the shift registers.
- To store n-bits in a n-bit SISO register, then the minimum “n” clock pulses are required.
- To retrieve n-bits from a n-bit SISO register, then the minimum “(n-1)” clock pulses are required.
  **4. 10 .2. SIPO (serial-in, parallel-out) Shift Register**

In serial-in, parallel-out shift register, data is applied at the input of register in serial form and the output can be obtained in
parallel form after the completely shifting of data in register. Figure below shows the serial input data, and then parallel output.

```
Fig. 4.24. SIPO Shift Register
```

- To store n-bits in a n-bit SIPO register, the minimum “n” clock pulses are required.
- To retrieve n-bits from a n-bit SIPO register, there is no pulse required.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 10 .3. PISO (parallel-in, serial out) Shift Register**

In parallel-in, serial-out shift register, data is loaded into shift register in parallel form
and the data output obtained will be serial form as shown in figure below:

- To store n-bit in a n-bit PISO register, a single clock pulse is required.
- To retrieve n-bit from n-bit PISO register, the minimum “(n-1)” clock pulses are

```
required.
```

**4. 10 .4. PIPO (parallel in, parallel out) Shift Register**

In parallel-in, parallel-out shift register, data is loaded in parallel form and the data output obtained will be in parallel, as shown
in figure below:

```
Fig. 4.26. PIPO Shift Register
```

- To store n-bit in n-bit PIPO register, only a single clock pulse is required.
- To retrieve n-bits from n-bit PIPO register, no clock pulse is required.

Serial Input: The data in the serial form is applied at the serial input after clearing the flip-flops using CLR.

The waveform of serial input shift register is shown below:

```
Fig. 4.27.
```

```
Fig. 4.25. PISO shift register
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Parallel Input: Data can be entered in the parallel form making use of the pre-set inputs. Then after clearing the flip-
flops, if the data lines are connected to the parallel lines and ‘1’ is applied to the PRESET input.

**4. 10 .5. Universal Shift Register**

If the flip-flop outputs of a shift register are accessible, then information entered serially by shifting can be taking out in parallel
from the outputs of the flip-flops. If a parallel

```
Fig. 4.28. Second form of serial adder
```

load capability is added to a shift register, then data entered in parallel can be taken out in serial fashion by shifting the data
stored in the register. Some shift registers provide the necessary input and output terminals for parallel transfer. They may also
have both shift-right and shift-left capabilities.
The most general shift register has the following capabilities:

1. A clear control to clear the register to 0.
2. A clock input to synchronize the operations.
3. A shift-right control to enable the shift-right operation and the serial input and output lines associated with the shift
   right.
4. A shift-left control to enable the shift-left operation and the serial input and output lines associated with the shift left.
5. A parallel-load control to enable a parallel transfer and the n input lines associated with the parallel transfer.
6. “n” parallel output lines.
7. A control state that leaves the information in the register unchanged in response to the clock.
   Other shift registers may have only some of the preceding functions, with at least one. shift operation. A register capable
   of shifting in one direction only is a unidirectional shift register. One that can shift in both directions is a bidirectional shift
   register. If the register can shift in both directions and has parallel-load capabilities, it is referred to as a universal shift register.
   The block diagram symbol and the circuit diagram of a four-bit universal shift register is shown in figure below:

```
Fig. 4.29. 4 - bit Universal Shift Register
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 4.30. Logic Diagram of 4-bit Universal shift register
```

The function for the Universal Shift Register is as follows:

Mode Control
Register Operation
S 1 S 0
0 0 No change
0 1 Shift right
1 0 Shift left
1 1 Parallel load
Shift registers are often used to interface digital systems situated remotely from each other. For example, suppose it is
necessary to transmit an n-bit quantity between two points. If the distance is far, it will be expensive to use n lines to transmit
the its bits in parallel. It is more economical to use a single line and transmit the information serially, one bit at a time. The
transmitter accepts the n-bit data in parallel into a shift register and then transmits the data serially along the common line. The
receiver accepts the data serially into a shift register. When all n bits are received, they can be taken from the outputs of the
register in parallel. Thus, the transmitter performs a parallel-to-serial conversion of data and the receiver does a serial-to-parallel
conversion.

**4. 10 .6. Applications of Shift Registers**

(a) Delay line: A shift register can be used to introduce a delay (Δt) in signals

(^) Δ= ×^1
c
tN
f
Where N is number of stages & fc is the clock frequency.
(b) Serial-to-parallel converter
(c) Parallel-to-serial converter

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

(d) Ring counter
(e) Twisted ring counter
(f) Sequence counter

**4. 11. Asynchronous Counter Or Ripple Counter**

A circuit which is used for counting the numbers or pulses is known as counter. Counter is referred to as modulo-N (or divide
by N), where the word modulo indicates the number of states in the counter.

**4. 11 .1. 3 - Bit Binary Counter**

Consider a 3-bit binary counter which has total ’8’ number of states which require three flip-flops and Q 2 , Q 1 and Q 0 are the
outputs of those flip-flops.
The circuit diagram or logic circuit diagram for 3-bit binary counter,

```
Fig. 4.31. A 3-bit Binary Counter
```

The truth table for 3-bit binary counter is given as:

Output waveforms of the above counter is:

```
Fig. 4.32.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The frequency ‘f’ of clock pulses for reliable operation of the counter is given as

Where, N = number of flip-flops

```
tpd = propagation delay of one flip-flop.
Ts = strobe pulse width.
If during the operation of counter, if some pulses are falsely operated for short duration, known as spikes, which change
```

the state of the flip-flop. It may happen when the propagation delay of each flip-flop may vary and may happen that, all the

flip-flops may not change their states or may be only one flip-flop changes its state during the pulse time.

```
This problem of spikes can be eliminated by using a strobe pulse with the help of strobe pulse, the state will charge only
```

when flip-flops of the counter are in steady state.

Example: In a 4-stage ripple counter, the propagation delay of a flip-flop is 50n sec. If the pulse width of the strobe is 30n

sec. Find the maximum frequency at which the counter operator reliably.

Solution: The maximum frequency is

```
max
=^1
pd+ s
```

```
f
nt t
```

n = number of flip-flops or stage = 4

tpd = propagation delay of each flip-flop = 50 nsec.

ts = Strobe pulse width = 30 nsec

```
max -9
=^1 =^1000 MHz
(4 × 50 + 30) × 10 (200 + 30)
```

```
f
```

```
1000
= MHz
230
```

**4. 11 .2. Modulo-6 Asynchronous Down Counter**

Down counter is the counter which counters the values of pulses in descending order. Consider or Stable-8 counter (2^3 = 8),
which uses three flip-flops.

```
Fig. 4.33.
```

1. Only sequential counter can be designed. Random counter cannot be designed.
2. Glitch (undesirable state) would appear in case of asynchronous counter.
3. Speed of asynchronous counter is not fast.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 11 .5. BCD Ripple Counter**

A decimal counter follows a sequence of 10 states and returns to 0 after the count of 9. Such a counter must have at least four
flip-flops to represent each decimal digit, since a decimal digit is represented by a binary code with at least four bits. The
sequence of states in a decimal counter is dictated by the binary code used to represent a decimal digit. If the BCD code is used,
the sequence of states is as shown in the state diagram. A decimal counter is similar to a binary counter, except that the state
after 1001 (the code for decimal digit 9) is 0000 (the code for decimal digit 0).

```
Fig. 4.34. State diagram of a decimal BCD counter.
```

The logic diagram of a BCD ripple counter using JK flip-flops is shown in figure below. The four outputs arc designated by

the letter symbol Q, with a numeric subscript equal to the binary weight of the corresponding bit in the BCD code. Note that

the output of Q 1 is applied to the C inputs of both Q 2 and Q 4 and the output of Q 2 is applied to the C and output of Q 2 and Q 3

applied to J through a two input AND gate.

```
Fig. 4.35. BCD ripple counter
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**4. 12. Synchronous Counter**

The ripple counters have the advantage of simplicity (only FLIP-FLOP’s are required) but their speed is low because of ripple
action. The maximum time is required when the output changes from 111....1 to 00....0 and this limits the frequency of operation
of ripple counters.
The speed of operation improves significantly if all the FLIP-FLOPS are clocked simultaneously. The resulting circuit
is known as a synchronous counter. Synchronous counters can be designed for any count sequence (need not be straight binary).
The output Q 0 of the least-significant FLIP-FLOP changes for every clock pulse. This can be achieved by using a T-type
FLIP-FLOP with T 0 = 1. The output Q 0 changes whenever Q 0 changes from 1 to 0. Therefore, if Q 0 is connected to T input (T 1 )
of the next FLIP-FLOP, Q 1 will change from 1 to 0 (or 0 to 1) when Q 0 = 1 (T 1 = 1) and will remain unaffected when Q 0 = T 1
= 0. Similarly, Q 2 changes whenever Q 1 and Q 0 are both “1”. This can be achieved by making the T-input (T 2 ) of the most-
significant FLIP-FLOP equal to Q 1 .Q 0.
In addition to FF’s, synchronous counters require some gates also. JK FLIP-FLOPS are the most commonly used FLIP-
FLOP’s for the design of synchronous counters. In this, each FLIP-FLOP has two control inputs (J and K) and circuit is required
to be designed for each control input. Many programmable logic devices (PLDs) used for the design of digital systems utilise
D FLIP-FLOPS for their memory elements, therefore, counter design using D FLIP-FLOPS will be useful for programming
inside a PLD. It has only one control input which makes its design simpler than the design using J-K FLIP-FLOPS.

```
Fig. 4.36. A 3-bit Synchronous Counter
```

**4.12.1. Synchronous Counter Design**

Synchronous counters for any given count sequence and modulus can be designed in the following way:

1. Find the number of FLIP-FLOPs required.
2. Write the count sequence in the tabular form.
3. Determine the FLIP-FLOP inputs which must be present for the desired next state from the present state using the
   excitation table of the FLIP-FLOPS.
4. Prepare K-map for each FLIP-FLOP input in terms of FLIP-FLOP outputs as the input variables.
5. Simplify the K-maps and obtain the minimized expressions.
6. Connect the circuit using FLIP-FLOPS and other gates corresponding to the minimized expressions.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: Design a 3-bit synchronous counter using JK Flip-Flops.

Solution: The number of FLIP-FLOPs required is 3. Let the FLIP-FLOPs be FF0, FF1, FF2 and their inputs and outputs are

given below:

```
FLIP-FLOP Inputs Outputs
FF0
FF1
FF2
```

### J 0 , K 0

### J 1 , K 1

### J 2 , K 2

### Q 0

### Q 1

### Q 2

The count sequence and the required inputs of FLIP-FLOPs is shown below.

```
FLIP-FLOP INPUTS
Counter state FF0 FF1 FF2
```

```
Q 2 Q 1 Q 0 J 0 K 0 J 1 K 1 J 2 K 2
0 0 0 0 1 1 1 1 0
0 0 1 1 0 0 1 1 0
0 1 0 1 0 1 0 1 0
1 X 1 X 1 X 1 x
X 1 X 1 X 1 X 1
0 1 X x 0 1 X X
X X 0 1 X X 0 1
0 0 0 1 X X X x
X X X X 0 0 0 1
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 4.37. K-Maps of 3-bit Synchronous Counter
```

Example:

Design a natural binary sequence mod-8 synchronous counter using D FLIP—FLOPS.

Solution:

```
The number of FLIP-FLOPS required is 3. Let the FLIP—FLOPS be FF0, FF1 and FF2 with inputs D 0 , D 1 and D 2 ,
respectively. Their outputs are Q 0 , Q 1 , and Q 2 respectively
```

```
Counter State FLIP-FLOP inputs
Q 2 Q 1 Q 0 D 0 D 1 D 2
0 0 0 0 1 1 1 1
0 0 1 1 0 0 1 1
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 1 0 0 1 1 0
0 0 0 1 1 1 1 0
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
Fig. 4.38. K-Maps for 8-bit Synchronous counter
```

The K – maps for D 0 , D 1 and D 2 are given as,

```
Fig. 4.39.
```

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The minimised expressions for D0, D1 and D2 are:

(^) DQ 00 =
D 1 =+Q Q 1 0 Q Q 1 0
D 2 =Q Q 2 0 +Q Q 2 1 +Q Q Q 2 1 0 =Q Q 2 () 0 + +Q 1 Q Q Q 2 1 0 =+Q Q Q 2 (. ) 0 1 Q Q Q 2 ( 1 0)
=Q 2 Q Q 1. 0
The complete circuit of the synchronous counter using positive edge triggered D FLIP-FLOPs is shown in figure below as
Fig. 4.40. 8 - bit Synchronous Counter Circuit
**4.12.2 Synchronous Sequential Circuit Models**
A general block diagram of clocked sequential circuit is also known as finite stable machine (FSM). Depending upon the
external outputs, there are two types of models of sequential circuits.
Mealy Model
In mealy model, the next of the function depends on present state as well as present inputs.
Moore Model
In more model, the next state depends on the present state. The block diagram of a Moore model is given as
Fig. 4.41.
The systematic procedure for designing of clocked sequential circuit is based on the concept of ‘state’. Hence the
sequence of inputs, present & next states and output is represented by a state table or state diagram & if the procedure follows
in the form of flow chart, it is known as algorithms state machine (ASM).
**4.12.3. State Diagram**
It is a directed graph, consisting of vertices (or nodes) and directed are between the nodes. Every state of the circuit is
represented by a node in the graph. A node is represented by a circle with the name of the state written inside the circle. The
directed are represents the state transitions.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

With the circuit in may one state, at the occurrence of a clock pulse, there will be a state transition to the next state and
there will be an output, corresponding to the requirement of the circuit. This state transition is represented by a directed line
and we use each (/) for representing present state and the next state.

Example:

```
Draw the state diagram of D-flip-flop.
```

Solution:

```
The D flip-flop has only input (D) & two output states (Q = 0 & Q = 1).
```

Using the state table or characteristic table of the D-flip flop. The state diagram is given as

```
Fig. 4.42.
```

Example:

Draw the state diagram of a JK flip-flop.

Solution:

A JK flip-flop has inputs (J & K) and one clock input (CLK) and the two output states (Q = 0 & Q = 1).

Using the state table or characteristic table of the JK flip-flop, the state diagram is given as

```
Fig. 4.43.
```

### 

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

5

**NUMBER SYSTEM**

**5. 1. NUMBER SYSTEM**

**5.1.1. Base (Radix)**

Total number of digit used in the system

{Digit 0 – 9) {Digit – 0,1} {Digit 0 – 7} {digit 0 – 9 , A – F}

```
Fig. 5.1.
```

**5.1. 2. Decimal Number System**

... 104 103 102 101 100 10 –^1 10 –^2 10 –^3 ...

... a 4 a 3 a 2 a 1 a 0 a– 1 a– 2 a– 3 ...

ai → Coefficient of decimal number system

10 i^ → Weight of decimal number system

Example: - (501.23) 10
102 101 100 10 –^1 10 –^2

(^5 0 1 2 3)
Base Digit
2 0, 1
3 0, 1, 2
4 0, 1, 2, 3
5 0, 1, 2, 3, 4
6 0, 1, 2, 3,4,5

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

### 7 0, 1, 2, 3, 4, 5, 6

### 8 0, 1, 2, 3, 4, 5, 6, 7

### 9 0, 1, 2, 3, 4, 5, 6, 7, 8

### 10 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

### 11 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A

### 12 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B

### 13 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C

### 14 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D

### 15 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E

### 16 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

**5.1.3 Binary Number System (Base (Radix) = 2)**

... 24 23 22 21 20 2 –^1 2 –^2 2 –^3 ...
... a 4 a 3 a 2 a 1 a 0 a– 1 a– 2 a– 3 ...
2 i → Weight of Binary number system

ai^ → Coefficient of Binary number system {0, 1}

Example:- (101.11) 2
22 21 20 2 –^1 2 –^2

(^1 0 1 1 1)
**5.1.4. Octal Number System (Base (Radix) = 8)**
... 83 82 81 80 8 –^1 8 –^2 8 –^3 ...
... a 3 a 2 a 1 a 0 a– 1 a– 2 a– 3 ...
8 i → Weight of Octal number system
ai^ → Coefficient of Octal number system {0 -7}
Example:- (728.64) 8
82 81 80 8 –^1 8 –^2
(^7 2 8 6 4)
**5.1.5 Hexadecimal Number System (Base (Radix) = 16):**
... 163 162 161 160 16 –^1 16 –^2 16 –^3 ...
... a 3 a 2 a 1 a 0 a– 1 a– 2 a– 3 ...
16 i → Weight of Hexadecimal number system
ai^ → Coefficient of Hexadecimal number system {0 – 9, A–F}
Example: (A2C.F) 16
162 161 160 16 –^1
(^) A 2 C F
**5.1.6. In base conversion 2 key points are there:**
(A) Any base to Decimal conversion
(B) Decimal to any other base conversion

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

(A) Any base to Decimal conversion:

(a a 3 2 a a 1 0 .a−− 1 a 2 )=( ) 10

(^) ( 3 3 2 2 1 1 0 0 1 1 2 2 )
a r a r a r a r a r a r 10
 +  +  +  +  + −−−−^
Case (1) : Binary to Decimal conversion
Ex. (1011.11) 2 = ( ) 10
 (1 2 ) (0 2 ) (1 2 ) (1 2 ) (1 2 ) (1 2 ) +  +  +  +  + ^3210 −−^12
 8 0 2 1 0.5 0.25+ + + + +  10
 (11.75) 10
Case (2) : Octal to Decimal conversion
Ex. (721.4) 8 = ( ) 10
 2 1 0 1
(7 8 ) (2 8 ) (1 8 ) (4 8 ) 10

###  +  +  +  −

### ^

 (^) 448 16 1 0.5+ + +  10
 (465.5) 10
Case (3) : Hexadecimal to Decimal conversion
Ex. (A2B.C) 16 = ( ) 16
 2 1 0 1
(A 16 ) (2 16 ) (B 16 ) (C 16 ) 10

###  +  +  +  −

### ^

###  1

```
10
```

### (10 256) (2 16) (11 1) (12 16 ) +  +  +  −

 2560 32 11 0.75+ + +  10

 (2603.75) 10

Case (4) : Base 5 to Decimal conversion
Ex. (432.22) 5 = ( ) 10

 2 1 0 1 2
(4 5 ) (3 5 ) (2 5 ) (2 5 ) (2 5 ) 10

###  +  +  +  + −−

### ^

 (^) 100 15 2 0.4 0.08+ + + +  10
 (117.48) 10
(B) Decimal to any other Base conversion

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

```
1 2 3 0 1 2
1 2 1 3 4
3 4 2 5 6
```

```
0
0
0
```

```
a a a r x x x
x x r x x x
x x r x x x
```

```
− − − − −
− − − −
− − − −
```

```
  = 
  = 
  = 
```

(a a a a a a a3 2 1 0 − − − 1 2 3 ) 10 =(b b b b x x x3 2 1 0 0 1 2)r

Case (1) : Decimal to Binary Base conversion.
Ex.

Case ( 2 ) : Decimal to Octal Base conversion.
Ex.

Case ( 3 ): Decimal to Hexadecimal Base conversion.
Ex.

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

**5.2. Some Special Case**

Case ( 1 ): Binary to Octal base conversion

Example: (10110111) 2 = ( ) 8

Octal → means base 8

8 = 2^3

Every three digits of binary represent one digit of octal

010 110 111

2 6 7

Hence (10110111) 2 = (2 67 ) 8

Case ( 2 ): Binary to Hexadecimal base conversion

Example: (1011011) 2 = ( ) 16

Hexadecimal → means base 16

16 = 2^4

Every four digits of binary represent one digit of Hexadecimal.

0101 1011

5 11(B)

Hence (1011011) 2 = (5B) 16

**5.1.2. BCD (Binary Coded Decimal)**

- In this each digit of the decimal number is represented by its four-bit binary equivalent. It is also called natural BCD
  or 8421 code. It is weighted code.
- Excess **–** 3 Code: This is an non weighted binary code used for decimal digits. Its code assignment is obtained from
  the corresponding value of BCD after the addition of 3.
- BCO (Binary Coded Octal): In this each digit of the Octal number is represented by its three-bit binary equivalent.
- BCH (Binary Coded Hexadecimal): In this each digit of the hexadecimal number is represented by its four bit binary
  equivalent.
  Decimal
  Digits

```
BCD 8421 Excess – 3 Octal digits BCO Hexadecimal
Digits
```

### BCH

### 0 1 2 3 4 5 6 7 8

### 0000

### 0001

### 0010

### 0011

### 0100

### 0101

### 0110

### 0111

### 1000

### 0011

### 0100

### 0101

### 0110

### 0111

### 1000

### 1001

### 1010

### 1011

### 0 1 2 3 4 5 6 7

### 000

### 001

### 010

### 011

### 100

### 101

### 110

### 111

### 0 1 2 3 4 5 6 7 8

### 0000

### 0001

### 0010

### 0011

### 0100

### 0101

### 0110

### 0111

### 1000

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

### 9

### 1001 1100

### 9 A B C D E F

### 1001

### 1010

### 1011

### 1100

### 1101

### 1110

### 1111

Don’t care values or unused states in BCD code are 1010, 1011, 1100, 1101, 1110, 1111.

Don’t care values or unused states in excess – 3 code are 0000, 0001, 0010, 1101, 1110, 1111.

The binary equivalent of a given decimal number is not equivalent to its BCD value.

Example: 2510 = 11001 2.

The BCD equivalent of decimal number 25 = 00100101 from the above example the BCD value of a given decimal number is

not equivalent to its straight binary value.

The BCO (Binary Coded Octal) value of a given Octal number is exactly equal to its straight binary value.

Example: 258 = 21 10 = (^0101012)
The BCO Value of 25 8 is 010101.
From the above example, the BCO value of a given Octal number is same as binary equivalent of the same number.
The BCH (Binary Coded Hexadecimal) value of a given hexadecimal number is exactly equal to its straight binary.
Example: 2516 = 37 10 = 100101 2
The BCH value of hexadecimal number 25 16 = 00100101.
From this example the above statement is true.
Complement
(r – 1)’s
r’s Complement
Binary
r =2
1’s
2’s
Octal
r = 8
7 ’s
8 ’s
Decimal
r = 10
9’s
10’s
Hexadecimal
r = 16
15 ’s
16 ’s
Example: Add the two Binary numbers 101101 2.
Augned 101101
addend 100111
1111
Sum 1010100
Example: Subtract the Binary number 100111 2 from 101101 2.
Minuend : 101101
Subtracted: 100111
Difference: 000110

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

Example: Multiple the Binary number 1011 2 from 101 2.
Multiplicand: 1011
Multiplier: X101
1011
0000
1011
+
Product: 110111

While storing the signed binary numbers in the internal registers of a digital computer} most significant bit position is always
reserved for sign bit and the remaining bits are used for magnitude.

```
Fig. 5.2.
```

When the binary number is positive, the sign is represented by ' 0 ’. When the number is negative, the sign is represented by ' 1’.

**5.2.2. Fixed-Point Representation and Floating-Point Representation;**

The representation of the decimal point (ordinary point) in a register is complicated by the fact that it is characterized by a

position between two flip- flops in the register.

```
There are two ways of specifying the position of the decimal point in a register.
( 1 ) Fixed Point and
(2) Floating Point.
The fixed point method assumes that the decimal point (or binary point) is always fixed in one position. The two positions
```

most widely used are (1) a decimal point in the extreme left of the register to make the stored number a fraction, and (2) a

decimal point in the extreme right of the register to make the stored number an integer.

The floating-point representation uses a second register to store a number that designates the position of the decimal point in

the first register.

Positive numbers are stored in the registers of digital computer in sign magnitude form only.

Negative number can be represented in one of three possible ways.

1. Signed – magnitude representation.
2. Signed – 1’s complement representation.
3. Signed – 2’s complement representation.

Example: +9 – 9
Signed – magnitude 0 0001001 (a) 1 000 1001 signed – magnitude
(b) 1 111 0110 signed – 1’s complement
(c) 1 111 0111 signed – 2’s complement

GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Digital Electronics
```

The 2’s complement of a given binary number can be formed by leaving all least significant zeros and the first non-zero digit

unchanged, and then replacing 1’s by 0’s and 0’s by 1’s in all other higher significant digits.

Example: The 2’s complement of 10011000 2 is 01101000.

Subtraction using 2’s complement: Represent the negative number in signed 2’s complement from, add the two numbers,

including their sign bit, and discard any carry out of the most significant bit.

Since negative numbers are represented in 2’s compliment form, negative results also obtained in signed 2’s compliment

form.

Example: 1’s complement:

+ 6 0000110 – 6 1111001 + 6 0000110 – 6 1111001
+ 9 0001001 + 9 0001001 – 9 1110110 – 9 1110110
+ 15 0001111 +3 (i) 0000010 – 3 1111100 – 15 (1) 1101111
  Carry + 1 Carry + 1
+ 3 0000011 1110000
  carry carry
  The advantage of signed 2’s complement representation over the signed 1’s compliment from (and the signed – magnitude

form) is that it contains only one type of zero.

The general form of floating – point number is mre. Where M = Mantissa, r = base, e = exponent.

Example: + 0.3574 × 10^5.

The mantissa can be a fixed point fraction or fixed point integer.
Normalization: Getting non-zero digit in the most significant digit position of the mantissa is called Normalization.

- If the floating point number is normalized, more number of significant digits can be stored, as a result accuracy can be
  improved.
- A zero cannot be normalized because it does not contain a non-zero digit. The hexadecimal code is widely used in
  digital systems because it is very convenient to enter binary data in a digital system using hexcode.
- The parity of a digital word is used for detecting error in digital transmission. Hollerith code is used for punched card
  data.
- In weighted codes, each position of the number has specific weight. The decimal value of a weighted code number is
  the algebraic sum of the weights of those positions in which 1's appears.
- Most frequently used weighted codes are 8421, 2421 code, 5211 code and 8421 code.
- Reflective Code: A code is called reflective or self-complimenting, if the code for 9 is the compliment for the code
  for 0, code for 8 is the compliment from 1 and so on. 2421 , 842 ′ 1 ′, 5211 are examples for reflected codes.
- Sequential Code: A code is called sequential, if each successive code-is one binary number greater than its preceding
  code.
  Example: 8421

```

```

**ComputerComputer**

**OrganizationOrganization**

**& &**

**ArchitectureArchitecture**

**Computer**

**Organization**

**&**

**Architecture**

```
Design Against Static Load
```

1. Machine Instructions ........................................................................................................... 4. 1 – 4. 5
2. Addressing Modes ................................................................................................................ 4. 6 – 4. 8
3. ALU Data Path ...................................................................................................................... 4. 9 – 4. 13
4. CPU Control Unit Design ....................................................................................................... 4. 14 – 4. 19
5. Memory Interfacing ............................................................................................................. 4. 20 – 4. 22
6. Input Output Interfacing ...................................................................................................... 4. 23 – 4. 28
7. Pipelining ............................................................................................................................. 4.2 9 – 4. 43
8. Cache Memory ..................................................................................................................... 4. 44 – 4. 48
9. Main Memory ...................................................................................................................... 4. 49 – 4. 51
10. Secondary Storage ................................................................................................................ 4. 52 – 4. 56

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**MACHINE INSTRUCTIONS**

**1. 1 Introduction**

Opcode – Specifies the operation code. The number of bits in opcode depends on total operations.
Address – Specifies the operand address.

- The basic computer has three instruction code formats.
  (i) Memory **–** Reference instruction
  I = O  Direct addressing
  I = 1  Indirect addressing

```
opcode address
```

### 15 12 11 0

```
Instruction format
```

### I

### 14

```
(opcode = 000 to 110)
(ii) Register – Reference instruction
```

```
0 1 1 1 Register Operation
```

(^15 12 11 0)
(opcode = 111, I = 1)
(iii) Input **–** output Instruction
1 1 1 1 I/O Operation

### 15 12 11 0

```
(op code = 111, I = 1)
```

A stack can be placed in a portion of a large memory or it can be organized as a collection of a memory words or registers. i.e.,
it may be
(i) Register stack
(ii) Memory stack

**1.1.1. Register Stack**

- The following figure shows the organization of a 64-word register stack. The stack pointer register SP contains a binary
  number whose value is equal to the address of the word that is currently on top of stack.
- Initially SP is cleared, EMPTY is set to 1, FULL is cleared to 0. If the stack is not full (if FULL = 0), a new item is
  inserted. With a push operation.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
A
```

```
B
```

```
C
```

```
4
3
2
1
0
```

```
DR
```

```
SP
```

```
63
```

```
Address
FULL EMPTY
```

### PUSH:

### SP  SP + 1

### M  DR

```
If (SP = 0) then FULL  1
EMTY  0
```

```
[increment stack pointer]
[write item on top of stack]
[check if stack is full]
[mark the stack not empty]
```

- A item is deleted from the stack if the stack is not empty (if EMTY = 0), called POP operation

DR  M{SP} [Read item from top of stack]

SP  Sp – 1 [Decrement stack pointer]

If (SP = 0) then EMTY – 1

**1.1.2. Memory Stack**

- A stack can be implemented in a random-access memory. The stack can be implemented by assigning a portion of

```
memory to a stack operation and using a processor register as a stack pointer. i.e.,
```

- A new item is inserted with the push operation as follows:

PUSH: SP  SP – 1

M[SP]  DR

- A new item is deleted with a POP operation as follows

DR  M[SP]

```
SP  SP + 1
```

### PC

### AR

### SP

```
Program
(instructions)
```

```
Data
(operands)
```

```
Stack 3000
```

### 2000

### 1000

### 3997

### 3998

### 3999

### 4000

```
Memory unit
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- A stack pointer is loaded with an initial value. This initial value must be the bottom address of an assigned stack in
  memory. SP is automatically incremented or decremented with every PUSH or POP operation.

**1.1.3. Reverse Polish Notation**

- An expression in post fix form is often called reverse polish notation.

The infix expression (A + B) * [C*(D + E) + F] in reverse polish notation as AB + DE + C * F + *

- A reverse polish expression can be implemented or evaluated using stack for the expression
  X  (A + B) * (C + D)
  With values A = 2, B = 3, C = 4, d = 2 is
  X  (2 + 3) * (4 + 2)  Infix expression
  x  23 + 42 + *  Reverse polish expression

**1.2 Instruction Types**

- The basic unit of program is the instruction.

Instructions are classified based on

(1) Opcode – called functional classification

(2) Based on number of references.

**1.3 Functional Classification**

- Data transfer instructions – (LOAD, STOR, MOV, EXCT, IN, OUT, PUSH, POP)
- Arithmetic instructions – (INC, DEC, ADD, SUB, MUL, DIV)
- Logical Instructions & Shift instructions. (CLR, COM, AND, XOR, OR, SHR, SHL, SHRA, SHLA, RO, ROL....)
- Branching instructions. (ABR, JMP, SKP, CALL, RETURN)

**1.4 Based on Number of References**

Based on number of references, the instructions can be classified as

- 4 – address instructions
- 3 - address instructions
- 2 – address instructions
- 1 – address instructions
- 0 – address instructions
- RISC Instructions

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Computer Organizations and Architecture
```

```
(i) 4 – Address Instructions:
```

(^) Opcode A 1 A 2 A 3 A 4

- A 1 , A 2 refers operands
- A 3 refers destination
- A 4 next instruction address.
- Since A 4 is like program counter, the processor which supports 4-address instructions need not use PC.
- The length of instruction is more, hence requires more than one reference.

```
(ii) 3 – address Instructions
```

(^) Opcode A 1 A 2 A 3

- Each address field specify a register or memory operand.
- It results in short program when evaluating arithmetic expressions.
- Requires too many bits to specify three addresses
  Example: To evaluate X = (A + B) * (C + D)
  Add R 1 , A, B R 1  M[A] + M[B]
  Add R 2 , C, D R 2  M[C] + M[D]
  MUL X, R 1 , R 2 M[X]  R 1 * R 2

For these instructions program counter must be required.

```
(iii) 2 – address Instructions:
```

(^) Opcode A 1 A 2

- A 1 – first operand and destination
- A 2 – second operand
- Uses MOV instruction for data transfer

```
Example:
```

```
X  (A + B) * (C + D)
MOV R 1 , A
ADD R 1 , B
MOV R 2 , C
ADD R 2 , D
MUL R 1 , R 2
MOV X R 1
```

```
One of the operand permanently lost.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

(iv) 1 **–** address Instructions

(^) Opcode A 1

- Uses an implied accumulator (AC) register for all data manipulation.
- Easily decoded and processed instructions.

Example: X  (A + B) * (C + D)

LOAD A AC  M[A]

ADD B AC  AC + M[B]

STOR T M[T]  AC

LOAD C AC  M[C]

ADD D AC  AC + M[D]

MUL T AC  AC * M[T]

STOR X M[X]  AC

(v) Zero **–** address Instructions:

(^) Opcode

- The operands are referenced complexity from stack.
- More complex approach than others.
- Any changes in order of operands effect the result.

Example: X = (A + B) * (C + D)
PUSH A
PUSH B
ADD
PUSH C
PUSH D
ADD
MUL
POP X
(vi) RISC Instructions:

- All instructions are executed with in the registers of CPU, without referring to memory (Except LOAD, STOR)
- Uses in RISC processor
- LOAD & STOR are used between data transfer.
  Example: X = (A + B) * (C + D)
  LOAD R 1 , A
  LOAD R 2 , B
  LOAD R 3 , C
  LOAD R 4 , D
  ADD R 1 , R 1 , R 2
  ADD R 3 , R 3 , R 4
  MUL R 1 , R 1 , R 3
  STOR X, R 1

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

2

**ADDRESSING MODES**

**2 .1 Introduction**

The various addressing modes commonly used are:
Implied Mode:

In this mode the operands are specified implicitly in the definition of the instruction.

Example:

- Complement Accumulator (CMA) [All register reference instructions that use an accumulator are implied -
  mode instructions]
- Zero-address instructions in a stack organized computer. [here the operands are implied to be on top of the stack]

Immediate Mode:

In this mode the operand is specified in the instruction itself.

- It is very faster
- Useful for initializing register to a constant value.

Example:

ADD 10 i.e., AC ← AC + 10

- The range of value limited by the address field

Register Mode:

In this mode the operands are in registers that reside within the CPU.

- A K-bit field can specify any one of 2k registers.
- Reduces the length of the address field.

Example:

ADD R1

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

Register Indirect Mode:

In this mode the instruction specifies a register in the CPU whose contents give the address of an operand in memory.

- Before using this mode, the programmer must ensure that the memory address of the operand is placed in the processor
  register with a previous instruction.
- The advantage is the address field uses fewer bits to select or register.
  Example:

ADD (R1)

```
R 1
R 0
```

(^3000)
(^10)
R 1
(^3000)
Autoincrement or Autodecrement Mode:
It is similar to register indirect mode except that the register is incremented or decremented after its value is used to access
memory.
Example:
ADD (R 1 )
R 1
(^3000)
(^10)
(^3000)
R 1
(^20)
(^30)
Direct Addressing Mode:
In this mode the effective address is equal to the address part of the instructions.

- The operand resides in memory and its address is given directly
  by the address field of the instruction.
- Used to represent global variables in a program.
- In a branch type instruction, the address field specifies the actual
  branch address space.
- Allows to access limited address space.
- The effective address is defined to be the memory address
  obtained from the computation dictated by the given addressing
  mode.
- The direct addressing mode is also called “Absolute mode”.

```
Example. ADD 3000
```

(^3000)
(^3000)
(^10)
i.e. AC  AC + M [3000]

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
Indirect Addressing mode:
In this mode, the address field of the instruction gives the
address where the effective address is stored in memory.
```

- Allows to access larger address space
- Requires 2 memory cycles to read an operand

```
Example ADD 3000
```

(^3000)
(^3000)
(^8400)
(^8400 10)
**2.1.1 Displacement addressing modes**
The address field of the instruction added to the content of a specific register in the CPU. i.e,
Effective Address = Address part of instruction + content of Register.
**2.1.2 The Various displacement addressing modes are**
Relative addressing mode:
In this mode the content of program counter (PC) is added to the address part of the instruction.

- The address part is a signed number (2’s complement) that can be either positive or negative.
- The result produces effective address whose position in memory is relative to the address of the next instruction.
  EA = Address Part (off set) + PC value
- Used with branch-type instructions when the branch address is in the area surrounding the instruction word itself.
- The advantage is, address field can be specified with a small number of bits compared to direct address.

Indexed Addressing mode:

```
In this mode the content of an index register is added to the address part of the instruction.
```

- Index register contains index value.
- Address part specifies the beginning address of a data array in memory.
  EA = Address Part (base address of data array) + Index register value (index value)
- Used for accessing array of data.
- The index register can be special CPU register or any general purpose register.
  Base register Addressing mode:

In this mode the content of a base register is added to the address part of the instruction.

- The base register is assumed to hold base address.
- The address field gives the displacement relative to this base address.
  EA = Address Part (displacement/offset) + Base register value (Base address)

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

3

**ALU DATA PATH**

**3 .1 Introduction**

- The sequence of operations involved in processing an instruction constitutes an instruction cycle.
  The instruction cycle consists of phases like.
  (1) Fetch cycle (2) Decode cycle
  (3) Operand fetch cycle (4) Execute cycle
- To perform these, the processor unit has to perform set of operations called “Micro-Operations”.

**3.2 The Basic Operations Performed are**

**3.2.1 Register transfers:**

- In general, the input & output of register Ri are connected to the bus via switched controlled by the signals Ri in and Riout

```
Ri
```

```
Ri out
```

```
Ri in
B
u
s
```

- When Ri in is set to 1, the data on the bus are loaded into Ri.
- When Ri out is set to 1, the contents of register Ri are placed on the bus.
- To transfer the contents of R 1 to register R 4 : R 4  R 1.
- Enable the output of register R 1 by setting R 1 out to 1. This places the contents of R 1 on the processor bus.
- Enable the input to register R 4 by setting R4 in to 1. This loads data from the processor bus into register R 4.

**3.2. 2 Performing ALU operations**

The ALU has two inputs A and B and one output

- A gets operand from output of MUX
- B gets operand from bus
- The result is gets stored in Z-register.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

The sequence of steps for ALU operation R 3  R 1

(1) The contents of R 1 are loaded in Y.
(2) The contents of Y 1 R 2 are applied to A & B inputs of ALU, performs ALU operation & stores the result in Z-
register.
(3) The contents of Z are stored in R 3.

- The sequence of operations is
  (1) R1 out, Yin
  (2) R2 out, select Y, Add, Zin
  (3) Zout, R3 in
  - The functions performed by ALU depends on the signals applied to its control lines. (Here Add line is set to 1).
  - Only one register output can be connected to the bus during any clock cycle.
  - The no of steps indicates no of clocks.

**3.2.3 Fetching a word from memory (read operation)**

- To read a memory word, consider MOV (R 1 ), R 2. The action needed to execute this instruction are
  (1) MAR  [R 1 ]
  (2) Start a read operation on the memory bus
  (3) Wait for the MFC (Memory function to complete) response from memory.
  (4) Load MDR from the memory bus
  (5) R 2  [MDR]
- Hence the memory read operation sequence of operations is
  (1) R1 out, MARin, Read
  (2) WMFC (wait for memory operation to complete), MDR inE
  (3) MDRout, R2 in

### MDR

```
MDRoutE MDRout
```

```
MDRin
```

```
MDRinE
```

```
Memory bus
```

```
data lines
Internal
processor bus
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**3.2.4 Storing a word in Memory (write operation)**

- The sequence of steps for write operation MOV R 2 ,

```
(1) The desired address is loaded into MAR
(2) The data to be written is loaded into MDR
(3) Write command is issued.
(4) Wait for memory operation to complete.
```

- The sequence of operations is
  (1) R1 out, MAR in
  (2) R2out, MDRin, write
  (3) MDRoutE, WMFC

**3.2.5 Branch Instructions**

- A branch instruction replaces the content of PC with the branch target address. The address is obtained by adding an offset
  X, which is given in the branch instruction, to the updated value of PC.
- The control sequence for branching (unconditional is

```
(1) PCout, PCin, Yin, WMFC
(2) Zout, PCin, Yin, WMFC
(3) MDRout, IRin
(4) Offset – of – IRout, Add, Zin
```

**3.2.6 Execution of complete Instruction**

- Executing an instruction requires (Add (R 3 ), R 1 )
  (1) Fetch the instruction
  (2) Fetch the first operand (memory location specified by R 3 )
  (3) Perform the addition
  (4) Load the result into R 1
- The control sequence for the execution of ADD (R 3 ), R 1 in a single-bus organization is

```
(1) PCout, MARin, Read, Select, Add, Zin
(2) Zout, PCin, Yin, WMFC
(3) MDRout, IRin
4) R3out, MARin, Read
(5) R1 out, Yin, WMFC
(6) MDRout, select Y, Add, Zin
(7) Zout, R1 in, End
```

**3.3 Multiple – Bus Organization**

- With simple single bus structure, the resulting control sequence is quite long because only one data item can be transferred

```
over the bus in a clock cycle. To reduce the number of steps needed, most commercial processors provide multiple internal
paths that enable several transfers to take place in parallel.
```

- The three bus organization of data path is

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
Bus A^ Bus B^ Bus C^
```

```
Incrementer
```

### PC

```
Register file
```

```
Instruction
decoder
```

### IR

### MDR

### MAR

### A

### B

### ALU

### R

```
Memory bus
```

- All general – purpose registers are combined into a single block called register file. It has two – outputs, allowing the
  contents of two different registers to be accessed simultaneously and have their contents placed on buses A and B.
  The data on bus ‘C’ to be loaded into third register during same clock.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- Buses A and B are used to transfer the source operands to the A and B inputs of ALU, the result is transferred to the
  destination over bus C.
- The control sequence for instruction ADD R 4 , R 5 , R 6
  (1) PCout, R = B, MARin, Read, Inc PC
  (2) WMFC
  (3) MDTout B, R = B, IRin
  (4) R4 outA, R5 outB, select A, Add, R6 in, end.

Example (1)

```
MAR MDR
```

### IR PC GPRS

### ALU

The ALU, bus & registers in data path are of identical size. All operations including incrementing of PC and GPRSs are to be carried out

in the ALU. 2-clock cycles are needed for memory read operation. (one for loading address in MAR and loading data from memory into
the MDR).

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

4

**CPU CONTROL UNIT DESIGN**

**4 .1 Introduction**

To execute instructions, the processor must have some means of generating the control signals needed in the proper

sequence. The two approaches used for this purpose are

(1) Hardwired control

(2) Micro programmed control

The purpose of control unit is to generate accurate timing & control signals.

**4.1 Hardwired Control**

- The control unit uses fixed logic circuits to interpret instructions and generate control signals from them. Every

```
control signal is expressed as SOP (sum of products) expression and realized using digital hardware.
Control step
counter
```

```
External Inputs
```

```
Condition codes
```

### IR

### CLK

Control signals (^)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- The below figure shows the detailed hardwired control unit design.

```
Step decoder
```

```
External Inputs
```

```
Instruction Condition codes
decoder
```

### CLK

```
Control signals
```

### IR

### INSM

### INS 2

### INS 1

```
Control step
counter
```

```
Encoder
```

```
T 1 T 2 Tn
```

- For executing an instruction completely each step is completed in one clock period. A counter is used to keep

```
track of the control steps.
```

- The required control signals are determined with the following information.

```
(1) Contents of control step counter.
(2) Contents of instruction register
(3) Contents of condition code flags
(4) External input signals, such as MFC and interrupt requests.
```

- The instruction decoder decodes the instruction loaded in IR
- The step decoder provides a separate signal line for each step or time slot in a control sequence.
- The encoder gets input from instruction decoder step decoder, external inputs and condition codes, thus uses to
  generate the individual control signals.
- After execution of each instruction, the end signal is generated which resets control step counter and makes it
  ready for generation of control step for next instruction.

For example:

```
(1) The encoder circuit implements the following logic function to generate Yin.
```

Yin = T 1 + T 5 Add + T 4 BR +.....

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
i.e. Here Yin signal is asserted during time interval T 1 for all instructions, during T 5 for add instruction,
during T 4 for branch instruction.
The generation of Yin control signal is
```

```
T 1
```

```
BR T 4 T 5 Add
```

```
Yin
```

```
(2) The logic function to generate Zout signal can be given by
```

Zout = T 2 + T 7 add + T 6 BR + ......

```
i.e., the Zout signal is asserted during time interval T 2 for all instructions, during T 7 for add instruction,
during T 6 for unconditional branch ........ etc.
```

### T 1

```
BR T 6 Add T 7
```

```
Zout
```

**4.2 Microprogrammed Control**

- Every instruction in a processor is implemented by a sequence of one or more sets of micro operations. Each

```
micro operation is associated with a specific set of control lines which when activated, causes that micro
operation to take place.
```

- Using micro programmed control, control signals are generated by a program. Using this the control signal

```
selection and sequencing information is stored in ROM or RAM called control memory (CM).
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- The control memory is part of control unit; it contains fixed programs (micro programs) that cannot be altered by
  occasional user.
- A control word (CW) is a word whose individual bits represent the various control signals.
- A sequence of CWs corresponding to the control sequence of a machine instruction constitutes the micro
  routine for that instruction, (micro program)
- The individual control words in the microprogram are referred as micro instruction.
- The basic organization of a microprogrammed control unit is

### IR

```
Starting
Address
Generator
```

### UPC

```
Control
store
```

### CW

```
Clock
```

- To read the control words sequentially from the control memory a “micro program counter” (PC) is
  used.

```
Next
address
Generator
```

```
Control
Address
register
(CAR)
```

```
Control
memory
```

```
Control
Data
register
```

```
External I/P
```

sequencer UPC/CAR CDR (^) CW

### CDR

- The sequence of operations are:

```
(1) CAR holds the address of next micro instruction to be read.
(2) When address is available in UPC, the sequencer issues the READ command to CM.
(3) The word from addressed location is read into CDR/UIR.
(4) The UPC is incremented automatically by the clock, causing successive micro instructions to be read from CM.
(5) The contents of UIR generates control signals which are delivered to various parts of the processor in
correct sequence.
```

- The PC or CAR can be updated with various options using the address sequencer circuit as:

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
(1) When a new instruction is loaded in IR, the PC is loaded with the starting address of the micro routine for that
instruction (called mapping process).
(2) When a branch instruction is (micro) encountered and branch condition satisfied, the PC is loaded with the branch
address.
(3) When END instruction is encountered, the PC is loaded with address of first word.
(4) In any other situation, the PC is incremented every time a new micro instruction is fetched from CM.
```

```
1 0 1 1 Address^
```

```
XXXX
```

```
0 1 0 1 1 0 0
```

```
Instruction code
```

```
Mapping
```

```
Micro instruction
address
```

```
Mapping Process
```

- The transformation from the instruction code bits to an address in control memory where the routine is located

```
is called Mapping process.
```

- The basic microinstruction format is
- The function fields (F1, F2, F3,), condition
  field (CD) & Branch field (BR) may be
  optional.

(^) F1 F2 F3 CD BR Address
3 3 3 2 2 7
20 bits (^)
Comparison between Hardwired & Microprogramed
Hardwired Micro programmed

1. Speed Fast Slow
2. Control functions Implemented in Hardwire Implemented in software
3. Ability to handle complex instructions Complex Easier
4. Design process Complicated Orderly and systematic
5. Instruction set size Under 100 Over 100
6. ROM size NIL 2k to 10k
   ( 20 – 400 bit micro instruction)
7. Applications RISC processors CISC, Main frames

**4.2.1. The Micro Programmed Control Unit Can be**

(1) Horizontal Microprogramming:

- One bit per control signal.
- Maximum parallelism i.e., more than one signal can be simultaneously.
- No extra decoders are required for decoding.
- The length of control word is large, need to access more than once from control memory.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

(2) Vertical Microprogramming:

- The control signals are encoded in form for k-bits 2k signals.
- Maximum degree of parallelism is 1.
- The length of micro instruction is small.
- Response is relatively slower.
- Requires a decoder additionally.
- To increase the degree of parallelism soft vertical microprogramming is used which divides the control signals

```
into mutually exclusive groups. Each group is associated with associated number of control bits. (i.e.,
combination of both vertical and horizontal microprogramming).
```

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

5

**MEMORY INTERFACING**

**5. 1 Memory Hierarchy**

- The memory hierarchy system consists of all storage devices.

```
The purpose of memory hierarchy is to bridge the
speed mismatch between the fastest processor to the
slowest memory component at reasonable cost.
```

- In the structure of memory hierarchy Ith level memory
  is physically positioned higher than (I + 1)H level
  memory.
- Let Ti, Si, Ci, & Fi are the access time, size, cost per
  bit and frequency of references to the Ith level
  memory. Therefore

```
Registers
Primary
Cache L1
Secondary
Cache L2
Man memory
(RAM / ROM)
Magnetic disks
```

```
Magnetic Tapes
```

```
Ith
```

```
I+1th
```

Ti < Ti + 1

Si < Si + 1

Ci > Ci + 1

fi > fi + 1

- Since same data presents at different levels. Ith level memory is the subset of I i + 1th level.

i.e. I i  I i + 1

**5.2 Memory Characteristics**

Location: Memory can be placed in 3 locations like registers, main memory, Auxiliary (or) secondary storage.

Capacity: Word size, number of words i.e. capacity = number of words * word size.

Unit of transfer: Maximum number of bits that can be read or written (blocks, bytes...)

Access method: Random or sequential

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

Performance: Access time, memory cycle time, transfer rate, physical type.

Physical: Volatile / non volatile

erasable / non erasable

- When processor reads Ith level memory, if it is found in that level, his will occur otherwise it will be fault.

**5.2.1. In a Two – Level Memory System**

Case **–** I: When fault occurs, in L1 reads from L2 (Proxy Hierarchy)

```
T 1 , S 1 , H 1 , C 1
L 1
```

```
T 2 , S 2 , C 2
L 2
```

Tavg = H 1 * T 1 + (1–H 1 ) * T 2

Case **–** II: When fault occurs in L 1 , must be brought from L2 to L1 memory. (strict hierarchy)

Tavg = H 1 * T 1 + (1–H 1 ) * (T 2 + T 1 )

**5.2.2. In a Three – Level Memory System**

Case **–** I: When fault occurs in one level, then reads from its down level.

```
T 1 , S 1 , H 1 , C 1
L 1
```

```
Serial Access Random Access
```

```
(1) Memory is organized into units of data called
records/blocks accessed sequentially
```

```
(1) Each storage location has an address uniquely
```

```
(2) Access time depends on position of storage
location
```

```
(2) Access time is independent of storage location
```

```
(3) Slower to Access (3) Faster to access
```

```
(4) Cheaper (4) Costly relatively
```

```
(5) Nonvolatile memories (5) May be relative or non
```

```
(6) Example: Magnetic tapes (6) Example: Magnetic disks.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
T 2 , S 2 , H 2 , C 2
L 2
```

```
T 2 , S 2 , H 2 , C 2
L 3
```

Tavg = H 1 * T 1 + (1 – H 1 ) * H 2 * T 2 + (1 – H 1 ) * (1 – H 2 ) * T 3

Case **–** II: When fault occurs, must access from L1.

Tavg = H 1 * T 1 + (1–H 1 ) (H 2 ) (T 2 + T 1 ) + (1–H 1 ) (1–H 2 ) (T 3 + T 2 + T 1 )

* Average cost per bit

CAvg =
1 2

```
1 1 2 2
S S
```

```
CS CS
+
```

```
+
(Two - level)
```

CAvg =
1 2 3

```
1 1 2 2 3 3
S S S
```

```
CS CS CS
+ +
```

```
+ +
(Three - level)
```

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

6

**INPUT OUTPUT INTERFACING**

**6.1 Input – Output Organization**

- The input – output subsystem (I/O) provides an efficient mode of communication b/n system and outside environment.
  The Commonly used peripheral devices are. Keyboard, monitors, printer & magnetic tape, magnetic disc.....
- The input & output devices that communicates with computer & people usually with alphanumeric character from ASCII
  - 128 - character set, 7 – bits are used represent each character. It contains 26 upper case letters, 26 lower case letters, 10
    numerals, 32 special chars such as %, *, $ ...... In general ASCII chars are stored in a single unit called 1 byte (8-bits).
    The 8th bit may be used for parity bit for error detection.

**6.1.1. Input – Output Interface**

- The I/o interface provides a method of transferring information b/n internal storage (main memory) & external I/o devices.

```
The devices/ peripherals connected to a computer need special communication links for interfacing with CPU because.
```

- Peripherals are electromechanical & electromagnetic devices, whereas CPU & memory are electronic devices hence
  the operations are different.
- The data transfer rate is shown then the transfer rate of CPU.
- The data codes & formats are different.
- The operating modes of peripherals is different and must be controlled.
- The four types of I/o command an interface will receive are

**6.1.2. Control Command**

Issued to activate the peripheral & and to inform it what to do. Depending on mode of operation a control command sequence
is issued.

**6.1.3. Status Command**

Used to test various status conditions in the interface & the peripheral. Eg. Checking status of device, errors detected by

interface. The status information is maintained in status register.

**6.1.4. Data Output**

Causes the interface to respond by transferring data from the bus into one of its registers buffer.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**6.1.5. Data Input**

With this command, interface receives an item of data from peripheral & places it in its buffer register. Then transfers to data
bus of processor.

The I/o read & I/o write are enabled during I/o transfer, memory ready & memory write are enabled during memory
transfer. The two configurations possible for communication are.

(a) Isolated I/o:

```
The CPU has distinct input & output instructions, each instruction is associated with the address of an interface register.
When CPU fetches & decodes the opcode, it places address associated with the instruction into the common address lines,
at the same time, it enables the I/o read or I/o write control line.
An isolated I/o method isolates memory & I/o addresses each has its own address space, hence memory address values are
not affected by interface address. Uses one common bus for memory & I/o, with common control lines.
```

(b) Memory **–** Mapped I/o:

In this configuration, only one set of read & write signals and do not distinguish b/n memory & I/o addresses.
and I/o.

**6.2 Modes of Data Transfer**

Data transfer b/n the central computer (main memory) and I/o device may be handled in a variety of modes like

programmed I/o, Interrupt – Initiated I/o & Direct memory access.

**6.2.1. Programmed I/O**

- Programmed I/o operations are the result of I/o instruction written in computer program:
  Example:
  In programmed I/o, the I/o device doesn’t have direct access to memory. A transfer from I/o device to memory
  requires the CPU to extents several instruction.

```
CPU Data Regr^
```

```
Interface
```

```
Staters
register
```

```
Data bus
```

```
Address bus
I/O read
I/O write
```

```
I/O bus
```

```
Data valid
Data
accepted
```

### I/O

```
device
```

F – flag bit (^)

- (Data transfer from I/o device to CPU) The device transfers bytes of data one at a time as they are available. When a byte
  of data is available the device places it on I/o bus and enables its data valid line. The Interface accepts the byte into its
  data register and enables the data accepted line. The interface sets the Flag bit. Then the device disables the data valid
  line, but it will not transfer another byte until the data accepted line is disabled by the interface.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**6 .2.2. Interrupt – Initiated I/O**

- In programmed I/O, the CPU stays in a program loop until the I/o unit indicates that it is ready to transfer. Hence this

```
process keeps processor busy needlessly. meanwhile keeps monitoring the device. When the interface determining that
the device is ready, it generates an interrupt request
```

- Priority Interrupt: It is a system that establishes a priority over the various sources to determine which condition is to

```
be serviced first when two or more requests arrive simultaneously. It also determines which conditions are permitted
during processing of an
```

**6.2.3. Daisy – Chaining Priority (Serial – Priority Interrupt)**

The system consists of a serial connection of all devices that request an interrupt. The device with the highest priority

is placed in first position followed by lower – priority devices. The lowest priority will be placed last in the chain.

```
Device 1
```

```
PI PO
```

```
Device 2
```

```
PI PO
```

```
Device 3
```

```
PI PO
```

```
INT
```

```
CPU
```

```
INTACK
```

```
interrupt Acknowledgement
```

```
Interrupt regst
```

```
To next
device
```

```
Processor data bus
```

**6.2.4. Parallel Priority Interrupt**

- This method uses a register whose bits are set separately by the interrupt signal from each device Priority is established
  according to the position of bits in the register. The CKT will also include a mask register to control the starting of each
  interrupt request. The mask register can be programmed to disable low-priority interrupts while a high – priority device is
  being revised. If will also allow a high-priority device to interrupt the CPU while low – priority device is being serviced.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
0
```

```
1
```

```
2
```

```
3
```

```
Disk
```

```
Printer
```

```
Reader
```

```
Keyboard
```

```
0
```

```
1
```

```
2
```

```
3
```

```
I 0
```

```
I 1
```

```
I 2
```

```
I 3
```

```
Printing
```

```
encoder
```

```
Mask Regr
```

```
Vector Adding to
CPU
```

**6.2.5. Direct Memory Access (DMA)**

- The speed of data transfer can be increased by removing CPU from the path and the peripheral device to manage the

```
memory buses directly. This kind of transfer technique is called DMA transfer during DMA transfer the CPU is idle and
```

```
has no control of the memory buses. The DMA controller takes control of buses to manage the transfer directly b/n i/o
```

```
device & memory.
```

- To keep CPU idle to use bus, the “bus request (BR) input is used by the DMA controller to request the bus to relinquish

```
control of the buses. When BR is active, CPU terminates current execution and places data, control & address lines in high
```

```
impedance state. Then the bus behaves like an open circuit. The CPU then activates. “Bus grant” (BG) output to DMA,
```

```
then DMA takes control of the bus to transfer without CPU intervention, when the transfer completes DMA disables the
```

```
Bus request & CPU disables the bus grant. Then the CPU gets the control of the buses.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**6.3. The DMA Transfer Take Place in Two Modes**

( 1 ) Burst transfer:

```
A block sequence consisting of a number of memory words is transferred in a continuous burst while DMA
controller is master of the memory buses. Used to transfer fast devices like magnetic disks for large volumes. In
this mode the data transfer will not be stopped, until an entire block is transferred.
```

(2) Cycle Stealing:

```
In this mode, DMA controller transfers one word at a time, after which it must return control of the buses to the
CPU, later it will ‘steal’ memory cycle when CPU is idle.
```

```
Data bus
Address
bus
Read
Write
```

### BR

### BG

### CPU

### DMA

```
select
```

```
Register
select
```

```
write
Bus
grant
```

### DS

### RS

### RD

### WR

### BR

### BG

```
Control
logic
```

```
Data bus
buffers
```

```
Data bus
Data bus
Address
register
```

```
Word count
register
```

```
Control
register
```

```
Address bus
buffers
```

```
Address
bus
```

### I/O

```
device
```

```
DMA request
```

```
DMA acknowledgment
```

DMA controller (^)

- The DMA controller communicates with the CPU the data bus and control lines. The register in DMA are selected by
  CPU through address bus by enabling DS & RS inputs. When BG = 1 (bus grant) the CPU has relinquished the buses and
  the DMA can communicate directly with the memory by specifying address in address bus & activating the RD or WR
  control. The DMA communicates with the external device through the request and acknowledge lines.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**6.4. The CPU Initialize the DMA by Sending**

(1) The starting address of memory block where data are available (for read) or where data are to be stored (for

```
write)
```

(2) Word count, the no of words in memory block.

(3) Control of specify mode of transfer such as read or write.

(4) A control to start the DMA transfer.

- Once DMA is initialized, the CPU stops communicating with the DMA unless it receivers an interrupt signal.

**6.5. DMA Transfer**

When the peripheral device sends a DMA request, the DMA controller activates the BR line, informing the CPU to relinquish
the buses. The CPU responds with its BG line, informing DMA that its buses are disabled. DMA then puts the current value of

its address register into the adder bus and initiates RD or WR signal. It then sends DMA acknowledge to the peripheral device.
When BG = 0, then CPU communicates with the internal DMA registers, when BG = 1 then RD & WR lines are used from

DMA controller to RAM to specify read or write operation.

(^) Interrupt
BG
BR
RD WR ADD Data
RD WR ADD Data
DS
RS
BR
BG
Interrupt
Address
select
RD WR ADD Data
RAM
(Random Access
memory)
Read control
Write control
Data bus
Address bus
bus
I/O
Peripheral
device
DMA
acknowledge
DMA request
When the device receives DMA acknowledge, it puts a word in the data bus (write) or receives on word from the data bus
(read). In this way the peripheral communicates with memory without any involvement of CPU. For each word transfer DMA
increments the address register and decrements its word count register. When count reaches to zero, the DMA disables bus
request line so that the CPU can continue to execute its program DMA transfer is very useful for fast transfer of data.
❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

7

**PIPELINING**

**7.1 Introduction**

- “Parallel processing” denotes a large class of techniques that are used to provide simultaneous data–processing tasks for
  the purpose of increasing the computational speed of a computer system.
- The purpose of parallel processing is to speed up the computer processing capability and increases its throughput. “Through
  put” is the amount of processing that can be accomplished during a given interval of time”.
- Parallel processing can be viewed from various levels as

```
(i) At registers level, Registers with parallel load operate with all the bits of the word simultaneously. (Instead
of shift registers). This is at lowest level.
```

```
(ii) Higher level of complexity can be achieved by having a multiplicity of functional units that perform
identical or different operations simultaneously.
```

```
(iii) By distributing the data among the functional units in multiple. Eg: The arithmetic logical & shift
operations can be separated.
```

```
(iv) Using multiple processors. (Flynn’s classification) (SISD, SIMD, MISD, MIMD).
```

```
(v) Using pipelining in unit processor systems.
```

**7.2 Pipelining**

- Pipelining is a technique of decomposing a sequential process into sub operations, with each sub process being executed
  in a special dedicated segment that operates concurrently with all other segments.
- The result obtained from one segment is transferred to the next segment in the pipeline. The final result is obtained after
  the data have passed through all segments.

Example:

```
The perform Ai * Bi + Ci , for i = 1 to 6. Each sub operation multiply & add implemented in a segment with in a pipeline.
Each segment has one or more registers.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

### R1

```
Ai
```

### R2

```
Bi
```

```
Multiplier
```

### R3

```
addder
```

### R4

### R5

```
Ci
```

```
Seg1
```

```
Seg2
```

```
Seg3
```

- R1 through R5 are registers that receive new data with every clock pulse.
- The effect of each clock pulse can be shown as

```
Clock pulse Number
```

```
Segment – 1 Segment - 2 Segment - 3
```

```
R1 R2 R3 R4 R5
```

```
1 A 1 B 1 --- --- ---
```

```
2 A 2 B 2 A 1 * B 1 C1 ---
```

```
3 A3 B3 A2 * B2 C2 A1 * B1 + C1
```

```
4 A4 B4 A3 * B3 C3 A2 * B2 + C2
```

```
5 A5 B5 A4 * B4 C4 A3 * B3 + C3
```

```
6 A6 B6 A5 * B5 C5 A4 * B4 + C4
```

```
7 --- --- A6 * B6 C6 A5 * B5 + C5
```

```
8 --- --- --- --- A6 * B6 + C6
```

- The “General structure” of a “4 – segment pipeline” is

S1 (^) R1 S2 (^) R2 S3 (^) R3 S4 (^) R4
Clock
input

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- The operands pass through all four segments in a fixed sequence.
- Each segment consists of combinational circuit Si that performs a sub operation.
- The segments are separated by registers Ri that holds the intermediate results between stages.
- Information flows between adjacent stages under the control of common clock applied to all registers simultaneously.
- A task as the total operation performed going through all the segments in the pipeline.
- The behaviour of a pipeline can be illustrated with “Space – time diagram”. It shows the segment utilization as a function
  of time. The following diagram is for tasks T1 to T6 executed in 4 – segment pipeline.

```
Segments 1 2 3 4 5 6 7 8 9
```

```
S – 1 T1 T2 T3 T4 T5 T6
```

```
S – 2 T1 T2 T3 T4 T5 T6
```

```
S – 3 T1 T2 T3 T4 T5 T6
```

```
S – 4 T1 T2 T3 T4 T5 T6
```

- “An Arithmetic pipeline divides an arithmetic operation into sub operations for execution in the pipeline segments.”

**7.2.1 Pipeline performance evaluation**

- Consider a K – segment pipeline with a clock cycle time tp is used to execute n tasks.
- To complete n – tasks using a K – segment pipeline requires K + (n–1) clock cycles.

(1) The number of clock cycles needed in a pipeline to execute 100 tasks in 6 segments.

Ans. K = 6

n = 100

 6 + (100-1) = 105 clocks

- The processing time in each stage is called as “stage delay”, In a pipeline. (tp).
- The time delay due to interstage transfer of data is “interstage delay” (td)
- The interstage delays can be same between the stages, stage delay very from stage to stage based on segment operation.

```
The time period for clock cycle, ‘t’p is
```

tp = max {ti} + td

tp = tm + td

Since tm > > td, maximum stage delay denotes the clock period.

i.e. tp = tm

- The total time required in pipeline execution is

TP = [K + (n–1)] * tp.

```
Clock cycles
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**7.2.2 Speed up Ratio**

- The speed up of a K – stage pipeline over an equivalent non-pipelined processor is defined as

```
time with pipeline
```

```
S=time without pipeline
```

- Consider a non-pipeline processor that performs the same operation as pipelined and takes a time equal to “tn” to complete
  each task.

( ( )) p

```
n
K n- 1 *t
```

```
n*t
S
+
```

```
=
```

- As the number of tasks increases, k + n - 1 approaches to n

Since tn ~^ K * tp

### S =

( ( )) p

```
p
K n- 1 *t
```

```
n*K * t
+
```

```
 tn ~^ ntp
```

### S =

K (n- 1 )

```
nK
+
```

```
p
```

```
n
n*t
```

```
S= nt  K + n – 1 ~^ n
```

```
p
```

```
n
t
```

```
t
S=^
```

For large number of tasks

```
K n- 1
```

```
S nk
+
```

```
=
p
```

```
n
t
```

```
t
S=
```

Or

n

```
nK
=
p
```

```
p
t
```

```
K t
S
```

```

=
```

S = K S = K

- The maximum speed up that can be achieved in a pipelined processor is equal to “number of stages”. [as n is large, K + n
  - 1 is K]. (K).

Sideal = Smax = K

**7.2.3 Efficiency**

- The efficiency of a pipeline is defined as the ratio of speed up factor and the number of stages in the pipeline.

( )

```
/K
K n- 1
```

```
nk
K
```

```
E S
k 

```

```


```

```

+
```

```
= =
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
K n- 1
```

```
E n
K= +^
```

```
K
```

```
S
EK=^
```

**7.2.4 Throughput**

- It is the number of tasks that can be completed by a pipeline per unit time.

```
K (K (n- 1 )) tp
H n
+ 
```

```
=
```

**7.2.5 Stall cycle**

- The performance of a pipeline is influence by

```
Number of instructions
Uneven stage delays
Buffer overhead (Interstage delay)
Dependencies.
```

- The objective of pipelines is CPIavg = 1.

```
(i.e. Clocks per instruction – CPI)
```

- Depending on control mechanism used, the pipelines can be categorized as

**7.2.6 I Asynchronous pipeline**

- Data flow along the pipeline stages is controlled by handshaking protector i.e. when Si is ready to send/transmit, it sends
  ready signal to Si+1 and Si+1 send A.
  ck to Si after receiving.

### S 1

```
Input
data
```

Ready (^) S 2
Ack
Ready (^) Sn
Ack
output
data
**7.2.7 II Synchronous pipeline**

- Clocked high speed latches are used to interface between stages. At the falling edge of the clock pulse, all latches transfer
  data to the next stages simultaneously.

```
L
A
T
C
H
```

```
Data
Input
S 1
```

```
L
A
T
C
H
```

```
S 2
```

```
L
A
T
C
H
```

```
Sn
```

```
Clock
```

```
Data
output
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**7.2.8 Instruction pipelining**

- An instruction pipeline operates on a stream of instructions by overlapping the Fetch, Decode, Execute and other phases
  of instruction cycle.
- The instruction cycle with 4 – segments is

```
Instructions 1 2 3 4 5 6 7 8 9
I 1 FI DA FO FX
I 2 FI DA FO EX
I 3 FI DA FO EX
I 4 FI DA FO EX
I 5 FI DA FO EX
```

Here FI - fetches an instruction

DA - Decodes the instruction & calculates effective address

FO - fetches the operand

EX - Executes the instruction

- “In general, each stage in a pipeline is expected to complete its operation in one clock cycle, hence the clock period must
  allow the longest task to be completed.
- “The performance of a pipeline is high if different stages require about same amount of time.”
- The use of cache solves the memory access problem.

(5) Consider a 4–stage pipeline, where different instructions require different number of clock cycles, at different stages.

```
The total number of clocks required for execution of 4 instructions is ______
```

Ans.:

```
1 2 3 4
I 1 2 1 2 2 7
I 2 1 3 3 2 9
I 3 2 2 2 2 8
I 4 1 3 1 1 6
30
```

Through sequential process 30 clocks. But using pipeline the number of clock cycles required is 14. That is,

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14
I1 S1 S1 S2 S3 S3 S4 S4
I2 S1 S2 S2 S2 S3 S3 S3 S4 S4
I3 S1 S1 - S2 S2 - S3 S3 S4 S4
I4 S1 - - S2 S2 S2 S3 - S4
```

```
Clock
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**7.2.9 Data Hazards**

- A data hazard is situation in which the pipeline is stalled because the data to be operated on are delayed for some reason,
  as illustrated in Figure. We will now examine the issue of availability of data in some detail.
- Consider a program that contains two instructions, I 1 followed by I 2. When this program is executed in a pipeline, the
  execution of I 2 can begin before the execution of I 1 is completed. This means that the results generated by I 1 may not be
  available for use by I 2. We must ensure that the results obtained when instructions are executed in a pipelined processor
  are identical to those obtained when the same instructions are executed sequentially. The potential for obtaining incorrect
  results when operations are performed concurrently can be demonstrated by a simple example. Assume that A = 5, and
  consider the following two operations:

A  3 + A

B  4  A

- When these operations are performed in the order given, the result is B = 32. But if they are performed concurrently, the
  value of A used in computing B would be the original value, 5, leading to an incorrect result. If these two operations are
  performed by instructions in a program, then the instructions must be executed one after the other, because the data used
  in the second instruction depend on the result of the first instruction. On the other hand, the two operations.

A  5  C

B  20 + C

- Can be performed concurrently, because these operations are independent.

```
Fig: Pipeline stalled by data dependency between D 2 and W 1
```

- This example illustrates a basic constraint that must be enforced to guarantee correct results. When two operations depend
  on each other, they must be performed sequentially in the correct order. This rather obvious condition has far-reaching
  consequences. Understanding its implications is the key to understanding the variety of design alternatives and trade-offs
  encountered in pipelined computers.
- Consider the pipeline in Figure. The data dependency just described arises when the destination of one instruction is used
  as a source in the next instruction. For example, the two instructions

Mul R2.R3.R4

Mul R5.R4.R6

```
Clock cycle
```

```
Instruction
```

```
I 1 (Mul)
```

```
I 2 (Add)
```

```
I 3
```

```
I 4
```

```
1 2 3 4 5 6 7 8 9
```

```
Time
```

```
F 4 D 4 E 4 W 4
```

```
F 1 D 1 E 1 W 1
```

```
F 2 D 2 D2A E 2 W 2
```

```
F 3 D 3 E 3 W 3
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- Give rise to a data dependency. The result of the multiply instruction is placed into register R4. which in turn is one of the
  two source operands of the Add instruction. Assuming that the multiply operation takes one clock cycle to complete;
  execution would proceed as shown in Figure. As the Decode unit decodes the Add instruction in cycle 3, it realizes that
  R4 is used as a source operand. Hence, the D step of that instruction cannot be completed unit the W step of multiply
  instruction has been completed. Completion of step D 2 must be delayed to clock cycle 5, and is shown as step D2A in figure.
  Instruction I 3 is fetched in cycle 3, but its decoding must be delayed because step D 3 cannot precede D 2. Hence, pipelined
  execution is stalled for two cycles.

**7.2.10 Operand Forwarding**

- The data hazard just described arises because one instruction, instruction I 2 in Figure, is waiting for data to be written in
  the register file. However, these data are available at the output of the ALU once the Execute stage completes step E 1.
  Hence, the delay can be reduced, or possibly eliminated, if we arrange for the result of instruction I 1 to be forwarded
  directly for use in step E 2.
  Figure shows a part of the processor data path involving the ALU and the register file.
- Interstage buffers needed for pipelined operation, as illustrated in Figure. With reference to Figure, registers SRC1 and
  SRC2 are part of buffer B2 and RSLT is part of B3. The data forwarding mechanism is provided by the blue connection

```
Source 1
Source 2
```

```
Register
file
```

```
Destination
```

```
RSLT
```

```
ALU
```

```
(a) Datapath
```

```
SRC1 SRC2
```

```
SRC1, SRC2 RSLT
```

```
Forwarding Path
```

```
W: Write
(Register file)
```

```
E: Execute
(ALU)
```

```
(b) Position of the source and result registers in the processor pipeline
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
lines. The two multiplexes connected at the inputs to the ALU allow the data on the destination bust to be selected instead
of the contents of either the SRC1 or SRC2 register.
```

- When the instructions in Figure 8.6 are executed in the data path of Figure, the operations performed in each clock cycle
  are as follows. After decoding instruction I 2 and detecting the data dependency, a decision is made to use data forwarding.
  The operand not involved in the dependency, register R2, is read and loaded in register SRC1 in clock cycle 3. In the next
  clock cycle, the product produced by instruction I 1 is available in register RSLT, and because of the forwarding connection,
  it can be used in step E 2. Hence, execution of I 2 proceeds without interruption.

**7.2.11 Handling Data Hazards in Software**

- In Figure, we assumed the data dependency is discovered by the hardware while the instruction is being decoded. The
  control hardware delays reading register R4 unit cycle 5, thus introducing a 2-cycle stall unless operand forwarding is
  used. An alternative approach is to leave the task of detecting data dependence and dealing with them to the software. In
  this case, the compiler can introduce the two-cycle delay needed between instructions I 1 and I 2 by inserting NOP (No-
  operation) instructions, as follows:

I 1 : Mul R2, R3, R4

NOP

NOP

I 2 : Add R5, R4, R6

- If the responsibility for detecting such dependencies is left entirely to the software, the compiler must insert the NOP
  instructions to obtain a correct result. This possibility illustrates the close link between the compiler and the hardware. A
  particular feature can be either implemented in hardware or left to the compiler. Leaving tasks such as inserting NOP
  instructions to the compiler leads to simpler hardware. Being aware of the need for a delay, the compiler can attempt to
  reorder instructions to perform useful tasks in the NOP slots, and thus achieve better performance. On the other hand, the
  insertion of NOP instructions leads to larger code size. Also, it is often the case that a given processor architecture has
  several hardware implementations, offering different features.

**7.3 INSTRUCTION HAZARDS**

- The purpose of the instruction fetch unit is to supply the execution units with a steady stream of instructions. Whenever
  this stream is interrupted, the pipeline stalls, as Figure illustrates for the case of cache miss. A branch instruction may also
  cause the pipeline to stall. We will now examine the effect of branch instructions and the techniques that can be used for
  mitigating their impact. We start with unconditional branches.

**7.4 UNCONDITIONAL BRANCHES**

- Figure shows a sequence of instructions being executed in a two-stage pipeline. Instructions I 1 to I 3 are stored at successive
  memory addresses, and I 2 is a branch instruction. Let the branch target be instruction Ih. In clock cycle 3, the fetch operation
  for instruction I 3 is in progress at the same time that the branch instruction is being decoded and the target address
  computed. In clock cycle 4, the processor must discard I 3 , which has been incorrectly fetched, and fetch instruction Ih. In
  the meantime, the hardware unit responsible for the Execute (E) step must be told to do nothing during that clock period.
  Thus, the pipeline is stalled for one clock cycle.
- The time lost as a result of a branch instruction is often referred to as the branch penalty. In Figure, the branch penalty is
  one clock cycle. For a longer pipeline, the branch penalty may be higher. For example, Figure shows the effect of a branch

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
instruction on a four-stage pipeline. We have assumed that the branch address is computed in step E 2. Instructions I 3 and
I 4 must be discarded, and the target instruction, Ih, is fetched in clock cycle 5. Thus, the branch penalty is two clock cycles.
```

- Reducing the branch penalty requires the branch address to be computed earlier in the pipeline. Typically, the instruction
  fetch unit has dedicated hardware to identify a branch instruction and compute the branch target address as quickly as
  possible after an instruction is fetched. With this additional hardware, both of these tasks can be performed in step D 2 ,
  leading to the sequence of events shown in Figure. In this case, the branch penalty is only one clock cycle.

```
(a) Branch address computed in Execute stage
```

```
Clock cycle
```

```
Instruction
```

```
I 1
```

```
I 2 (Branch)
```

```
I 3
```

```
Ik
```

```
Ik+1
```

```
1 2 3 4 5 6
```

```
Time
```

```
F 1 E 1
```

```
F 2 E 2
```

```
F 3 X
```

```
Fk Ek
```

```
Fk+1 Ek+1
```

```
Execution unit idle
```

```
Clock cycle
```

```
I 1
```

```
I 2 (Branch)
```

```
I 3
```

```
I 4
```

```
Ik
```

```
Ik+1
```

```
1 2 3 4 5 6 7 8
```

```
Time
```

```
F 1 D 1 E 1 W 1
```

```
F 2 D 2 E 2
```

```
F 3 D 3 X
```

```
F 4 X
```

```
Fk Dk Ek Wk
```

```
Fk+1 Dk+1 Ek+1
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
(b) Branch address computed in Decode stage
```

**7.4.1 Instruction Queue and Prefetching**

- Either a cache miss or a branch instruction stalls the pipeline for one or more clock cycles. To reduce the effect of these
  interruptions, many processors employ sophisticated fetch units that can fetch instructions before they are needed and put
  them in a queue. Typically, the instruction queue can store several instructions. A separate unit, which we call the dispatch
  unit, takes instructions from the front of the queue and
- Sends them to the execution unit. This leads to the organization shown in Figure 8.10. The dispatch unit also performs the
  decoding function.
- To be effective, the fetch unit must have sufficient decoding and processing capability to recognize and execute branch

```
instructions. It attempts to keep the instruction queue filled at all times to reduce the impact of occasional delays when
fetching instructions. When the pipeline stalls because of a data hazard, for example, the dispatch unit is not able to issue
instructions from the instruction queue. However, the fetch unit continues to fetch instructions and add them to the queue.
Conversely, if there is a delay in fetching instructions because of a branch or a cache miss, the dispatch unit continues to
issue instructions from the instruction queue.
```

```
Clock cycle
```

```
I 1
```

```
I 2 (Branch)
```

```
I 3
```

```
I 4
```

```
Ik
```

```
Ik+1
```

```
1 2 3 4 5 6 7
```

```
Time
```

```
F. D 1 E 1 W 1
```

```
F 2 D 2
```

```
F 3 X
```

```
Fk Dk Ek Wk
```

```
Fk+1 Dk+1 Ek+1
```

```
Instruction fetch unit
Instruction queue
F:Fetch
instruction
```

```
D: Dispatch
Decode
unit
```

```
E: Execute
instruction
```

```
W: Write
results
```

```
...
```

```
Fig: 	Use of an instruction queue in the hardware organization of fig (b)
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**7.5 CONDITIONAL BRANCHES AND BRANCH PREDICTION**

- A conditional branch instruction introduces the added hazard caused by the dependency of the branch condition on the

```
result of a preceding instruction. The decision to branch cannot be made until the execution of that instruction has been
completed.
```

- Branch instructions occur frequently. In fact, they represent about 20 percent of the dynamic instruction count of most

```
programs. (The dynamic count is the number of instruction executions, taking into account the fact that some program
instructions are executed many times because of loops.) Because of the branch penalty, this large percentage would reduce
the gain in performance expected from pipelining. Fortunately, branch instructions can be handled in several ways to
reduce their negative impact on the rate of execution of instructions.
```

**7.5.1 Delayed Branch**

- In Figure the processor fetches instruction I 3 before it determines whether the current instruction, I 2 , is a branch instruction.

```
When execution of I 2 is completed and a branch is to be made, the processor must discard I 3 and fetch the instruction at
the branch target. The location following a branch instruction is called a branch delay slot. There may be more than one
branch delay slot, depending on the time it takes to execute a branch instruction. For example, there are two branch delay
slots in Figure and one delay slot in Figure. The instructions in the delay slots are always fetched and atleast partially
executed before the branch decision is made and the branch target address is computed.
```

- A technique called delayed branching can minimize the penalty incurred as a result of conditional branch instructions. The

```
idea is simple. The instructions in the delay slots are always fetched. Therefore, we would like to arrange for them to be
fully executed whether or not the branch is taken. The objective is to be able to place useful instructions in these slots. If
no useful instructions can be placed in the delay slots, these slots must be filled with NOP instructions.
```

```
LOOP
```

```
NEXT
```

```
Shift left
Decrement
Branch=0
Add
```

```
R1
R2
LOOP
R1.R3
```

```
LOOP
```

```
NEXT
```

```
R2
LOOP
R1
R1.R3
```

```
Decrement
Branch=0
Shift left
Add
```

```
(a) Original program loop
```

```
(b) Reordered instructions
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- The effectiveness of the delayed branch approach depends on how often it is possible to reorder instructions as in Figure.

```
Experimental data collected from many programs indicate that sophisticated compilation techniques can use one branch
delay slot in as many as 85 percent of the cases. For a processor with two branch delay slots, the compiler attempts o find
two instructions preceding the branch instruction that it can move into the delay slots without introducing a logical error.
The changes of finding two such instructions are considerably less than the changes of finding one. Thus, if increasing the
number of pipeline stages involves an increase in the number of branch delay slots, the potential gain in performance may
not be fully realized.
```

**7.5.2 Branch Prediction**

- Another technique for reducing the branch penalty associated with conditional branches is to attempt to predict whether

```
or not a particular branch will be taken. The simplest form of branch prediction is to assume that the branch will not take
place and to continue to fetch instructions in sequential address order.
```

- Until the branch condition is evaluated, instruction execution along the predicted path must be done on a speculative basis.

```
Speculative execution means that instructions are executed before the processor is certain that they are in the correct
execution sequence.
```

- Hence, care must be taken that no processor registers or memory locations are updated until it is confirmed that these

```
instructions should indeed by executed. If the branch decision indicates otherwise, the instructions and all their associated
data in the execution units must be purged, and the correct instructions fetched and executed.
```

```
Clock cycle
```

```
Instruction
```

```
Decrement
```

```
Branch
```

```
Shift (delay slot)
```

```
Decrement (Branch taken)
```

```
Branch
```

```
Shift (delay slot)
```

```
Add (Branch not taken)
```

```
1 2 3 4 5 6 7 8
```

```
Time
```

```
F E
```

```
F E
```

```
F E
```

```
F E
```

```
F E
```

```
F E
```

```
F E
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**7.5.3 Dynamic Branch Prediction**

- The objective of branch prediction algorithms is to reduce the probability of making a wrong decision, to avoid fetching

```
instructions that eventually have to be discarded. In dynamic branch prediction schemes, the processor hardware assesses
the likelihood of a given branch being taken by keeping track of branch decision every time that instruction is executed.
```

- In its simplest form, the execution history used in predicting the outcome of a given branch instruction is the result of the

```
most recent execution of that instruction. The processor assumes that the nest time the instruction is executed, the result is
likely to be the same.
```

**7.6 INFLUENCE ON INSTRUCTION SETS**

- We have seen that some instructions are much better suited to pipeline execution than others. For example, instruction side

```
effects can lead to undesirable data dependencies. In this section, we examine the relationship between pipelined execution
and machine instruction features. We discuss two key aspects of machine instructions – addressing modes and condition
code flags.
```

**7.6.1 Condition Codes**

- In many processors, the condition code flags are stored in the processor status register. They are either set or cleared by

```
many instructions, so that they can be tested by subsequent conditional branch instructions to change the flow of program
execution. An optimizing compiler for a pipelined processor attempts to reorder instructions to avoid stalling the pipeline
when branches or data dependencies between successive instructions occur. In doing so, the compiler must ensure that
reordering does not cause a change in the outcome of a computation. The dependency introduced by the condition-code
flags reduces the flexibility available for the compiler to reorder instructions.
```

```
Clock cycle
```

```
Instruction
```

```
I 1 (Compare)
```

```
I 2 (Branch>0)
```

```
I 3
```

```
I 4
```

```
Ik
```

```
1 2 3 4 5 6
```

```
Time
```

```
F 1 D 1 E 1 W 1
```

```
F 2 D 2 /P 2 E 2
```

```
F 3 D 3 X
```

```
F 4 X
```

```
Fk Dk
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- Consider the sequence of instructions in Figure, and assume that the execution of the Compare and Branch = 0 instructions

```
proceeds as in Figure. The branch decision takes place in step E 2 rather than D 2 because it must await the result of the
Compare instruction. The execution time of the Branch instruction can be reduced
```

Add R1, R2

Compare R3, R4

Branch = 0...

---

(a) A program fragment

---

Compare R3, R4

Add R1, R2

Branch = 0...

---

```
(b) Instructions reordered
```

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

8

**CACHE MEMORY**

**8.1. Introduction**

- The speed of the main memory is very low in comparison with the speed of modern processors. For good performance an

```
efficient solution is to use a fast cache memory.
```

```
Processor Main
memory
```

```
Cache
memory
```

```
Words Blocks
```

Words (^)
➢ It is the smallest and fastest memory component in the hierarchy.
➢ By placing active portions of the program and data in a fast small memory, the average access time can be reduced.
➢ The effectiveness of cache mechanism is based on principle called **“locality of reference”**
➢ The Locality of reference states that, “The references to memory at any given interval of time tend to be confined
within a few localized areas in memory. i.e. many instructions in localized areas of the program are executed
repeatedly. It can be

1. Temporal: It means that recently executed instruction is likely to be executed again very soon.
2. Spatial: It means that instructions in close proximity to Cl recently executed instruction,
   Example: loops, nested loops, procedure calls. Etc.

- The performance of cache is measured using Hit ratio

### 0

```
Hit ratio
```

```
Hit ratio
```

```
no. of hits 100
Total CPU references
no. of hits 10
no.of hits
```

### =

```
no.of misses
```

### 

### 

### =

### +

- The performance of cache can be analysed with the following characteristics.

```
(1) Cache size (Small in KB’s) (2) Block or line size
(3) No. of levels of cache (4) Cache mapping process.
(5) Cache replacement algorithm (6) Cache updating scheme.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**8.2. Cache Mapping Functions**

- Consider a cache consisting of 128 blocks of 16 words cache, assume the main memory is addressable by a 16-bit address.

```
The main memory is addressable by a 16 –bit address. The main memory has 64K words viewed as 4K blocks of 16 words
each.
```

- The various mapping functions are

```
(i) Direct mapping
(ii) Associative mapping
(iii) Set – Associative mapping
```

**8.2.1 Direct Mapping**

- The simplest way to determine cache locations in which to store memory blocks.
- Each block from the main memory has only one possible location in cache.
- Block j of the main memory maps to block j mod n. Where n is the no. of blocks in the cache.

```
Block 0
Block 1
```

```
Block 127
```

```
Tag
Tag
```

```
Block 0
Block 1
```

```
Block 127
Block 128
```

```
Block 255
```

```
Block 3968
```

```
Block 4095
```

```
Block 129
```

```
Page 31
```

```
Page 1
```

```
Page 0
```

- If the processor needs to access same memory locations from two different pages of the main memory frequently, hen miss
  & will be more.
- Easy to implement but hit ratio is less.
- To implement this the address is divided into Three fields.
- Example :

(^5 7 4)
Tag Block Word

- As execution proceeds, the higher order tag bits of the address are compared with the tag bits associated with that cache
  location. If they match, then the desired word is in that block of cache. If there is no match, then miss will occur.
- Requires only one comparison.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

**8.2.2 Associative Mapping**

- In which a main memory block can be placed into any cache block position.
- It gives complete freedom in choosing the cache location in which to place the memory block. Thus the space in the cache

```
can be used effectively.
```

- A new block that has to be brought into the cache has to replace an existing block if the cache is full.
- The cost is high, because of need to search all tag patterns to determine whether a given block is in the cache, i.e.

```
comparison circuit is more complex.
```

- Requires maximum of n comparisons. Where n is the number of cache blocks.
- The no. of tag comparators = no. of cache blocks.
- The address is divided into 2 fields.

```
Block 0
Block 1
```

```
Block 127
```

```
Tag
Tag
```

```
Block 0
Block 1
```

```
Block 127
Block 128
```

```
Block 255
```

```
Block 3968
```

```
Block 4095
```

```
Block 129
```

```
Page 31
```

```
Page 1
```

```
Page 0
```

```
Tag
(12)
```

```
Word
(4)
```

```
16 bits Main Memory^
```

```
Cache
```

- We need an algorithm to select the block to be replaced.

**8.2.3 Set – Associative Mapping**

- For efficiency, a combination of direct and associative mapping techniques can be used.
- Blocks of the cache are grouped into sets, and the mapping allows a block of the main memory to reside in any block of a

```
specific set. i.e. contains several groups of directed mapped caches in parallel.
```

- The contention problem of the direct mapped method is eased by having a few choices for block placement.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

- The hardware cost is reduced for comparing tags unlike associative mapping.
- A block can occupy either of blocks in the set.

```
Block 0
Block 1
```

```
Block 127
```

```
Tag
Tag
```

```
Block 0
Block 1
```

```
Block 63
Block 64
```

```
Block 127
Block 128
```

```
Block 4095
```

```
Block 65
```

```
Page 63
```

```
Page 1
```

```
Page 0
```

- A cache that has K blocks per set, then it is referred as K-way set-associative cache.
- The address is divided into 3- fields.

(^6 6 4)
Tag Set Block
16 bits

- Number of tag comparisons is equal to number of blocks in the set.

**8.3. Cache Replacement Policy**

- In direct mapped cache, the position of each block is predetermined hence no replacement strategy exists.
- In Associative and set – Associative caches there exists some flexibility, when a new block is to be brought into the cache
  and all positions that it may occupy are full. Hence replacement strategy exists.
- The replacement policies are aimed for reducing the penalty (miss) to feature references.
  The various block replacement policies are

```
(1) FIFO: The block which enters first will be the candidate for replacement. i.e. Assumes that, since it has spent long
time in cache all the references to it are slightly exhausted. Implemented using queue data structure.
(2) LRV: The block in the se t which has been in the cache longest with no references to it is selected for the replacement.
(Least recently used).
(3) LFU: The block in the set which has the fewest references is selected for replacement. (Least frequently used).3
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
(4) Random: No specific criteria for replacement of any block. The existing blocks are replaced randomly.
```

**8.4. Cache Updation Policy**

- The two cache updation schemes employed are

➢ Write **–** through: The simplest and commonly used approach. Updation of cache and main memory are done

```
simultaneously.
o Main memory contains the same data as the cache. Which is important for DMA transfers.
```

➢ Write **–** back: In this method, only the cache location is updated during a write operation. The location is then marked by

```
a flag so that later when the word is removed from the cache it is copied into main memory.
o i.e. updation of main memory is postponed until the cache block selected for replacement.
```

**8.5. Cache Memory & Arrays**

An array is a homogeneous collection of data items stored in contiguous memory locations either in row major order or column
major order.

Example:

### 3 1 2

### 5 6 9

### 8 4 7

### 

### 

### 

### 

Row major:

```
3 1 2 5 6 9 8 4 7
```

```
00 01 02 10 11 12 20 21 22
```

Col major:

```
3 5 8 1 6 4 2 9 7
```

```
00 10 20 01 11 21 02 12 22
```

Q.1. Consider an array is A[100] and each element occupies 4 – words, 32 – word cache is used and it is divided into 8 – word
blocks (a) what is the hit ratio for the following instruction.
(a) For (i = 0 ; i < 100 ; i ++ )
A [i] = A [i] + 10 ;

Ans. R W
A[0] M H
A[1] H H
A[2] M H
A[3] H H

(b) How many times block ‘0’ is modified in the cache memory.
Ans. 0, 8, 16, - - - - - 80, 88, 96.  13 times.

(c) How many times block ‘0’ is replaced.
Ans. 12 times.
❑❑❑

### A(0)

### A(1)

### A(2)

### A(3)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

9

**MAIN MEMORY**

**9.1. Introduction**

- The main memory is the central storage unit in a computer system. The principal technology used for the main memory is
  based on semiconductor integrated circuits. Main memory is made up of RAM and ROM chips. Different types of
  integrated circuit memories are given in Table 1.
- Integrated circuit RAM chips are available in two possible operating modes, static and dynamic. The static RAM consists
  of interval flip flops that store the binary information. The stored information remains valid as long as power is applied to
  the unit i.e. ROM is volatile. The dynamic RAM stores the binary information in the form of electric charges that are
  applied to capacitors.

```
Memory Access Volatile Features
```

```
Read/Write
```

```
Random
or serial Yes^
```

```
Data can be read or written with equal case. Used whenever data is needed fast and
often, and is frequently changed.
Read-only
(ROM) Random^ No^
```

```
(a) Data is stored permanently by a masking step during manufacture.
(b) Used whenever data is not to be changed as in fixed tables, constants or computer
instruction sets.
```

```
Programmable
Read-only
(PROM)
```

```
Random No
```

```
(a) Can be programmed after IC is manufactured.
(b) Data is written by opening fusible metal links or P-N junction’s wit high currents.
(c) Can only be written into once. Same use as a ROM, but is cheaper in small
quantities.
```

```
Re-
programmable
read-only
```

```
Random No
```

```
Are ROMs that can be written into many times. Are really “read-mostly” rather than
“read-only” memories Two main types:
(a) Those in which writing is by voltage application and erasing (all data at once) by
exposing chip to ultra-violet radiation through a window on the IC
(b) Those in which reading and writing is electrical. Data remains stored even with
no power applied through the use of MNOS transistors.
Used where frequent or at least more than one change in a program is required as in
debugging a program.
```

```
Content-
addressable
(CAM)
```

```
Random Yes
```

```
This extracts all data in an address when a part of the contents of that address match a
specified number. Used in associative memories to obtain stored data related in some
way to the input data.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
Charge-
coupled device
(CCD)
```

```
Serial Yes
```

```
(a) Digital input is converted to charge and stepped through a shift register.
(b) Requires refresh circuitry to present data loss.
```

```
Programmable
logic array
(PLA)
```

```
Random No
```

```
(a) Is a memory structure that is mask or field (FPLA) programmed as is a ROM.
However, it implements logic function.
(b) Inputs are functions of the input variables and the logic operation stored in the
address.
(c) Is more flexible than random (hard-wired separate IC) circuits because PLAs
and FPLAs are programmable.
```

Refreshing is done by cycling through the words every few milliseconds to restore the decaying charge. The dynamic RAM

offers reduced power consumption and larger storage capacity in a single memory chip. The static RAM is easier to use and

has shorter read and write cycles. The Table 2 shows the summary of various types of integrated circuit memories.

```
(a) Types of Memory Access
Random access Any address can be accessed at random, that is, without going through other address first. Data
retrieval time is relatively fixed.
Serial access Typified by shift register or charge-coupled-device (CCD) memories. Data retrieval is serial in a
fixed order. All data ahead of required data must be read first.
(b) Static verses Dynamic Storage
Static storage Data is stored in flip-flops or other memory cells in which the data does not deteriorate with time.
```

```
Dynamic storage Data is stored in leaky capacitors so that refresh circuitry is required to prevent data loss.
```

**9.2. Memory Interface**

A computer uses memory capacity of 512 bytes of RAM and 512 bytes of ROM. The IC sizes of RAM and ROM are 128 x 8

and 512 × 8 bits respectively.

(a) Find the number of RAM ICs.

(b) Find the number of ROM ICs.

(c) Give the memory map of the system

(d) Mention the size of decoder.

(e) Give the diagram of memory connection to the CPU.

Solution:

(a) The number of RAM ICs =
RAM IC size

```
Total'RAM size
```

=
128 8

```
512 8

```

```

```

= 4

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

(b) The number of ROM ICs =
ROM IC size

```
Total'ROM size
```

=
512 8

```
512 8

```

```

```

= 1

(c) The memory map of this system is given by Table. 3

```
Component Hexadecimal address
```

```
Address bus
10 9 8 7 6 5 4 3 2 1
```

RAM 1 0000 – 007F (^0 0  0)       
RAM 2 0030 – 00FF 0 0 1       
RAM 3 0100 – 017F (^0 1  0)       
RAM 4 0180 – 01FF (^0 1  1)       
ROM 0200 – 03FF (^1)         
(d) 2 × 4 decoder
Each RAM receives the seven low-order bits of the address bus to select one of 128 possible bytes. The
particular RAM chip selected is determined from lines 8 and 9 in the address bus. This is done through a
2 × 4 decoder. The outputs of decoder are given to the CSI inputs in each RAM chip. Thus when address
lines 8 and 9 are equal to 00, the first RAM chip is selected when 01, the second RAM chip is selected and
so on.
(e) The connection of memory chips to the CPU is shown in Fig. RAM and ROM chips are connected to a CPU
through the data and address buses. The low order lines in the address bus selected the byte within the chips
and other lines in the address bus select a particular chip through its chip select inputs.

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

10

**SECONDARY STORAGE**

**10. 1 Introduction**

- The cost per bit of stored information is high in c semi-conductor memories (main memory). This limits the use of these
  memories for large storage. Large storage requirements of most of computers are economically fulfilled by magnetic disks,
  magnetic tapes and optical disk memories. These memories are referred as secondary storage devices.

**10.2 Magnetic Disks**

- A magnetic disk is a thin, circular metal plate. It is coated with a thin magnetic film usually on both sides.
- Digital information is stored on the magnetic disk by magnetizing the magnetic surface in a particular direction.
- Magnetic disks are semi random access memories.

```
The head consists of a magnetic yoke and the magnetizing
coil. The Digital information can be stored on the film by
applying current pulses of suitable polarity.
```

```
Coil^
```

```
Yoke
```

Magnetic thin film (^)
**10.2.1. Data organization & Formatting**

- The data on the disk is organized in a concentration set of rings. These concentric set of rings are called tracks.

```
✓ Each track has same width as head and adjacent tracks are separated by gaps.
✓ Each track is divided into manageable units called sectors.
✓ Each sector stores a block of data which can be transferred to or from the disk.
✓ The universal size of sector is 512 bytes.
✓ The R/W head is capable of reading a sector from disk and writing a sector to disk.
✓ Placing R/W head on desired track is random access and reading concerned sector is serial. Hence disks are semi
random access devices.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
Inter track Gap
```

```
Sectors
```

```
Tracks
```

Inter sector gap (^)
**10.2.2. Physical Characteristics**
(i) Head Motion - Fixed head (one per track)
Movable head (one per surface)
(ii) Disk portability - Non removable or Removable
(iii) Sides - Single sided, Double – sided.
(iv) Disk/surface - Single surface, Multiple – surfaces
(v) Head Mechanism - Contact, fixed Gap, Aerodynamic Gap.
Surface 1
Surface 0
Spindle
R/W Head
(1 per surface)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

A vertical set of all of the tracks with the same number on each surface of a diskette or hard disk is called “cylinder.”

(vi) Platters - Single platter,

Multiple platters – some disk
Accommodate multiple platters

Stacked vertically a fraction of an inch apart.
(1) If all the tracks are having constant capacity then the disk moves with “constant angular capacity” and “recording density”
varying from track to track.

(2) If each track is having variable capacity then the disk is moving with “constant linear velocity”

- Placing the control information in the sector is called as formatting.
- The disk controller is the hardware interface to control the operation of a disk drive. Used to control more than one
  drive. The major functions are seek, read, write and error checking.
- The start and end of each sector is determined by the control data stored in the sector.
- Disk performance parameters:

Seek Time: It is the time required to more the disk arm to the required track.

Rotational Delay: The time taken for the beginning of sector to reach. (latency)

Access time: The sum of seek time and the rotational delay.

- The average time to disk access is

tavg = tseektime + trotational delay + tdata transfer + tover (^) head

- Maximum Recording Density (P) = No. of Bytes/cm
- Data transfer rate (D) = Number of Bytes/Sec.

**10.3 Secondary Storage Devices**

**10.3.1. Magnetic Tapes**

- Magnetic tape is one of the most popular storage medium for large data that are sequentially accessed and processed.
- The tape is formed by depositing magnetic film on a very thin and ½ or ¼ inch wide plastic tape.
- Usually, iron oxide is used as a magnetizing material.
- The information is recorded on the tape with the help of read/write head. It magnetizes or non magnetizes tiny invisible
  spots (1’s & 0’s).
- Usually 7 or a bits are recorded (a character) in parallel across the width of the tape, perpendicular to the direction of

```
motion. A separate R/Wo head is provided for each bit position on the tape.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
Magnetic field
```

```
Plastic tape
```

```
R/w Head
```

- Data on the tape are organized in the form of records separated by gaps.
- A set of related records constitutes a file.

```
1
```

```
2
```

```
3
```

```
4
```

```
5
```

```
6
```

```
7
```

```
8
```

```
9
```

```
Parity bit
```

```
Tracks
```

- The data on a 9 th track (a) tape is stored in parallel consists of data byte and a parity bit.

```
Record Record Gap
```

```
File Mark File
```

File Gap (^)

- Data transfer takes place when the tape is moving at constant velocity relative to a read/write head.
- Hence the maximum data transfer rate depends largely on the storage density along the tape and speed of the tape.
- The file mark is used as header or identifier.
- The information on the magnetic tape is organized into blocks. These blocks have a fixed length and separated by gap
  between them.
- If the block length is BL and inter block gap length is GL, then the utilization factor of the tape (u) is given by

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Organizations and Architecture
```

```
L L
```

```
L
B G
```

```
B
u
+
```

```
=^
```

- The unit of data transfer is a record.
- The tape is moving with a linear velocity and Read/write head is constant.
- Let L is the length of the tape,
  - N is the number of parallel tracks,
  - P is the constant recording density.

(i) Capacity of the tape

C = L  N  P

(ii) Let V is the linear velocity of the tape, then the data transfer rate
D = V * N * P
✓ With utilization factor, the effective data transfer rate is

```
Deff = D *
L L
```

```
L
B G
```

```
B
+
✓ Due to inter block gap and time needed to start and stop and tape between accesses, the effective data transfer rate deff
is actually less than the maximum rate d.
```

```
D G ss
```

```
D
eff t t t
```

```
t d
d
+ +
```

```

=^
```

```
tD = time to scan a data block
tG = time to scan the inter block gap.
Tss = time to start and stop the tape.
```

.


**ProgrammingProgramming**

**&&**

**Data StructuresData Structures**

**Programming**

**&**

**Data Structures**

```
Design Against Static Load
```

1. Data Types and Operators ................................................................................................... 5. 1 – 5. 5
2. Control Flow Statements ...................................................................................................... 5. 6 – 5. 8
3. Storage Class & Function ..................................................................................................... 5. 9 – 5. 12
4. Arrays and Pointers .............................................................................................................. 5. 13 – 5. 22
5. Strings .................................................................................................................................. 5. 23 – 5. 26
6. Types of Data Structure, Array & Linked List ........................................................................ 5. 27 – 5. 31
7. Stack and Queue .................................................................................................................. 5. 32 – 5. 33
8. Tree Data Structure .............................................................................................................. 5. 34 – 5. 38
9. Graph Traversal ................................................................................................................... 5. 39
10. Hashing ................................................................................................................................. 5. 40 – 5. 41

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**DATA TYPES AND OPERATORS**

**1. 1 Data Types**

**1.1.1 Primitive Data Type**
(a) Integer Types:
✓ short int, unsigned short int
✓ int, unsigned int
✓ long int, unsigned long int
✓ long long int, unsigned long long int

(b) Character Types:
✓ char,unsigned char

(c) Floating Types:
✓ float, double, long double

(d) Other:
✓ void, bool

**1.1.2 Non – Primitive Data Type**
(a) Derived data type:
✓ Array
✓ Pointer
✓ String

(b) User defined data type:
✓ Structure
✓ union
✓ Enum
✓ typedef

- C standard does not specify how many bits or bytes to be allocated for every type and different compiler may choose
  different ranges.
- Only restriction is that short and int types are at least 16 bits, long types are at least 32 bits and short is no longer than int
  which is no longer that long type.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**1.2 Operators**

Depending upon the number of operands, an operator in C language can be unary, binary or ternary.

**1.2.1 Arithmetic Operators**
(i) Addition (+)
(ii) Subtraction (-)
(iii) Multiplication ()
(iv) Division (/)
(v) Modulus (%)

- Both operands for % operator must be integer types, otherwise error will be raised.
- The sign of the result for modulo operator is machine dependent.

**1.2. 2 Relational Operators**
(i) Less than (<)
(ii) Greater than (>)
(iii) Less than equal to (< =)
(iv) Greater than equal to (> =)
(v) Equal checking (= =)
(vi) Not Equal to (! =)

- The result of these operators is always 0 to 1
  Ex.1: printf (“%d”,20 > 10)
  O/P: 1
  Ex.2: printf (“%d”,20 = = 10)
  O/P: 0
  **1.2. 3 Assignment Operator (=)**
- Used to assign a value or value of an expression to a variable.
- Typically, the system is
  Lvalue = Rvalue
- Lvalue must be a variable.
- Lvalue cannot be a literal or expression.
- Rvalue can be an expression, variable, literal.

Ex1.
The following are invalid
10 = a;
a + b = c;

- The result of assignment statement is the value we are assigning i.e......
  int x;
  x = 3 + (x = 10); is perfectly valid.
  Firstly x = 10 evaluated and
  ( 1 ) 10 is assigned to x (2) then the result of (x = 10) will be 10
  so,
  x = 3 + 10

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

x = 13
Finally, 13 is assigned to x.

**1.2.4 Logical Operators**
(i) Logical AND (&&)
(ii) Logical OR (||)
(iii) Logical NOT (!)

- Just like rational operators, the result of every logical operator is either 0 or 1.
- Logical NOT is a unary operator
- Logical NOT converts a non-zero operand into 0 and a zero operand in 1.

**1.2.5 Short Circuiting in Logical Operators**

- In case of logical AND, the second operand is evaluated only if the first operand is evaluated to be true.
  If the first operand is evaluated as false then the second operand is not evaluated.
- In case of logical OR operation, the second operand is not evaluated if the first operand is evaluated as true.
  Example1: void main () {
  printf (“Hello”) || printf (“Pankaj”);
  }
  O/P: Hello
  printf function display everything written within double quotes on the monitor and the result / value returned
  by printf () is the number of characters successfully displayed on the screen.
  So, printf (“Hello”) prints Hello and return 5.
  So, the expression
  printf (“Hello”) || printf (“Pankaj”);
  becomes
  5 || printf (“Pankaj”)
  As the first operand for logical OR is evaluated as true, second printf () will never execute.

**1.2. 6 Increment and Decrement Operators**
(i) pre increment ++x
(ii) post increment x++
(iii) pre decrement - - x
(iv) post decrement x - -

- unary operator.
- can’t be applied on constant / literals.
- Pre increment: can be viewed as 2 step operators.
  1 st step: Increment the value of variable.
  2 nd step: After increment, use the value of variable.
- Post increment: can be viewed as 2 step operators
  1 st step: Use the value.
  2 nd step: Increase the value of variable by 1.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**1.2.7 Bitwise operators**
(i) Bitwise AND (&)
(ii) Bitwise OR (|)
(iii) Bitwise XOR (^)
(iv) Bitwise Left Shift (<<)
(v) Bitwise Right Shift (>>)
(vi) Bitwise Not ( )

- All these operators work on binary representation of numbers.
- Typically, faster than arithmetic operators and other operators.

#include<stdio.h>
int main () {
int x = 3, y = 6;
printf (“%d\n”,x & y); // output 2
printf (“%d\n”,x|y); // output 7
printf (“%d\n”, x^y) // output 5
return 0;
}
binary representation of 3: 00000000...0011
binary representation of 6: 00000000...0110
3 & 6: 00000000...0010
3 | 6: 00000000...0111
3 ^ 6: 00000000...0101
XOR of two bits is 1 if both bits are different.
XOR of two bits is 0 if both bits are same.

-  x has output as – (x + 1)
- printf (“%d\n”, ~2) has output -3 i.e., -(2 + 1)
- Comma has lowest precedence among all operators in C language.
- sizeof() is used
  (i) To find the number of elements present in an array.
  (ii) To dynamically allocate block of memory.

**1.2. 8 Ternary operator (? :)**

- It requires 3 operands i.e., Left, Middle, Right
  Left? Middle : Right
- If left expression evaluates as true, then the value returned is middle argument otherwise the returned value is
  Right expression
  int a;
  a = 7 > 2? 3  2 + 5 : 6! = 7
   Left expression: 7 > 2 is true
   So, the value returned would be the middle argument.
  i.e., 3  2 + 5 = 11
  so, a will get 11.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

Note:
(a) No of ‘?’ and ‘:’ should be equal.
(b) Every colon (:) should match with just before ‘?’.
(c) Every? followed by : not immediately but following.
Example: int a;
a = 2 > 5? 10 : !5! = 2 > 5? 20 : 30

L 1 M 1 R 1
2 > 5 is false.
so, for Leftmost? the value returned is its right expression.
a =! 5! = 2 > 5? 20 : 30 :

Left Mid Right

Left expression:
!5! = 2 > 5
0! = 2 > 5
0! =0
0 i.e., false.
As left operand is false, the final value is right expression
a = 30

```
Operators Associativity
() [] ->. Left to right^
!  ++ -- + - * (type) size of Right to left
* / % Left to right
+ - Left to right
<< >> Left to right
< <= > >= Left to right
= =! = Left to right
& Left to right
^ Left to right
| Left to right
&& Left to right
|| Left to right
? : Right to left
= += -= *= /= %= &= ^= |= <<= >>= Right to left
, Left to right
```

```

```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

2

**CONTROL FLOW STATEMENTS**

**2.1 Switch Statement**

- “Case Value” can be of character type and int type.
- There can be one or many number of cases.
- Statements associated with a matching case executes until a break statement is reached.
- The position of default case does not matter. It can be placed anywhere.
- Default case is optional.
- Duplicate case labels are not allowed.
- Statements written before all the cases are ignored by the compiler.
- The break statement is optional.
- Case label cannot be a variable.

**2.2 Iterative statements (Loop)**

An iterative statement, or loop, repeatedly executes a group of statements, known as body of loop, until the controlling
expression is false.
**2.2.1 For Loop**

- The for statement evaluates 3 expressions and executes the loop body until second controlling expression
  executes to false.
- It is recommended to use for loop when the number of iterations is known in advance.
- Syntax of for loop is:
  for (expression – 1(optional); expression – 2(optional); expression – 3(optional))
  {
  statement – 1
  statement – 2

statement – n
}

- for loop executes the loop body 0 or more times.
- for statements works as follows:
  (a) expression – 1 is evaluated once before the first iteration of the loop.
  (b) expression – 2 is a expression that determines whether to terminate the loop. expression – 2 is evaluated before every
  iteration.
  If the expression is true (non - zero), the loop body executed.
  If the expression is false (zero), execution of the for statement is terminated.
  (c) expression – 3 is evaluated after each iteration.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

(d) The for statement executes until expression-2 is false (0), or until a jump statement terminates execution of the loop.

- All 3 expression can be omitted
  (a) If we omit expression-2, the condition is considered as true for an example:
  for (i = 0; ; i++) represent an infinite loop
  statement.

**2.3 While Statement**

- The while statement evaluates a controlling expression before every execution of the loop body.
- If the controlling expression is true (non-zero), the loop body is executed. If the controlling expression is false (zero),
  then the while statement terminates.
- Syntax:
  while (expression) while (expression)
  OR {
  statement statement- 1
  statement- 2

statement-n
}

**2.4 Do-while Loops**

- Both for and while loop checks the loop termination condition before every iteration but do while loop check the
  condition after executing the loop body.
- do while loop body executes at least 1 time, no matter whether the loop termination condition is false or true.
- Syntax is:
  do do {
  statement statement- 1
  OR statement- 2
  while (expression);
  statement-n
  } while (expression);

**2.5 Break Statement**

- The break statement provides an early exit from for, while and do while.
- A break statement causes the innermost loop or switch to be exited immediately.
- In implementation, when we know the maximum number of repetition but some condition is there, where we require to
  terminate the repetition process, then use break statement.
  Example:
  void main ()
  {
  int i = 1;
  while (i < = 15)
  {

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

printf(“%d\t”,i);
if (i > 4)
break;
i = i + 1;
}
printf(“End”);
}
Output: 1 2 3 4 End
In above code, when i becomes 5, the condition i > 4 becomes true, so break statement executes & control passed outside of
the loop body i.e., printf(“End”) executed.

**2.6 Continue Statement**

- Continue statement is related to break but it is not used that much frequently.
- Whenever continue is encountered in a loop, it skips the remaining statement of the current iteration and continues with
  the next iteration of the loop.
- Only applicable with loops, not with switch statement.
  Example:
  void main () {
  int i = 1;
  for (i = 1; i < = 10; i++)
  {
  if(i%2 = = 0)
  continue;
  printf(“%d”,i);
  }
  }
  Output: 13579 (All odd numbers between 1 to 10)
  whenever i becomes even, condition i%2 = = 0 becomes true & continue causes the control to go to i++ & printf is skipped.

### 

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

3

**STORAGE CLASS & FUNCTION**

**3.1 Memory Organization of C Program**

**3.1.1 Code Segment**

- It is also known as text segment.
- It contains executable instructions and this segment is a read only segment.
- Usually, this section is sharable.
  **3.1.2 Uninitialized data segment**
- This section contains all static and global variables that are not initialized by the programmer and hence initialized to
  zero (default value).
  **3.1.3 Initialized data segment**
- This section contains all static and global variables that are initialized by the programmer.
  **3.1.4 Stack**
- In this local variables are stored and some other information is also saved.
- A set of values stored for a function is called as stack frame which atleast contain return address.
  **3.1.5 Heap**
- This area is responsible for dynamic memory allocation. The heap area is managed by malloc(), calloc(), ralloc() and free()
  which may be use brk() and sbrk() system calls.
  **3.1.6 Static Memory**
- Compile time allocation
- Static variable
- Global Variable

**3.2 Storage Classes**

```
Storage
Class
```

```
Scope Life Time Default Storage area
```

auto Local (^) functionWithin Garbage Value RAM
static Local
Till end of
main
program

### 0 RAM

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

```
extern Global
```

```
Till end of
main
program
```

### 0 RAM

```
Register Local Within
function
```

```
Garbage Register
```

- Stack Overflow: Abnormal Termination
- If conflict between global and local variable occurs, then local variable gets preference.
- Declaration of a register variable is only a recommendation/request not a command.
- Cannot apply ‘&’ operator with register variable.
- No physical memory is allocated using ‘extern’ keyword.
- Extern declaration is mandatory when an external variable is referred before it is defined or if it is defined in
  some other source file from the file where it is being used.
- Declaration of an external variable tells about the properties like its type, while definition leads to storage allocation.

**3.3 Recursion**

Definition: When the body of a function call the function itself directly or indirectly.

- Certain arguments for which the function does not call itself are called as base argument, base values.
- In general, for recursion to be non-cyclic whenever a function calls itself the formal arguments must get closer to the base
  argument.
  Example 1:
  Consider the factorial code:
  int factorial (int n)
  {
  if (n = = 0)
  return 1;
  else
  return n * factorial (n - 1);
  }
  If we call factorial (3), it will call factorial of 2 and so on ...the argument will get closer to 0 i.e., the base argument.
- Recursion code is shorter than iterative code.
- Overhead is present.
- Some standard problems are best suited to be solved by using recursion for example- Tower of Hanoi, Factorial, merge
  Sort.

**3.4 Static and dynamic scoping**

**3.4.1 Static Scoping**
Static scoping is also called as lexical scoping. In this scoping, the binding of a variable can be determined by the program text.
In this type of scoping compiler first looks in the current block (local), then in global variables i.e., local and then ancestors’
strategy is followed.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

Example 1 :
int a = 10;
void main ()
{
int a = 1;
{
int a = 2
printf(“%d”,a);
}
}
Output: 2
As printf is referring to a, compiler first check in the current block & gets a variable whose value is 2.

Example 2:
int a = 10;
void main ()
{
int a = 1;
{
Scope S 1 int b;

Scope S 2 printf(“%d”,a);

}
}
Output: 1
Compiler looks for ‘a’ in scope S 1 , because S 1 does not have variable a, it will look into higher scope S 2 that contains a variable
name a whose value is 1.
**3.4.2 Dynamic Scoping**
In this type of scoping, the compiler first searches the current block and then successively searches all calling functions.
Example:
int i;
program main ()
{
i = 10;
call f ();
}
procedure f ()
{
int c = 20;
call g();
}
Procedure g() {
print i;
}
Assuming that the above program is written in a hypothetical programming language which allows global variables

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

and dynamic scoping, let’s try to find the output.
The order of function calls is:

```
main () ⎯⎯⎯⎯→calling f()⎯⎯⎯⎯→calling g()
```

g() is printing i, which is not present inside current block. So, because of dynamic scoping compiler will go to the function that
calls g() i.e., compiler will search f() for variable i. Hence 20 is printed.

### 

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

4

**ARRAYS AND POINTERS**

**4.1 Array**

- An array is defined as the collection of similar type of data items stored at contiguous memory locations.
- Arrays are the derived data type in C programming language which can store the primitive type of data such as int, char,
  double etc.
- It has the capability to store the collection of derived data types such as pointer, structure etc.
- Each element of an array is of same data type and carries the same size example int = 4 byte.
- Elements of the array are stored at contiguous memory locations, meaning, the first element is stored at the smallest
  memory location.
- Elements of the array can be randomly accessed since we can calculate the address of each element of array with the given
  base address and size of the data element.

**4.1.1 Advantages of C Array**

1) Code Optimization: Less code to access the data.
2) Ease of traversing: By using the for loop, we can retrieve the elements of an array easily.
3) Ease of sorting: To sort the elements of the array, we need a few lines of code only.
4) Random Access: We can access any element randomly using the array.
   **4.1.2 Disadvantages of Array**

- Fixed Size: 1) Whatever size, we define at the time of declaration of the array, we can’t exceed the limit.
  2) It does not grow the size dynamically like linked list.
  Declaration of C Array
  Syntax:

Example:

```
Initialization of C array:
```

```
We can initialize each element of the array by using the index. Suppose array int marks [5]. Then
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

```
marks [0] = 80
marks [1] = 60;
marks [2] = 70;
marks [3] = 85;
marks [4] = 75;
```

```
C Array Example:
# include <stdio.h>
int main ()
{
int i = 0;
int marks [5];
marks [0] = 80;
marks [1] = 60;
marks [2] = 70;
marks [3] = 85;
marks [4] = 75;
for(i = 0; i<5; i++)
{
printf(“%d\n”,marks[i]);
}
return 0;
}
```

**4.1.3 Array: Declaration with Initialization**

- We can initialize the C array at the time of declaration.
  Example: int marks [5] = {20, 30, 40, 50, 60};
- In such case, there is no requirement to define the size.
  Example: int marks [ ] = {20, 30, 40, 50, 60}
  Example:

# include<stdio.h>

int main ()
{
int i = 0;
int marks [5] = {20, 30, 40, 50, 60}
for(i = 0; i < 5; i++)
{
printf(“%d\n”,marks[i]);
}
return 0;
}

```
80 60 70 85 75
Marks [0]
Marks [1]
Marks [2]
```

```
Marks [4]
```

```
Marks [3]
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**4.1.4 Two-Dimensional Array**

- The two-dimensional array can be defined as an array of arrays.
- The 2D array is organized as matrices which can be represented as the collection of row and columns.

**4.1.5 Declaration of two-dimensional array in C syntax**

Example:

Initialization of 2D Array

Example: Program of Two-Dimensional Array

# include<stdio.h>

int main()
{
int i = 0, j = 0;
int arrayHello[4][3] = {{1, 2, 3}, {2, 3, 4}, {4, 5, 6}};
for(i = 0; i < 3 ; i++)
{
for(j = 0; j < 3; j++)
{
printf(“arrayHello[%d][%d]=%d\n”,i,j,arrayHello[i][j])
}
}
return 0;
}

Output: arrayHello[0][0] = 1
arrayHello[0][1] = 2
arrayHello[0][2] = 3
arrayHello[1][0] = 2
arrayHello[1][1] = 3
arrayHello[1][2] = 4
arrayHello[2][0] = 3
arrayHello[2][1] = 4
arrayHello[2][2] = 5
arrayHello[3][0] = 4

```
data_type array_name [rows] [columns]
```

```
int hello [4] [3]
```

```
No of rows
```

```
Array name
(user define)
```

```
Data
Type
```

```
No of columns
```

```
int array Hello [4] [3] = {{1,2,3}, {3,4,5}, {4, 5, 6}};
```

```
Array name
(user define)
```

```
Data
Type^1 st Row^2 nd Row^3 rd Row
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

arrayHello[3][1] = 5
arrayHello[3][2] = 6

**4.1.6 Passing array to a function**

Example:

# include<stdio.h>

void Helloarray (int marks [ ])
for(int i = 0; i < 5; i++)
{
printf(“%d”, marks[i]);
}
}
int main()
{
int marks[5] = {45, 67, 34, 78, 90};
Helloarray(marks);
return 0;
}

Note: void Helloarray(int marks[ ])

Without return type function

**4.1.7 Passing Array to a Functions as a pointer**

Now, we will see how to pass an array to a function as a pointer.

# include<stdio.h>

void helloarray(char * marks)
{
printf(“Elements of array are:”);
for(int i = 0; i < 5; i++)
{
printf(“%c”, marks[i])
}
int main()
{
char marks[5] = {‘A’, ‘B’, ‘C’, ‘D’, ‘E’};
helloarray(marks);
return 0;
}
}
Note:
Whenever you pass an array, it is always call by reference. In previous 2 programs, we passed an address & formal
argument in both the cases is a pointer internally.

```
data type
```

```
User
defined
function User define^
Array name
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

How to return an Array from a function

# include<stdio.h>

int *fun()
{
int marks [5];
print f (“Enter the element in an array”);
for (int i = 1 ; i < 5; i++)
{
scanf(“%d”,& marks[i]);
}
return marks;
}
int main()
{
int *n;
n = fun();
printf(“\n Elements of array are:”);
for(int i = 0; i < 5; i++)
{
printf(“%d”,n[i]);
}
return 0;
}
Note:
fun() function returns a variable ‘marks’.
It returns a local variable, but it is an illegal memory location to be returned, which is allocated with a function in the
stack. Since the program control comes back to the main () function, and all the variables in the stack are fraud.
Therefore, we can say that this program is returning memory location, which is already de-allocated, so the output of the
program is a segmentation fault.

**4.1.8 Array declaration and initialization**

1. int A[ ] = {10, 20, 30}: valid
2. int A[3] = {10, 20, 30}: valid
3. int A[ ] ; invalid
4. int A[3] ; valid
5. int A[2][3]; valid
6. int A[ ] [3]; = {10, 20, 30}: invalid
7. int A[2] [3]; = {1, 2, 3, 4, 5, 6}: valid
8. int A[ ] [3]; = {1, 2, 3, 4, 5, 6}: valid
9. int A[2] [3] [2]; invalid
10. int A[ ] [3] [2]; invalid
11. int A[ ] [2] [ ]; invalid
12. int A[ ] [ ] [2]; invalid
13. int A[2] [3] [2]; = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,}; valid

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

14. int A[ ] [3] [2]; = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,}; valid
15. int A[2] [ ] [2]; = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,}; invalid
16. int A[2] [3] [ ]; = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,}; invalid

Note:

- while declaring an array, it is mandatory to provide the size of each dimension. (3), (6), (10), (11), (12) are not providing
  sizes of dimensions.
- While initializing an array, you have flexibility to omit only first dimension i.e., you are allowed to other dimension (1),
  (8),(14) are following this rule while (15), (16) are not following this rule.

**4.1.9 Pointers**

- In C, there is a strong relationship between arrays and pointers. An operation that can be achieved by arrays subscripting
  also be done with pointes.
- Consider the declaration
  int a[5] = {10, 20, 30, 40, 50};
  int* Pa;
  Pa = &a[0];
- Pointers are special variable that can hold address of other variables
  Syntax: data type * Identifier
  int *Pa: Pa is a pointer to integer variable
  i.e., Pa can hold address of integer variable

```
Pa contains address of a[0]
```

- Two operators are important to understand for understanding pointers: &, *
  i. &: address of operator
  ii. *: value at operator
- Pa is equivalent address 1020
- Pa is equivalent to value at (Memory location 1020)
  i,e *Pa is same as 10
- Pa is pointing to same element of array, then by definition Pa +1 points to next element, Pa + i points to elements after i
  elements before Pa.
  i.e, In our example Pa points to a[0]
  So, Pa+1 will point [1]
  Pa+2 will point to a[2]
  i,e
  Pa+i is address of a[i]
   Pa + i  & a[i]
   *(Pa+i)  *& a[i]  a [i]
- Array name always represent address of the very first element
  i.e., Pa = &a[0];
  and

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

```
Pa = a ;
both are same.
```

- a[i]  *(a+i)  *(i + a)  i [a]
  All are same and can be used interchangeably in program except in declaration.
- In declaration, we can not write
  int 3[a]; instead of int a[3]
- Array name represent a constant address.
  int a[10];
  i. a++, ++a, – – a , a – – are all invalid as we cannot apply increment/decrement operator on constants:
  ii. Array name cannot be Lvalue of on assignment statement.
  i.e.
  array_name = any expression/address/value is invalid
- On the other hand, pointer being a variable, the following operations are valid.
  int a[ 5 ]
  int = *Pa;
  Pa = a : valid
  Pa+ + ;
  Pa – –:
  + + Pa :
  - – Pa :

```
all are valid
```

### 

### 

### 

### 

### 

### 

### 

- Multi-level pointer
  int x : x can store value
  int *P : p can store address of integer variable
  int **q : q can store address of pointer variable
  x = 10 : valid
  p = &x : valid
  q = &p : valid

```
p  1020 i, e address of x
*P  value at (memory location 1020)
*p  10
q  1096 i,e address of variable p
*q  value at (memory location 1096)
 1020 which is again an address
*q^ ^ value at (memory address 1020)^
**q  10
```

1. Dangling pointer: The pointer pointing to a deallocated memory block is known as dangling pointer.
   This situation raises an error known as dangling pointer problem. Dangling pointer occurs when a pointer pointing to a
   variable goes out of scope or when a variables memory gets deallocated.
   Consider the code.
   int *f( ) {

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

```
int a = 10; // a is a local variable and goes out of scope after execution of f( )
return &a :
}
int main () {
int * ptr = f (); //Ptr points to something which is not valid
print (“/d”*,ptr);
return 0 ;
}
```

- To overcome this problem, just make variable a as static when x become static it has scope throughout the program.

2. Uninitialized pointer: An uninitialized pointer also known as wild pointer
   A pointer which has not been initialized to anything can be dangerous

- The value saved in an uninitialized pointer could be randomly pointing anywhere in memory
- int *p
- int *p
- Storing a value using an uninitialized pointer has the potential to overwrite anything in your program including your
  program itself.
- System may crash.
- Always initialize with NULL.

3. NULL pointer: It is a pointer which is pointing to nothing It is a specially designed pointer that stores a defined value
   but not a valid address of any element or object.
   NULL pointer does not hold valid address and that is why if you try to dereference it, you will get an error
   int *p = NULL:
   printf (“%d”,*p) : //NULL pointer dereferencing
4. void pointer: void pointer is a pointer that points to some location in memory but is does not have any specific type.
   It can point to any type of data and any pointer type is convertible to a void pointer.
   Its declaration:
   void *ptr :
   is saying that ptr is a pointer that can hold an address
   cannot be dereferenced directly
   i.e., void *ptr
   int x = 10:

```
100 10
100
```

```
Ptr a
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

ptr = &x :
printf (“%d”, *ptr); //invalid
you need to typecast the void pointer before dereferencing.
i.e.,
void *ptr
int x = 10;
ptr = &x;
printf(“%d”,*(int*)ptr);
typecasting
Here, (int*)ptr does type costing of void
*(int*) ptr dereferences the typecasted void pointer variable

- Pointer arithmetic in not possible on void pointer.
  i,e....... ptr+ +, + + ptr, – – ptr, ptr – – , ptr + 1 , ptr - 1 is not allowed an void pointer.
- An uninitialized pointer holds a garbage value while a NULL pointer holds a defined value but not a valid address.

**4.1.10 Memory leakage problem**

- Whenever a pragrammer allocated memory dynamically then it is the reponsibility of the programmer to free that
  memory after usage.
- Memory leakage problem occurs when a programmer allocates memory dynamically but does not de-allocate it after
  using it.
- It reduces the performance of the computer by reducing the amount of availbale memory.

**4.1.11 Understanding Declartion**

1. int *(P[10]) : P is an array of 10 pointer to integer
2. int (*P)[10] : P is a pointer to an array of 10 integers
3. int (*P)() : P is pointer to a function that takes no argument and returns an integer.
4. int (*P) (int, int) : P is a pointer to a function that takes 2 integer arguments and returns an integer.
5. int *P (char*) : P is a pointer to a function that takes a pointer to character argument and return a pointer to integer.

**4.1.12 Pointer to Functions / Function Pointer**

- Just like normal pointers we can have pointers to functions.
  int(*p)(int, int)

```
P is a pointer to a function that take 2 integer arguments and returns an integer value.
```

```
0 1 2 3 q
```

```
P
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- Declaration of function pointer: declaring a pointer to function is almost same as declaring the fuction except that in
  function pointer are prefix is with an asterik * symbol.
  For example: if the function is
  int add(int, int)
  Declaration of a fuction pointer for add() fuction is :
  int (*ptr)(int, int);
- How to call a function through function pointer : In order to all a function using function pointer, first we need to assign
  the address of function code to the pointer
  Ex 1 :
  int add (int, int):
  void main () {
  int (*ptr) (int, int);
  ptr = &add; // ptr is a pointer to add() function
  printf (“The sum of 10 and 20 is”, (*ptr )(10, 20)); //calling add()
  }
  int add (int, int);

Ex 2 :
void main() {
int (*ptr) (int, int);
ptr = add ; // same as ptr = & add
printf (“ The sum of 10 and 20 is”, (*ptr) (10, 20));

- A function can be called using following 4 ways using pointer to fuction.

```
int add (int int);
void main() {
int (*ptr) (int, int);
ptr = &add;
printf (“%d”, (*ptr)(10, 20));
}
```

```
int add (int int);
void main() {
int (*ptr) (int, int):
ptr = add;
printf (“%d”, (*ptr) (10, 20));
}
int add (int, int) ;
void main() {
int(*ptr) (int, int);
prt= &add;
printf (“%d”, (*ptr)(10, 20));
}
```

```
int add (int, int);
void main() {
int (*ptr) (int, int);
prt= add;
printf (“%d”, (*ptr) (10, 20));
}
```

- Using function poitnter we are able to pass a function as an argurment to other function and can also be returned from
  function.
  Array of function pointer
  int (*ptr[3])(int, int)
  Ptr is an array of 3 pointers to a function that takes 2 arguments and returns an integer.

### 

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

5

**STRINGS**

**5.1 Strings**

- Sequence of characters terminated by a null character ‘\0’.
  Syntax:
  char str_name[size];
- Initializing a string in c
  ➢ char str[] = “Pankaj”;
  Here, str is internally a pointer (holds the address of first character)
  ➢ char str[20] = “Pankaj”;
  Here, we predefine the size as 20 but we should always take one extra space along with size of string.
  i.e atleast 7 size must be there to store “Pankaj” (6+1)
  ➢ char str[7] = {‘P’, ‘a’, ‘n’, ‘k’, ‘a’, ‘j’, ‘\0’};
  must set the end character as ‘\0’
  ➢ chat str[] = {‘p’, ‘a’, ‘n’, ‘k’, ‘a’, ‘j’, ‘\0’};

**5.1.1 Reading a string**

- scanf():
  when we use scanf() to read, we use %s as a format specifier without using “&” to access the variable address
  because an array name acts as a pointer.
  #include <stdio.h>
  int main (){
  char name [20];
  printf(“enter your name \n”);
  scanf(“%s”,name);
  printf(“Hello %s”,name);
  }
  Output:
  Enter your name
  Pankaj Sharma
  Hello Pankaj // why not Hello Pankaj Sharma

```
The above code did not print Hello Pankaj Sharma as expected because scanf halts reading as soon
as a whitespace or a newline character is encountered, and that is why it reads only Pankaj.
```

- In order to read a string containing space, we use gets() function. gets() ignores the whitespace & stops reading
  when a newline is found.

# include<stdio.h>

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

void main(){
char name [20];
printf(“Enter your name :”);
gets(name);
printf(“Hello %s”, name);
}
Output :
Enter your name: Pankaj Sharma
Hello Pankaj Sharma

- A string literal always represent base address of a string. i.e address of first character.
- “Pankaj” represents address of character ‘P’
  Hence “Pankaj” [0] means ‘P’
  “Pankaj” [1] ≡ *(“Pankaj”+1) ≡ *(Address of ‘P’+1)
  ≡ *(Address of ‘a’)
  ≡ ‘a’

**5.2 Strings and pointers**

- Array name represents the address of its first element. Similar to character arrays, we can create a character pointer to

represent a string that will hold the starting address i.e address of first character of string.

Example - 1

# include<stdio.h>

void main() {
char *ptr = “pankaj”
printf(“%s”,ptr);
}
Output : pankaj

Example **–** 2

# include<stdio.h>

void main() {
char *ptr = “Pankaj”
printf(“%s”,ptr+1);
}
Output: ankaj

**5.3 Predefined functions for string**

( 1 ) strlen (): returns the length of the string passed as an argument.
(2) strcpy (): copies the contents of one string to another. strcpy (S 1 ,S 2 ) copies the content of string S 2 to string S 1.
(3) strcmp (): compares the first string with the second string. If both are same it returns 0.
strcmp (str1,str2) returns 0 if both strings are same.
(4) strcat (S 1 ,S 2 ): concat S 1 string with S 2 string and the result i.e concatenation of S 1 ,S 2 is stored in S 1.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**5.4 Important concepts**

(1) # include<stdio.h>
void main() {
char name [20] = “Pankaj” ;
name = “Neeraj” ; // Error
printf(“%s”, name);
}

- Array name being a constant can’t be presented at the left side of the assignment statement i.e it can’t be L-value.
  You can’t re-assign another string to array.

(2) # include<stdio.h>
void main() {
char name [20] = “Pankaj” ;
name [1] = ‘u’ ;
printf(“%s”, name);
}
Output: Punkaj

- We are allowed to change content of array and hence we can update any character.

(3) # include<stdio.h>
void main() {
char * ptr = “Pankaj” ;
ptr = “Neeraj” ;
printf(“%s”, ptr);
}
Output: Neeraj

- Pointer ptr being a variable can hold different address at different time. Hence, we can assign another string to a character
  pointer any time.

(4) # include<stdio.h>
void main()
{
char * ptr = “pankaj” ;
ptr [1] = ‘u’ ; // Invalid
printf(“%s”, ptr);
}

- String literals are stored in read only memory area i.e “pankaj” is stored first & then the address of character ‘p’ is given
  to ptr.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- As they are stored in read only area of memory, we are not allowed to update them.

### 

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

6

**TYPES OF DATA STRUCTURE,**

**ARRAY & LINKED LIST**

**6. 1 Introduction**

**6 .1.1 Linear data structure**

Every element can have almost 2 neighbours. Ex. arrays, linked list, stack, queue.

**6.1.2 Non-Linear data structure**

Element can have more than 2 neighbours. Ex. Tree, graph.

**6.2 Arrays**

**6.2.1 1 - D array**

Theoretically index can start from any integer value. Let A be a 1-D array of n elements and the size of each element is w bytes,
then the address of A[i] element.

Base Address A + i – starting index * w( ) ( )

**6.2.2 2 - D Array**

Analogous to matrix with rows and columns. Can be implemented in RMO (Row-major order) or CMO (Column-major order).

Let A[M] [N] be a 2-D array, where size of each element is w-bytes, then the address of A[i] [j] is :

(a) In RMO

Address (A[i] [j]) = Base Address (A) + [(j-starting index) + (i – starting index) × M]xw

(b) In CMO

Base Address (A) + [(i – starting index) + (j – starting index) × M] × w

**6.2.3 Sparse Matrices**

Most of the element of the matrix have 0 value and representing such matrix by a 2D array leads to wastage of memory and
that is why, it is better than we will only store non-zero elements (Efficient method).

**6.2.4 Lower Triangular Matrix**

n × n

Aij = 0 if i < j

Aij  0 if i > j

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

For ex.

```
11
21 22
31 32 33
41 42 43 44
```

### 000

### 00

### 0

### A

### AA

### A

### A A A

### A A A A

### 

### 

### =

### 

### 

### 

**6.2.5 Upper triangular Matrix**

```
11 12 13 14
22 23 24
33 34
44
```

### 0

### 00

### 0 0 0

### A A A A

### A A A

### A

### AA

### A

### 

### 

### =

### 

### 

### 

**6.2.6 Tri-diagonal Matrix**

Matrix that has non-zero elements only in the main diagonal, diagonal just below main diagonal and diagonal just above main
diagonal. All other elements are zero.

```
11 12
21 22 23
32 33 34
43 44 45
54 55
```

### 0 0 0

### 00

### 00

### 00

### 0 0 0

### AA

### A A A

### A A A

### A A A

### AA

### 

### 

### 

### 

### 

### 

### 

**6.2.7 Efficient method to store sparse matrix**

Using Row-major order for string lower triangular matrix, the element at index (i, j) can be represented as :

```
Index of
```

```
( )
( )
```

### 1

### 1

```
ij 2
```

```
ii
Aj
```

###  − 

### =+ −

### 

Using column-major order for storing upper triangular matrix, the element at index (i, j) is sparse matrix can be represented as:

```
Index of ( ) ( )
1 ( )(^2 )
ij 2
```

```
j i i
A i j j N
```

###  − − 

### = − + − −

### 

Matrix order

N × N

Using Row-major order for storing upper triangular matrix, the element at index (i, j) in sparse matrix can be represented as :

Index of ( ) ( )

```
( )( 2 )
1
ij 2
```

```
i i i
A j i i N
```

###  − − 

### = − + − −

### 

Where N : Number of rows/columns

Using column-major order for starting upper-triangular matrix the element at index (i, j) can be represented as

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

```
Index of ( )
1 (^1 )
ij 2
```

```
jj
Ai
```

###  − 

### = − +

### 

Using Row-major order for storing tri-diagonal matrix,

```
Index of element Aij = 2i + j – 3
```

Using column-major order for storing tri-diagonal matrix,

```
Index of element Aij = i + 2j – 3
```

**6.3 Linked List**

**6.3.1 Linked List**

Linked list is collection of elements called node, where each node contains atleast 2 fields.

(i) Data field : that contains information.

(ii) Link field : contains address of next note.

**6.4 Types of Linked List**

**6.4.1 Singly Linked List**

Every node contains data and a pointer to the next node in the linked list, we can traverse the linked list only in forward
direction.

```
Head
```

```
10 20 30 40
```

```

→ → → 
```

- Head : Pointer that contains address of 1st node.
- Head contains NULL represent empty Linked List.
- If Ptr contains address of some note (Ptr is a pointer to node) then to go to the next node, we need.

```
Ptr = Ptr → Link
```

- Node can be implemented by structure in C

```
Struct Node {
```

int data;

Struct Node * Link;

```
}
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**6.4.2 Doubly Linked List**

A two-way linked list in which every node contains a pointer to the next node as well as pointer to previous node in the list we
can traverse it in backward direction also.

Structure of a Node :

Struct Node {

struct Node * Prev;

int data;

struct node * next;

### };

**6.4.3 Circular Linked List**

A linked list in which last node points back to the first node in the list.

- Circular linked list has no beginning and no end.

```
Head
```

### 10 20 3 4

**6. 4. 4 Doubly circular linked list**

It is a 2-way circular linked list.

Head

10 20 3 40

Prev data Next Prev Next Prev Next Prev Next

List

**6.4.5 Header Linked List**

A linked list that contains a special node called header node at the beginning of the list.

- Head will not point to first node.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- Head points to the header node.

**6.4.6 Applications**

- used to implement other data structure link stack, queue data structure.
- used for dynamic memory allocation.

**6.4.7 Advantages and Disadvantage**

- Insertion and deletion are efficient.
- Using pointers in every node, require more memory.
- Random accessing in not possible.
- Circular linked list can be used to implement Fibonacci Heap.

### ❑❑❑

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

7

**STACK AND QUEUE**

**7.1 Introduction**

Linear data structure in which both insertion and deletion operation are performed at one end called TOP of the stack. Works
on LIFO (Last In First Out) Policy.

**7.1.1 Application**

To post-pone certain decision (To wait/To delay)

- Stack Permutation : Order of insertion of key is fixed but we can pop an element any time.

Number of possible stack permutation with n elements

```
2
1
```

```
nCn
n
```

### =

### +

- Infix to postfix
- Infix to prefix
- Prefix Evaluation
- Postfix Evaluation
- Recursion
- Tower of Hanoi

**7.2 Queue Data Structure**

Linear data structure in which insertion is done at one end called rear of the queue and deletion is performed at other end called
front end of the queue.

Works on FIFO (First In First Out) policy.

**7.2.1 Applications of Queue Data Structure**

- Whenever a resource is being shared among many users.
- When data is transferred asynchronously.
- FCFS scheduling
- Algorithms like BFS.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

**7.3 Implementation**

Can be implemented using arrays, linked list.

(a) Using Array :

- Easy to implement and memory efficient.
- Not dyanmic

(b) Using Linked List :

- Dynamic
- Require extra memory because of pointer field.

**7.4 Standard Operations**

**7.4.1 Stack**

(a) Push ( ) : Insertion of an element onto stack.

(b) Pop ( ) : Deletion of an element.

(c) Is_empty ( ) : Returns true if stack is empty otherwise return false.

**7.4.2 Queue**

(a) Enqueue : Insertion of an element.

Performed at rear end of the queue.

(b) Dequeue : Deletion of an element.

Performed at front end of the queue.

**7.5 Circular Queue**

Extended version of simple queue in which last element is connected to the first element.

In simple queue, even though space is available, we are not able to insert a new element and declaring it a overflow. Circular
queue solves this problem.

Queue Full

(i) Front = = 0 & & Rear = = SIZE – 1 OR

(ii) Front = = (Rear + 1)% SIZE

**7.6 Priority Queue**

A queue in which a priority is associated with every element and elements are processed according to their priorities and if two
elements have same priority then they are processed as per their arrival in the queue.

```
❑❑❑
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

8

**TREE DATA STRUCTURE**

**8.1 Introduction**

**8.1.1 Terminology**

(i) Internal Node : Node with atleast 1 child.

(ii) Leaf Node : Node without any child.

(iii) Root Node : Only node that does not have any parent.

(iv) Complete binary Tree : Binary tree in which nodes are inserted from left to right at every level and we can not insert at
node at (K+ 1)th level until all levels upto K are fully filled.

(v) Full Binary Tree : A binary tree in which every internal node has exactly two children and all the leaf nodes are at some
level.

Binary tree that contains maximum number of nodes.

(vi) Strict Binary Tree : A binary tree in which every internal node has exactly two children.

(vii) Complete K-ary tree : Tree in which every internal node has exactly K-childs.

**8 .1.2 Mathematical Result**

(i) For a binary tree of height h

- Maximum number of nodes = 2(h+1) – 1
- Minimum number of nodes = h + 1

(ii) For a complete binary tree of height h

- Maximum number of nodes = 2 (h+1) – 1
- Minimum number of nodes = 2h

(iii) For a full binary tree :

Number of nodes = 2h+1 – 1

(iv) Total number of unlabelled binary trees with n nodes =

```
2
1
```

```
n
Cn
n+
```

(v) Total number of labelled binary tree with no keys =

```
2
!
1
```

```
n
Cn n
n
```

### 

### +

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

(vi) Total number of binary trees with a given preorder (n length) =

```
2
1
```

```
nCn
n+
```

(vii) Total number of binary trees with a given proorder/postorder/inorder =

```
2
1
```

```
nCn
n+
```

(viii)Number of binary trees with a given preorder and inorder = 1

(ix) Number of binary trees with a given postorder and inorder = 1

(x) Number of leaf nodes = Number of nodes with two children + 1

**8.2 Binary Tree Traversal**

(1) Preorder :

(i) Process the root.

(ii) Traverse the left subtree of root in preorder.

(iii) Traverse the right subtree of root in preorder.

(2) Inorder

(i) Traverse the left subtree of root in inorder.

(ii) Process the root.

(iii) Traverse the right subtree of root in inorder.

(3) Post-order

(i) Traverse the left subtree of root in post-order.

(ii) Traverse the right subtree of root in post-order.

(iii) Process the root.

In-order

- Morrison Traversal :

```
In-place traversal of a binary tree
```

No recursion

Constant extra space.

**8.3 Binary Search Tree**

A binary tree in which every node satisfy the property that all the keys in the left subtree of the node are smaller than node’s
key and all the keys in the right subtree of the node are greater than node’s key.

- Inorder traversal of a binary search tree is ascending order of keys in the BST.
- Insertion in a BST

(a) O (log n) best case

(b) O (n) worst case.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- Deletion from a BST :

(a) Deletion of leaf node : can be done directly

(b) Deletion of node with one child : copy the child to the node and delete the child.

(c) Deletion of a node with two children : first find the inorder successor of the node, copy the contents of this
successor to the node and dlete the inorder successor.

We can also use inorder predecessor.

- TC : O (log n) best case

O (n) worst case

**8.4 Heap**

A complete binary tree in which every node satisfy heap property (min heap or max heap)

(i) Min heap : A complete binary tree in which every node satisfy the property that the value of the node is smaller than both
its children.

(ii) Max heap : A complete binary tree in which every node satisfy the property that the value in the node is greater than both
its children.

20

10 8

6 4

20

10 8

12 3

```
Not a heap Not a heap
```

- Construction of Heap :

(i) By inserting keys one after another : O (n log n)

(ii) Using build-heap method/heapify algo : O(n)

- Number of min-heaps possible with n keys

T(n) = T(k). T(n – k – 1). n–^1 Ck

K : Number of elements in the left subtree of root node.

- Deletion :

(1) Swap A[1], A[n]

(2) Apply Heapify on A[1] considering there are only (n – 1) nodes.

T.C = O (log n)

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- Heapsort (Assuming max heap)

(i) Build Max Heap O(n)

(ii) Replace root element with last element (A (^1) A n ) reduce the heap size by 1 and then apply heapify at root node.
(iii) Repeat step 2 while heap size is greater than 1.
**8.5 AVL Search Tree**

- Height balanced BST.
- Balance factor (Bf) is given by

Bf= − |hL hR| 1

i.e., Balancing factor of a node can be +1, –1 or 0.

**8.5.1 Insertion**

To ensure that the tree remains AVL tree, after insertion some re-balancing is performed i.e., certain rotations are needed.

**8.5.2 Types of Rotation**

(i) Left-Left (LL) Rotation :

10

6

2

+2

L

+1

0

L

(^210)
6
(^00)
0
(ii) Right-Right (RR) Rotation :
(^210)
6
(^00)
0
10
6
2

- 2

R

- 1

0

R

(iii) Left-Right (LR) Rotation :

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

10

6

2

+2

L

- 1

R

(^210)
6
(^00)
0
(iv) Right-Left (RL) Rotation :
10
6
2

- 2

L

+ 1

R

(^210)
6
(^00)
0

- LL, RR are single rotation.
- LR, RL are double rotation.
- Just work no tri-node structure.
- Minimum number of nodes in an AVL tree of height h is given by recurrence.

n(h) = 1 + n(h – 1) + n(h – 2) h  2

n(0) = 1

n(1) = 2

i.e., it also forms a Fibonacci series

1, 2, 4, 7, 12, .............

### ❑❑❑

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

09

**GRAPH TRAVERSAL**

**9.1 Introduction**

**9.1.1 Breadth First Search**

- Uses a queue data structure.
- To find whether a graph is connected or not.
- To find number of connected components in a given graph (Breadth First traversal is used)
- To detect cycle in a graph.
- To find whether a given graph is bipartite or not.
- T.C. = O (V + E) using Adjacency List

= O(V^2 ) using Adjacency matrix.

- To find shortest path in undirected graph without weights.

**9.1.2 Depth First Search**

- Uses stack.
- To detect a cycle in a graph.
- To find whether a graph is connected or not.
- To find whether given graph is bipartite or not.
- To find number of connected components in the graph.
- To find bridges in the graph.
- To find articulation points in the graph.
- To find topological sort of a graph.
- To find biconnected components.
- To find strongly connected components.

### ❑❑❑

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

10

**HASHING**

**10.1 Introduction**

- Searching technique.
- Mapping keys into hash table using a hash function.
- Efficiency based on hash function used for mapping.

**10.1.1 Terminology**

(i) Collision : When two keys mapped to same location, collision occurs.

H(k 1 ) = H(k 2 ), where H(k) is the hash function used.

(ii) Load factor no. of keys
Hash table size

### =

**10.1.2 Collision resolution technique**

(i) Open addressing (closed hashing)

```
(a) Linear probing
(b) Quadratic probing 1
(c) Double hashing
```

```




```

(ii) Separate chaining

**10.1.3 Linear Probing**

Whenever there is a collision at memory location ‘L’, then we will search for empty slot sequentially starting from ‘L’ then L

+ 1, L + 2, L + 3, ..........

**10.1.4 Problem with linear Probing**

Linear probing suffers with primary clustering problem, consecutive keys forms a cluster and the time to find a free slot
increases.

**10.1.5 Quatratic Probing**

Hash function h(x) = x modm. It leads to a collision and it is ith collision for key x then the collision resolution function is given
as:

H(x, i) = (h(x) + i^2 ) modm

Searching order : L, L + 1, L + 4, L + 9, .........

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
C Programming
```

- Free from primary clustering
- Suffers with secondary clustering problem.

**10.1.6 Double Hashing : Using 2 hash functions**

(hash – 1 (key) + i * hash-2 (key))% m

M : table size

Hash-2 (key) : Secondary hash function must not give output 0.

* One of the best probing.
* Uniform distribution.
* Tree from primary and secondary clustering.
* Computation overhead because of two hash function computation.

**10.2 Chaining**

Uses the concept of linked list (chain) when more than one element are hashed to same location (slot) then elements are inserted
into a singly linked list (chain).

- Deletion is easy compared to open addressing.
- Deleting in open addressing require rehashing remaining keys.

### ❑❑❑

**AlgorithmsAlgorithmsAlgorithms**

```
Design Against Static Load
```

1. Asymptotic Notation ........................................................................................................... 6 .1 – 6. 18
2. Divide and Conquer .............................................................................................................. 6. 19 – 6. 25
3. Greedy Technique ............................................................................................................... 6. 26 – 6. 29
4. Dynamic Programming ......................................................................................................... 6. 30 – 6. 34

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 1
Algorithm**
1
**ASYMPTOTIC
NOTATION
1.1 Introduction of Course**

**1. 2 Algorithm Concept and Life Cycle Steps

1. 2 .1 Algorithm**

- An Algorithm consists finite number of steps to solve any problem.
- Every step involves some operations and each operation must be definite and effective.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 2
Algorithm**

**1. 2 .2 Life Cycle Steps**

**1.3 Needs of Analysis**

In performance comparison comparing different algorithms for optimal solution.

**1.3.1 Time Complexity**

Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the input size.

**1.3.2 Space Complexity**

Space complexity of an algorithm quantifies the amount of space or memory taken by an algorithm to run as a function of input
size.

```
Note:
To find the time complexity of an algorithm, find the loops and also consider larger loops.
Space complexity is dependent on two things input size and some extra space (stack space link, space list etc).
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 3
Algorithm**

**1. 4 Methodology of Analysis

1. 5 Types of Analysis**

Worst Case

The input class for which the algorithm does maximum work and hence, take maximum time.

Best Case

The input class for which the algorithm does minimum work hence, take minimum time.

Average Case

Average case can be calculated form best case to worst case.

**1. 6 Asymptotic Notations**

Suppose, T(n) be a function of time for any algorithm.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 4
Algorithm**

**1. 7 Types of Asymptotic Notations

1. 7 .1 Big O – Notation**

```
Two Functions f n g n( ), ( )
f n( )=O g n( ( ))
```

When the growth of gn()is same or higher than fn() like ab

Example:

```
f n( ) 3= +n 10, ( )g n = + +n^22 n 5
f n( ) O( ( ))= g n
```

**1. 7 .2 Ω - Notation**

```
f n( )=( ( ))g n
  f n( ) C g n( ) (a b )
```

Example: 3 nn=(2 )

**1. 7 .3**  **- Notation**

```
If f(n) ≤ g(n)
And
f(n) ≥ g(n)
```

f(n) = g(n)
∴ f(n) = (g(n))

Example:
f(n) = 2n^2 , g(n) = n+10
f(n) > g(n) here
so, f(n) = Ω(g(n)) or g(n)=O(f(n))

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 5
Algorithm**

**1. 7 .4. Properties with respect to asymptotic notations**

```
Reflexive Symmetric Transitive Transpose symmetric
Big oh (O) ^ × ^ ^
Big omega () ^ ×^ ^ ^
Theta ()    ×
Small oh (o) × ×  
Small omega () × × ^ ^
```

Example 1. Consider the following function

```
1
```

### ()

```
n
p
```

```
f n p q
=
```

==

Which of the following is/are true for ‘q’
(a) (n^4 ) (b) (n^5 ) (c) O(n^5 ) (d) (n^3 )
Solution: (a, c, d)

f (n) =^3
P1

### P

```
n
```

```
=
```

^

= 1^3 + 2^3 + 3^3 + 4^3 ................. + n^3

=

### 1 2

### 2

```
nn+


```

= O(n^4 ) or  (n^4 )

=  (n^4 )
Example 2. Consider the following functions:

f (n) = ½
1

```
n
```

```
P
```

### P

```
=
```

 = q^

Find the value of q in terms of asymptotic notation.

Solution: f (n) = ½
1

```
n
```

```
P
```

### P

```
=
```

^

= 1 + + +( (^2) )½½( (^3) ) .......
=====================================

(^232)
1
3
n −

====

(^2232)
33
n −
= O(n1.5)
= O(nn)
Example 3. Arrange the following functions in increasing order.
f 1 =nlog ,n f 2 = n f, 3 =2 ,n f 4 =3 ,n f 5 =n f!, 6 =nn,f 7 = log ,n f 8 =100 logn n
→f 7   =    f 2 fl f 8 f 3 f 4 f 5 f 6

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 6
Algorithm**
Example 4. Arrange the following functions in increasing order.
f 1 =10,f 2 = n f, 3 =log log ,n f 4 =(log ) ,n^22 f 5 =n
f 6 =nlog ,n f 7 =n f!, 8 =2 ,nnf 9 =n f, 10 =n^2 logn
→ f 1         f 3 f 4 f 2 f 6 f 5 f 10 f 8 f 7 f 9
Example 5. Arrange the following functions in increasing order.
f 19 ==log logn f nlog logn
f 2 ==logn f 10 n^2 logn
f 3 ==(log )n^23 f 11 n
f 4 ==logn f 12 2 n
f 5 ==n1/10 f 13 en
f 6 ==n f 14 n!
f 7 ==n^2 f 15 nn
f 8 ==nlogn f 16 n3/2
f 1 < f 4 < f 2 < f 3 < f 5 < f 6 < f 9 < f 8 < f 16 < f 7 < f 10 < f 11 < f 12 < f 13 < f 14 < f 15
aclogbbca log
^2 log^2 nnnlog 2^2 =
Example 6. Arrange the following functions in increasing order.
fn 1 = !,fn 2 = n
f 1 =  − −    n (n 1)(n 2) ... 3 2 1
f 2 =       n n n n ... n n n
ff 21 
=ff 12 O( )
2 n   ^3 n^4 n nn! n
Question.
Which of following is TRUE?
(1) 2 log^2 n=O(n )^2 TRUE
(2) nn^25 = 2 3log^2 n O( ) TRUE
(3) 2 nn=O(2 )^2 TRUE
(4) lognn=O(log log ) FALSE
(5) log logn=O( log )n n TRUE
Solution:
(1) 2 log^2 n=O(n )^2
=nlog 2^2
=n

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 7
Algorithm**
(^) ==nnO( )^2
(2) nn^25 = 2 3log^2 n O( )
=nn^2 3log 2^2
=nn^23
=n^5
==nn^55 O( )
(3)
2
2
2

### 22

### 2 2 .2

### 22

```
2 (2 ) True
```

```
nn
n n n
nn
nnO
```

### =

### =

### 

### =

(4) (^) log log log
log (log )
False
nn
n O n


(5) log log log
log log ( log )
True
n n n
n O n n

==

**1.8. Analysis of an Algorithm**
Algorithms
Without Loop Interactive Algorithm Recursive Algorithm

**1. 8 .1 Without loop**

Example: int fun (in + n)
{
return n*(n+1)/2;
}

Solution.
Here 1 multiply, 1 division, 1 addition
⸫ O (1) [no loops, no recursion]

**1. 8 .2. Iterative Algorithm Analysis**

Example 1:
**for (i =1; i ≤** n; i=i*2)

```
printf(“Sushil”)
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 8
Algorithm**
Solution.
i=1, 2, 2^2 , 2^3 ..., 2k
→
2k ≤ n
k log 2 ≤ log n
k ≤ log
log 2
n
⸫ k ≤ log 2 n
k = log 2 n
So, this will execute log 2 n +1 time and Complexity O (log 2 n)
Example 2:
For (i=1; i **≤** n; i=i*3)
**printf(“Aaveg”);**
Solution.
So, this will execute log 3 n + 1 time and complexity O (log 3 n)
➢ i = 1→2→4→8→16→...→n
i = n→n/2→n/4→n/8→...1
Example 3:
**for (i = 1; i ≤** n; i++)
{
**for (j=1; j ≤ 10; j++)**
{
**printf(“Dhananjay”);**
}
}
Solution.
This will execute 10⸳n times and complexity O(n)
Example 4:
for (i = 1; i <= n; i = i*3)
for **(j = 1; j ≤** n; j++)
**printf(“Prapti”);**
Solution.
Total nn(log 3 + (^1) )time execute and Complexity = O (nnlog 3 )

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 9
Algorithm**

**1. 8 .3. Recursive Algorithm Analysis**

Example 1:
void fun (in + n) T(n)
{
if (n > 0) 1 compare; C 1 time
{
**if (“% d”,** n); C 2 time
fun (n - 1); T(n-1)
}
}
Let T(n) be the Complexity time taken by algo for n size i/p

Solution.

```
T(n) = C 1 +C 2 +T(n-1)
T(n) =T(n-1) + C n > 0
```

```
T (0) = C Constant
```

```
T(n) = C; n = 0
T(n) = T (n - 1) + C; n > 0
```

Example 2:
void fun (in + n) T (n)
{
if (n > 0) C 1 time
{
for (i = 1; i <= n; i + 1) n time
printf **(“Hello”);**
fun (n - 1); T (n - 1)
}
}
Solution.
T(n) = C 1 + n - 1 + T (n - 1)
= T (n - 1) + n n > 0
T (0) = C n = 0

Example 3:
void fun (in + n) T(n)
{
if (n > 0) C 1
{

for (i = 1; i < = n; i = i*2) (^) log 2 n

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 10
Algorithm**
printf **(“Divyajyoti”);**
fun (n - 1); T (n - 1)
}
}
Solution. T (n) = T (n - 1) + O (log 2 n); n > 0
or
T (n) = T (n - 1) + log 2 n
T (0) = C or n = 0
T (0) = O (1)

**1. 9 Solving Recurrence Relation

1. 9 .1 Substitution Method**

Example: (1)
T (n) = T (n - 1) + C
T (1) = C

```
n size on problem n – 1 size x 1 convert them
T (n) = T (n - 1) + C
```

```
[ T (n - 2) + C] + C
T (n) = T (n - 2) + 2C
```

```
= T (n - 3) +3C
T (n) = T (n - k) + kC
⸫ n – k = 1
T (n) = T (1) + (n - 1) C
= C + (n - 1) C
T (n) = O (n)
```

```
Example (2)
```

T (n) = T (n - 1) + C **⸳** n
T (1) = C
Solution.
⸫ T (n) = T (n - 1) + C⸳n
= [T (n - 2) + C⸳(n – 1)] + C⸳n
= [T (n - 3) + C⸳(n – 2)] + C (n - 1) + C⸳n
= T (n - 3) + (n - 2)⸳C + (n - 1)⸳C + n⸳C
= T (n - k) + C (n – k +1) + C (n – k + 2) + ... + C (n – k + k)
⸫ n – k =1
T (n) = T (1) + T (2) + C (3) + C (4) + ... + C (n - 1) + C (n)
= C + C (2) + (3) C + 4 (C) + ... + (n - 1) C + (n)⸳C
= C [1 + 2 + 3 + ... + n]

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 11
Algorithm**
= C⸳n( 1)
2
n+
= O (n^2 )
Example (3)
T (n) = T (n/2) + C
T (1) = 1
Solution.
T (n) = T (n/2) + C
= [T (n/2^2 ) + C] + C
= T (n/4) + 2C
= T (n/2^3 ) + 3C
T (n) = T (n/2k) + kC
= (n/2k) = 2
T (n) = T (2) + (log 2 n - 1) C
= 1 + (log 2 n - 1) C
= O (log n)
Example ( 4 )

### T (1) = 1

```
T (n)= 2T (n/2) + C
```

Solution. T(n) = 2 2T 2 C C
2

```
n ++


```

```
= 2 T^222 2 C + C
2
```

```
n +


```

```
= 22 2T 3 C 2C C
2
```

```
n + + +


```

```
= 2 T^323 2 C + 2C + C
2
```

```
n +


```

```
= 2 Tk k 2 k 1C + 2k 2C ... 2 C C^1
2
```

```
n + −−+ +  +
^
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 12
Algorithm**
(^) k 12 k
2
n =  =n
→ T (n) = nT (1) + 2k -^1 ⸳ C + 2k -^2 ⸳ C + ... + 2C + C
= 2k + 2k -^1 ⸳ C + 2k –^2 + ... + 2C + C
= 2k + C (2k-^1 + 2k-^2 + ... + 2^1 + 2^0 )
= 2k^ + C (2 1)
21
k−
−
= 2k + C (2k - 1)
= 2k + 2k⸳ C – C
= n⸳C
= O (n)

**1. 9 .2 Master’s Method**

```
T (n) = aT n
b
```

### 

```
+ Θ (n
```

k (^) (log n) p)
a ≥ 1, b > 1, k ≥ 0, p = real number
If a > bk or logbak
T (n) = Θ (nlogba)
Question 1. T (n) = 2T
2
n
^ + (n)^0 log n^
Solution. a = 2, b = 2, k = 0
a > bk; 2 > 2^0 ; 2 > 1
T (n) = Θ (n)
Question 2. T (n) = 2T
2
n +n
^
Solution. a = 2, b = 2, k = 1, p = 0
T(n) = Θ (n ⸳log n)
Question 3. T(n)=2 +

T log
2
n nn
Solution. a = 2 , b = 2, k = 1, p = 1
⸫ T (n) = Θ( n (log n)^2 )
(b) If p < 0 then T (n)
T (n) = O (nk)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 13
Algorithm**
Question 4. (^) =+


### T( ) T

### 2

```
nCn^
```

Solution.
T(n) = Θ (n^2 log n)

**1. 9 .3. Recursive Tree**

(1) T( ) 2T C
2

```
n =+n
^
T (1) = C
```

```
2 k^12 k log^2
```

n= → = → =n k n

```
Total Work done = C + 2C + 2^2 C + 2^3 C + ... + 2 kC
= C (1 + 2 + 2^2 + ... + 2k)
```

```
=
211
21
```

```
k
c
```

```
+ −

−
```

```
= C (2k+1 - 1
= C (2⸳ 2 k - 1)
= C (2n - 1)
= O (n)
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK** (^) **6. 14
Algorithm**
(2) ( ) 2
2
T n =+Tn n
^
1; 2 ; log 2
2
k
k
n − −n k− n
⸫ n + n + n + ... + n
= k n
= n nlog n 2
= (^) O(nlog n 2 )
(3) ( ) 4
2
n
T n =+Tn

n = 2k, k = log 2 n
= 4 42 ... 4
2 2 2
n+    n + n + + k n
         ^

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

```
= n1 2 2+ + + + +^232 ... 2k
```

### =

```
211
21
```

```
k
n
```

```
+ −

−
```

= n (^) ( 2  2 k−^1 )
= n (^) ( 2 n (^) ) − (^1)
= O (n^2 )

### (4)

```
2
()
33
```

```
nn
T n =T      +T +n
   
```

### T(1) = 1

```
3 1; 3 ; log^3
```

```
n n i i n
i
```

### − − − 3

```
= n + n +...+ log 3 n T (n)
= (n + n + n +...+ log 3 n) ≥ n + ... + log 3 n
Ω(n⸳ log 3 / 2 n )
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**1. 10 Recurrence Relations and their Time Complexity**

```
T (n) = C; n = 2
T(n) = 2 T(√𝑛) + C; n > 2 O (logn)^
T (n) = C; n = 2
T(n) = T(n – 1 ) + C ; n > 2 O(n)^
T (n) = C; n = 1
T(n) = T(n – 1 ) + n + C ; n > 2 O(n
```

(^2) )
T (n) = C; n = 1
T(n) = 2T(n – 1 ) + C ; n > 1 O(2
n)
T (n) = C; n = 1
T(n) = 2T
2
n
^ + C ; n^ > 1^
(n)
T (n) = C; n = 1
T(n) = 2T
2
n
^ + n^ ; n^ > 1^
(nlogn)
T (n) = C; n = 1
T(n) = T
2
n
^ + C; n^ > 1^
(logn)
T (n) = 1; n = 2
T(n) = T( n) + C; n > 2 (loglogn)^
**1.1 1 Space Complexities**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

Int n, A[n];
Algorithm Rsum(A, n)
{
if (n = 1) return (A(1));
else;
return (A[n] + RSum(A, (n–1));
}

- Time Complexity = O(n)
- Space Complexity
- We need stack space
- Stack is used to store activation records of function calls
- Size of activation records is trivial
- Stack size that we need = O(n)
- Space complexity = O(n)

Algorithm A(n)
{
if (n = 1) return;
else;
{

A
2

```
n
;^
```

}
}

Recurrence relation
T(n) = C; n = 1

T(n) = T
2

```
n
+ C; n^ > 1^
```

Time Complexity = O(log n)

Space Complexity

- Space complexity will depend on number of activation record pushed into the stack
  Suppose, n = 16
  A (1)

```
For n = 2K we are pushing
the ‘K’ activation record
```

### A (2)

### A (4)

### A (8)

### A (16)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

 Space Complexity

n = 2K^
log n = Klog 2 2

K = log 2 n

Space Complexity O(log )= n

Example 3

Algorithm A(n)
{
if (n = 2) return;
else;

return (A n);
}

Solution:

T (n) = 1; n =2

T (n) = T( n)+C; n > 2

Time Complexity = O (loglogn)

Space Complexity

Suppose n = 16

```
A(1)
A(2)
A(4)
A(16)
```

 For 2 2

```
nk
manner we are pushing in stack
```

222

```
nk

```

log 2 log 2 22
2 k

```
n 
```

n  2 K
K  log 2 n

Space complexity O log= ( 2 n)

```
❑❑❑
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

2

**DIVIDE AND CONQUER**

**2 .1 DAC Application**

**2. 2 Finding Maximum Minimum element**

Recurrence Relation:

```
1 if 1 or 2
()
2 1; 2
2
```

```
nn
Tn n
Tn
```

### ==

### =

### +

### 

### 

Time Complexity:

T n( )=O n( )

- Time complexity is same for every case (Best case/Worst case).

Space Complexity:

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

Space Complexity

```
( ) (log )
()
```

```
O n O n
On
```

### =+

### =

Number of comparisons to find maximum / minimum element on an given array of n elements:

Comparison =^32
2

```
n−
```

**2. 3 Power of an Element**

Recurrence relation:

```
1 if 1
()
1; 1
2
```

```
n
Tn n
Tn
```

### =

### =

### +

### 

### 

Time Complexity:

```
()
2
( ) (log )
```

```
T n T n C
```

```
T n O n
```

### =+

### 

### =

Space Complexity:

Space Complexity = 4B + O(logn)

= O(logn)

Number of multiplications to find an

Multiplication = O(logn)

**2. 4 Binary Search**

Given a sorted array and an element x, need to return the index of element x if it is present then 1, otherwise – 1.

Recurrence relation:

```
1 ; 1
()
;1
2
```

```
n
Tn n
T C n
```

### =

### =

### +

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

Time Complexity:

Space Complexity:

Space complexity = O(n) + O(1)

```
= O (n)
```

**2. 5 Merge Algorithm**

- Merging two sorted sub arrays of input size m,n.
- Number of comparisons to merge two sorted sub arrays of size m,n.

```
Comparisons = m + n – 1 (worst case)
```

```
Number of moves =m + n (Outplace Algorithm)
```

Number of comparisons in best case of merging two sorted subarrays of size m, n.

```
comparisons = min (m, n)
```

```
Moves = m + n (Always)
```

```
Note:
Best Case comes in comparisons no effect on moves.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**2.5.1 Merge Sort Algorithm:**

```
Note:
```

- In GATE exam if merge sort given then always consider outplace.
- If array size very large, merge sort preferable.
- If array size very small, then prefer insertion sort.
- Merge sort is stable sorting technique.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**2. 6 Quick Sort Algorithm**

Example 1 : In Quick for sorting n elements, the

```
th
16
```

```
n
smallest element is selected as pivot. what is the worst-case time^
Complexity?
```

Solution.

```
T (n) = T
16
```

```
n


```

### + T

```
15
16
```

```
n


```

```
+O (n)
```

```
= (solve by recursive tree method)
```

Example 2: The median of n elements can be found in O (n) time then, what is the time complexity of quick sort algo in
which median selected as pivot?

Solution.

```
T (n) = O (n) + C + O (n) + T (n/2) + T (n/2)
```

Find median swap median Partition algo
with last
= 2T (n/2) + C ∙ n
= O(n log n)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**2. 6 .1 Randomized Quick Sort**

- In Randomized quick short algorithm selection of pivot element can be taken randomly.
  **2. 7 Counting Number of Inversion**
- Counting number of inversion on given an array of an element.

```
Time complexity T(n) = O(nlogn)
```

**2. 8 Selection Procedure**

Find Kth smallest on given an array of an element and integer K.

Time Complexity:

```
T(n) = O(n^2 )
```

Space complexity:

```
Space Complexity = O(n)
```

**2. 9 Strassen’s matrix Multiplication**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**2. 10 Comparison Based Sorting Algorithms**

```
Sorting
Algorithm
```

```
Basic logic of sorting Algo BC AC WC Stable
sorting
```

```
Inplace
sorting
```

```
Quick sort Choose pivot element place in
correct position
```

```
(nlogn) (nlogn) (n^2 ) No^ Yes^
```

```
Merge sort Divide to equal parts recursively sort
each sub part & marge them
```

```
(nlogn) (nlogn) =
n logn
```

```
(nlogn) = n
log n
```

```
Yes No
```

Heap sort Build heap(max) delete max place (^) (nlogn) (nlogn) (nlogn) No Yes
Bubble sort Compare exchange (^) (n) (n^2 ) (n^2 ) Yes Yes
Selection sort Find position of min element
from [1 to n]
(n^2 ) (n^2 ) (n^2 ) No Yes
Insertion sort Insert a [i + 1] into correct position (^) (n) (n^2 ) (n^2 ) Yes Yes

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

3

**GREEDY**

**TECHNIQUE**

**3. 1 Greedy Technique**
    - Greedy method is an algorithm design strategy used for solving problems where solution are seen as result of making
       a sequence of decisions.
    - A problem may contain more than one solution.
**3. 2 Terminology
3. 3 Applications of greedy**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**3. 4 Knapsack Problem**

Time complexity T(n) = O(nlogn)

**3. 5 Job Sequence with Deadline**

- Single CPU only.
- Arrival time of each job is same.
- No pre-emption.
  **3. 6 Optimal Merge Pattern**
- This is a problem related to merging of files. Given a set of n-files in sorted order. It is required to merge

```
them into a single sorted file with 2-way merging.
```

- This problem is like merging process in merge sort. In merge sort we were interested in number of

```
comparisons but in optimal merge pattern we are interested in record movement (i.e moving a record from
one file to another file).
o If file F1 has 'n' records and file 'F2 ' has 'm' records then number of record movement will be 'm+n'. 1 2
The problem of optimal merge pattern involves merging of n-files (n≥2).
```

- At any point choose two records with least weight merge them and put them in list and continue it until all records are

```
merged.
```

- Time complexity T(n) = O(nlogn)
- Space complexity = O(n)
  **3. 7 Huffman Coding**
- Huffman coding is essentially a non-uniform encoding with convention that the character with higher

```
frequency (probability) of occurrence will be enclosed with less number of bits.
```

- It comes under data compression technique.
- Time complexity T(n) = O(nlogn)

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Algorithm
```

**3. 8 Minimum Cost Spanning Tree
3. 8 .1 Graph**
Graph (V., E)

```
Set of vertices set of edges
```

- Let G(V, E) be a simple graph then

```
Maximum edges = V(V-1)
2
```

```
E V(V-1)
2
```

```

```

```
E  C.V^2 C is constant
Note:
E = O(V^2 )
Log E = O(logV)
```

**3. 8 .2 Graph Representation**
Graph Representation

```
Adjacency matrix Adjacency list
```

- For more edges (Dense Graph) Adj. matrix is better (density more).
- For less edge (sparse graph) Adj list is better.

```
(1) Finding degree of vertex Time Complexity
```

```
Matrix List
O(V) Every Case O(1) Best Case
O(V1) Worst Case
```

```
(2)Finding total edges  Time Complexity
```

```
O(V^2 ) Every Case O(V+2E) Worst Case
O(V) Best Case
```

```
(3) Finding 2-vertices adjacent (or)not  Time Complexity
```

```
O(1) O(V-1) Worst Case
O(1) Best Case
```

```
(4) G(V,E)  space
```

```
O(V^2 ) Every Case O(V+E) Every Case
```

**3. 8 .3 What is Spanning Tree**
A subgraph T(V, E’) of G(V, E) where E’ is the subset of (Eʹ E) is a spanning tree iff ‘T’ is a tree.
A sub graph G(‘V, E’) of G(V, E) is said to be spanning tree.
(1) T’ should contain all vertices of G
(2) T’ should contain (V-1) edged where V is number of vertices without cycle.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

(3) T’ should connected.

**3. 8 .4 Minimum Cost Spanning Tree**

Minimum cost spanning tree is the one in which cost of the spanning tree formed should be minimum.

**3. 8 .5 Prims Algorithm**

- Select Any vertex

Time complexity = V + VlogV + 2E + ElogV

```
= O(E + V)logV
```

Using Sorted Array & Adjacency List

```
V + 2E + E × V = O(EV)
```

Using Sorted Array & Adjacency List

```
V × O(1) + V2 + E × V= O(EV)
```

**3. 8 .6 Kruskal algorithm**

- Take first minimum edge

```
Time complexity = E log E + (V + E)
= O(E log E) = O(ElogV)
```

If edges are already sorted

```
TC = O(E + V)
```

**3. 9 Single Source Shortest Path
3. 9 .1 Dijkstra Algorithm**
    - Using min heap & adjacency list = O(E + V)logV
    - Using adjacency Matrix & Min heap = O(V^2 ElogV)
    - Using adjacency list & Unsorted Array = O(V^2 )
    - Using adjacency list & Sorted Doubly Linked List = O(EV)
**3. 9 .2 Bellman-Ford**
    - Time Complexity = O(EV)
    - If negative edge weight cycle then for some vertices Incorrect answer.
       ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

4

**DYNAMIC**

**PROGRAMMING**

**4. 1 Dynamic Programming**

In dynamic programming for optimal solution always computes distinct function calls.

**4. 2 Terminology
4. 3 Application of Dynamic Programming
4. 4 Fibonacci Series**

- Time complexity T(n) = O(nlogn)
- Computes distinct function calls.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**4. 5 Job Sequence with Deadline**

- Single CPU only
- Arrival time of each job is same
- No pre-emption
  **4. 6 Longest Common Sub sequence (LCS)**
- For common subsequence always consider two strings:
- P = <ABCDB></abcdb> – Q = <BDCABA></bdcaba>
- Common subsequences for both ‘p’ are
- S = <A></a>
- S = <AB></ab>
- S = <CAB></cab>
- S = <BDAB></bdab>
- A common subsequence of longest length is known as longest common subsequence.
- For above problem longest common subsequence will be of length u.
  **4. 6 .1 Applications of LCS**
  1. Genomics
  2. Software engineering applications
  3. Plagiarism
  4. Data gathering system of search engines
     **4. 6 .2 Algorithm for LCS**

LCS (p,q)
{
1.
01
[ 1] 0

```
For i to n
Li
```

```
−
−=
```

01
[ 1, ] 0

```
For j to m
Lj
```

```
−
−=
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

### 3.

```
01
01
```

```
For i to n
For j to m
```

```
−
−
```

 

### ( [ ] [ ])

### [ , ] 1 ( 1, 1];

### [ , ]

```
If p i q j then
L i j L i j
else
L i j max L i j L i j
```

### =

### = + − −

### = − −

### }

- Time complexity of step 1 = O(n)
- Time complexity of step 2 = O(m)
- Time complexity of step 3 = O(mn)
- Total Time complexity = O(n) + O(m) + O(mn)
  = O(mn)
- Space complexity = O[(M+1).(n+1)]
  = O(mn)
  **4. 7 Matrix Chain Multiplications**

Two matrices ‘A’ and ‘B’ are compatible if and only number of column of first matrix must be equal to number of rows of
second matrix.

**4. 7 .1 Brute force method**

Number of parenthesizing for a given chain is given by Catalan number:

```
1 2
1
```

```
n
n Cn
```

```


+
```

Time complexity = O(nn)

Space complexity = O(n)

**4. 7 .2 Algorithm For Matrix Chain Multiplication**

The time complexity of multiply the given chain of n matrices <A 1 , A2 A3.... An> using dynamic programming (district
function call) is O(n^3 )

Space complexity = O(n^2 )

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**4. 8 O/1 Knapsack Problem**

The maximum profit can be achieved by O/1 knapsack problem where capacity of problem is ‘p’ and number of objects are

‘q’.

**4. 9 Sum of Subset Problem**

- Given n-elements and an integer 'm', it is required to determine whether there exists a subset of given n elements, whose

```
sum equal M.
```

- This is a decision problem (True/False).
  **4. 9 .1 Algorithm for Sum of Subset Problem**

SoS(n, M, A)
// A [1... n] is an array of elements

{

1. for i = 0 to n

for j = 0 to M

if (i > =0 and j = 0)

SoS [i, j] = T

else

if (i = 0 and j > 0)

SoS [i, j] = F;

else

if (A[i] > j)

SoS [i, j] = SoS [i – 1, j]

else

SoS [i, j] = SoS [i – 1, j] or

SoS [i – 1, j – A[i]]

}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Algorithm
```

**4. 9 .2 Time Complexity of SoS**

Two for loops are there thus repeating for (n * m) times. Thus, time complexity = O(n * m)

Time complexity of SoS becomes exponential if M = 2n

T.C = O(n × 2n)

### 

**TheoryTheory**

**of of**

**ComputationComputation**

**Theory**

**of**

**Computation**

```
Design Against Static Load
```

1. Basics of Theory of Computation ......................................................................................... 7 .1 – 7. 5
2. Finite Automata ................................................................................................................... 7. 6 – 7. 21
3. Push Down Automata .......................................................................................................... 7. 22 – 7. 29
4. Turning Machine ................................................................................................................. 7. 30 – 7.39

**INDEX**

GATE-O-PEDIA MECHANICAL ENGINEERING

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**BASICS OF THEORY OF**

**COMPUTATION**

**1.1 Symbol**

Symbol represents very unique in the world. Any small thing that never be broken into any other is called as symbol.

**1.2 Alphabet (**  **)**

It is a set of finite number of symbols.

Example:

- English alphabet = {a, b, ... z}
- Binary alphabet = {0, 1 }
- Decimal alphabet = {0, 1, 2, ... 9 }
- We can create our own alphabet = {gate, cs, it, exam}
  where gate, cs, it, exam all are symbols

**1.3 String**

- It is sequence of symbols defined over given alphabet.
  let  = {a, b}
- Strings possible are , a, b, aa, bb.........
- Strings over English Alphabet: deva, gate, exam, etc.
- Strings over Binary Alphabet: 0010, 1011, 1101, 1111, etc.
- Strings over Decimal Alphabet: 30 12, 2345, 5438 , etc.
  Note:
- Different length strings over given alphabet
  I Zero length string  Empty string / Null string  or  is used to denote empty string length of empty string. || = 0.
  II One length string over  = {a, b} are a, and b (2 strings).
  III Two length strings over  = {a, b} are da, ab, ba, and bb (4 strings).

```
Symbol
```

```
One Length string
```

```
It is smallest one
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**1.4 Operations on Strings**

There are various operations on strings:

- Unary and Binary operations

1. length of a string: Length of a string is denoted as |w| and is defined as the number of positions for the symbol in the
   string.
   Example: w = aba
   |w| =|aba| = 3
2. Reversal of a string: It will reverse or changes the order of a given string w.
   Example: w = abb
   wR^ = bba
   **1.4.1 Concatenation of Two Strings**

Given two strings w 1 and w 2 , we define the concatenation of w 1 and w 2 to be the string as w 1 w 2.

Example:

```
w 1 = a, and w 2 = ba
```

```
Then w 1 w 2 = a.ba = aba.
```

**1.4.2 Prefix of a String**

A substring with the sequence of beginning symbols of a given string is called a “prefix”.

Example:

(i) w = aaaa

```
Prefixes = {, a, aa, aaa, aaaa}
```

(ii) w = abcd

```
Prefixes = {, a, ab, abc, abcd}
```

Note:
If |w| = n then |wRev| = n.
If length of w 1 is n 1 and length of w 2 is n 2 then length of w 1 w 2 = |w 1 w 2 | = n 1 + n 2.

- Let w be n length string.
  (i) Number of prefixes in w = n+1
  (ii) Number of non-empty prefixes of w = n
  (iii) Number of different length prefixes of w = n + 1
  (iv) Number of different length prefixes of w excluding zero length = n

**1.4.3 Suffix of a String**

A substring with the sequence of ending symbols of a given string is called a “suffix”.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

Example:

(i) w = aaaa

```
Suffixes = {, a, aa, aaa, aaaa}
```

(ii) w = abcd

```
Suffixes = {, d, cd, bcd, abcd}
```

```
Note :
```

- Let w be n length string.
  (i) Number of suffixes of w = n + 1
  (ii) Number of non-empty suffixes of w = n
  (iii) Number of different length suffixes of w = n + 1
  (iv) Number of different length suffixes of w excluding zero length = n

**1.4.4 Substring of a String**

- Let w be n length string.
- Number of different length substrings of any given n length string =n+1
- Number of different length substrings of any given n length string excluding zero length=n.

**1.5 Relation between Symbol, Alphabet, String and Language**

```
Character
```

```

```

```
Character set
```

```

```

```
Token
```

```

```

```
C Language
```

```
Symbol
```

```

```

```
Alphabet
```

```

```

```
String
```

```

```

```
Language
```

```
(i) Number of substrings of w
```

```
minimum = n +1
(over 1 symbol)
```

```
maximum = 1+ n + (n – 1) + ....+1
(all characters distinct) =1 + n
= n +1
```

(ii) Number of non-empty substrings of w

minimum = n

maximum =n

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**1.5.1 Chomsky Hierarchy**

- Chomsky hierarchy includes all the problems in the world classified into classes.

### 

- Type 3 is the smallest class, and Type 0 is the biggest class.

```
Type 3 Type 2 Type 1 Type 0
```

```
Language: Regular Context free Context sensitive Recursively
Enumerable
Automata: Finite Automata Push down
Automata
```

```
Linear Bounded
Automata
```

```
Turing Machine
```

```
Grammar: Regular Context free Context Sensitive Unrestricted
```

**1.6 Language**

- Language is set of strings defined over alphabet ().
- Let  = {a,b}. Then  = ^0 ^1 ^2  .......
  = set of all strings
  = universal language
  = {, a, b, aa, ab, ba, ...}
- ^2 = ^1 • ^1 ={a,b}. {a,b} = {aa, ab, ba, bb}
- Language: It is a subset of *

 L*

- A language is a collection of strings that must be a subset of * where * is a universal language.

Example:

L = ab* = {a, ab, abb,..........}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**1.7 Types of Languages**

- Finite Language
- Infinite Language
- Regular language
- DCFL (Deterministic CFL)
- CFL
- CSL
- Recursive Language
- Recursive Enumerable Language (REL)

**1.8 Types of automata**

- Ralations between these machines:

### 

1. Less power: It can Represent less number of languages.
2. More power: It can Represent more number of languages Compare to all these machines.

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

2

**FINITE AUTOMATA**

**2.1 Introduction**

- Finite Automata describes or represents a regular language.
- Finite Automata is of two types:
  (i) Acceptor: Accepts or rejects given string.
  (ii) Transducer: Produces output string for given input string.

Example:

1's complement of binary number: Input = 10100, Output = 01011

**2.2 Finite Acceptor (Finite Automata)**

- Finite Automata:

```
FA = (Q, Σ, δ, q 0. F)
```

```
Transition function
Set of input symbols
Set of finite number of states
```

```
Set of final states
Initial state
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**2.3 Construction of DFA**

1. If epsilon belongs to L, then initial state must be final in DFA.
2. Dead state: It is non-final state but it never contain a path to final.

- Once we reach the dead state, there is no way to reach to the final state.
- If every state is final then every string accepted in the DFA.

3. If all states are finals in DFA then L(DFA) = *
4. If every state is non final in a DFA then L(DFA) =  or L(DFA) = {},

### L  * L

### L  L *

### LL

- If |w| = n or |w| n, then number of states in minimum DFA = (n + 2) states
- If |w|  n then number of states in minimum DFA = n+ 1 states.
- Start condition, exactly, atmost length question requires Dead state but end condition, contain substring, atleast length
  questions do not require dead state.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

- Over one symbol  = {a}. Length of string is equal to number of a's in string. |w|= na(w).
- Let L={w|w {a,b}*, na(w) is divisible by m, nb(w) is divisible by n}. Then Number of states in DFA= m×n.
- Let L={w | w belongs to {a. b}*, nth symbol of w from begin is 'a'}. Then Number of states in DFA = (n + 2).
- Number of equivalence classes for any regular set L = Number of states in minimal DFA that accepts L.

**2.4 Non-Deterministic Finite Automata**

**2.4.1 Introduction**

- Finite Automata can be designed in two ways:
- All these finite state machines are equivalent. DFA. NFA
- We can convert one finite state machine to any other finite state machine.
- For every gular language, we can design infinite equivaent DFAs or infinite equivalent NFAs but minimum DFA is uique
  for given regular language.
- For every regular language, one or more minimum NFAs may exist.

```
Note : For every regular language:
(i) Unique minimum DFA exists.
(ii) One or more minimum NFAs exists.
```

**2.5 Comparison of NFA and DFA**

```
|w| = n |w|  n |w|  n
```

```
Number of states in
NFA
```

```
n + 1 n + 1 n + 1
```

```
Number of states in
DFA
```

```
n + 2 n + 2 n + 1
```

- If every string has nth symbol from begin is 'a' over binary alphabet {a, b} then (n + 1) states in minimum NFA but (n+2)
  states in minimum DFA.

```
Finite Automata
```

```
DFA NFA (NDFA)
```

```
without
- moves
```

```
with
- moves
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

- If every string has nth symbol from end is 'a' over binary alphabet {a, b} then 2n states in minimum DFA and (n + 1) states
  in minimum NFA.
  **2.5.1 COMPARISON OF DFA AND NFA (NFA vs DFA)**

### NFA DFA

```
(1) Transition Function () Q ×  → 2 Q Q ×  → Q
(2) Number of paths for string For valid string: 1 path
For invalid string: >=0 paths
```

```
For valid string: 1 path
For invalid string: 1 path
```

**2.5.2 Number of states in DFA and NFA for Regular Languages**

```
Language NFA states DFA states
(1) {w | w  {a, b}*, |w| = n} n + 1^ n + 2^
(2) {w | w  {a, b}*, |w|  n} n + 1^ n +^2
```

```
(3) {w | w  {a, b}*, |w|  n} n + 1^ n +^2
(4) {w |w  {a, b}*, w starts with a} 2 3
(5) {w| w {a, b}*, nth symbol from begin is a} n + 1^ n +^2
(6) {w| w  {a, b}*, nth symbol from end is 'a'} n + 1^2 n^
```

**2.5.3 Finding number of states in DFA using NFA**

NFA (n states)
 Subset Construction
DFA (2n sates exists)
 Partition algorithm
Minimum DFA ( 2 n states) atmost 2n states

- Every DFA is NFA, but NFA need not be DFA.

**2.5.4 Relation between NFA with epsilon, NFA without epsilon, and DFA**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**2.6 Regular language Representation**

**2.7 FA Classification**

**2.8 Moore machine and mealy machine**

```
Moore machine Mealy machine
```

```
Transition Function  : Q ×  Q
Output Function  : Q  
Outpput is asociated with every state.
```

###  : Q ×  Q

###  : Q ×  

```
Output is associated with
transition.
```

```
Regular Language
```

```
FA Regular Expression Regular Grammar
```

```
DFA NFA
```

```
without
moves
```

```
with
moves
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**2.8.1 Example for Moore machine and Mealy machine**
Moore Mealy

### Q =

###  =

```
 = {x, y}
Outpput is asociated with state.
```

- Extra one output is produced other than desired
  output.
- So, we can ignore this extra output as this is the
  machine property.

### Q =

###  =

```
 = {x, y}
Output is associated with transition.
```

- No extra output is produced.
- For 3 length input, we are getting the 3 length
  output.

**2.9 Difference between Moore machine and Mealy machine**

```
Moore machine Mealy machine
```

1. (^)  Q ×  Q Q ×  Q

### 2.

###  Q   Q ×  

### 3.

```
Length of O/p
If n length I/P (assume 1 length O/P
symbol is taken at each state) then
O/P length is (n+1).
```

```
If n length input (assume 1 length
O/P symbol is taken at each
transition) is given then O/P length
is n.
```

4. By default DFA no final state. DFA no final state.

**2.10 Constuction of FA with output**

```

```

```
Moore Machine
```

```
Mealy Machine
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
Note :
For every problem, if moore machine exists the we can also construct equivalent mealy machine.
```

Example:

**2.11 Classification of Finite State Machine (FSM)**

**2.12 Regular Expression**

Definition:

```
o Regular expression represents a regular language.
o It describes a regular set.
o L (regular expression) is regular set.
o It is a kind of declarative way to represents a regular language.
o Regular expression generates a regular set.
o It uses 4 operators to represent a regular language.
```

```
Sum of present bit and previous bit.
Mealy Machine
0/00
0/01
1/10
1/01
Previous bit ‘0’ Previous bit ‘1’
```

```

```

```
Moore Machine
```

```
Mealy Machine
```

```
Bzoth are equivalent
```

```
Operators Operandas
(Regular expression)
```

```
Regular Expression
```

```
Unary Binary
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**2.13 Operators of Regular Expression**

1. OR ( )
   Binary Operator
2. Concatenation(.)

```
 


```

3. Kleenestar ( )*
   Unary Operator
4. Kleenestar (+)

```



```

```
Regular Expression Equivalent Regular Set
a + b L(a + b) = {a, b}
a + a = a L(a + a) = {a}
a +  = a L(a + ) = {a}
a +  =  + a L(a + ) = {a, }
 +  =  L(+) = {}
 +  = φ L( + ) = {}
a  b = ab L (a  b) = {ab}
a   = a L (a  ) = {a}
   =  L() = {}
   = φ L(  ) = {}
a  a = aa = a^2 L (a  a) = aa = {a^2 }
```

**2.14 Kleene star/ kleene closure / closure**

```
R* ( Kleene closure of R):
R* = R° +R^1 + R^2 +R^3 + ... =  + R + RR + RRR+ ....
```

Example:
a* = {a^0 , a^1 , a^2 , a^3 , ...} = {, a , aa, aaa, ...} = Set of all strings over a.
* = ^0 + ^1 + ^2 + ^3 + .... =  +  +  +  + .... =  +  = 

**2.15 Positive Closure (Kleeme Plus)**

```
R+ (Positive Closure of R):
```

```
R+= R^1 + R^2 + R^3 + .....
R* = R^0 i.e. repeart R any number of time
R+ = R^1 i.e. repeat R atleast 1 time.
R* = R+ + R^0
Example:
(1) a^ + = {a, aa, aaa, ...} = {an | n  1}
(2) + =  = *
(3) + = 
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

Properties :

```
OR Concatenation
```

1. Identity (^)  
2. Associative Yes Yes
3. Commutative Yes No
4. Annihilatior (^) * 
   **2.16 Identification of Regular Languages**
5. L={anbm |n, m  0 } = a*b* (Regular language)
6. L= {anbm|m<n<10} (Finite Set, Regular language)
7. L={anbm^ |m > n > 10} (Non Regular language)
8. L= {anbm^ |m = n, m < 10} (Regular language)
9. L={ anbm |m = n, m > 10} (Non Regular language)
10. L={ambn^ | gcd (m, n) = 1} (Non Regular language)
11. L={ambn^ |LCM (m, n) = 1} (Regular language)
12. L= {anbn^ | n >= 0} (Non Regular language)
13. L={anb2n^ |n  0} (Non Regular language)
14. L={ambn^ | m=even, n =odd} (Regular language)
15. L={ambn^ | m = n = even} (Non Regular language)

OR

L = {a^2 nb2n | n = even}

12. L={a*} over = {a}

= Regular language

13. L={a2n^ | n >= 0} over  = {a}.

L= a^2 n=(aa)*

= Regular language

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

14. L= {aPrime} over  = {a}

= Non regular language

15. L={
    n^2
    a |^ n^ ^ 0} over ^ = {a}^

L={epsilon, a, aaaa, a^9 , a^16 ...}, FA Not possible for L. So, it's Non-Regular language.

16. L= { 2

```
n
a | n > 0 }over  = {a}
```

Non Regular language

17. L= {^2

```
n
a | n  10}
```

= Regular language

18. L={an!^ |^ n  100} over S = {a}

= Non Regular language

19. L={
    nn
    a |n  10} over  = {a}

= Non Regular language

20. L = {aPrime}* over  ={a}

L = complement of {a} = *– {a} ={, a^2 , a^3 a^4 ,a^5 , a^6 , a^7 ,...}= Regular language

21. L = {aprime^ | prime <100} is finite language (regular)
22. L = {w # w | w  a*}

= Non Regular language

23. L = {w # w | w  (a+b)*}

= Non Regular language

24. L = {w # wR | w  a*} is non regular
25. L = {w x w | w  {a, b}*, x  {a, b}+}

Put w = , and x = (a + b)+

L = (a + b)^ +

= Regular language

26. L = {x w w | w  {a, b}* x  {a, b}+}

```
L = {an # an}
dependency
```

```
L = {an # an}
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

L = (a + b)+

= Regular language

27. L = {w wR^ x | w  {a, b}*, x  {a, b}+}

L = (a + b)+

= Regular language

28. L = {w x wR |w  (a + b)*, x  {a, b}+}

L = (a + b)^ +

= Regular language

29. L = {x w wR | w  {a, b}*, x  {a, b}+}

L = (a + b)+

**2.17 Closure Properties of Regular Languages**

1. Closure properties for finite languages:

**2.18 Table for FINITE sets**

(^) Finite sets Closed/Not Closed
(1) Union () F 1  F 2  Finite ^
(2) (^) Intersection () F 1  F 2  Finite 
(3) (^) Complement (L) F NOT finite 
(4) L 1 – L 2 F 1 – F 2  Finite ^
(5) L 1. L 2 F 1  F 2  Finite ^
(6) L* , L+^ F*, F+  May or may not be finite^ ^
(7) Subset (L) Subset (Finite set)  Finite^ ^
**2. 18 .1 Table for Infinite sets**
Union 
Intersection 
Complement 
Difference 
Concatenation 
Reversal 
Kleene closure
Subset 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
Infinite sets
```

(1) (^) Union () Infinite  Infinite  Infinite
(2) (^) Intersection () Infinite  Infinite  Need not be infinite
(3) (^) Complement (L) Complement of Infinite  May or may not be
infinite
(4) L 1 – L 2 Need not be infinite
(5) L 1. L 2 Infinite
(6) L*, L+^ Infinite
(7) Subset (L) Need not be infinite
**2.19 Closure Properties of Regulars**
Li→ Regular

1. (^)  2. (^) 
2. (^) L 4. (^) LL 12 
3. (^) LL 12  6. (^) LRev
4. (^) L 8. (^) L
5. Subset (L) is not closed for regular languages 10. Prefix (L)
6. Suffix (L) 12. Substring (L)
7. Substitution (L) 14. Homomorphism (L)
8. (^) -free homomorphism (L) 16. h–^1 (L) (Inverse homomorphism (L))
9. L 1 /L 2 (Quotient) 18. Symmetric difference
10. Half (L) 20. Second half (L)
11. One-third (L) [1/3 (L)] 22. Middle 1/3 (L)
12. Last 1/3 (L) 24.
    New L L 1 , 2 Suffix (L 1 L 2 )
13. Finite Union 26. Finite Intersection
14. Finite Difference 28. Finite Concatenation

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

 Out of the given 36 closure properties, how many are closed for regular languages?

```
Subset operation, and 6 infinite operations are not closed, remaining all are closed for regular languages.
```

Out of 36 operations total 7 operations are not closed.

**2. 19 .1 Operations over regular languages**
Examples:

(1)

```
*
1 *
+^12
2
```

```
L = a
L L = a
L=
```

### .

```
a
```

### 

### 

### 

(2) (^1122)
2

### L

### L + L = L

```
L Any
```

###  

### 

###  

### (3)

```
*
1 **
*^12
2
```

```
L = a
L + L = a + b
L = b
```

### 

### 

### 

### (4)

```
**
1 1 2
2 1
```

```
L L L
L Any language over same L
```

```
     
 

```

(5) (^)    
**
*^12
(^1) *
*
2
L + L = a b
La
a,b (^) a + b
L = b (^) 
  
 
  
 

Note :

1. (^112)
   2
   L
   LL
   L Any

### 

###  

```

```

```

```

```
 


```

```
2.
```

```
*
1
1 2 2
2
```

```
L
L + L = L
L Any
```

```
 

 
```

**2. 19 .2 Properties of regular languages**
I. If both L 1 and L 2 are regular sets then LL 12  is Regular.

II. IF LL 12  is regular set then

```
 L 1 “need not be regular”
```

29. Finite Subset 30. Finite Substitution
30. Infinite Union 32. (^) Infinite 
31. Infinite Difference 34. Infinite Concatenation
32. Infinite Subset 36. Infinite Substitution

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
 L 2 “need not be regular”.
```

III. If L is regular then L is regular.

IV. If L is regular then L is regular.

V. L is regular iff L is regular

VI. L is not regular iff L is not regular.

Example:

(^) abnn is not regular and abnn is not regular.
**2. 19 .3 Arden’s Lemma and Kleene Method
Arden’s Lemma:**
If R = Q + RP and P does not contain  then R = QP*
R = Q + RP ...(1)
= Q + (Q + RP) P = Q + QP + RP^2 ...(2)
Substitute R one more time in equation (2)
R = Q + QP + QP^2 + RP^3
If we do repetitive substitution infinite time, we will get R = QP*
Kleene Method:
(^)  
k k 1 k 1 k 1 * k 1
Rij Rij Rik Rkk Rkj
   

### LLG RLG

```
Each production in LLG follows
V → VT*
OR
V→T*^
```

```
Each production in RLG follows
V→T*V
OR
V→T*^
```

**2. 20 Identify the Language Generated by Regular Grammar**

```
Regular Grammar Regular Language
```

1. (^) S →  L = {}
2. (^) S → |a L = {, a}
3. S → aa | abc | d L = {aa, abc, d}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

4. S → Aa
   A → b

```
By default S is a start symbol here.
L = {ba}
```

5. S → Aa Useless production. It has no meaning.
   L = {} = 
6. 

```
Useless
```

```
SbAb |

```

```
 L = {b}^
```

### 7.

```
Look from bottom to top
```

```
L = {aa, bb}
```

### 8.

```
Regular Language Regular Grammar
a*^ (I) S → Sa | 
OR
(II) S → aS | 
a+ (I) S → Sa | a
OR
(II) S → aS | a
(a + b)*^ (I) S → Sa | Sb | 
OR
(II) S → aS | bS | 
(a + b)+^ (I) S → Sa | Sb | a | b
OR
(II) S → aS | bS | a | b
(ab)*^ (I) S → Sab | 
OR
(II) S → abS | 
```

**2.21 Pumping-Lemma (PL)**

**2 .2 1 .1 Pumping Lemma for Regular Languages**

**2.21.2 Pumping Lemma for Non-Regular Languages using contradiction**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**2 .2 1 .3 Proof for Regular Languages**
 If L is Regular language, then how pumping lemma proves it as regular?

**2.22 Equivalence Classes**

(1) L is regular iff L has finite number of equivalence classes.
(2) L is not regular iff L has infinite equivalence classes.

### 

### 

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

3

**PUSH DOWN AUTOMATA**

**3 .1 Context Free Grammar**

CFG: It represents a Context Free Language.

 Rule of each production in P:
V → (V  T)*
V = only 1 variable in LHS
 To derive a string, following derivations can be used.

1. Linear Derivation: Linear derivation is two types

(a) Left Most Derivation (LMD)

(b) Right Most Derivation (RMD)

2. Non- linear Derivation: Non- linear Derivation OR Parse Tree OR Derivation Tree

**3 .2 Types of Context Free Grammars**

There are two types of CFG:

1. Ambiguous CFG: At least one string has more than one derivation.
2. Unambiguous CFG: Every string (w) generated by CFG has exactly one derivation.

**3 .3 Pushdown Automata (PDA)**

PDA accepts context free language (CFL). PDA also called as NPDA.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**3. 4 PDA acceptance mechanisms**

 PDA acceptance mechanisms are three types:

1. PDA acceptance using final state.
2. PDA acceptance using empty stack.
3. PDA acceptance using both final state and Empty stack.
   All PDA acceptance mechanisms are equivalent.
    DPDA acceptance mechanism are two types:
   1. DPDA using final stack.
   2. DPDA using both final state and empty stack.

**3 .5 PDA configuration**

PDA = (Q, ∑, , q 0 , F, Z 0 , ).
where Q = Set of states
∑ = input alphabet
 = Transition Function (PDA/NPDA : Q∑  2 Q^ ^ *)
F = Set of Final state
Z 0 = Bottom symbol or initially TOS
 = Stack Alphabet
 DPDA transition Function is [: Q∑  Q  *]
 Difference between DPDA and PDA

```
DPDA PDA
[1] :Q∑ Q* :Q∑  2 Q^ ^ *
[2] Every DPDA is PDA Every PDA need not be DPDA
[3] DPDA acceptance with
(a) Final state mechanism
(b) Both Final and empty stack
```

```
PDA acceptance with
(a) Final state mechanism
(b) Empty stack mechanism
(c) Both Empty stack and Final
state
```

 Relation between Regular, DCFL and CFL.

Regular languages ......(FA)
DCFLs (DPDA)
CFLs (PDA or NPDA)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

I If L is regular language, then it is also DCFL and CFL.
II Every DCFL is CFL, but it need not be regular.

**3 .6 Closure Properties of CFLs**

- Operation Closed / Not Closed
  Union (L 1  L 2 ) ^
  Intersection (L 1  L 2 ) ^
  Complement (L) ^
  Set difference (L 1 - L 2 ) 
  Concatenation (L 1 .L 2 ) 
  Reversal (LRev) 
  Kleene Closure (L) 
  Kleene Plus (L) ^
  Subset (L) 
  Prefix (L) 
  Suffix (L) 
  Substring (L) 
  Substitution (L) ^
  Homomorphism (L) 
  - free Homomorphism h(L) 
  Inverse Homomorphism h-^1 (L) 
  quotient (L 1 , L 2 ) = L 1 /L 2 
  Symmetric difference (L 1 , L 2 ) 
  Finite Union 
  Finite Intersection 
  Finite difference 
  Finite concatenation 
  Finite subset 
  Finite substitution ^
  Infinite Union ^
  Infinite intersection 
  Infinite difference 
  Infinite concatenation 
  Infinite Subset 
  Infinite Substitution 
  Union with Regular (L U Regular) 
  L U Regular 
  L – Reg 
  Reg – L 

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Theory of Constraints
```

```
Note :(i) CFL  CFL = Need not be CFL
(ii) CFL  Regular = CFL (Need not be DCFL)
(iii) CFL  DCFL = May or may not be CFL
(iv) CFL  Finite = Finite
(v) CFL  infinite = Need not be CFL
```

**3 .7 Closure Properties of DCFLs**

- Operation Closed / Not Closed
  Union (L 1  L 2 ) ^
  Intersection (L 1  L 2 ) ^
  Complement (L) ^
  Set difference (L 1 - L 2 ) 
  Concatenation (L 1 .L 2 ) 
  Reversal (LRev) 
  Kleene Closure (L) = L* 
  Kleene Plus (L) = L+ 
  Subset (L) 
  Prefix (L) 
  Suffix (L) 
  Substring (L) ^
  Substitution (L) ^
  Homomorphism (L) 
  - free Homomorphism h(L) 
  Inverse Homomorphism h-^1 (L) 
  quotient (L 1 , L 2 ) 
  Symmetric difference (L 1 , L 2 ) 
  Finite Union 
  Finite Intersection 
  Finite difference 
  Finite concatenation 
  Finite subset 
  Finite substitution ^
  Infinite Union 
  Infinite intersection 
  Infinite difference 
  Infinite concatenation 
  Infinite Subset 
  Infinite Substitution 
  Union with Regular (L U Regular) 
  L U Regular 
  L – Regular 
  Regular – L ^

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
Note :
DCFL  Regular : DCFL
DCFL  Regular : DCFL
DCFL - Regular : DCFL
Regular - DCFL : DCFL
DCFL  CFL : CFL (need not be DCFL)
DCFL  CFL : Need not be CFL
DCFL - CFL : Need not be CFL
CFL - DCFL : Need not be CFL
DCFL  Finite : DCFL
DCFL  Finite : Finite
DCFL – Finite : DCFL
Finite - DCFL : Finite
```

**3 .8 Comparison of Regular Grammars and CFGs**

 CFL and CFG both are equivalent. CFLCFG

 LLG: Left Linear Grammar, RLG: Right Linear Grammar, RG: Regular Grammar, LG: Linear Grammar, CFG: Context

```
Free Grammar.
```

 Every LLG is RG

 Every RLG is RG

 Every RG is LG

 Every RG is CFG

 Every LG is CFG

 Every RG need not be RLG

 Every RG need not be LLG

 Every LG need not be RG

 Every CFG need not be RLG

 Every CFG need not be LG

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**3 .9 Context Free Languages and DCFLs**

I. Comparison of various languages

II. Identification of Regulars, DCFLs, and CFLs

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

[1] L = {anbnck n, m, k 0}
= a*b*c*
= Regular

[2] L = {anbn n 0}
L = DCFL but not regular
S → aSb  

[3] L = {anb2n n 0}
L = DCFL but not regular

S → aSbb  (^) 
[4] L = {a2nbn n 0}
L = DCFL
S → aaSb  
[5] L = {a2nb2n n 0}
L = DCFL
S → aaSbb  
[6] L = { anbnc*} Assume always n 0 in all examples
OR
= { ambnc* m = n}
DCFL but not regular
[7] L = { anb*cn} DCFL
[8] L = { a*bncn} DCFL
[9] L = { ambnc* m n }
DCFL
[10] L = { ambnc* m < n }
DCFL
[11] L = { ambnc* m > n }
DCFL
[12] L = { ambnc* cn }
DCFL
[13] L = { ambnc* m  n }
DCFL
[14] L = { ambncm+n m, n0 } is DCFL

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

[15] L = { am+nbn+kck+m m, n0 } is CFL

[16] L = { wwr w belongs to {a, b}* } is CFL but not DCFL

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

4

**TURNING MACHINE**

**4 .1 Classification of Languages**

1. All languages which are not RELs
2. All not recursive languages
3. All not CSLs
4. All not CFLs
5. All not DCFLs
6. All not regulars
7. All recursive languages which are not DCFLs
8. All RELs which are not DCFLs

**4 .2 There are Two types of TM**

(a) DTM (Deterministic TM)
(b) NTM (Non- Deterministic TM)

DTM

(^) :QQ
LeftRight

### LR,

```

```

### 

### 

### 

### NTM

: Q    2 Q{ L, R}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**4 .3 Unrestricted Grammar (UG) and Context Sensitive Grammar (CSG)**

Unrestricted grammar (UG) also called as
 RE grammar
 Phase structure grammar
Context sensitive grammar (CSG) is also called as
 Non contracting grammar
 Bound restricted grammar

**4 .4 Grammars**

Left Linear Grammar (LLG): V VT*  T*
Right Linear Grammar (RLG): V T*V  T*
Linear Grammar (LG): V T*VT*  T*

Context Free Grammar (CFG): LHS  RHS, (^) LHS RHS
Unrestricted Grammar (UG): LHS  RHS
**4 .5 Equivalence of various TMs**
TM Single tape TM
TM One-way infinite tape TM
TM Two-way infinite tape TM
TM Multi tape and multi head TM
TM Universal TM
TM Two stack PDA
TM Multi stack PDA
TM FA with two stacks
TM FA + R/W tape + Bidirectional head
**4 .6 Restrictions on TM**
(1) If TM tape is read only tape, this TM accepts regular.
TM FA (TM with read only tape)
(2) If TM head is unidirectional then L(TM) = Regular.
(3) If TM tape is read only and unidirectional head then L(TM) = Regular.
(4) If TM always halts then L(TM) is recursive language.
(5) If TM always halts and uses linear bound tape then L(TM) is CSL.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**4. 7 LBA, HTM and TM**

HTM: It is a TM that always halts for every input.
TM: It halts for every valid string and for invalid strings either halts at “non final state” or “never halts”.
LBA: It is HTM but length of the tape we use linearly bounded.
 LBA accepts CSL languages.
 HTM accepts recursive languages.
 TM accepts Recursive Enumerable (RE) languages.

**4. 8 Recursively Enumerable Language**

It is also called as:
 Enumerable language
 TM recognizable language
 TM Enumerable language
 Partially decidable language
 Semi-decidable language

**4. 9 Recursive Language**

 Recursive language is acceptable by HTM, and hence acceptable by TM.
 Recursive also called as decidable language.
 Recursive also called as Turing decidable language.
If TM always halts, then TM is called as HTM.

**4 .10 Difference between Recursive and REL**

 All Recursive languages are RE languages.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
Note :
```

1. Union:
   REL  Finite  REL
   REL  Regular  REL
   REL  CFL  REL
   REL  Recursive  REL
   REL 1  REL 2  REL
   2. Intersection:
   REL  Finite  REL (Finite)
   REL  CFL  REL
   REL  Rec  REL
   REL 1  REL 2  REL

**4. 11 Closure Properties of Recursive languages**

I. The following operations are not closed for recursive languages:
 Subset
 Substitution
 Homomorphism
 Finite substitution
 Infinite union
 Infinite intersection
 Infinite concatenation
 Infinite difference
 Infinite substitution
II. The following operations are closed for recursive languages:
 Complement
 Difference
 Finite difference
 Infinite followed by , , -, , , f
 Remember not closed operations

**4 .1 2 Complement of Recursive Vs Complement of REL**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

 Complement of Recursive set is Recursive.
 Complement of REL is either Recursive or non-REL.
 Complement of REL never be “REL which is not recursive”.

**4 .13 Decidable and Undecidable**

**4 .14 Decidable Vs Undecidable, RE Vs Not RE, Countable Vs Uncountable**

[1] Decidable and Undecidable

```
HTM exist HTM not exist
(Rec language) (not Rec language)
```

[2] RE and Not RE

TM exist TM not exist

[3] Countable set and Uncountable set

X is countable set (X is not countable set)
iff
Xf(X) is bijective where f(X) is known countable set.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
Note :
 If problem p is decidable then p is also decidable.
 If problem p is Undecidable then p is also UD.
 If problem p is RE but not recursive then p is not RE.
 If problem p is not RE then p is either “Not RE” or “RE but not Recursive”.
```

**4 .15 Decision Properties Table**

 D: Decidable
 UD: Undecidable

```
FA DPDA PDA LBA/HTM TM
H (Halting) D D D D UD
M
(Membership)
```

### D D D D UD

```
Em
(Emptiness)
```

### D D D UD UD

```
F (Finiteness) D D D UD UD
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

```
T (Totality) D D UD UD UD
Eq
(Equivalence)
```

### D D UD UD UD

```
D (Disjoint) D UD UD UD UD
S (Set
Containment)
```

### D UD UD UD UD

**4 .16 Decidable problem for DFA / NFA/ FA/ Regular**

(1) Halting problem for FA / Reg/ DFA / NFA is decidable.

(2) Non-halting problem for FA / Reg/ DFA / NFA is decidable.
(3) Membership problem for FA / Reg/ DFA / NFA is decidable.

(4) Non-membership problem for FA / Reg/ DFA / NFA is decidable.

(5) Emptiness for FA / Reg/ DFA / NFA is decidable.
(6) Non-emptiness problem for FA / Reg/ DFA / NFA is decidable.

(7) Fitness problem for FA / Reg/ DFA / NFA is decidable.
(8) Non-fitness problem for FA / Reg/ DFA / NFA is decidable.

(9) Totality problem for FA / Reg/ DFA / NFA is decidable.
(10) Non-totality problem for FA / Reg/ DFA / NFA is decidable.

(11) Equivalence problem for FA / Reg/ DFA / NFA is decidable.
(12) Non-equivalence problem for FA / Reg/ DFA / NFA is decidable.

(13) Disjointness problem is decidable for FA / Reg/ DFA / NFA.

(14) N0n-disjointness problem is decidable for FA / Reg/ DFA / NFA.
(15) Set containment problem for FA / Reg/ DFA / NFA is decidable

(16) Non-set containment problem for FA / Reg/ DFA / NFA is decidable.

**4 .17 Decidable problems for CFLs/DCFLs**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**4 .18 Decidability problems for Recursive languages**

(^) Problems Recursive

1. Halting D
2. Non-Halting D
3. Membership D
4. Non-membership D
5. Emptiness UD [Not REL]
6. Non-emptiness UD [RE but not Rec] [SD but UD]
7. Finiteness UD [Not RE]
8. Non-finiteness UD [Not RE]
9. Totality UD [Not RE]
10. Non-totality UD [RE but not Rec] [SD but UD]
11. Equivalence UD [Not RE]
12. Non-equivalence UD [RE but not Rec]
13. Disjointness UD [Not RE]
14. Non-disjointness UD [RE but not Rec]
15. Set containment UD [Not RE]
16. Non-set containment UD [RE but not Rec]

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

**4 .19 Classification of Languages based on Decidability**

All RE languages can be classified into 3 important classes.

**4 .19.1 Decidability Vs Turing Machine**

**4 .20 Decidable languages**

(1) Finite set  Decidable
(2) ∑ = {a, b}  Decidable
(3) ∑ Set of finite number of symbols  Decidable
(4) ∑* over alphabet ∑ = {a, b}  Decidable
(5) {M  M is DFA, M accepts ab}  Decidable

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Theory of Constraints
```

(6) {TM  Number of states in TM= 2}  Decidable
(7) {TM  TM reaches state q within 100 steps}  Decidable
(8) { TM  TM accepts REL}  Decidable

### 

### 

**CompilerCompiler**

**DesignDesign**

**Compiler**

**Design**

```
Design Against Static Load
```

1. Introduction and Lexical Analysis ......................................................................................... 8 .1 – 8. 2
2. Parsing ................................................................................................................................. 8. 3 – 8. 11
3. Lexical Analysis .................................................................................................................... 8. 12 – 8. 13
4. Syntax Directed Transaction ................................................................................................ 8. 14 – 8. 16
5. Intermediate, Code Optimization ........................................................................................ 8. 17 – 8. 23

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

1

**INTRODUCTION AND LEXICAL**

**ANALYSIS**

**1.1 CD Introduction**

**1.1.1 Definition**

Convert High Level Language to Low Level Language.

 High Level Language can perform more than one operation in a single Statement.
 lol Level Language can perform atmost one operation in a statement.

**1.2 Analysis and Synthesis model of Compiler**

 There are 6 phases of the Compiler

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

1. Lexical Analyzer:

 Program of DFA, it checks for spelling mistakes of program.

 Divides source code into stream of tokens.

2. Syntax Analyzer:

 Checks grammatical errors of the program (Parser).

 Parser is a DPDA.

3. Semantic Analyzer:

Checks for meaning of the program.

Example:

Type miss match, stack overflow

4. Intermediate Code Generation:

 This phase makes the work of next 2 phases much easier.

 Enforces reusability and portability.

5. Code optimization:

 Loop invariant construct

 Common sub expression elimination

 Strength Reduction

 Function in lining

Deadlock elimination

6. Symbol Table:

(1) Data about Data (Meta data)

(2) Data structure used by compiler and shared by all the phrase.

### 

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

2

**PARSING**

**2.1 CD - Grammar**

 In compiler we only use: Type – 2 (CFG) and Type – 3 Regular grammar.
 Compiler = Program of Grammar
 Compiler = Membership algorithm

- Every programming Language is Context Sensitive Grammar (Context Sensitive Language)

**2.1.1 Parse Tree and Syntax Tree**

G: E  E + T / T E  E + T  T + T  T (^) * F + T  F * F + T  (^2) * F + T  (^2) * 3 + T  (^2) * 3 + F
T  T (^) * F / F
E  2 * 3 + 4
Parse Tree:
Syntax Tree:
 To check to priority / Associativity:
Randomly derive till you have enough operators, then check which one is done first.
 If priority of 2 operators is same and both Left and Right associative  Ambiguous Grammar [Useless]

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

**2. 1. 2 Types of Parsers in Bottom Up: [CD - Parser]**

**2.2 CD-Syntax Analysis / Parsing**

Grammatical Errors are checked by the help of parsers.

 (^) Parsers are basically DPDA
 All of these parsers are table driven.
**2.2. 1 Mathematical Model of Parser**
 Parsers generate Parse Tree, for a given string by the given grammar.

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

**2.2. 2 Top-Down Parser (LL (1))**

 It uses LMD and is equivalent to DFS in graph.

**2.2. 3 Algorithm to construct Parsing Table**

1. Remove Left Recursion if any.
2. Left Factor [Remove Common Prefix]
3. Find first and follow set
4. Construct the table.

 If we increase the look ahead symbol:

**2.2. 4 Removal of common Prefix: (Left Factor)**

1. S  a | a b | a A S  a Y

Y   |b| A

2. A  a b A | a A | b

A  a  | b A  a  | b

X  b A | A X  b A | a x | b

A  a X | b

X  a X | b

Y Y  A | 

**2.2. 5 First and Follow**

 First Set  extreme Left terminal from which the string of that variable starts.

 it never contains variable, but may contain ‘’.

 we can always find the first of any variable.

 Follow set  Follow set contains terminals and $.

```
It can never contain variable and ‘’.
How to find follow set?
```

1. Include $ in follow of start variable.
2. If production is of type 

```
A  B   strings of grammar symbol].
follow (B) = first ().
If,   , i.e. A  B, then follow(B) = follow(A).
```

 Productions like: A  A gives no follow set.

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

```
First^ Follow^
E C, id $, )
```

E’ (^) +,  $, )
T C, id +, $, )
T’ (^) *,  +, $, )
F C, id *, +, $, )
**2.2. 6 Example of first and follow set**

1. S  AB | CD

```
A  aA | a
B  bB | b
C  cC | c
D  dD | d
```

**2.2. 7 Entity into Table: Top Down**

1. No of Rows = number of unique variable in Grammar.
2. No of columns = [Terminals + $]
3. For a Variable (Row) fill the column (Terminal) if its P, there in its first with the production required.
4. If  is in first put V   under $ and its follow.

 If any cell has multiple items, then its not possible to have LL (1) Parser, since that will be ambiguous.
 In top down we do: Derivation
In Bottom up we do: Production.

Question: Construct LL (1) Parsing Table for the given Grammar: E^ ^ E^ +^ T^ |^ T;^ T^ ^ T^ *^ F^ |^ F;^ F ^ (E) |^ id;^ ^ G 0
 Removing Left Recursion:
E  TE’
E’ + TE’ | 
T  FT’ G 1
T’ *FT’| 
F  (E) | id

 Left Factoring not Required:
Construction of Table: [LL ( 1 )]
+^ *^ (^ )^ id^ $^

E Error Error (^) ETE’ Error (^) ETE’ Error
E’ (^) E’TE’ Error Error (^) E’ Error (^) E’
T Error Error TFT’ Error TFT’ error
T’ (^) T’ T’*FT’ Error (^) T’ Error (^) T’
F Error Error (^) F() Error (^) Fid error
 Since for^ G 1 ,^ Table^ constructed^ with^ no^ multiple entries.^ Hence^ successfully^ completed.^ Hence^ G^1 is^ LL^ (1)
Question: Construct LL (1) Parsing Table for the following Grammar:
S  L = R | R; L  * R | id; R  L  G 0
Solution: Left Factoring:
First^ Follow^
S a, c $
A a b
B b $
C c D
D D $

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

Co nstruction of Table:^

```
*^ =^ Id^ $^
```

S (^) SLX Error (^) SL
X
Error
L (^) L*R Error (^) Lid Error
R (^) RL Error (^) RL Error
 Error^ X = R^ Error^ X^
 G 1 is a LL (1) Grammar.
**2.2. 8 Hierarchy of Parsers: [for**  **- free Grammar]**
 (^) For  - producing grammars every LL (1) may not be LALR ( 1 ).
Example:
G: S  a S a | b S b | a | b (Unambiguous but no parser) L(G) = (a + b)  R
(Odd palindrome)
 Every RG is not LL (1) as it may be ambiguous, or Recursive or Common Prefix.
 Parsers exists only for the grammar if its Language is DCFL.
 There are some grammars whose Language is DCFL but no parser is possible for it.
Note:
We can’t construct any parser for ambiguous grammar. Except: Operator precedence, parser possible for some
ambiguous grammar.

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

**2 .4. 9 Operator Precedence Grammar**

Format: (1) No 2 or more variable side by side
(2) No  production.

Example:

**2.2. 10 Checking LL (1) without Table**

A  1 | 1 | 1 then  A  1 | 2 | 3 |

first ( 1 )  first ( 2 ) =  first ( 1 )  first ( 2 ) = 
first ( 1 )  first ( 3 ) =  first ( 1 )  first ( 3 ) = 
first ( 2 )  first ( 3 ) =  first ( 2 )  first ( 3 ) = 
follow (A)  first ( 1 ) = 
follow (A)  first ( 2 ) = 
follow (A)  first ( 3 ) = 

**2.2. 11 Bottom-UP Parser**

 It uses RMD in reverse and has no problem with:
(a) Left recursion (b) Common Prefix

LR (1) = LR(0) + 1 Lookahead
 No parser possible for ambiguous grammar.
 There are some unambiguous grammars for which, there are no Parser.

**2.2. 12 Basic Algorithm for Construction**

 Augment the grammar and expand it, and give numbers to it
 Construct LR (0) or LR (1) item set.
 From that fill the entries in the Table Accordingly.

### SLR (1) LR (0)

```
LR (0) items
```

### CLR (1) LR (1)

```
LALR (1) items
```

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Compiler Design
```

**2.2. 13 Types of Entries**

(1) Shift Entries: Transitions or Terminals

E ntry:
a^
I 0 S 1

a Terminal I 0 , I 1 : Item sets.



 Shift entries are some for all Bottom – up Parser.

(2) State Entry: Transition or non – terminal (variable)^

A  Variable

Entry:

```
A
I 0 1
 Same for all Bottom-up Parser.
(3) Reduce Entity: done for each separate production in the item set of type:
i > ×  
where, i  Production Number
```

```
×  Producing Variable
  Grammar String
```

```
(a) LR (0) Parser:
Put Ri in every cell of the set-in action table (ALL).
(b) SLR (1) Parser:
Put Ri only in the follow(x) form the Grammar. (Follow(x))
(c) LALR (1) and CLR ( 1 ):
Put Ri only in the look ahead of the production (Lookaheads)
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 10
Compiler Design
2.2. 14 Conflicts**
LR (0) Parser:
SR: Shift Reduce Conflict
S  X    t then SR
R  Y  δ  conflict
RR: Reduce Reduce conflict
R  X    then RR
R  X   
SLR (1) Parser:
SR:
t  follow (Y)
RR:

Follow (x)n follow (y) 
LALR (1) and CLR ( 1 ): Same as SLR ( 1 ), but instead
SR:

### T  L 2

### RR:

### L 1  L 2  




**2 .4. 15 Inadequate Static**

A static having ANY conflict is called a conflicting state or independent state.

 The only difference between CLR (1) and LALR (1) is that, the states with the similar items, but different Lookaheads are
merged together to Reduce space.

**Important Points**

1. If CLR (1) doesn’t have any conflict, then conflict may or may not arise after merging in LALR (1).
2. If LALR (1) has SR – conflict, then we can conclude that CLR (1) also has SR – Conflict.
3. LALR (1) has SR – conflict if and only if CLR (1) also has SR.

```
Note:
The state S’  S. or S'  S.,$ is accepted state, and this is not a reduction.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 11
Compiler Design**

- We can construct parser for every unambiguous regular grammar: [CLR (1) Parser].

### S

```
Simple
```

### L

```
L to R
Scan
```

### R

```
Using
Reverse
RMD
```

### (1)

```
Lookahead
```

### L

```
Look
```

### A

```
Ahead
```

### L

```
L to R
Scan
```

### R

```
Revers
RMD
```

### (1)

```
Lookahead
```

```
C
Canonical
```

### L

```
L to R
Scan
```

### R

```
reverse
RMD
```

### (1)

```
Lookahead
```

Very Important Point:
LALR (1) Parser can Parse non LALR (1) grammar, when only non-SR – Conflict by favouring shift over reduce.

Example: E  E + E | E * E | id | 2 + 3 * 5  E + E  (^) * 5

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 12
Compiler Design**
3
**LEXICAL ANALYSIS
3.1 Lexical Analysis
3.1.1 Definition**
Scan the whole program, char by char and produces the corresponding token.
 Also produces /Lexical Errors (if any).
 Functions of Lexical Analyzer.
(1) Scans all the character of the program.
(2) Token recognizer.
(3) Ignores the comment & spaces.
(4) Maximal Munch Rule [Longest Prefix Match].
 Lexeme  smallest unit of program or Logic.
 Token  internal representation of Lexeme.
**3.1.2 Types of Token**
(1) Identifier
(2) Keywords
(3) Operators
(4) Literals/Constants
(5) Special Symbol
Note:
The Lexical Analyser uses, the Regular Expression.
Prioritization of Rules.
Longest Prefix match.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 13
Compiler Design
3.1.3 Token Separation**
(1) Spaces
(2) Punctuation
**3.1.4 Implementation**
 LEX tool  Lex.yy.e
 All identifiers will have entry in symbol Table/ LA, gives entries into the symbol Table.
Regular Expression  DFA  Lexical Analyzer
**3.1.5 Find number of Tokens**
(1) void main () {
Printf(“gate”);
}
{11 Tokens}
(2) int x, *P;
x = 10; p = &x; x++;
[18 Tokens]
(3) int x;
x = y;
x == y;
[11 Tokens]
(4) int 1x23; [Lexical Error]
(5) char ch = ‘A’;
[5 Token]
(6) char ch = ‘A;
Lexical Error.
(7) char *p = “gate”;
[6 Tokens]
(8) char * p = “gate;
Error.
(9) int x = 10;
/* comment x = x + 1; ERROR
x = x + 1; [11 Tokens]

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 14
Compiler Design**
4
**SYNTAX
DIRECTED TRANSACTION
4.1 Syntax Directed Transaction**
SDT: CFG + Transition → 1) Meaning 2) Semantic
**4.1.1 Application of SDTL**
(1) Used to perform Semantic Analysis.
(2) Produce Parse Tree.
(3) Produce intermediate representation.
(4) Evaluate an expression.
(5) Convert infix to prefix or postfix.
Example: S  S 1 S 2 [S.count = S 1 .count + S 2 .count]
S  (S 1 ) [S.count = S 1 .count + 1]
S   [S.count = 0]
 Count is an attribute for non–terminal
**4.1.2 Attributes**
(1) Inherited Attribute
(2) Synthesized Attribute
(1) Inherited Attribute: (RHS)
 The computation at any node (non-terminal) depends on parent or siblings (S).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 15
Compiler Design**
 In above Example, x is inherited attribute.
(2) Synthesized Attribute: (LHS)
x is synthesized attribute.
The computation at any node (non-terminal) depends on children.
**4.1.3 Identifying Attribute Type**
 Always check every Translation.
**4.1.4 Syntax Directed Definitions (SDDs): (Attribute Grammar)**
(1) L-Attributed Grammar
 Attribute is synthesized or restricted inherited. (1) Parent 2) Left sibling only).
 Translation can be appended anywhere is RHS of production.
 Example: S  AB {A.x = S.x + 2}
or, S  AB {B.x = f (A.x | S.x)}
or, S  AB {S.x = f (A.x | B.x)}
 Evaluation: In Order (Topological).
(2) S-Attributed Grammar:
 Attribute is synthesized only.
 The transaction is placed only at the end of production.
 Example: S  AB {S.x = f (Ax | Bx)}.
 Evaluation: Reverse RMD (Bottom-Up Parsing).

1) (^) D  T : L ; {L.Type = T.Type} inherited
   L  L 1 , id ; {L 1 .Type = L.Type} inherited
   L  id
   T  integer {T.Type = int} synthezised
   Type is neither inherited
   nor synthesized
2) 

E  E1 + T {E.val = E1.val + T.val} synthesized
E  T {E.val = T.val} Synthesized
T  T 1 – F {T.val = T 1 .val – F.val} Synthesized
F  id {F.val = id.val} synthesized
Val is
synthesized attribute
3)
S  AB {Aa = B.x; S.y = A.x} x is inherited | y is
synthesized
A  a {A.y = a} y is synthesized
B  b {B.y = a.y} y is synthesized
x  inherited
y  synthesized
4) (^) D  T L {L.in = T.type} inherited(in)
T  int {T.type = int} /synthesized
L  id {Add type(id.entry,L.in)}
in  inherited
type  synthesized

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 16
Compiler Design
4.1.5 Identify SDD**
(1) E  E 1 + E 2 {E.type = if (E 1 .type = = int & & E.type = = int) then int} Synthesizer else type – error.
E  id {E.type = Lookup (id.entry)} synthesizer.
 type is synthesized, hence S-attribute and also L-attributed Grammar.
 Every S-attributed Grammar is also L-attributed Grammar.
 For L-attributed Evaluation, use the In-order of annotated Parser Tree.
 For S-attributed, reverse of RMD is used.
 find RMD Order.
 Consider its reverse.



**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 17
Compiler Design**
5
**INTERMEDIATE, CODE
OPTIMIZATION
5.1 Introduction**
Example Expression:
(^) Syntax Tree 
(^) DAG 
3 - address Code: Code in which, at most 3 addresses. [including LHS]^

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 18
Compiler Design**
 3 AC done using operator precedence.
Find minimum number of variables required in equivalent 3 AC:
1.
u u t u t z
v u * u z w * v
w v w
   



 5 variables only
 Evaluating the expression:
a  c + b  d – b + b  b + c – b + b
 b + a + d – b + b
 b + b + c + d – b + b
 (^) b + b + c + d

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 19
Compiler Design**
 Minimum:
b b b
c b c
a c d




 only 3 variables [most optimal]
**5.1.1 Static Single Assignment Code: (SSA Code)**
Every variable (address) in the code has single assignment [single meaning] + 3AC.
1.
 [u, t, v, w, z] are already assigned so we can’t use them.
Equivalent SSA Code:
x = u – t y = x * v
p = y + w
q = t – x
r = p * q
in use: x, y, p, q, r  additional
 Total Variable  10.
2.
 [a, b, c, u, v] are already assigned,
Equivalent SSA Code:
p = a – b
q = p * c
p 1 = v * u
q 2 = p 1 + q
in use: p, q, p 1 , q 2
 Total Variable = 9

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 20
Compiler Design
5.1.2 Control Flow Graphs**
 CFG contain group of basic blocks and controls. CFG has nodes and edges to define basic blocks and controls.
 Basic Blocks: Sequence of 3-address code statements, in which control enters only from 1st statement (called as leader),
and leaves from last statement.^
Example:
**5.2 Code Optimization**
Saves space / time. (Basic Objective)
**5.2.1 Optimization Methods**

1. Constant folding
2. Copy propagation
3. Strength Reduction
4. Dead code elimination
5. Common sub expression elimination.
6. Loop Optimization
7. Peephole Optimization
   1. i = 1 LB 1
   2. j = 1 LB 2
   3. t1 = 5 * i
   4. t2 = t1 + 5
   5. t3 = 4*t2
   6. t4 = t3
   7. a[t4] = 1
   8. j = j + 1
   9. if j ≤ 5 goto 3 LB 4
   10. i^ =^ i^ +^1 LB 5
   11. if i < 5 goto 2 LB 6

### LB 3

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 21
Compiler Design**

1. Constant Folding
   (i) x = 2 * 3 + y  x = 6 + y
   Folding
   ii) x = 2 + y * 3} can’t fold the constant
2. Copy Propagation
   i) Variable Propagation:
   x = y;
   z = y + 2;
    z = x + 2;
   ii) Constant Propagation:
   x = 3
   z = 3 + a;
    z = x + a
3. Strength Reduction:
   Replace expensive statement / instruction with cheaper one.

(i) x = 2 * y costly (^)  x = y + y; Cheap
(ii) x = 2 * y (^)  x = y < < 1 ; Much Cheaper
(iii) x = y / (^8)  x = y > > 3 ;

4. Dead Code Elimination:

- Hence, above dead code never executes during execution. We can always delete such code.

5. Common Sub Expression Elimination:
   DAG is used to eliminate common sub expression.
   Example: x = (a + b) + (a + b) + c;
    t 1 = a + b
   x = t 1 + t 1 + c
   

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

(^) **8. 22
Compiler Design**

6. Loop Optimization:
   (i) Code Motion – Frequency Reduction:
   Move the loop invariant code outside of loop.^

```
(ii) Induction Variable elimination:
```

(iii)^ Loop^ Merging^ /^ Combining:^ (Loop^ Jamming)^

```
(iv) Loop Unrolling:
```

```
1) for (i = 0; i < 3; i++)
printf(“CD”);
```

```
printf(“CD”);
printf(“CD”);
printf(“CD”);
3  3 + 2 = 11 Statements 3 statements^
```

```
2)
for (i = 0; i < 2 n; i ++) {
printf(“CD”);
}
```

```
for (i = 0; i < n; i++) {
printf(“CD”);
printf(“CD”);
}
( 2  3n + 2) = 6n + 2 (4n + 2)
```

7. Peephole Optimization:

```
Examines a short sequence of target instructions in a window (peephole) and replaces the instructions by a faster and/or
shorter sequence when possible.
```

- Applied to intermediate code or target code
- Following Optimizations can be used:

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Compiler Design
```

- Redundant instruction elimination
- Flow-of-control optimizations
- Algebraic simplifications
- Use of machine idioms
  
  

 

**OperatingOperating**

**SystemSystem**

**Operating**

**System**

```
Design Against Static Load
```

1. Introduction and Background of OS ..................................................................................... 9 .1 – 9. 3
2. Process Concepts ................................................................................................................. 9. 4 – 9. 6
3. CPU Scheduling .................................................................................................................... 9. 7 – 9. 10
4. Multithreading...................................................................................................................... 9. 11 – 9. 12
5. Synchronization ................................................................................................................... 9 .1 3 – 9 .2 6
6. Deadlock .............................................................................................................................. 9. 27 – 9 .2 9
7. Memory Management ......................................................................................................... 9. 30 – 9 .35
8. Virtual Memory .................................................................................................................... 9. 36 – 9 .3 8
9. File Systems ......................................................................................................................... 9. 39 – 9 .42
10. Disk Scheduling ..................................................................................................................... 9. 43 – 9. 44

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

1

**INTRODUCTION AND**

**BACKGROUND OF OS**

**1.1 What is OS**

Operating system is an interface between the user applications and the computer hardware to develop and execute programs.

**1.2 Goals of OS**

- The primary goal of the operating system is to provide an easy-to-use environment to the user.
- The secondary goal of the operating system is the efficient use of the computer resources. (Operating system is also
  called as the resource allocator)
- Modularity
- Abstraction
- Ease of debugging

**1.3 Functions of OS**

- Process Management
- Memory management
- Resource Allocation
- File systems management
- Protection and Security

**1.4 Types of OS**

**1.4.1. Batch Operating System**

- Jobs with similar requirements are grouped into batches by the operating system.
- The idea is to execute the jobs onto the CPU one at a time. Another job cannot occupy the CPU time until the previous
  job has completed execution.
- Increased CPU idleness.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

- Decreased throughput of the system.

**1.4.2 Multi-programmed/multi-tasking operating system**

- Multiple programs/jobs reside in the main memory for execution. The operating system selects and executes one of these
  jobs on to the CPU.
- If the job in execution requires an I/O operation, another job which is ready for execution is scheduled on the CPU.
- Increased CPU utilization.
- Increased throughput of the system.
- Multi-tasking is a logical extension of multi-programming systems. The jobs are executed on the CPU in time sharing
  mode.
- The main advantage of multi-tasking systems is good response time.

**1.4.3 Real time operating system**

- It has well-defined and fixed time constraints.
- Processing of the programs must be done in the defined constraints or the system will fail.
- They are categorized into-hard and soft real time systems.

**1.4.4 Distributed operating system**

- A distributed operating system handles jobs that are executed by multiple processors networked to each other.
- They are also termed as loosely coupled systems.
- The advantages of distributed systems include resource sharing, computation speed up and reliability.

**1.5 Dual Mode Operations**

A processor supports two modes of instruction execution:

- User mode/ non-privileged mode
- Kernel mode/ Privileged mode/ Monitor mode

The primary goal of the dual mode operation is to provide protection and security to the user application programs and the
operating system from the unauthorized users. The mode bit is used to determine the particular mode in which an instruction
is executing.

```
Mode bit: 0 Kernel mode
Mode bit: 1 User mode
```

- A process running in kernel mode has direct access to the hardware and full access to the machine instruction set. The
  operating system always runs in kernel mode.
- Other examples of privileged instructions include I/O operations, context-switching, clearing the memory map etc.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

- A process running in user mode has no access to the hardware and limited access to the machine instruction set.
- Other examples of non-privileged instructions include reading the time of the clock, reading the status of the processor,
  generate trap etc.

**1.6 System Call**

- System calls provide the services of the operating system to the user application programs.
- They act as entry points into the kernel system.

**1.6.1 Fork () System Call**

- The fork () system call is used to create the child processes.
- It returns 0 to the newly created child process.
- It returns the process id of the child process to the parent process on successful creation of the child process.
- It returns negative value to the parent process on unsuccessful creation of the child process.
- If the program contains ‘n’ fork () system calls, then-

```
Number of child processes created = 2n– 1.



       
```

###  

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

2

**PROCESS CONCEPTS**

**2.1 Program Versus Process**

```
Program Process
Program is a set of instructions and data. A program under execution is called a process.
It resides in the secondary memory. It resides in the main memory.
It is passive. It is active and dynamic.
It is not allocated any resources. The operating system allocates resources to the
process for its execution.
```

**2.2 Process as ADT**

The process image can be described as:
Process
Process attributes (Process Control Block)
Run time Stack
Dynamic data
Static data
Code section

Any process has the following attributes:
 Process identification information
 Priority
 Process state information
 Program counter
 Memory limits
 List of files
 List of open devices
 Protection information
All the attributes of the process are stored in the Process Control Block (PCB). The features of Process Control Block are as
follows:
 Every process has its own process control block.
 The process control blocks of all the processes are stored in the main memory.
 They are implemented using double linked list data structure.
The context of a process includes the process attributes and the stack information.

```
Context
```

```
User address space
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**2.3 Process State Transition Diagram**

A process passes through multiple states in its lifetime as follows:

 When the process is present in the Ready, Run or Wait state, it still resides in the main memory.
 When the process is present in the Suspend Ready or Suspend Block state, it resides in the secondary memory.
 There can be multiple processes present simultaneously in the Ready, Wait, Suspend Ready and Suspend Wait states.
 In the Run state, only one process can exist at a time.

**2.4 Schedulers**

The operating system deploys three kinds of schedulers:
 Long-term scheduler.
 Medium-term scheduler.
 Short-term scheduler.

**2.4.1 Long-term scheduler**

 It is responsible for the creation and bringing of new processes into the main memory.
 It controls the degree of multi-programming.
 It should generate a good mix of CPU and I/O bound process for efficient resource utilization.
 It is involved in the New → Ready state transition.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**2.4.2 Medium-term scheduler**

 The medium-term scheduler acts as the swapper by doing swap-out (suspending the process from the main to secondary
memory) and swap-in (resuming the process by bringing it from the secondary to main memory) operations.
 It is involved in Ready ⇌ Suspend Ready and Block ⇌ Suspend Block state transitions.

**2.4.3 Short-term scheduler**

 The short-term scheduler selects a process from the ready state to be executed.
 It is involved in the Ready → Run state transition.

**2.5 Dispatcher**

 The dispatcher is responsible for loading the job (selected by the short-term scheduler) onto the CPU.
It performs context switching. Context switching refers to saving the context of the process which was being executed by
the CPU and loading the context of the new process that is being scheduled to be executed by the CPU.



              

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

3

**CPU SCHEDULING**

**3.1 Scheduling Criteria**

CPU scheduling will occur when:
 A new process arrives into the Ready state.
 A process undergoes Wait → Ready state transition.
 A process undergoes Run → Wait state transition for an I/O request.
 A process undergoes Run → Ready state transition every q second where q is the time slice.
 The priority of a ready process is higher than the priority of a running process.

**3.2 Goals of CPU Scheduling**

 Maximize CPU utilization.
 Minimize the response time and waiting time of the processes.

**3.3 Process times**

**3.3.1 Arrival Time (AT)**

The time at which the process arrives into the Ready state is called arrival time of the process.

**3.3.2 Burst Time (BT)**

The time required by the process for its complete execution is called burst time/service time of the process.

**3.3.3 Completion Time (CT)**

The time by which a process completes its execution post arrival is called completion time of the process.

**3.3.4 Turnaround Time (TAT)**

The time difference between completion and arrival times of a process is called as the turnaround time of the process.
TAT = CT _–_ AT

**3.3.5 Waiting Time (WT)**

The time spent waiting for the CPU to complete the execution is called as waiting time of the process.
WT = TAT _–_ BT

**3.3.6 Response Time (RT)**

The time difference between the first response and arrival times of a process is called the response time of the process.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**3.4 Gantt Chart**

Gantt chart shows the execution time period of the processes. For example:

P 1 P 2 P 3
0 10 12 17 23

 Process P 1 started execution at time t = 0 and finished just before time t = 10.
 The CPU was idle from t = 10 to t = 12.
 Process P 2 started execution at time t = 12 and finished at time t = 17.
 Process P 3 started execution at time t = 17 and finished at time t = 23.

**3.5 Scheduling Algorithms**

**3.5.1 FCFS**

 It is a non pre-emptive algorithm.
 Processes are assigned to the CPU based on their arrival times. If two or more processes have the same arrival times, then
the processes are assigned based on their process ids.
 It is free from starvation.
 It suffers from Convoy effect.

**3.5.2 Shortest Job First (SJF)**

 It is a non-pre-emptive algorithm.
 Processes are assigned to the CPU based on the shortest burst time. If two or more processes have the same burst times,
then the processes are assigned to the CPU based on their arrival times.
 If all the processes have the same burst times, SJF behaves as FCFS.
 In SJF, the burst times of all the processes should be known prior execution.
 It minimizes the average response time of the processes.
 There is a chance of starvation.

**3.5.3 Shortest Remaining Time First (SRTF)**

 It is a pre-emptive algorithm.
 Processes are assigned to the CPU based on their shortest remaining burst times.
 If all the processes have the same arrival times, SRTF behaves as SJF.
 It minimizes the average turnaround time of the processes.
 If shorter processes keep on arriving, then the longer processes may starve.

**3.5.4 Longest Remaining Time First (LRTF)**

 It is a pre-emptive algorithm.
 Processes are assigned to the CPU based on their longest remaining burst times.
 It minimizes the average response time of the processes.
 If favours CPU bound processes.
 It is free from starvation.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**3.5.5 Priority based Scheduling**

 Priority scheduling can either be pre-emptive or non-pre-emptive.
 In pre-emptive priority scheduling, a process is voluntarily pre-empted whenever a higher priority process arrives.
 In non-pre-emptive priority scheduling, the scheduler picks up the highest priority process.
 If all the processes have equal priority, then priority scheduling behaves as FCFS.

**3.5.6 Round Robin Scheduling**

 RR scheduling is a pre-emptive FCFS based on the concept of time quantum or time slice.

 If the time quantum is too small, then the number of context switches (overhead) will increase and the average response
time will decrease.
 If the time quantum is too large, then the number of context switches (overhead) will decrease and the average response
time will increase.
 If the time quantum is greater than the burst times of all the processes, RR scheduling behaves as FCFS.

**3.5.7 Highest Response Ratio Scheduling**

 It is a non pre-emptive algorithm.
 Processes are assigned to the CPU based on their highest response ratio.
 Response ratio is calculated as-

```
Response Ratio =
```

### WT + BT

### BT^

 It is free from starvation.
 It favours the shorter jobs and limits the waiting time of the longer jobs.

**3.5.8 Multilevel Queue Scheduling**

Multi-Level Queue Scheduling

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 Depending on priority of the process, in which particular ready queue, the process has to be placed will be decided.
 High priority processes will be placed in top-level ready queue and low priority process will be placed in bottom level
ready queue.
 Only after completion of all the processes, from top level ready queue the further level ready queue processes will be
scheduled.
 If this is the strategy followed, then the processes which are placed in bottom level ready queue suffer from starvation.
If higher priority processes keep on arriving, the lower priority processes may starve. This problem can be solved with the
help of aging. Aging is a technique which automatically increases the priority of the processes that have been waiting in
the system for a very long time.


 

                

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

### 

4

**MULTITHREADING**

**4.1 Threads**

 A thread is a light-weight process.
 In multithreading, the threads of the same process share user address space, files, signal and signal handlers etc.
 In multithreading, each thread has its own stack, thread id, CPU state information (control and status registers, stack
pointers) and scheduling information (thread state, priority etc.).

**4.2 Benefits of Threads**

 Improved response time.
 Faster context switches.
 Effective utilization of multiprocessor systems
 Enhanced throughput of the system.
 Economical.
 Effective resource sharing and utilization.

**4.3 Types of Threads**

**4.3.1 Based on the number of threads**

There are two types of threads:
(i) Single thread process
(ii) Multi thread process

**4.3.2 Based on level**

There are two types of threads:
(i) User-level threads
(ii) Kernel-level threads

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**4.3.3 User level threads versus kernel level threads**

```
User level threads Kernel level threads
These threads are managed at user level. These threads are managed at kernel level.
These threads are not recognized by the kernel. These threads are recognized by the kernel.
They are implemented as dependent threads. They are implemented as independent threads.
All user-level threads of a process can run on
one processor only and only one thread runs at
a time.
```

```
The kernel-level threads of a process can run on
different processors concurrently in a multi-
processor environment.
Blocking one user-level thread of a process
blocks the entire process.
```

```
Blocking one kernel-level thread of a process does
not affect the other threads of the process.
These threads have less context. These threads have more context.
Scheduling of user-level threads is done by the
thread libraries.
```

```
Scheduling of kernel-level threads is done by the
operating system.
No hardware support is required. Hardware support is required.
Implementation is easy and simple. Implementation is complicated and difficult.
```

**4.4 Multithreading Models**

**4.4.1 Many-to-One**

 Many user level threads are mapped to single kernel-level thread.

**4.4.2 One-to-One**

 Each user level thread is mapped to single kernel-level thread.

**4.4.3 Many-to-Many**

 Many user level threads are mapped to multiple kernel-level threads.
 It allows the OS to create a sufficient number of kernel threads

**4.5 Thread Libraries**

 Thread libraries provide programmer with API for creating and managing threads.
 There are two primary ways of implementing thread libraries:
(i) Library entirely in user space

(ii) Kernel-level library supported by the OS

 Examples include pthread libraries, java threads, green threads etc.

**4.6 Disadvantages of Multithreading**

 Blocking: Blocking one user-level thread of a process blocks the entire process. If the kernel thread is single threaded,
then blocking the kernel thread will block the whole process. Consequently, CPU may remain idle during this period.
 Security: Since, there is an extensive sharing among threads, there is a potential problem of security.
 Maintaining Thread Control Block (TCB) is considered as overhead for the system.


```

```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

5

**SYNCHRONIZATION**

**5.1 Synchronization**

Processes are categorized into two types
Process
Cooperative
Independent
Execution of one process affects or affected by other process then those processes are said to be cooperative process.
Otherwise, they are said to be Independent Process.

Processes must be cooperative to be synchronized.

**5.2 Understanding Synchronization**

(1) The problems arise not having synchronization between the processes.
(2) The conditions to be followed to achieve synchronization.
(3) The solutions (wrong and right).

**5.3 Problems arises for not having synchronization between the processes**

**5.3.1 Producer Consumer**

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

int count = 0; // Initially buffer will be empty and only producer will be allowed to execute first.
void producer (void)
{
int itemp;
while(true)
{
produce_item(itemp);
while (count = = N); // Buffer Full
Buffer [in] = itemp;
in = (in + 1)modN; //  to repeat in value from 0 - 7
count = count + 1;
} Register of producer memory
}
I. Load Rp.m[count]
II. INCR Rp
III. Store m[count], Rp

void consumer(void)
{
int itemc;
while(true)
{
while (count = = 0);
itemc = Buffer [out];
out = (out + 1) modN;
count = count – 1;
process_item(itemc);
}
} I. Load Rc,m[count]
II. DECR Rc
III.^ Store m[count], Rc^

 IN is a variable used by the producer to identify the next empty slot in the buffer.
 OUT is a variable used by the consumer to identify from where it has to consume the item.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 Count is a variable used both producer and consumer to identify no of items present in the buffer at any point of time.
 Shared Resources:
(1) Count Variable
(2) Buffer
 Two conditions to be followed:
(1) If the buffer is full, producer is not allowed to produce the item into the buffer.
(2) If the buffer is empty, consumer is not allowed to consume the item from the buffer.

**5.3.2 Universal Assumption**

The running process can get pre-empted at any point of time after completion of current instruction.
Analysis:

Itemp = ‘A’ count
Itemc = ‘X’ 3 2 4

P  I Rp 3 in 3 4 out 0 1

P  II Rp 34

### C  I

C  II Rc 32

C  III

P  III
Final count value = 4. Though actually three values are there.

(1) Inconsistency:
The producer and consumer are not properly synchronized while sharing the common variable “count”. Hence
it is leading to the problem of inconsistency.

**5.3.4 Printer Spooler Daemon (Daemon**  **Background process)**

**5.3.5 Definitions**

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

(1) Critical Section:
The portion of program text where shared variables or shared resources will be placed.
Example:
Count = Count + 1
OR
Count = Count – 1
(2) Non-Critical Section:
The portion of program text where the independent code of the processes will be placed.
Example:
Tn = (in + 1) modN

(3) RACE condition:
The final value of any variable depends on execution sequence of the processes. This type of condition is called
as RACE condition.

 To avoid the RACE condition, only one process is allowed to enter into critical section.

**5.3.6 Conditions to be followed to achieve Synchronization**

(1) Mutual Exclusion (M.E):
 No two processes may be simultaneously present inside the critical section at any point of time.
 Only one process is allowed to enter into critical section at any point of time.
(2) Progress:
 No process running outside the critical section should block the other intersected process from entering into
critical section when critical section when critical section is free.
 If there is only one process trying to enter into critical section then it should be definitely allowed to enter into
critical section.
 If two or more processes are trying to enter into critical section then one process should be definitely allowed
to enter critical section.
(3) Bounded Waiting:
 No process should have to wait forever to enter into critical section.
 There should be a bound on getting chance to enter into critical section.
 Some process is indefinitely waiting to enter into critical section because critical section is always busy by
some other processes. This situation should not arise.
 If the bounded waiting is not satisfied then it is possible for starvation.
(4) No assumptions related to hardware and the processor speed:
 Number of processes.

Solutions:

I. Software Type:
(a) Lock Variables
(b) Strict alteration or Decker’s Algorithm
(c) Petersons Algorithm
II. Hardware Type:
(a) TSL Instruction Set
(b) Test and Set Lock
III. OS Type:

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

(a) Counting semaphore
(b) Binary Semaphore
IV. Programming Language Compiler Support Type:
(a) Monitors

I. Software Types:

(a) Lock Variables:

Entry Section:
I. Load Ri, m[Lock] (Ri  Respective Process Register)
II. Cmp Ri, #0
III. JNZ to Step (I)
IV. Store m[Lock], #1
V. C.S
VI. Store m[Lock], #0

Analysis:

We have proved that both the processes P 1 and P 2 are entering into the critical section at the same time, Hence
mutual exclusion is not satisfied and the solution is bound to be incorrect.

(b) **Strict Alteration or Decker’s Algorithm:**

(Process takes ‘Turn’ to enter into C.S)

```
Process ‘P 0 ’ code Process ‘P 1 ’ code
while (true)
{
non_cs ();
while (turn! = 0);
c.s
turn = 1;
}
```

```
while (true)
{
non_cs();
while(turn! = 1);
c.s
turn = 0;
}
```

Important Points:

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 The pre-emption is just a temporary stop and the process will come back and continue the remaining execution.
 If there is any possibility of solution becoming wrong by taking the pre-emption then consider the pre-emption.
 If any solution is having deadlock the progress is not satisfied.

(c) **Peterson’s Algorithm:**

(Two Process Solution)
#define N 2
#define TRUE 1
#define FALSE 0
int turn;
int interested [N];
void enter_Region (int process)
{

1. int other
2. other = 1 – process;
3. interested [process] = TRUE;
4. turn = process;
5. while (turn = = process && interested [other] = = TRUE);
   }
   C.S
   void leave_Region(int process)
   {
   interested [process] = FALSE;
   }
   initially
   interested [0] = FALSE;
   interested [1] = FALSE

TURN is a shared variable used by both the processes P 0 and P 1 , interested [N] is also shared by both the processes.

**5.3.7 Hardware Type**

(a) TSL Instruction Set: (Test and Set Lock):

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 TSL Register Flag:
Copies the current value of flag into register and stores the value of ‘1’ into flag in a single atomic cycle without
any pre-emption.
 Entry Selection:

1. TSL Ri, m[flag]
2. Cmp Ri,  0
3. JMP to step (1)
4. c.s
5. Store m[flag],  0

```
Algorithm M.E. Progress Bounded Waiting
```

1. Lock Variable   
2. Strict alteration or
   **Decker’s Algorithm**

###   

**3. Peterson’s Algorithm** ^ ^ ^
4. TSL Instruction ^ ^ ^

**5 .3.8 OS Type**

Semaphore:
Semaphore is an integer variable which is used by the various processes in a mutual exclusive manner to achieve
synchronization.
Improper usage of semaphore will also give the wrong results.
Semaphore is categorised into 2 types:

The two different operations will be performed on the semaphore variable.
(1) Down, or wait (); or p ()
(2) up (); or signal (); or v (); or release ();

(a) Counting Semaphore:

Down (Semaphore s)
{
s.value = s.value – 1;
if (s.value < 0)
{
Block the process and
place its PCB in the

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

suspended list ();
}
}
Up (Semaphore s)
{
s.value = s.value + 1;
if (s.value  0)
{
Select a process from
suspended list and
wakeup ();
}
}

(b) Binary Semaphore:

Down (Semaphore S) Up (Semaphore S)
{ {
if (S.value = = 1) if (Suspended list is empty)
S.value = 0; S.value = 1;
else else
{ {
block the process select a process
and place its PCB from suspended list
in the suspended list () and wakeup ();
} }
} }

Notes: (Applicable for both counting and binary semaphore).
 Every semaphore variable will have its own suspended list.
 The down and up operations are atomic [OS will prevent the interrupts]
 If more than one process is in the suspended list then every time when we perform one up operation one process will
wakeup from the suspended list and this will be based on (FIFO  to ensure bounded waiting)
 If two or more processes are in the suspended list and there is no other process to wakeup these processes then those
processes are said to be involved in the deadlock.

**5.4 Classical problems of IPC (Inter Process Communication)**

 Producer consumer with semaphore:

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

```
semaphore mutex = 1;
```

semaphore empty = N;

semaphore full = 0;

void producer(void)

{

int item p;

while(true)

{

produce_item (item p);

down(empty);

down(mutex);

buffer [in] = item p;

in = (in + 1) mod N

up(mutex);

up(full);

}

}

void consumer (void)

{

int item c;

while (true)

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

### {

down (full);

down (mutex);

item c = buffer [out];

out = (out + 1)mod N;

up (mutex);

up (empty);

process_item (item c);

}

}

 mutex is a binary semaphore used by the producer and consumer to access the buffer in a mutual exclusive manner.
 empty is counting semaphore variable represents number of empty slots in the buffer at any point of time.
 full is counting semaphore variable represents number of slots full in the buffer at any point of time.

**5.5 READERS WRITERS PROBLEM**

int rc = 0;

semaphore mutex = 1;

semaphore db = 1;

void reader (void)

{

while (true)

{

down (mutex);

rc = rc + 1;

if (rc = = 1) down (db);

up (mutex);

}

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

### }

void writer (void)

{

while (true){

down (db);

D.B

up (db);

}

}

**5.5.1 conditions to be followed**

1) R - W  2) R – R 
2) W – R  4) W – W 

 rc is a integer variable represents readers count i.e number of readers present in the data base at any point of time.
 mutex is a binary semaphore used by the readers in mutual exclusive manner.
 db is a binary semaphore variable used by readers and writers in a mutual exclusive manner.

**5.5.2 Dining Philosophers’ problem**

```
Dining Philosophers problem
 N philosophers and N forks
 Philosophers eat/think
 Eating needs 2 forks
 Pick one fork at a time
```

**5.5.3 Solution 1 for Dining Philosophers problem**

```
# define N5 /* number of philosophers */
```

```
Void philosophers (int i) /* i: philosophers’ number from 0 to 4 */
{
while (TRUE) {
think (); /* philosopher is thinking */
take_fork (i); /* take left fork */
take_fork ((i+1)%N) /* take right fork; % is modulo operator */
eat (); /* yum-yum spaghetti */
put_fork (i); /* put left fork back on the table */
put_fork ((i+1)%N) /* put right fork back on the table */
```

```
{
```

```
 This solution to dining
philosopher problem
suffers from Deadlock.
 Everyone picks up their
left fork first, then waits
for right fork... this
leads to Starvation!
```

 This solution to dining philosophers’ problem suffers from Deadlock everyone picks up their left fork first, then waits for
right fork => This leads to Starvation!

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**5.5.4 Solution 2 – state based**

```
# define N 5 /* number of philosophers */
# define LEFT (i+N-1)%N /* number of I’s left neighbours */
# define RIGHT (i+1)%N /* number of I’s right neighbours */
# define THINKING 0 /* philosopher is thinking */
# define HUNGRY 1 /* philosopher is trying to get forks */
# define EATING 2 /* philosopher is eating */
typedef int semaphore /*semaphores are a special kind of int */
int state [N]; /* array to keep track of everyone’s state */
semaphore mutex = 1; /* mutual exclusion for critical regions */
semaphore s[N]: /* one semaphore per philosopher */
```

```
void philosopher (int i) /* i: philosopher number, from 0 to N -1 */
{ while (TRUE) { /* repeat forever */
Think(); /* philosopher is thinking */
Take_forks(i); /* acquire two forks or block */
Eat(); /* yum-yum spaghetti */
Put_forks(i); /* put both forks back on table */
}
}
void take_forks(int i) /* i: philosopher number, from 0 to N -1 */
{
down(&mutex); /* enter critical region */
state [i] = HUNGRY; /* record fact that philosopher is hungry */
test(i); /* try to acquire two forks */
up(&mutex); /* exit critical region */
down(&s[i]); /* block if forks were not acquired */
}
void put_forks(i) /* i: philosopher number, from 0 to N -1 */
{
down(&mutex); /* enter critical region */
state [i] = THINKING; /* philosopher has finished eating */
test(LEFT); /* see if left neighbour can now eat */
test(RIGHT); /* see if left neighbour can now eat */
up(&mutex); /* exit critical region */
}
void test(i) /* i: philosopher number, from 0 to N -1 */
{
if (state[i] = = HUNGRY && state [LEFT] = EATING && state [RIGHT] = EATING) {
state [i] = EATING;
up(&s[i]);
}
}
Made picking up left and right chopsticks an atomic operation or, N – 1 philosophers but N chopsticks  ...both
changes prevent deadlock.
```

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**5.6 Monitors:**

 Monitors is a programming language compiler support type of solution to achieve synchronization.
 Monitors is collection of variables and procedures combined together in a special kind of module or package.
 The process running outside the monitor cannot directly access the internal variables of the monitor but however they can
call the procedures of the monitor.
 Monitors has an important property that only one process can be active inside the monitor at any point of time.

**5.6.1 Syntax**

```
Monitor example
{
Variables;
Condition variables;
Procedure P 1
{
}
Procedure P 2
{
}
```

}

**5.6.2 Condition variables**

Condition x,y;
The two different operations performed on the condition variables of the monitor.

1. Wait operation: wait ()
2. Signal operation: signal ()

 Wait ()
Ex – x.wait (); or wait (x)
The process performing wait operation on any condition variable will be suspended and suspended process will be
placed in the “ block queue” of respective condition variable.
 Signal ()
Ex – x.signal (); or signal(x)

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**5.6.3 Concurrent Programming**

```
S 1 : a = b + c ;
S 2 : d = e * f ;
S 3 : g = a / d ;
S 4 : h = g * i ;
```

Read set = {b, c, e, f, a, d, g, i}

Write set = {a, d, g, h}

**5. 6 .4 Precedence graph**

S 1 , S 2 can execute concurrently

 Any two statements Si and Sj can be executed concurrently or parallel if they are following the conditions.
(1) R(Si)  W (Sj) = 
(2) W(Si)  R (Sj) = 
(3) W(Si)  W (Sj) = 
 The real concurrent programming is possible only on the multiprocessor system.
 Concurrent has 3 different meanings
o They can execute concurrently or parallel
o They don’t have any dependency
Anyone can start first [for single processor this will be applicable]

### 

###  

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

6

**DEADLOCK**

**6.1 Concept of Deadlock**

 A set of blocked processes each holding a resource and waiting to acquire a resource held by another process in the set.
 Example:
○ System has 2 disk drives.
○ P 1 and P 2 each hold one disk drive and each needs another one.

**6.2 System Model**

 Resource types R 1 , R 2 ,.. ., Rm
 Resources include CPU cycles, memory space, I/O devices
 Each resource type Ri has Wi instances.
 Each process utilizes a resource as follows:
○ request
○ use
○ release

**6.3 Deadlock Characteristics**

**6.3.1 Mutual Exclusion**

There should be a one-to-one relationship between a resource and a process.

**6.3.2 Hold and Wait**

This condition arises when a process is requesting another resource while holding on to a resource.

**6.3.3 No Pre-emption**

The resource has to be voluntarily released by the process after its execution. It is not allowed to forcibly pre-empt a process to
release its held resources.

**6.3.4 Circular Wait**

The processes are circularly waiting on each other for the resources.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

```
Note:
If all the deadlock characteristics simultaneously exist in the system, then the system is in deadlock.
```

**6.4 Deadlock Prevention**

It ensures that the system will never enter into a deadlock state. Deadlock can be prevented by unsatisfying one of the mentioned
deadlock characteristics.
 Mutual exclusion cannot be unsatisfied because of the concept of sharable and non-sharable resources.
 Hold and Wait characteristic can be unsatisfied through any of the following strategies:
(i) A process should be assigned all the required resources before the start of its execution. This may lead to low device
utilization.

(ii) The process should release all the existing resources before making a new request. This may eventually lead to
starvation.

 Pre-emption can be achieved as:
 Suppose a process P 1 is requesting for a resource R which is held by another process P 2. If P 2 is already in execution then
P 1 has to wait; else, the resource R will be pre-empted from P 2 and allocated to P 1.
 Circular wait can be avoided by the following algorithm:
(i) Assign unique numbers to resources. (assume there exists single instance of a resource).

(ii) A process can request for a resource in either increasing or decreasing order of enumeration.

**6.5 Deadlock Avoidance**

Deadlock avoidance is achieved by implementing Banker’s algorithm. Banker’s algorithm ensures that the system never enters
in unsafe state.
 When a process requests an available resource, system must decide if immediate allocation leaves the system in a safe
state.
 System is in safe state if there exists a sequence <P 1 , P 2 , ..., Pn> of ALL the processes in the systems such that for each Pi,
the resources that Pi can still request can be satisfied by currently available resources + resources held by all the Pj.
 If a system is in safe state  no deadlocks.
 If a system is in unsafe state  possibility of deadlock.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**6.5.1 Data Structures for Banker’s algorithm**

Let n = number of processes and m = number of resources, then-
 Available: Vector of length m. If available [j] = k, there are k instances of resource type Rj available.
 Max: n x m matrix. If Max [i,j] = k, then process Pi may request at most k instances of resource type Rj.
 Allocation: n x m matrix. If Allocation[i,j] = k then Pi is currently allocated k instances of Rj.
 Need: n x m matrix. If Need[i,j] = k, then Pi may need k more instances of Rj to complete its task.
 Need [i,j] = Max[i,j] – Allocation [i,j].

**6.5.2 Banker’s Algorithm**

 Algo Bankers(i , Request, Available, Allocation, Need){
If(Needi ≤ Maxi)
{
If(Needi ≤ Available)
{
Available = Available – Needi ;
Allocation = Allocation + Needi^ ;^
Maxi = Maxi - Needi ;
Run safety Algorithm;
If the system is in safe state, then grant the Needi;
Else block the process;
}
}

**6.6 Deadlock Detection**

 A cycle in the resource allocation graph represents deadlock only when resources are of single-instance type.
 If the resources are of multiple instance type, then the safety algorithm is used to detect deadlock.

**6.7 Deadlock Recovery**

A system can recover from deadlock through adoption of the following mechanisms:
 Process termination
 Resource Pre-emption
 Ostrich Algorithm:
 Ignore the problem and pretend that deadlocks never occurred in the system; used by most operating systems, including
UNIX.


### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

7

**MEMORY MANAGEMENT**

**7.1 Introduction**

 In multiprogramming system, the task of subdividing the memory among the various processes is called memory
management.
 The task of the memory management unit is the efficient utilization of memory and minimize the internal and external
fragmentation.

**7.2 Logical versus Physical Address**

 The address generated by CPU is called the logical address.
 The address perceived by the memory unit is called physical address.

**7.3 Memory Management Unit**

 Hardware device that maps virtual to physical address.
 In MMU scheme, the value in the relocation register is added to every address generated by a user process at the time it is
sent to memory.
 The user program deals with logical addresses; it never sees the real physical addresses.

**7.3.1 Loading**

It is defined as bringing the program from the secondary to the main memory.
It is classified into three types:
(i) Absolute Loading
 A given program is always loaded into the same memory location whenever loaded for execution.
(ii) Relocatable Loading
 A given program is loaded into any desired memory location whenever loaded for execution.
 The compiler must generate relative address for the program.
(iii) Dynamic Loading
 Routine is not loaded until it is called better memory-space utilization (unused routine is never loaded, postponed until
execution time).
 Useful when large amounts of code are needed to handle in frequently occurring cases.
 No special support from the operating system is required. It is implemented through program design
 Address translation is performed through the hardware.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**7.3.2 Linking**

Linking is the process of collecting and combining various pieces of code and data into a single file that can be loaded (copied)
into memory and executed. It can be performed at compile time, load time or run time.

It is classified into two types:
 Static Linking
Static linkers take as input a collection of relocatable object files and command-line arguments and generate as output a
fully linked executable object file that can be loaded and run.
 Dynamic Linking
A shared library is an object module that, at run time, can be loaded at an arbitrary memory address and linked with a
program in memory. This process is dynamic linking.

**7.3.3 Address Binding**

Association of the program instructions and data into the actual physical memory locations is called as address binding. Address
binding of instructions and data to memory addresses can happen at three different stages
 Compile time: If memory location known a priori, absolute code can be generated. It must recompile code if starting
location changes.
 Load time: It must generate relocatable code if memory location is not known at compile time.
 Execution time: Address binding is delayed until run time if the process can be moved during its execution from one
memory segment to another. It needs hardware support for address mapping (e.g., base and limit registers).

**7.4 Memory Management Techniques**

**7.4.1 Contiguous Memory Allocation**

It comprises of – Fixed Partition Scheme and Variable Partition Scheme
Fixed Partition Scheme / Static Partitioning
 The memory is divided into a fixed number of partitions of equal/unequal sizes.
 Every partition is associated with limit registers.
 The degree of multiprogramming is restricted by the number of partitions.
 Partition size may not be large enough for any waiting process.
 Internal fragmentation may be present.
Variable Partition Scheme / Dynamic Partitioning
 Initially, memory is available as a single continuous free block. When a process arrives, a hole large enough to
accommodate it is created in the memory.
 There is no internal fragmentation.
 It suffers from external fragmentation.
 It is associated with the overhead of compaction.
Note
If more than one partition is sufficient to accommodate a process, then any of the following dynamic allocation methods can
be adopted:
 First Fit: Allocate the first partition that is big enough starting from the beginning of the memory.
 Next Fit: It behaves similar to first fit except that it scans the memory after the ‘last allocation point’.
 Best Fit: It scans the entire memory to find the smallest sufficient partition to accommodate the process.
 Worst Fit: It scans the entire memory to find the largest sufficient partition to accommodate the process.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**7.4.2 Non-Contiguous Memory Allocation**

Paging
 The technique of mapping CPU generated logical address to physical address is called paging.
 Logical address space is divided into equal size pages. Physical address space is divided into equal size frames. In paging,
the frame size is equal to the page size.
 When a process is created, paging will be applied on the process. A page table will be maintained in the main memory for
a process. The base address of the page table will be stored in the process control block.
 The number of entries in the page table is equal to the number of the pages in the logical address space. Each page table
entry contains the frame number. Hence, the page table is also known as the address translation table.

 There is no external fragmentation in paging. Internal fragmentation may exist in the last page and is formulated as ⌈𝑝 2 ⌉

```
where p is the page size.
```

Paging with TLB

 Translation Look Aside Buffer is a hardware device implemented using associative registers.
 TLB is added to improve the performance of paging. The TLB access time will be very less compared to the main
memory access time.
 TLB contains frequently referred page numbers and their corresponding frame numbers.

 TLB access time = c
 TLB hit ratio = x
Then the formula for effective memory access time:

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

Multilevel Paging
 To avoid the overhead of maintaining large size page tables, multilevel paging will be applied.
 In multilevel paging, pages of the page table are brought into the main memory.
 The page tables of all the levels of multi-level paging are kept in the memory.
 The entries of the level-1 page table are pointers to the level-2page table.
 The entries of the level-2 page table are pointers to the level-3 page table.
 The entries of the last level page table will have frame numbers of the actual page.
 All levels page table entry must contain frame number.
 Address translation is done as:

 Performance of multi-level paging with TLB:
Assume, TLB hit ratio = p, TLB access time = c, Main Memory Access time = m
If the system uses n-level paging, then effective memory access time is given as-
𝐸𝑀𝐴𝑇=𝑝(𝑐+𝑚)+( 1 −𝑝)(𝑐 +(𝑛+ 1 )𝑚 )
Inverted Paging
 Inverted paging maps physical frames to virtual pages.
 Instead of maintaining multiple page tables for different processes, an inverted page table can be maintained.
 The number of entries in the inverted page table is equal to the number of the frames in the physical address space.
 Each inverted page table entry contains a page number and a process identifier. It gives an idea about ‘which page of which
process is allocated in which frame’.
 The disadvantage of inverted paging is the increased lookup time and hard to implement.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 Address translation is done as:

Segmentation
 Paging does not follow user’s view of memory allocation. Instead of dividing the process into equal sized pages, it can be
divided into variable length segments.
 A segment table is maintained for each process. The number of entries in the segment table is equal to the number of
segments of a process.
 Each segment table entry contains the base (starting address) and limit(length) of the segment.
 Segmentation does not suffer from internal or external fragmentation.
 Address translation is done as:

Segmented Paging:
 To avoid the overhead of bringing large sized segments of a process into the main memory, paging will be applied on the
segments.
 Pages of the segment will be loaded into the main memory.
 A page table will be maintained for each segment of the process.
 The number of entries in the page table is equal to the number of the pages of the segment in the logical address space.
 Lookup time increases.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

 It suffers from internal fragmentation only.
 Address translation is done as:

### 

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

08

**VIRTUAL MEMORY**

**8.1 VM Concept**

 It gives an illusion to the programmer that programs having larger size than the physical memory can be executed.
 It allows address spaces to be shared by several processes.

**8.2 VM Implementation**

Virtual memory can be implemented through:

 Demand Paging
 Demand Segmentation

**8.2.1 Demand Paging**

Loading the pages from the secondary memory to the main memory on demand is called ‘demand paging’.

 When the CPU tries to refer a page which is not available in the main memory, ‘page fault’ occurs. A signal is sent to the
OS regarding the page fault. The OS locates the page into the Logical address space and loads it into the main memory
frame. If the memory frames are full, appropriate page replacement algorithm is used. The respective page table entries
are also updated accordingly.
 The time taken to service a ‘page fault’ is called ‘page fault service time’.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

**8.3 Performance of virtual Memory**

**8.3.1 Temporal Issues**

Let,

Page fault service time = ‘S’

Main memory access time = ‘M’

Page fault rate = ‘P’ where 0 ≤ P ≤ 1

The effective memory access time is formulated as-

```
EMAT = P × S + (1 – P) × M
```

(Assume, page table access time is neglected)

**8.3.2 Demand Paging with TLB**

Assume, TLB hit ratio = ‘h’

TLB access time = ‘c’

Page fault service time = ‘S’

Main memory access time = ‘M’

Page fault rate = ‘P’ where 0 ≤ P ≤ 1

The effective memory access time is formulated as-

EMAT = h(c + m) + (1 – h)(c + (P × S + (1– P) × M) )

**8.3.3 Page Replacement Algorithms**

FIFO

 When a page fault occurs and all the memory frames are full, FIFO algorithm replaces the oldest page to allocate the
page referred by the CPU.
 It is implemented using a queue or time-stamp on pages.
 Sometimes, even on increasing the number of frames, the page fault rate increases. This situation is called Belady's
Anomaly.

LRU

 LRU algorithm replaces the page that has not been used for the longest period (least recently used page).
 It is implemented using a stack or counter.

Optimal

 Optimal algorithm replaces the page that will not be used for the longest period in future.
 For a fixed number of frames, optimal algorithm gives the least page fault rate.
 It cannot be implemented in real time as it requires future references.

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

```
Note
Reference String is a set of successively unique pages referred in a given list of virtual addresses.
```

**8.3.4 Thrashing**

When CPU utilization is low, the OS may increase the degree of multiprogramming. After a certain point, the throughput of
the system will gradually decrease as the system spends more time in page replacements owing to the lack of frames. This
phenomenon is called ‘thrashing’.

**8.3.5 Working Set Model**

It is defined as the set of the unique pages referred during the past ‘∆’ references.

 If ∆ < (total number of frames), the OS can bring in more processes.
 If ∆ > (total number of frames), the OS should instruct the mid-term scheduler to suspend some of the processes to avoid
thrashing.

                    

### GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK

```
Operating Systems
```

9

**FILE SYSTEMS**

**9. 1 File**

 Collection of logically related entities/records

**9.1.1 Attributes**

 File Name
 File Type
 File Size
 Location of file
 Generation date

```
 Last modified date
 Permission
 Owner/Author
 Password
```

**9.2 File Context**

File context is stored in file control block (FCB)

File will have various types–

 .doc
 .txt
 .pdf
 .exe
 .obj
 .dll
 .png

 .xls/.xlsx
 .jpg
 .mp3
 .mp4
 .avi/.flv/.mkv/.3gp
 .c/.cpp/.java/.xml/.html
 .apk

**9.3 Operations performed on file**

 create
 open
 write
 read
 hide
 save
 save as
 close

```
 copy
 paste
 cut
 delete
 rename
 send/share
 print
```

**GATE WALLAH CSE/IT HANDBOOK**

```
Design Against Static Load
```

```
4
0
```

**9.4 Access methods**

 Sequential Access
 Random Access
 For better classification of files, files will be stored in directory.

**9.5 Disk Space Allocation Methods**

**9.5.1 Contiguous Allocation**

```
File Starting Disk Block
Address
```

```
Size w.r.t no. of DB
```

```
Abc.docx 2 4
Xyz.docx 9 5
```

 In contiguous allocation, whenever file is created, disk blocks are allocated in a continuous
manner.
 Every file is associated with two parameters
(1) Starting DBA
(2) Size
 Increasing the file size may not be possible always.
 It suffers from external fragmentation.
 Internal fragmentation may exist in the last disk block of the file.
 It supports both sequential and random access of file.
Starting disk block Address + Offset Value  Random location

**9.5. 2 Linked Allocation/Non-contiguous allocation**

File Starting DBA Ending DBA
abc.docx 2 1
xyz.docx 9 10
 In the linked allocation disk blocks are allocated in a non-continuous manner.
 Every file is associated with 2 parameters–
(1) Starting DBA
(2) Ending DBA
 Increasing file size is always possible if free disk block is available.
 There is no external fragmentation.
 Internal fragmentation may exist in last disk block of the file.
 There is an overhead of maintaining power in every disk blocks.
 If the pointer of any disk block is lost, the file will be truncated.
 It supports only sequential access of the file.

```
0 1
```

```
5
```

```
9
```

```
13
```

```
4
```

```
8
```

```
12
```

```
2 3
```

```
7
```

```
11
```

```
15
```

```
6
```

```
10
```

```
14
```

```
/0
```

```
/0
```

```
Dark Block
DBA of new DB
or Pointer to new DB
```

(^01)
5
9
13
4
8
12
2 3
7
11
15
6
10
14

**GATE WALLAH CSE/IT HANDBOOK**

```
Operating Systems
```

**9.5.3 Indexed Allocation**

```
File Index Node
abc.d 4
```

 In the indexed allocation, every file is associated with its own index node.
 Index node contains all the disk block address of the file.
 There is no external fragmentation but internal fragmentation may exist is the last disk block of file.
 If the file is very large, then one disk block may not be sufficient to store all the disk block addresses of the file.
 If the file is very small, then it is waste of using one entire disk blocks. Just to store, the addresses.

**9.7 UNIX I-NODE IMPLEMENTATION**

**9.7.1 An extension of indexed allocation**

```
File I-NODE
abc.docx 27
```

(^01)
5
9
13
4
8
12
2 3
7
11
15
6
10
14
11
3
7
10
–1
DBA’s of file
End of file
DB Size
Reference Unit
Date & Time
Owner
Direct
DBA’s
Location
Single indirect
double indirect
Triple indirect
Quadruple indirect
x
y
z..
.
INODE 27
#hard links press
pointing to I Node
DBA
DB
DB
Data Blocks
DB
DB
DB
DBA
DBA
DBA
Data Blocks
Data Blocks
Addresses Addresses
DB
DB
DB
DB
Addresses

**GATE WALLAH CSE/IT HANDBOOK**

```
Operating Systems
```

**9.8 DISK FREE SPACE MANAGEMENT**

Size of Disk = 20 MB
DB Size = 1 KB
DBA = 16 Bits = 2 B

# Disk blocks available on given disk =

```
Size of disk
DB size
```

### =

```
20
10
```

```
20 2
2
```

```
B
B
```

###  =20 K

**9.8. 1 Free List Approach**

 In the free list approach, some disk blocks are used just to store the free disk block addresses.

# Disk block addresses possible to store in one disk block =

```
D B Size
D BA
```

### =

```
210
2
```

### = 2^9

29 addresses  1 disk block

20 K addresses  19 211 10
2

```
  22 × 10 = 40 disk block
```

**9.8. 2 Bit Map Approach**

 In Bit map approach, every disk block were be mapped with 1 binary bit

Free Disk Blocks

0, 2, 4, 6, 9, 11, .........

Busy Disk Blocks

1, 3, 5, 7, 8, 10, .......
Disk blocks we can map in 1 disk block = 1 K × 8 bits = 8 K bits.
8 K bits  1

20 K bits  1 ×20K
8K

### = 2.4 = 3

### 

### 

### 

### 

### 

### 

```
x
y
z.
..
..
```

```
a
b
c.
..
..
```

```
\o
```

```
Free DBA's Free DBA's
```

```
0101
1010
1110
1011
```

```
0101
1010
0111
1101
```

```
0123 4567
Bit
0 1
Free Busy
```

**GATE WALLAH CSE/IT HANDBOOK**

```
Operating Systems
```

10

**DISK SCHEDULING**

**10.1 Goal of Disk Scheduling**

 Enhanced throughput.
 Minimize the average seek time of the disk.
 Fair chance to all the I/O requests.

**10.2 Disk scheduling Algorithms**

**10.2.1 FCFS**

It serves the first request in the queue.

**10.2.2 SSTF**

It selects the request with minimum seek time for the current head position.

**10.2.3 SCAN or Elevator Algorithm**

The disk arm starts from the current head position and moves towards the other end, servicing requests until it gets to the
other end of the disk, where the head movement is reversed and servicing continues.

**10.2.4 C–SCAN**

The disk arm starts from the current head position and moves towards the other end, servicing requests until it gets to the
other end of the disk, where the head movement is reversed and immediately returns to the beginning of the disk without
servicing any requests at the return trip. The servicing then continues from the beginning of the disk again.

**10.2.5 C–LOOK**

It is similar to C-SCAN where the arm goes as far as the last request in each direction, then reverses the direction
immediately, without first going all the way to the end of the disk.

Note:

**GATE WALLAH CSE/IT HANDBOOK**

```
Operating Systems
```

 Performance depends on the number and types of requests.
 I/O requests can be influenced by the file allocation methods.
 Either SSTF or LOOK is a reasonable choice for the default algorithm.

**10.2.6 Comparison Among the Disk Scheduling Algorithms**

```
Algorithm Advantages Disadvantages
```

First Come First Served (^)  Easy to implement
 Fair chance to all the I/O requests
 It doesn’t suffer from starvation
 Seek time is not
optimized.
 It doesn’t maximize
throughput.
Shortest Seek Time First  It tends to minimize the arm movement.
 It has better throughput than FCFS.
 It may suffer from
starvation.
SCAN/LOOK (^)  It eliminates starvation.
 It works well with light to heavy loads.
 It is complex to
implement.
 Increased overhead.
 It needs a directional bit to
keep track of the head
direction.
C-SCAN/C-LOOK  No directional bit is required.
 It works well with light to heavy loads.
 It is complex to
implement.
 Increased overhead.



**DatabaseDatabase**

**ManagementManagement**

**SystemsSystems**

**Database**

**Management**

**Systems**

```
Design Against Static Load
```

1. Database Design ................................................................................................................... 10 .1 – 10. 9
2. ER Model ............................................................................................................................. 10. 10 – 10. 13
3. Relation Model and SQL ...................................................................................................... 10. 14 – 10. 25
4. File Organization and Indexing [B and B+ Tree] ................................................................... 10. 26 – 10. 31
5. Transactions and Concurrency Control ................................................................................ 10. 31 – 10.46

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**DATABASE DESIGN**

**1. 1 Introduction**

A database is an organized collection of structured data or related data.

**1. 2 Limitations of File System**

- The physical details of the data to access the database are managed by the user.
- File system can be used to manage small database.
- When database is large, the operating system fails to control the concurrency.
- Only single user can access the whole data of the file system at a time.

**1.3 Integrity Constraints Of RDBMS**

- According to codd, data in database file must be stored in tabular format (set of row’s and column’s).
- According to codd, no two row’s/records of the table should be equal.

**1.3.1 Arity**

Number of attributes of database table.

**1.3.2 Cordinality**

Number of records of database table.

**1. 4 Keys in database**
    - Condidate Key: A minimal set of attributes that differentiate records/row’s of DB table uniquely.
    - Primary Key : One of the candidate key whose field value cannot be null.
    - Simple Candidate Key: A candidate key with only one attribute.
    - Compound Candidate Key: A candidate key with atleast two attributes.
    - Overlapped Candidate Key: Two or more candidate key with some common attribute.
    - Prime attribute: The attribute that belongs to some candidate keys of a relation.
    - Non-prime attribute: The attribute that does not belongs to any of the candidate keys of the relation.

```
Example :
Consider a relation R (ABCDE)
```

1. Assume candidate key : {AB, BC}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

2. The above candidate keys are compound and overlapped.
3. Prime attribute {A, B, C}
4. Non-prime attribute : {D, E}
   **1. 4. 1 Difference between Primary key and Alternative key**

```
Primary Key Alternative Key
```

1. Any one candidate key whose field value can not be null.
2. Atmost one primary key allowed for any DB table.
   1. All candidate key of relation except primary key, whose
      field value can be null.
   2. Many (o or more) alternative keys are allowed for DB
      table.
      **1. 4. 2 Super key**

The set of attributes which can differentiate records/tuples uniquely or super set of candidate key.
Example 1: R (ABCD) with CK = {A}
 Super key = CK ⸱ [Any subset of other attributes (BCD)]
= A ⸱ [2^3 ] = 8 Super key.
Example 2 : Let R be the relational schema with n-attibutes, R (A 1 , A 2 , ....... An) then number of superkeys possible:
(I) With (A 1 ) as candidate key : 2n–^1
(II) With {A 1 , A 2 } as candidate key : 2n–^1 – 2 n–^2 + 2n–^1
(III) With {A 1 A 2 , A 3 A 4 } as candidate key: 2n–^2 – 2 n–^4 + 2n–^2
(IV) The maximum number of super keys possible when each attribute of R is candidate key : 2n–^1
(V) The minimum number of super key possible when all the attributes combined form single candidate key:
1 {A 1 A 2 ..... An : candidate key}

**1. 5 Referential Integrity Constraints

1. 5 .1 Foreign key**

Foreign key is a set of attributes that references primary key or alternative key of the same relation or other relation.

Referenced Relation

```
Student Sid Sname Age Sid Cid Fee
```

```
Referencing relation Referencing relation
```

```
Referential
key must be
(PK or AK)
```

```
Sid is foreign
key in Enroll
```

```
Enroll
```

```
Note:
For any RDBMS table there must be atleast one candidate key, whose field value can not be null.
```

```
(Unique + Not Null) Primary key^
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

1. Insertion : No violation
2. Deletion : [May cause violation]
   (a) On delete no action : Means if it cause problem on delete then deletion is not allowed on table.
   (b) On delete cascade : If we want to delete primary key value from referenced table then it will delete that value from
   referencing table also.
   (c) On delete set null : If we want to delete primary key value from referenced table then it will try to set the null
   values in place of that value in referencing table.
   Note:
   If foreign key field is not null attribute then “On delete set null” is same as” on delete no action.”
3. Updation : [May cause violation]
   (a) On update no action
   (b) On update cascade
   (c) On update set null

Referencing Relation

1. Insertion : [May cause violation]
2. Deletion : No violation
3. Updation : [May cause violation]

```
Note
If integrity violation occurs because of insertion or updation in referencing table then restrict insertion and updation.
```

Example:

So, If we delete (2, 4) then PK “2”. gets deleted from the table and all the tuples in which B is referencing PK.2” also gets
deleted.

**1. 6 Database Design Goals**

1. 0% redundancy
2. Loss-less join
3. Dependency preservation

```
A 2 3 4 5 6
B 4 4 5 4 2
```

```
P.K F.K
B is foreign key referencing
A. delete (2, 4) and on delete cascade.
```

```
A
3
4
5
```

```
B
4
5
4
```

```
Result
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**1. 6 .1 Functional Dependency**

Let R be the relational shcema and x, y be the non-empty set of attributes. Consider t 1 , t 2 are any tuples of relation then x → y
(y functionally determined by x):

If t 1 , t 2 t 1 ⸱x = t 2 ⸱x then t 1 ⸱y = t 2 .y

**1. 6. 2 Types of Functional Dependency**

1. Trivial Functional Dependency

Consider relational schema R(ABCD)
A FD x → y is trivial FD only if x  y.

Example :
AB → A
A → A
B → B

2. Non-trivial Functional Dependency

Consider relational schema R(ABCD)
A FD x → y is non-trivial only if
x  y =  means no common attributes between x and y attribute sets.

Example :
A → B
AB → CD

3. Semi-Non-Trivial Functional Dependency

A combination of both trivial FD and non-trivial FD.
Example :
A → AB  {A → A, A→B}

**1.6.3 Attribute Closure (X+)**

The set of all possible attributes determined by x.
Example :
R (ABCD) {A → B, B → C, C → D}
 (A)+ = {A, B, C, D}

**1. 6 .4 Armstrong’s Axioms**

1. Reflexive : If x  y then x → y or x → x
2. Transitivity : If x → y and y → z then x → z
3. Augmentation : If x → y then xz → yz
4. Splitting : If x → yz then x → y, x → z
5. Union : If x → y and x → z then x → yz
6. Pseudo transitivity : If x → y, yw → z then xw → z

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**1. 6 .5 Finding Candidate Key [Minimal Super Key]**

X is candidate key of R
If and only if

1. x must be super key of relation R
   (x)+ = {determine all attributes of R}
2. No proper subset of ‘x’ is super key of relation R.
    y  x : (y)+ = {not determine all attributes of R}
   - x → y is a non-trivial FD in R with y is a prime attribute then relation R has atleast two candidate key.

(x → y) : Non – trivial FD
↓
Prime-attribute

**1.7 Membership of FD**

A FD x → y is member (logically implied) of FD set F if and only if (x)+ should determine ‘y’ in FD set F.
Example : Given FD Set F : { ....}
↓

x → y FD belongs to F or not?
↓
x+ = {...y...}
then x → y is member of F.

**1.7.1 Testing of Two FD Sets whether they are equal or not**

F and G FD sets equality test:
F and G FD sets logically equal if and only

1. **F cover’s G :** All FD’s of G set must be member’s of F set.
   F  G
2. **G cover’s F :** All FD’s of F set must be member’s of G set.
   F G
   F Cover G G Cover F Result
   True True F  G
   True False F  G

False True (^) F  G
False False F & G are not comparable
**1.7.2 Minimal Cover or Canonical Cover**

- Minimal Cover of given FD Set (F) is minimum possible FD’s (Fm), which is logically equal to ‘F’ : (F = Fm)
- Remove extraneous attribute (useless attribute) from each determinant of FD set F.

```
{wxy →z, w→x}  {wy → z, w → x}
```

- Every FD must be simple (RHS of any FD should have single attribute).

```
w x y → z
Extraneous
attribute
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Example : F = {A → CD} then {A → C, A→ D}

- FD set must be non-redundant FD. (eliminating unnecessary FD’s)
  Example : F = {A → B, B → C, A→ C} then
  F = {A → B, B→ C} because A → C is redundant.

```
Note:
Minimal Cover of FD Set (F) may not unique, but all minimal cover’s logically equal.
 Fm 12  =Fm F
```

**1.8 Normalization**

Normalization used to eliminate/reduce redundency in DB relations.
The normalization is especially meant to eliminate the following anomalies:

- Insertion anomaly
- Deletion anomaly
- Update anomaly
- Join anomaly
  **1. 8 .1 Normalization of DB table**

Decompose relation into two or more sub-relations in-order to reduce or eliminate redundancy and DB anomalise.

**1. 8 .2 Properties of Decomposition**

- Loss-less Join decomposition: Relational Schema R decomposed into R 1 , R 2 , R 3 , .... Rn sub-relations.
- In general [R 1 ⋈ R2 ⋈ R3 ......... Rn]  R

1. If [R 1 ⋈ R 2 ⋈ R 3 .......⋈ Rn]  R then loss-less join decomposition.
2. If [R 1 ⋈ R 2 ⋈ R 3 ........ ⋈ Rn]  R then lossy join decomposition.

Example :
Let R be the relational schema decomposed into R 1 and R 2.
Given decomposition is loss-less join if–

1. R 1  R 2 = R (all attributes covers)
2. R 1  R 2  
3. 

```
1 2 1
```

```
1 2 1
R R is SK of R
```

### R R R

```

```

```
→ or
1 2 2
```

```
1 2 2
R R is SK of R
```

### R R R

```

```

### →

**1. 8 .3 Dependency Preserving Decompostion**

Relational Schema R with FD set F decomposed into R 1 , R 2 , ......... Rn sub relations
Assume F 1 , F 2 , ......... Fn FD sets of sub relations respectively.
In general
[F 1  F 2  ....... Fn]  F

1. If [F 1  F 2  ....... Fn]  F then dependency preserving decomposition.
2. If [F 1  F 2  ....... Fn]  F then not dependency preserving decompostion.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**1.9 Normal Forms**

Used to find degree of redundancy

- BCNF relations have 0% redundancy over FD’s where as 4NF relations have 0% redundancy over FD and MVD.
- To Eliminate redundancy over Non-Trivial FD, relation should decompose into BCNF but BCNF may not avoid the
  redundancy due to MVD.
- To eliminate redundancy over non-trivial MVD, relation should decompose into 4NF (4th Normal Form).

**1.9.1 First Normal Form**

- Default NF of RDBMS relations.
- Relation (DB Table) R is in 1 NF if and only if no multivalued attributes in R. [Every attribute of R must be atomic/single
  valued].

```
Note:
Degree of redundancy is very high in 1NF relation.
```

Important Point 1

- x → y FD forms redundancy in relational schema R if and only if –
  (i) Non-Trivial FD
  and
  (ii) X is not super key.
- x → y FD not forms any redundancy in relation R if and only if–
  (i) Trivial FD [x  y] or Semi-trivial
  or
  (ii) x : super key

**1.9.2 Second Normal Form (2NF)**

Relational Schema R is in 2 NF iff

- R should be 1NF
- R should not contain any partial dependency
  Partial Dependency
  Let R be the relational schema and x, y, z are non-empty set of attributes.
  X : Any candidate key of R.
  Y : Non-prime attribute
  Z : Proper subset of candidate key

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

 z → y is said to be partial dependency iff–

- z is proper subset of candidate key
- y should be non-prime attribute.

Important Point 2

```
   
Not super key
```

```
Proper subset of Candidate key →Non-Prime attribute
```

The above FD forms redundancy in R.

**1.9.3 Third Normal Form (3NF)**

Relational schema R is in 3NF iff every non-trivial FD x → y in R with–
(i) x must be super key (SK)
or
(ii) y must be prime attribute.
 {SK → Prime/Non-Prime, (Not SK) → Prime attribute}

Important Point 3

3NF allow FD set:
[Proper subset of candidate key] → [Proper subset of other candidate key]
which forms redundancy in R.

**1.9.4 Boyce codd Normal Form (BCNF)**

Relational schema R is in BCNF iff every non-trivial FD “x → y” with x must be super key.
 Prime/ Non-prime attributes must be determine by super key.

Important Point 4

If R is in 3NF but not BCNF then [Proper subset of candidate key] → [Proper subset of other candidate key]
must exists in R.

Important Point 5

If relational shcema are with only simple candidate key then R always in:
I. 2NF
II. May or may not 3NF/BCNF
Reason : [Proper subset of candidate key] → [Non-prime attribute]
From the above statement, we can conclude that “partial dependency” not possible if all CK’s are simple candidate key.

Important Point 6

If relational schema R with only prime attribute (No non-prime attribute in R) then R always in:
I. 3NF
II. May or may not BCNF

```
z y
```

```
x
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Important Point 7

If relational schema R with no non-trivial FD’s then R always in BCNF.

**1.9.5 Database design Table**

```
DB design goal 1NF 2NF 3NF BCNF
```

1. Loss-less jon decomposition Yes Yes Yes Yes
2. Dependency preserving decomposition Yes Yes Yes May not
3. O% redundency No No No Yes [Over FD]

- Every relation possible to decompose into 1NF, 2NF, 3NF, BCNF with loss-less join decomposition.
- Every relation possible to decompose into 1NF, 2NF, 3NF with Dependency preserving decomposition.
- Not every relation can decompose into BCNF and 4NF with dependency preserving decompostion.
- Most accurate normal form to design simple database is 3NF because every relation is possible to decompose into 3NF
  with loss-less join and dependency preserving.

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

2

**ER MODEL**

**2. 1 Introduction**

Entity relationship diagram used to represent diagrametic design (High level design) of DB.

**2. 2 Main components in ER Diagram**

(i) Attributes
(ii) Entity sets
(iii) Relationship sets

(a) Entity sets
It is a set of entities of the same type denoted by a rectangular box in ER diagram. Entity can be identified by a list of
attributes which are placed in ovals.

Represent by :

Example :

(b) Attributes

(i) Attribute :

(ii) Key attribute :

(iii) Derived attribute :

```
eid
```

```
Emp
```

```
DOB
```

```
Age
```

```
A
```

```
A
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

(iv) Composite attribute: Attribute which can be represented as two or more attributes.

(v) Multivalued attribute:

(c) Relationship set: It is used to relate two or more entity set.

Represented by :

Example:

**2. 3 Participation**

- If every entities of entity set are participated with relationship set then it is total participation (100% participation)
  otherwise it will be partial participation (< 100% participation)
  Example :
  Consider Emp and Dept entity set.
  Manages relationship set such that each dept must have manager.
  **2. 4 Mapping [Cardinality constraints of relationship set]**

One mapping : Atmost one (0 or 1)
Many mapping : 0 or more (0 ...... *)

**1. Binary Relationship Mapping (One : One)
2. Binary Relationship Mapping (One : Many)**

```
A
```

```
B C D
```

```
A
```

```
E 1 R E 2
```

```
Binary relationship
```

```
Candidate
key of R : {A, B}
```

```
A B
```

```
E 1 1 1 E 2
```

```
A B
```

```
R or E 1 R E 2
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**3. Binary Relationship Mapping (Many to One)
4. Binary Relationship Mapping (Many to Many)
2. 5 RDBMS Design of Given ER Diagram**

(For binary relationship)

**1. Partial participation on both side of binary relationship**

- One to Many : Merge relationship set towards many side. So, 2 relational tables.
- Many to one : Merge relationship set towards many side. So, 2 relational tables.
- One to one : Merge relationship set any one side. So, 2 relational tables.
- Many to Many : Separate table for each entity set and relationship set. so, 3 relational tables.
  **2. Full participation on “one” side of many to one relationship**

Merge the entities and relationship set into single relational table. So, 1 table.

**3. Full participation on “Many” side of Many-to-one relationship**

Merge relationship set towards many side. So, 2 relational tables.

**4. Full participation on any “one” side in one-to-one relationship**

Merge the entity sets and relationship set into single table. So, 1 table.

**5. Full participation on any “Many” side of Many-to-Many relationship**

Merge relationship set towards any “Many” side of relationship. So, 2 table.

```
Candidate
key of R:{B}
```

```
A B
```

```
E 1 1 M E 2
```

```
A B
```

```
R or E 1 1 R M E 2
```

```
Candidate
key of R:{A}
```

```
A B
```

```
E 1 M^1 E 2
```

```
A B
```

```
R or E 1 M R^1 E 2
```

```
Candidate
key of R:{AB}
```

```
A B
```

```
E 1 M N E 2
```

```
A B
```

```
R or E 1 M R N E 2
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**6. Full participation on both side of relationship**

```
1:1
Merge the entity sets and
1:M
relationship set into single
M:1
relational table so, 1 relational table
M:N
```

### • 

### • 

### • 

### 

### • 

**2. 6 Self-Referencial Relationship Set**

(Recursive entity set)
Entities of entity set (E) related to some other entity of same entity set (E).

**2.7 Weak Entity Set and Weak Relationship Set**

The entity set with no key. (Attributes of weak entity sets are not sufficient to differenciate entities uniquely).

Points:
(a) For each weak entity set there must be owner entity set, which is strong entity set.
(b) Relationship set between weak entity set and identifier entity set is also “weak relationship set”.
(c) The participation towards weak entity set end must be “total participation”.
(d) The mapping between identifier entity set and weak entity set must be one : many (1 : M)
Example:

```
Note:
Weak entity set and multivalued attributes allowed to represent in ER diagram but not allowed in RDBMS table.
```

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

3

**RELATION MODEL AND SQL**

**3. 1 Procedural Query Language and Non-procedural Query Language**

```
Procedural Query Language Non-procedural Query Language
Formulation of how to access data from the database table and
what data required to retrieve from DB tables.
“Relational Algebra”
```

```
Formulation of what data retrieve from DB tables.
“Relational Calculus”
```

**3.2 Relational Algebra**

(Always generate distinct tuples)

Relational algebra refers to a procedural query language that takes relation instances as input and returns relation instances as
output.

**3. 2. 1 Basic operators**

```
 : Projection operator
```

```
 : Selection operator
× : Cross-product operator
U : Union
```

- : Set difference
  ƍ : Rename operator

**3.2.2 Derived operators**

```
 : Intersection {using “_”}
```

```
⋈ : Join {using X, }
```

```
/ or ÷ : Division {using , x, –}
```

I.  : Projection

•  (^) attribute_name (R): It is used to project required attribute from relation R.
•  (^) Condition(P) (R): It is used to select records from relation R, those satisfied the condition (P).

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Example:

II. Cross product (×):

- R × S : It result all attributes of R followed by all attributes of S, and each record of R paired with every record of S.
- Degree (R × S) = Degree (R) + Degree (S)

• (^) (R S = ) R S
Note:

- Relation R with n tuples and
- Relation S with 0 tuples then
  number of tuples in R × S = 0 tuples
  **3. 3 Join (** ⋈ **)**

I. Natural join (⋈)

R⋈S  distinct attributes(equality between common attributes of R and S (R × S))

Example:

- T 1 (ABC) and T 2 (BCDE)

 T 1 ⋈T 2 = ABCDE 12 (^12 )
12

```
T B TBTT
T C T C
```

```
=

```

```

  =
```

### 

### 

### 

- T 1 (AB) and T 2 (CD)
   T 1 ⋈ T 2  T 1 × T 2 = ABCD (T 1 × T 2 )
  Note:
  Natural join equal to cross-product if join condition is empty.

II. Conditional Join (⋈c)

- R ⋈c S  c (R × S)

III Outer Joins:

(a) LEFT OUTER JOIN
R ⟕ S : It produces
(R ⋈ S)  {Records of R those are failed join condition with remaining attributes null}
(b) RIGHT OUTER JOIN (⟖)
R ⟖S : It produces]

(R ⋈ S)  {Records of S those are failed join condition with remaining attributes null}

```
A B C
8 4 5
2 4 5
7 4 6
3 5 5
```

πB, C(R) :

σA>S(R) :

```
R B C
45
46
55
A B C
8 4 5
7 4 6
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

### (C) FULL OUTER JOIN (⟗)

### R ⟗ S = (R ⟕ S)  (R ⟖ S)

**3.4 Rename operator (ƍ)**

- It is used to rename table name and attribute names for query processing.
  Example:
  (I) Stud (Sid, Sname, age)

```
ƍ(Temp, Stud) : Temp (Sid, Sname, age)
```

(II) ƍI,N,A (Stud) : Stud (I, N, A)

```
All attributes renaming
```

(III) ƍ^ Sidage→→IA (Stud) : Stud (I, Sname, A)

```
age →A
Some attribute renaming
```

Example:

```
Retrieve eicls of female employees whoose salary more than every male employee?
```

Result :

**3. 5 Division**

- It is used to retrieve attribute value of R which has paired with every attribute value of other relation S.
  AB(R)/B(S): It will retrieves values of attribute ‘A’ from R for which there must be pairing ‘B’ value for every ‘B’ of S.

**Expansion of ‘/’ by using basic operator**

- Example: Retrieve sid’s who enrolled every course.

Result:

```
sidcid(Enroll)/ cid(Course)
Step 1: Sid’s not enrolled every course of course relation.
(Sid’s enrolled proper subset of course)
```

```
sid((sid(Enroll) × cid (course)) – sidcid (Enroll))
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Step 2:

```
[sid’s enrolled every course] = [sid’s enrolled some course] – [sid’s not enrolled every course]
```

 sidcid (E)/ cid(c) = sid(E) – sid((sid(E)× cid(C) – sidcid (E))

**3.6 Set operator**

```
U: Union operator
```

- : Except minus
   : Intersection operator
- To apply set operations relations must be union compatable.
- R and S relations union compatable
- If and only if-
  (i) Arity of R equal to Arity iof S and
  (ii) Domain of attributes of R must be same as domain of attributes of s respectively.

Example 1:

```
Sid Sname(..........) Sid(..........)
```

{Arity not same so, set operation not allowed}

Example 2:

Sid S name(.......) Sid marks(.....)
{Arity same but Sname domain is different from marks so, not allowed}

Example 3:

(^) Sid Sname(.......) Stud ID, Stud name(.....)
{Arity and domains are same so, allowed for set operation}

- 1. Set operation on relation:

### 2 2 2 2 2 4 3

### R A

### S B

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

### : }

### 2

### 3

### 4

### – :

### 3

### :

### 2

```
R S x x R V x s A
```

```
R S x x R x S A
```

```
R S x x R x S A
```

###    

###   

###    

**3. 7 Cardinality Table**

Assume relation R with n Distinct tuples and relation S with m distinct tuples:
RA Expression Cardinality
R × S n * m tuples
R ⋈ S {0 to n * m tuples}
R =⋈ S {n to n* m tuples}
R ⋈= S {m to n*m tuples}
R =⋈= S {max (n,m) to n*m tuples}^
RS {max(n,m) to n + m}^
R S {0 to min (m, n}^
R–S {0 to n tuples}
R/S {0 to [n/m] tuples}

**3.8 SQL**

**3. 8 .1 [Structure Query Lang]
3. 8 .2 Relational Query and SQL query**

- SQL : SELECT DISTINCT A 1 , A 2 , ...... An

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
FROM R 1 , R 2 , ...... Rn
WHERE P;
Equivalent RA : A , A ..... A 1 2 n(  p(R 1 R 2 .....Rn))
```

- SELECT  projection of RA ()
  FROM  Cross-product (x)
  WHERE  Selection operator of RA ()
  **3. 8 .3 Basic SQL Clauses**

```
SELECT DISTINCT A 1 , A 2 , ...... An
FROM R 1 , R 2 , ...... Rn
WHERE condition
GROUP BY (attributes)
HAVING condition
ORDER BY (attributes) (DESC)
```

**3. 8 .4 Execution Flow**

```
FROM  cross-product of relations

WHERE  Selection operator () to apply condition for each record

GROUP BY

HAVING

SELECT

DISTINCT

ORDER BY
```

**3. 8 .5 GROUP BY:**

- It is used to group records data a based on specific attribute.
- It GROUP BY clause used then
  (a) Every attribute of GROUP BY clause must be selected in SELECT clause.
  (b) Not allowed to select any other attribute in SELECT clause.
  Allowed to select aggregate function along with GROUP BY attribute in SELECT Clause.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**3. 8 .6 HAVING Clause**

- HAVING clause must be followed by GROUP BY clause.
- HAVING clause used to select groups those are satisfied having clause condition.
- HAVING clause condition must be over aggregation function such as some ( ), Every ( ) etc. but not allowed direct attribute
  comparison

Example:

1. SELECT A
   FROM R
   GROUP BY A
   HAVING AVG (c) > 60;
2. SELECT A, AVG (c)
   FROM R
   GROUP BY A
   HAVING some (c) > 50;

### 3. SELECT A

### FROM R

### GROUP BY A

### HAVING C> 60;

```
Error
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
Not allowed
```

```
Note:
WHERE clause condition tested for each record but HAVING clause condition tested for each GROUP.
```

**3. 8 .7 WITH Clause**

- WITH clause is used to create sub-query result that can be re-used many times in query processing.

Example:
WITH Temp (Al, A 2 ) as
(SELECT T 1. A 1 , T 2. A 2
FROM Emp T 1 , Emp T 2
WHERE T 1. A 1 < T 2. A 1 )

```
Note:
Every Query which is written by using HAVING clause can be re-written by using WHERE clause.
```

**3. 8 .8 Nested Query Without Co-relations**

- Inner query independent of outer query.
- Execution flow must be Bottom to Top mean first bottom (Inner query) evaluated then outer query executed.
  **3. 8 .9 Co-related Nested Query**
- In Nested Co-related query inner query uses attributes from outer query tables.
- In Co-related Nested query inner query allowed in WHERE, HAVING clause of outer query.
  Example: SELECT A
  FROM R
  WHERE (SELECT count(*)
  FROM S
  WHERE S.B < R.A) < 5;

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**Important point 1**

- If co-relation in WHERE clause then inner query re-computes for each record of outer query From clause.
- If correlation in HAVING clause then inner query re-computes for each group of outer query.

**3.9 Function used for nested Queries**

1. IN Function
   It is used for membership testing.

```
Note:
Queries of "equi Join" can implement by IN function  (R S)
```

2. ANY Function (operator “<, ≤, >, ≥, =, < >”)
3. ALL Function

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
Note:
ANY function can be used as queries of conditional join query.
```

Example:

Important point 2

- IN function equal to ‘= ANY’ function
- IN function not equal to ‘= ANY’ if more than one attribute used for IN comparison.
- NOT IN function equal to “< > ALL”.

4. EXISTS clause
   - It is used to test result of inner query is empty or not empty.
   - 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Example:

```
Note:
EXISTS function can use as conditional join queries with join condition in inner query WHERE clause.
```

Emp (eid sal dno. Gen) Retrieve eids of femal’s whose salary more than (some) male emp.

 

SQL
JOIN Query
SELECT DISTINCT T 1. eid
FROM EMP T 1 , Emp T 2
WHERE
T 1 .gen = Female and
T 2 .gen = male and
T 1 .sal > T 2. sal

 

```
SQL
Mested Query
SELECT Eid
FROM Emp
WHERE gen = Female
and sal > ANY (SELECT sal
FROM Emp
WHERE gen = male);
```

 

```
SQL
Co related Nested Query−
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

SELECT Eid
FROM Emp T 1
WHERE T 1 .gen = Female and
EXISTS (SELECT *
FROM Emp T 2
WHERE T 2 .gen = male and T 1. Sal > T 2. sal);

### ❑❑❑

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

4

**FILE ORGANIZATION AND**

**INDEXING [B AND B**

```
+
TREE]
```

**4.1 File Organization**

- Database is collection of files [Tables].
- File is collection of blocks [Pages].
- Block is collection of records.

```
Note:
Data access from disk (DB file) to main memory block by block.
```

**4.2 Records organization of DB file**

```
Spanned Organization Unspanned Organization
```

1. Record allowed to span in more than one
   block.
   1. Complete record must be in one block.

```
2. Advantage: Possible to allocate file
without any internal fragmentation.
```

2. Advantage: less access cost and easy to
   organize DB file.
3. Disadvantage: More access cost to
   access spanned records.
4. Disadvantage: May not possible to
   allocate DB file without any internal
   fragmentation.

```
Note:
```

1. Spanned organization prefer to store database record of the file with variable length record.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

2. Unspanned organization prefer to store DB record of file with fixed length record.

**4.3 Block factor [BF]**

The maximum possible records which can store in block (maximum record per block).

Consider record size = R bytes

Block Factor Block size Header size
Record size

```
−
=

```

For unspanned organization

Block Factor Block size Header size
Record size

−
=

For spanned organization

**4 .4 Categories of Index**

**4.4.1 Dense Index**

For each DB record of DB file there must be index entry in index file.

**4.4.2 Sparse Index**

For set of DB records (blocks) of DB file there exists index entry in index file.

Important Point I

- Sparse index possible only over ordered field of DB file.
- In Sparse indexing
  No. of index No. of records
  file entries of DB file

###    

###    

###    

**4.4.3 Block Factor of Index**

Assume Block size = B Bytes
Header size = H Bytes
Search key = K Bytes
Pointer size = P Bytes

```
Block Factor of index = BH
KP
```

```
−
 
+
Note:
By default header size will be 0 bytes, if not given in problem.
```

**4.5 I/O Cost [Access cost]**

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

The number of secondary memory block (DB file block) required to transfer from disk to main memory in order to access
required record.

1. I/O cost to access data record without index from DB file of n blocks

(a) Over ordered field:
Access cost = [log n] 2 block

(b) Over unordered field:
Access cost = n blocks

2. If Dense Index Used:

- Number of Dense Index block =

```
number of records
Block Factor of Index
```

```



```

- Access cost (Number of Block access)

= log number of Dense index blocks at 1 level 2 ( st ) + 1

3. If sparse Index Used:

- Number of DB blocks =

```
number of records
BF of DB
```

```



```

- Number of sparse Index block (At 1st level)

```
number of DB blocks
BF of Index
```

```

=

```

- Access cost (Number of block access)

log number of sparse index blocks at 1 level 2 ( st ) + 1

**4.6 Types of Index**

- Search key: Fields of DB file which is used for indexing

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**4.6.1 Primary Index**

Search Key: Ordered field and key (candidate key)

- I/O cost to access record using primary index with multilevel indexing is (k + 1) blocks.
  Where k is level of indexing.
- For any database relation at most one primary index is possible because, search key must be ordered field.
- Primary index can be either dense or sparse but sparse primary index preferred.

**4.6.2 Clustered Index**

Search Key: Ordered field and non-key.

- I/O cost:

```
Single level index blocks :
```

```
No.of distinct values over non-key
BFof Index
```

```



 Access cost = log (singlelevelindex blocks) 2 + 1
```

- I/O cost to access cluster of record using clustered index with multilevel index is:
  k (oneor more block of DB)
  Until next cluster begins

```
+
```

- For any DB relation at most one clustering index is possible because search key is ordered field.

```
Note:
For any DB relation either primary index or clustering index is possible but not both simultaneously.
```

**4.6.3 Secondary Index [over key]**

Search Key : Unordered field and key.

- Secondary index is alternative index to access data records even primary or clustering index already exists.
- Secondary index over key is always dense index.
- I/O cost to access record using secondary index over key with multilevel index: (k + 1) blocks.

**4.6.4 Secondary Index [over non-key]**

Search Key: Unordered field and non-key.

- I/O cost to access record using secondary index over non-key with multilevel index = [k blocks from k level of index] +
  [some more DB blocks]

```
Note:
Many secondary index’s possible for DB file.
```

**4.7 Balanced Search Tree [ Height Restricted Search Tree]**

- The maximum height of search tree for n distinct keys should not exceed O (log n)
- Worst case search cost to search element is : O (log n)

**4.7.1 Why B/B+ Tree Index preferred rather than balanced BST/AVL for DB index**

(a) AVL: If AVL tree (balanced BST) used for DB index:

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Data Base Management System
```

- Disadvantage: Each index block with only one key so the number of levels of index is high. (I/O cost to access data is also
  very high).
- Wastage of disc space, which is allocated for index (only one key stored per block)

```
(b) B/B+ Tree:
```

- The access cost (I/O cost) is less because many keys store in one node (number of levels of index will be less).
- The wastage of disk space is less.
  **4.7.2 B Tree Definition**
- Order P (degree): The maximum possible child printers can be stored in B Tree node.
  Node structure: P child pointer, P – 1 Key and P – 1 Record Pointer (Rp).

```
 order of node 
```

```
P  (size of block pointer) + (P - 1) (size of key field + size of record pointer)  Block size
```

1. Every internal node except root must be atleast

```
p
2
```

```

^ block pointer and
```

```
p
2
```

```

-^ 1 keys^ and at most P block pointer and (P –^
1) keys.
```

2. Root can have at least 2 child/block pointer and 1 keys and at most P block pointer and (p - 1) keys.
3. Every leaf node must be at same level.

- Advantages:
  B Tree index best suitable for random access of any one record.

```
Example:
SELECT *
FROM R
WHERE A = 15;
 Worst case access cost = (k + 1) blocks
Best case access cost = 2 blocks
```

- Disadvantages:

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

B Tree index not suitable for sequential access of range of records.

**4.7.3 B+**^ **Tree**

Order P: The maximum possible pointers can be store in B+ tree node.

1. Node Structure:

- Leaf node: (set of (key, RP) pairs and one block pointer)

 Order of leaf node = (P –1) [ K + RP] + 1 * BP  Block size.

- Internal Node:
  Order of internal node = P * BP + (P – 1) * K  Block size.
- B+ Tree best suitable for random access of any one record and sequential access of range of records.
- I/O cost to access range of ‘x’ records sequential:

Important point 2

If disk block allocation for B and B+ tree nodes are equal size then

1. Order P of B tree < order P of B+ Tree.
2. [number of index blocks of B tree index for n keys]  [number of index blocks of B+ Tree nodes for n keys]
3. I/O cost  I/O cost

Important point 3

If order P of B Tree is equal to order P of B+ Tree then

1. [number of B Tree node n distinct keys]  [ number of B+ Tree nodes for n distinct keys]
2. [B Tree level for n keys]  [ B+ Tree levels for n keys]

```
❑❑❑
```

K 1 R 1 K 2 R 2 .......... KP- 1 RP- 1 BP (^) →Block Pointer {pointer to next leaf}

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

5

**TRANSACTIONS AND**

**CONCURRENCY CONTROL**

**5. 1 Transaction**

A set of logically related operation to perform unit of work.

**5.2 Degree of concurrency**

The number of users (Transactions) using data bases simultaneously (concurrently).

**5. 2 .1 Flat File System**

In flat file system 1 file is a resource so, only one user allowed at a time.

**5. 2 .2 DBMS File System**

- In DBMS file system 1 record is a resource so, it allows as many users as the number of records.
- More degree of concurrency.
  **5. 3 Main Operations in Transactions

5. 3 .1 Read (A)**

Access the data item ‘A’ from DB file ‘Disk’ to programmed variable (main memory) in order to use current value of ‘A’ in
transaction logic.

**5.3.2 Write (A)**

Modification of data item ‘A’ in DB file.

**5.4 ACID Properties**

To preserve integrity (correctness) each transaction must satisfy ACID properties

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
DBMS Software
```

```
A∶Atomicity
D∶Durability}^ Recovery management component of DBMS
software take cares of atomicity and durability
I : Isolation} Concurrency control component of DBMS
software is responsible for isolation.
```

```
DBA User
```

```
C : Consistency} User (DBA or DB developer) is
responsible for consistency.
```

**5.5 Atomicity**

Execute all operations of transaction including commit or execute none of the operation of transaction by the time of transaction
termination.
Recovery management component should roll back, if transaction fails anywhere before commit.

**5. 5 .1 Redo Operation**

- It performs all the modification of database file because of transaction commit.
- Clean all the log entries of committed transaction.
- Redo is not performed after every commit but after every check point.
  **5. 5 .2 Undo Operation**
- Undone all the write operation performed by the transaction.
- Convert dirty block (updated block) into clean block.
  **5. 5 .3 Check point**
- Check point issued by DBMS software in regular interval.
- If checkpoint issued
  (I) Performs Redo operation on all the committed transaction until previous checkpoint.

Example :

|   9 : 00 AM DB Started   |
| :-----------------------: |
| 9 : 05 AM 1 st checkpoint |
|             :             |
| 9 : 10 AM 2 nd checkpoint |
|             :             |
|  9 : 15 AM System Crash  |

**5. 5 .4 System Crash**

If System crash/failure happen, required operation to recover are
(I) All committed transaction until previous checkpoint will perform Redo.
(II) All uncommitted transaction in entire system will perform undo.
(III) Clean all log entries.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.5. 5 Roll back (Abort)**

Undo modification of database file which are done by failure transaction.

**5.6 Durability**

- Durability maintained by Recovery management component of DBMS Software.
- The transaction should able to recover under any case of failure.
- Transaction fails because of

1. Power failure
2. Software crash
   ➢ OS restarted
   ➢ DBMS restarted
3. OS/DBMS concurrency controller may kill transaction.
4. Hardware Crash (Disk failure)
   RAID architecture of disk design is used to overcome the problem.

**5.7 Consistency**

- User responsible for consistency.
- Database should be consistent before and after the execution of the transaction.
- DB operations requested by user (SQL queries/transaction operation) must be logically correct.

**5.8 Isolation**

- Isolation maintained by concurrency control component.
- Isolation means concurrent execution of 2 or more transaction result must be equal to result of some serial schedule.

**5.9 Schedules**

Time order execution sequence of two or more transactions.
Example :
S : R 2 (A) R 1 (A) W 3 (A)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.9.1 Serial Schedule**

- After Commit of one transaction, begins (Start) another transaction.
- Number of possible serial Schedules with ‘n’ transactions is “n!”
- The execution sequence of Serial Schedule always generates consistent result.

Example
S : R 1 (A) W 1 (A) Commit (T 1 ) R 2 (A)W 2 (A) commit (T 2 ).

**5.9.2 Advantage**

- Serial Schedule always produce correct result (integrity guaranteed) as no resource sharing.

**5.9.3 Disadvantage**

- Less degree of concurrency.
- Through put of system is low.
- It allows transactions to execute one after another.

**5.10 Concurrent Schedule**

Transactions can execute concurrently or simultaneously

- May result inconsistency.
- Better through put and less response time.
- To maintain consistency transaction should satisfy ACID property.
- If T 1 and T 2 transaction with ‘n’ and ‘m’ operations each, then

```
No. of concurrent Schedule = (𝑛𝑛+! 𝑚𝑚!)!
```

**5.11 Schedule Classification**

**5.12 Serializable Schedule**

A Schedule is serializable Schedule if it is equivalent to a Serial Schedule.
(i) Conflict Serializability
(ii) View Serializability

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.13 Conflict Serializability**

**5.13.1 Topological order**

Graph traversal algorithm for directed graph
(i) Visit vertex (v), whose indegree is ‘O’ and delete ‘V’ from the graph.
(ii) Repeate (i) for all the vertices of graph.

**5.13.2 Conflict Pairs**

Two operations form Schedule (s) are conflict pair if and only if
(i) Atleast one write operation.
(ii) Operation on different data item.
(iii) Operations are from different transactions.

```
ij
ij
ij
```

```
S : r (A)..........w (A)
S : w (A)..........r (A) Conflict Pairs
S : w (A)..........w (A)
```

```





```

**5.13.3 Precedence Graph**

A graph G in which vertex (v) represent the transaction of Schedule and edges (E) represent conflict pair precedence’s.
Example:
S : R 2 (A) R 2 (B) W 1 (A) W 2 (B) W 3 (A) W 3 (B)

**5.13.4 Conflict Equal Schedule**

Schedule S 1 and S 2 are conflict equal Schedule if and only if Schedule S 2 can derived by inter changing consecutive non-conflict
pairs of Schedule S 1.
Interchange
SS 12 ⎯⎯⎯⎯⎯⎯⎯⎯→Con sec utive non conflict pair−

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
Note:
If Schedule S 1 and S 2 have
(i) Same set of transactions, and
(ii) Same precedence graph and
(iii) A cyclic precedence graph then
S 1 and S 2 are conflict equal Schedule.
```

Important Point 1:

1. If S 1 , S 2 Schedule are conflict equal then precedence graph of S 1 and S 2 must be same.
2. If S 1 and S 2 have same precedence graph then S 1 and S 2 may or may not conflict equal.

**5.14 Conflict Serializable Schedule**

Schedule (s) is conflict serializable Schedule if and only if some serial Schedule (S) must be conflict equal to Schedule (S).
ConflictEqual ( ')
Conflict SerializableScchedule

```
Schedule (s)⎯⎯⎯→S Serial Schedule
```

Important Point 2:
Schedule (s) is conflict serializable Schedule if and only if

1. Precedence graph is a cyclic and
2. Conflict equal serial schedule are to apological order of precedence graph.

```
Note:
[No. of serial schedule conflict equal to schedule s] = [No. of topological order of schedules precedence graph]
```

**5. 15 View Serializable Schedule**

- Schedule (s) is view serializable if and only if some serial schedule (s’) view equal to schedule (s).
- Let S 1 and S 2 be two schedule with the same set of transactions, S 1 and S 2 are view equal view equivalent if the following
  three conditions are met:

**5.15.1 Initial Read**

For each data item A, if transaction Ti reads the initial value of A in Schedule S 1 , then transaction Ti must, in Schedule S 2 , also
read the initial value of A.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.15.2 Updated Read**

For each data item A if transaction Ti perform Read (A) in Schedule S 1 and that value was produced by transaction Tj, then
transaction Ti must in Schedule S 2 also read the value of A that is produce by the transaction Tj.

**5.15.3 Final Write**

S 1 : ......... Ti ....... S 2 : ........ Ti....

Final write of A : ( )
Last write

```
wA Final write of A : ( )
Last write
```

```
wA
```

For each data item A, the transaction that perform the final write (A) operation in schedule (S 1 ) must perform the final write
(A) operation in schedule S 2.

Important Point 3

- If schedule S is conflict serializable schedule, then S is also view serializable schedule.
- If schedule s is not conflict serializable then it may or may not view serializable
- Every view serializable schedule that is not conflict serializable.

**5.16 Classification based on Recoverability**

The concurrent execution may leads:

1. Irrecoverable schedule
2. Cascading rollback problem
3. Lost update problem
   The above problems can occur even if the schedule is serializable (Integrity satisfied)

**5.16.1 Irrecoverable Schedule**

- A schedule(s) is irrecoverable if and only if transaction Tj reads data item ‘x’, which is updated by Ti and commit of Tj
  before commit/rollback of transaction Ti.
- Irrecoverable means unable to recover or rollback.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.16.2 Recoverable Schedule**

A schedule(s) is recoverable if and only if
(I) No uncommitted read (no dirty ready in schedule(s).
Or
(II) If transaction Tj reads data item ‘x’ which is updated by transaction ‘Ti’, then commit of Tj must be delayed until
commit/rollback of Ti.

**5.1 6 .3 Uncommitted Read (Dirty Read)**

Transaction Tj reads data item ‘x’ which is updated by uncommitted transaction. Ti.

**5.1 7 Cascading Rollback Schedule (Problem)**

When some transaction reads data items which is updated by some other transaction then because of failure of the transaction
that updated the data item may rollback all the dependent transaction.

```
T 1 T 2 TTT 333 T 4 T 5 T 6
w(A)
R(A)
w(A)
w(B)
```

```
Ro
```

```
llb
```

```
ac
```

```
k^
```

```
Failed
```

```
w(A)
R(B)
R(B)
w(C)
R(C)
```

```
Roll back
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

Failure of T 1 forced to rollback T 2 , T 4 , T 5 and T 6.

- Disadvantage of Cascading Rollback
  1. It waste the CPU execution time.
  2. Wastage of I/O access cost.

**5.17.1 Cascadeless Rollback Recoverable Schedule**

- No dirty read in the schedule.
- Transaction Tj should delay read (x) which is updated by Ti, until Ti commit or rollback.

**5. 18 Lost Update Problem**

Lost update problem occur if Tj write (x) which is already written by uncommitted transaction Ti.

**5.19 Strict Recoverable schedule**

A schedule must satisfy

1. Cascadeless rollaback recoverable schedule and
2. If Ti writes (x) then other transaction Tj write (x) must be delayed until Ti commit or rollback.

Recoverable

Cascade less

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
Note:
```

1. Strict recoverable schedule may or may not be serializable.
2. Serializable schedule may or may not be recoverable.

serial schedule

```
cascade less R
ol
```

l (^) b
ac
k
Schedu
le^
Sch
edu
le
Sched
ule
Recoverable
Concurrent
Irrecoverable
schedule

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.20 Concurrency control protocol**

Concurrency control protocol should not allow to execute:

1. Non-serializable schedule (Violate Isolation).
2. Non-strict recoverable schedule (Violate atomicity and Durability).

**5.2 1 Locking Protocol**

Lock is as variable used to identify the status of data item.
Transaction (T 1 )
Lock (A):
R(A)
W(A)

```
Granted by concurrency controller
```

```
Lock(B): Denied by concurrency controller
```

**5.22 Types of Lock**

1. Shared Lock(s): Read only lock.
2. Exclusive lock (x): Read/write lock.
3. Shared (s mode)
   - Exists when concurrent transaction granted READ access.
   - Produce no conflict for Read only transactions.
   - Issued when transaction wants to read and exclusive lock not held on item.
4. Exclusive (x) mode
   - Exists when access reserved for locking transaction.
   - Used when potential for conflict exists.
   - Issued when transaction wants to updated unlocked data.

Example:
Transaction (T 1 )
S(A) : Granted shared lock
R(A) } only read allowed
X(B) : Granted exclusive lock
R(B)
Read and write
W(B)

```



```

**5.22.1 Lock compatible table**

```
Data item A
```

```
S
```

```
X
```

```
S
```

```
Yes
```

```
No
```

```
X
```

```
No
```

```
No
```

```
Holded by Ti
```

```
Requested
by Tj {
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.2 3 Phase Locking Protocol (2PL)**

- It guaranteed serializability.
- Transaction (T) allowed to request lock on any data item in any mode (x/s) until first unlock of transaction (T).
  **1. Growing Phase**

Acquires all the required locks without unlocking any data. Once all locks have been acquired, the transaction is in it locked
point.

**2. Shrinking phase**

Release all locks and can not obtain any new lock governing rules of 2 PL.
Example:

Important point 1

1. If schedule (s) is executed by 2PL then schedule guaranteed is conflict serializable schedule.
2. Conflict equal schedule is based on lock points order of the transaction.
3. If schedule is not conflict serializable schedule (cyclic precedence graph) then schedule not allowed to execute by 2 PL.

Note: Every schedule which is allowed by 2PL is always conflict serializable, but not every conflict serializable schedule is
allowed by 2PL.

```
Transaction (T)
S(A)
X(B)
S(C)
X(D)
U(C)
U(D)
U(A)
U(B)
```

```
Growing phase
(locking phase)
```

Locking point

```
Strriking phase
(unlocking phase)
```

```
Conflict
serializable
schedule
```

### 2PL

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

**5.2 3 .1 Limitations of 2PL**

1. 2PL restriction may leads to deadlock.
2. 2PL restriction may leads to starvation.
3. 2PL condition not sufficient to avoid
   (I) Ir-recoverable schedules
   (II) Cascading rollback problem
   (III) lost updated problem

**5.2 4 Strict 2PL protocol**

- Basic 2PL: Lock request of transaction (T) not allowed in shrinking phase of transaction T
  and
  Strict recoverable: All exclusive lock of transaction must hold until commit/Rollback of transaction T.

**5.24.1 Strict 2PL protocol guarantees**

(a) Serializability.
(b) Strict recoverable.

Disadvantage:

It is not free form deadlock and starvation.

Example:

Transaction (T)

```
( )
( )
( )
( )
```

### SA

### XB

```
growing phase
SC
XD
```

### 

### 

### 

### 

### 

### 

```
( )
( )
```

```
( )
( )
```

### UA

### UB

```
Commit Strinking phase
UB
UD
```

### 

### 

### 

### 

### 

### 

### 

**5.25 Rigorous 2PL**

Basic 2 PL : A lock request allowed only in growing phase of transaction and

all locks (shared/Exclusive) of transaction T must be hold until commit or Rollback.

**5.26 Conservative 2PL**

Transaction (T) must lock all required data itmes in starting phase.

If locks are not available then unlock all data items and re-request all data item lock again.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
Basic 2PL Strict 2PL Rigorous 2PL Conservative 2PL
Guaranteed
Serializability
```

```
Yes Yes Yes Yes
```

```
Guaranteed strict
Recoverable
```

```
No Yes Yes No
```

```
Free from dead lock No No No Yes
Free from starvation No No No NO
```

**5.2 7 Time stamp ordering protocol**

Assign global unique time stamp value to each transaction and produces order for transaction submission.

The time stamp values of transaction can be used for transaction identification and to set priority between the transaction.

**5.2 7 .1 Time stamp value for each data item**

- Assume data item is A
  I. Read TS value (A): It is the highest transaction time stamp value that has executed R(A) successfully.

II. Write TS value (A): It is the highest transaction TS value that has executed W(A) successfully.

1. Basic Time stamp ordering protocol:

a. If transaction T issues R(A) operation.

```
If (WTS(A)) > TS(T)
then Rollback T
else
{Allow to execute R(A) successfully
set RTS (A) = max {RTS(A), TS(T)}}
```

b. If transaction T issues W(A) operation
if (RTS(A)) > TS (T)
{then Rollback trans (T)}
else if (WTS(A) > TS(T))
{then Roll back T}
Else
{Allow to execute W(A) successfully
set WTS(A) = {TS(T)}}

2. Thomas write rule stamp ordering protocol

a. If transaction T issues R(A operation
if (WTS(A)) > TS(T)
{then Rollback transaction T}
else

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Data Base Management System
```

```
{allow to execute R(A) successfully
set RTS (A) = max {TS(T), RTS (A)}
```

b. If transaction T issue W(A) operation
if (RTS (A) > TS(T))
{then roll back T}
else if (WTS(A)) > TS(T)
{then ignore w(A) of transaction T and continue.}
else
{Allow to execute w(A) successfully
set WTS(A) = TS(T)}

3. Strick time stamp ordering protocol

A transition T 2 that issues a R(A) or W(A) such that TS (T 2 ) > WTS (A) has it read operation delayed until the transaction T 1
that write the value x has committed or rolled back.

```
Basic TS ordering protocol Thomas write TS ordering protocol Strict TS ordering protocol
```

1. Ensue conflict serialization 1. Ensure view serialization 1. Ensure conflict serialization
2. Free from deadlock 2. Free from deadlock 2. Free from deadlock
3. Not free from starvation 3. Not free from starvation 3. Not free from starvation
4. Not guaranteed strict recoverable 4. Not guaranteed strict recoverable 4. Guaranteed strict recoverable

### ❑❑❑

**Computer Computer**

**NetworksNetworks**

**Computer**

**Networks**

```
Design Against Static Load
```

1. IP Addressing, Subnetting & Supernetting ........................................................................... 11 .1 – 11. 3
2. Error Control ......................................................................................................................... 11. 4 – 11. 6
3. Flow Control ........................................................................................................................ 11. 7 – 11. 10
4. IPv4 Header ......................................................................................................................... 11. 11 – 11. 14
5. TCP & UDP ........................................................................................................................... 11. 15 – 11. 19
6. Medium Acess Control[MAC] ............................................................................................... 11. 20 – 11. 22
7. Routing Algorithms, Switching & IP Support Protocol .......................................................... 11. 23 – 11. 27
8. Application Layer Protocol .................................................................................................. 11. 28 – 11. 33
9. OSI and ICP/IP Protocol Stack .............................................................................................. 11. 34 – 11. 37

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**IP ADDRESSING, SUBNETTING**

**& SUPERNETTING**

**1.1 IP Addressing**

Class A : 0 → (1 - 126), No. of IP Addresses = 2^31
Class B : 10 → (128 - 191), No. of IP Addresses = 2^30
Class C : 110 → (192 - 223), No. of IP Addresses = 2^29
Class D : 1110 → (224 - 239), No. of IP Addresses = 2^28
Class E : 1111 → (240 - 255), No. of IP Addresses = 2^28

**1.2 Default subnet Mask**

Class A : 255.0.0.0
Class B : 255.255.0.0
Class C : 255.255.255.0

**1.3 Private Addresses Range**

10.0.0.0 to 10.255.255.255 → 1 class A Network.
172.16.0.0 to 172.31.255.255 → 16 class B Network.
192.168.0.0 to 192.168.255.255 → 256 class C Network.

```
Class Number of Networks Number of hosts per Network
```

Class A (^27) – 2 = 126 224 – 2 = 1,67,77,214 hosts
Class B (^214) = 16,384 216 – 2 = 65,534 hosts
Class C (^221) = 20,97,125 28 – 2 = 254 hosts
Class D No NID and HID, all 28 remaining bits are used to define multicast address
Class E No NID and HID, it is meant for research and future purpose
Note:
The IP address 127.x.y.z is known as loop back address and it is used to check the connectivity.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**1.4 Types of Communication**

(i) Unicast communication (1 : 1)

(ii) Broadcast communication (1 : All)

(iii) Multicast Communication (1: Many)

**1.5 Unicast Communication**

1. Transmitting the data from one computer to another computer is called as unicast communication.
2. It is one to one transmission.
3. In Unicast communication both source and destination either present in the same network or in the different network.

**1.6 Broadcast Communication**

```

```

### 

**1.6.1 Limited Broadcasting**

1. Transmitting data from one computer to all other computer in the same network is called as Limited Broadcasting.
2. Limited Broadcast Address = 255.255.255.255
3. Limited broadcast address can’t be used as a source IP Address.
4. Limited broadcast Address will always be used as a Destination IP.

**1.6.2 Direct Broadcasting**

1. Transmitting data from one computer to all other computer in the different network is called as Limited Broadcasting.
2. Direct broadcast address can’t be used as a source IP Address.
3. Direct broadcast Address will always be used as a Destination IP.

### NID^ HID^

1. – 0's → Network ID
2. – 1's → Direct Broadcast Address (DBA)
3. 1's 1's → Limited Broadcast Address (LBA)
4. 0 's – → Host with in the Network
5. 1 's 0's → Network Mask or Subnet Mask

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**1.7 Multicast communication**

Transmitting a packet from one computer to many computers (0 or more) is called Multicast communication.

**1. 8 CIDR Rules**

1. All the IP Address in the Block must be contiguous.
2. Block size must be a power of 2.
3. First IP address of the block must be divisible by size of the block.
   **1. 9 Supernetting**

The process of combining two or more network to get a single network is called as supernetting.

```

```

**1.10 Advantage of Supernetting**

1. Super netting Reduce Routing table entry.
2. Router will take less time for processing the packet.
3. It improve flexibility of IP Address Allotment i.e. If someone required 500 Address, then no need to purchase class B
   network we can combine two class C network.

**1.11 Rules of Supernetting**

1. Network ID must be contiguous.
2. Size of the Network must be same and number of Network must be a power of 2.
3. First Network ID must be divisible by size of the supernet.

```




```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

2

**ERROR CONTROL**

**2.1 Error Control**

```
Note:
 The number of corrupted bits or affected bits depends on the data rate and duration of noise.
 The number of corrupted bits or affected bits =Data rate * Noise duration.
 Burst error is more likely to occur than a single bit error.
 Error correction is more difficult than error detection.
```

```
Error Detection Error Correction
```

1. Once noticed error simply
   discard.

```
Capability of correcting error.
```

2. Ask for retransmission.
   Does not required retransmission.

### 

### 

### 

###  

**2.1.1 Hamming distance**

Hamming distance between two Binary string of same size is the number of differences between corresponding bits.
Hamming distance between two Binary string is denoted by d(x, y)
d(000, 011) = 2

```
Types of Errors
```

```
Single-Bit Error Burst Error
```

```
Error Control
```

```
Error detection Error correction
```

1. Simple Parity 1. Hamming code
   2. 2D parity
   3. Check sum
   4. CRC

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

```
d(100, 011)=3
d(10101, 11110)=3
```

Hamming distance can easily be found if we apply XOR operation (⊕) on the two words and count the Number of 1’s in the
result.

**2.1.2 Minimum Hamming distance**

In a set of codewords, the minimum Hamming distance is the smallest Hamming distance between all possible pairs of code
words.

**2.1.3 Minimum Hamming distance for Error detection**

To detect ‘d’ bit error minimum hamming distance required =d+1

**2.1.4 Min. Hamming distance For Error Correction**

To Correct ‘d’ bit error minimum hamming distance required =2d+1

**2.2 Simple Parity Check Code**

Simple parity

In the Simple parity concept one extra bit ( parity bit ) is added to each dataword.
Simple parity check can detect all single bit error.
Simple parity check can not detect an even number of errors.
Simple parity check can detect an odd number of errors.

**2.3 2D Parity Check Code**

2D parity

Two dimensional parity check can detect and correct all single bit error and detect two or three bit error that occur any where
in the matrix.
However only some pattern with four or more Errors can be detected.
In a 2D-parity check code, the information bits are organized in a matrix consisting of rows and columns.
For each row and each column one parity check bits is calculated.

**2.4 CRC**

Length of the dataword = n
Length of the divisor = k
Append (k-1) Zero’s to the original message
Perform modulo 2 division
Remainder of division = CRC
Codeword = dataword with Appended (k-1) Zero’s + CRC

```
010
101
1 1 0
001
```

```
(a)
(b)
(c)
(d)
```

```
d (a, b) = 3
d (a, c) = 1
d (a, d) = 2
d (b, c) = 2
d (b, d) = 1
d (c, d) = 3
```

```
Valid code word
Minimum Hamming
distance = 1
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

```
Note:
```

1. CRC must be (k-1) bits.
2. If the generator has more than one term and coefficient of x^0 is 1, all single bit error can be detected.
3. If a generator can’t divide xt + 1 (t between 0 and n – 1) then all isolated Double error can be detected.
4. The generator that contains a Factor of x + 1 can detect all odd numbered errors.

**2.4.1 A good polynomial generator needs to have the following characteristics**

1. It should have at least two terms.
2. The coefficient of the term x^0 should be 1.
3. It should not divide xt + 1, for t between 2 and n – 1.
4. It should have the factor x + 1.

**2.5 Hamming Code**

1. Hamming code is used for error correction.
2. Hamming code can correct 1 bit error only.
3. Hamming code can detect upto 2 bit error.
   m = Massege bits
   r = redundant bits or Check bits or parity bits or extra bits
   n = m + r (n = codeword)

According to the hamming code, number of redundant bits

```
mr   12 r
where r = lower limit
```

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

3

**FLOW CONTROL**

**3.1 Delay in Computer Network**

(1) Transmission Delay (Td)
(2) Propagation Delay (Pd)
(3) Queuing Delay (Qd)
(4) Processing Delay (Prd)

**3.2 Transmission Delay**

Amount of time taken to transfer a packet on to the outgoing link is called as Transmission delay.

```
d
```

```
d
```

```
Transmission delay (T ) = Length of packet
Bandwidth
L
T =
B
```

**3.3 Propagation Delay**

Amount of time taken to reach a packet from one (sender) point to another (receiver) point is called as propagation delay.

```
d
```

```
d
```

```
Propagation delay (P ) = distance
velocity
```

```
P = d
v
```

**3. 4 Stop wait Protocol**

**3.4.1 Sender Side Rule**

Rule 1 : Sender can send one data packet at a time.
Rule 2 : Sender can send the next data packet only after receiving the ACK of the previous packet.

**3.4.2 Receiver Side Rule**

Rule 1: Receiver will receive and consume the data packet.
Rule 2 : After consuming the data packet, Ack need to be sent.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**3.5 Efficiency OR Line utilization OR Link utilization OR Sender utilization**

```
Efficiency =Useful time
Total time
d
d d d rd d
```

```
Efficiency = T (frame)
T (frame)+2*P +Q +P +T (ACK)
```

**3.6 Throughput Or Effective Bandwidth Or Bandwidth Utilization Or Maximum Data**

**Rate Possible**

```
Throughput = Length of the Frame
Total time
```

```
d d d rd d
```

```
L
Throughput =
T (frame)+2*P +Q +P +T (ACK)
```

```
OR Throughput*B
```

**3. 7 Sliding Window**

In the sliding window concept instead of sending one packet and wait for the acknowledgement, we send ‘w’ packet and wait
for the Acknowledgement. Where ‘w’ is the sender window size.

**3. 7 .1 GB–N(N>1)**

1. In the GB – N the sender window size is N itself.
2. In the GB-N the receiver window size is equal to one always.

```
Note:
(1) Out of order packet is not received by Receiver.
(2) Timer is maintained only for the first frame (Rightmost) in window because if its timer expires then sender
assume that rest of the frame are also not received by receiver (because out of order delivery is rejected).
```

```
Note:
GB–N uses cumulative Acknowledgement and Acknowledgement number defines the number of the next expected frame.
```

```
Ack timer < Time out timer
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

Window Receiver (WR) size:
In the GB-N the window receiver size is equal to one always irrespective of window sender size (Wr=1).

Window Sender (WS) Size:
Window sender size is calculated based on the following formula:
Ws + WR ≤ Available Sequence Number
Ws + 1 ≤ Available Sequence Number
Ws ≤ Available Sequence Number – 1

**3. 7 .2 Efficiency and Throughput in GBN**

(^) Efficiency = Useful time
Total time
d
d d d rd d
Efficiency = N*T ( )
T ( )+2*P +Q +P +T ( )
frame
frameACk
(^) Throughput =N*Length of Frame
Total time
d d d rd d
Throughput = N*Length of Frame
T (frameACk)+2*P +Q +P +T ( )
OR Throughput*B
**3.8 Selective Repeat ARQ
3.8.1 Selective Repeat/Selective Reject ARQ**
(1) In SR Protocol window sender size is equal to window receiver size (WS = WR).
(2) SR Protocol uses independent acknowledgement, and acknowledgement number defines number of error free packet
received.
(3) SR receiver can receive out of order packet but packets are delivered to upper layer in sorted order.
(4) In SR protocol searching and sorting logic is required. Searching is done by sender and sorting is done by receiver.
(5) Timer is maintained for each and every frame in the window at sender side.
(6) For 1st out of order delivery or if packet received is corrupted then Negative acknowledgment (NACK) for respective
packet is sent by receiver to sender.
(7) When sender receive NACK 3 then it will search in the window for packet 3 & immediately packet 3 is retransmitted even
though its timer is not expired.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**3.8.2 Efficiency and Throughput of SR**

Efficiency =Useful time
Total time

 

```
d
d d d rd d
```

```
Efficiency = Ws × T ( )
T ( )+2*P +Q +P +T
```

```
frame
frameACK
```

Throughput = η B*

(^) Throughput = W * Length of the frames
Total time
   
s
d d d rd d
Throughput = W * Length of the frame
T frameACK+2*P +Q +P +T

**3. 9 Comparison among Stop and Wait, GBN and SR protocols**

```
Stop & wait GBN SR
```

```
Efficiency
```

```
η = Useful time
Total time
or
```

```
η =
```

```
 
T otal time
```

```
Tframed
```

```
η = Useful time
Total time
or
η = N*T (d )
Total time
```

```
frame
```

```
η = Useful time
Total time
or
η = W *T (sd )
Total time
```

```
frame
```

```
Throughput
```

```
Length of frame
Total time
or
η * B
```

```
N*Length of the frame
Total time
or
η * B
```

```
W *Length of the frames
Total time
or
η * B
Buffer 1 + 1 N + 1 N + N
Seq No. 2 N + 1 2N
```

```
Seq. No. = K bit
```

```
K
Ws 2 1
W1R
```

```
1
W2S
 K^
W2R K^1
```

RTT or Total Time = TdframeACK+ 2*P + Td d + P + Qrd d

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

4

**IPV 4 HEADER**

**4.1 IPv4 Header**

```
VER (4 bits) HL (4 bits) Services (8 bits) Total Length (16 bits)
```

```
Identification number (16 bits) Flags (3 bits) Fragment offset ( 13 bits)
```

```
Time to Live (8 bits) Protocol (8 bits) Header checksum (16 bits)
```

```
Source IP Address (32 bits)
Destination IP Address (32 bits)
Option (0-40 bytes)
```

**4.1.1 Version (4 Bit)**

It is used to indicate IPv4 or IPv6.

**4.1.2 Header Length(4 Bit)**

Header length is a 4 bit field that contains the length of header.

Minimum Header size is 20 byte.

Maximum Header size is 60 byte.

**4.2 Services [8 bit]**

In this Interpretation the first 3 bit are called precedence bit (Priority bit) and Next 4 bit are called types of services bits and
last bit is Not used.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**4.2.1 Priority**

It is a 3-bit subfield ranging from 0 to 7 (000 to 111 in binary). Priority field is needed if a router is congested and need to
discard some datagram, those datagrams which have the lowest priority are discarded first.

**4.2.2 Types of Services**

It is a 4 bit subfield. Each bit having a special meaning, although a bit can be 0 or 1. One and only one of the bits can have the
value 1 in each datagram.

**4.3 Total length (1 6 bits)**

Total length = Data + Header

**4.4 Identification Number (16 bits)**

1. Each datagram is associated with a sequence number is called as datagram number or identification number.
2. It is used to identify all the fragment of same datagram.
3. All the fragment of same datagram will have the same identification number.

**4.5 Flags**

It is the 3 bit field shown in the figure.

### X D^

### F

### M

### F

```
Not
Used
```

```
Don’t
Fragment
```

```
More
Fragment
```

**4.6 Fragment offset (13 bits)**

Fragment offset indicate no of data byte ahead of this fragment in that particular packet.

**4.7 TTL (8 bits)**

1. TTL is used to avoid infinite looping.
2. TTL field is used to control the maximum number of hops visited by datagram.
3. When a source host sends a datagram, it stores a number in this field. Each router that process the datagram decrements
   this number by one. If TTL field reaches zero before the datagram arrives at its destination, then the datagram is
   discarded and an ICMP message is sent back to sender.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**4.8 Protocol (8 bits)**

1. This 8 bits field tell us which protocol is encapsulated in the IP packet.
2. At the time of traffic, some packet must be discarded. In this case it will be advantageous to know which protocol data it
   contains.
3. The order in which router eliminate the datagram from buffer is-
   ICMP>IGMP>UDP>TCP
   (01) (02) (17) (06)

**4.9 Header Checksum**

1. It is calculated only for header part not the data because rest of the component in packet already covered by TCP
   checksum.
2. Header checksum is calculated at each and every Router because IP Header might be change when packet is moving
   from one router to another.
3. Every router makes one modification i.e. TTL so Header checksum is calculated at every Router.
4. Fragment offset, MF, Total length, option all may be changed at a Router.

**4.10 Source Address (32 bits)**

This 32 bit defines the IPv4 address of source. This field remain unchanged during the time the IPv4 datagram travel from the
source Host to destination Host.

**4.11 Destination Address (32 bits)**

This 32 bits Field defines the IPv4 address of the destination. This field remain unchanged during the time the IPv4 datagram
travel from source host to destination host.

**4.12 Option**

The Header of IPv4 data gram is made of two parts a fixed part and a variable part. The fixed part is 20 bytes long and
variable part that can be maximum of 40 bytes.

There are 5 options

1. Strict source Routing
2. Loose source Routing
3. Record Routing
4. Time stamp
5. Padding

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**4.12.1 Strict Source Routing**

A strict source routing is used by the source to predetermine a route for data gram as it travel through the internet.

**4.12.2 Loose Source Routing**

A loose source route option is similar to strict source route but it is less rigid. Each router in the list must visited, but the data
gram can visit other router as well.



**4.12.3 Record Routing**

A record route option is used to record the internet routers that handle the data gram. It can list up to 9 router Address.
All the Router are supposed to record their IP Address on their IP packets.

Note:
First 16 bits (2 byte) are reserved for option type (8 bit) and length (8 bit). Out of 40 bytes only 38 bytes are remaining
for storing IPv4 addresses. In 38 bytes we can store 9 IPv4 addresses as each IPv4 address is of 4 byte

```

```

**4.12.4 Time Stamp**

It is used to find out delays at each router. Every router should record incoming time and outgoing time.







**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

5

**TCP & UDP**

**5.1 Introduction**

Transport Layer can be connection oriented or connection less.

1. TCP is reliable process to process delivery of entire message.
2. TCP is a connection oriented.
3. TCP connection are full duplex and point to point.
4. TCP connection has 3 phases

```
i. Connection establishment
ii. Data transfer
iii. Connection termination
```

5. Each TCP connection is identified uniquely by Source Port + Destination Port + Source IP + Destination IP.
6. Each TCP connection is associated with Four window.
7. TCP uses three way “Handshake” to establish TCP connection.
8. TCP is not useful for Broadcasting and Multicasting.
9. TCP Header size is 20 bytes but if option (40 bytes) is added it will become 60 bytes.
10. TCP provide end to end error control and flow control.
11. Data will be received at the destination in order.
12. Data may arrive out of order and be temporarily stored by receiving TCP, but TCP guarantee that no out of order data

```
delivered to the process.
```

```
GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK
```

```
Computer Networks
```

**5.2 TCP header**

```
Source Port (16 bits) Destination Port (16 bits )
Sequence number (32 bits)
Acknowledgement number (32 bits)
Header Length
(4 bits)
```

```
Reserved bits
(6 bits)
```

### U

### R

### B

### A

### C

### K

### P

### S

### H

### R

### S

### T

### S

### Y

### N

### F

### I

### N

```
Window Size (Advertisement Window) (16 bits)
```

```
Check sum (16 bits) Urgent Pointer (16 bits)
Options
(0 - 40 bytes)
```

```
Port Number Name
0 – 1023 Well known port No.
1024 – 49151 Registered Port No.
49152 – 65535 Dynamic Port No.
```

```
Wrap Around time (WAT) =
 
```

```
Total sequence No.
Bandwidth Bytes / Sec
 Minimum sequence number required to Avoid wrap Around time with in Life time = B × LT
 Minimum number of bits required to Avoid wrap Around time with in LT = ⌈log 2 B * LT⌉
```

```
SYN = 1 → Consume one sequence number.
Ack = 1 → Consume zero sequence number.
FIN = 1 → Consume one sequence number.
1 Data byte → Consume one sequence number.
SYN Ack Meaning
1 0 request
1 1 reply
0 1 Ack
0 0 Data
```

```
Time out timer in TCP
```

Basic Algorithm **Jacobson’s Algorithm**
Time Out Timer = 2 * RTT
Next Round Trip Time (NRTT) = **α** (IRTT) + (1 – **α** )ARTT

0 ≤ **α** ≤ 1

```
Time Out Timer = 4 * ID + RTT
Next Round Trip Time (NRTT) = α (IRTT) + (1 – α ) ARTT
```

```
0 ≤ α ≤ 1
```

```
Actual Deviation (AD) = |IRTT – ARTT|
```

```
Next Deviation (ND) = α (ID) + (1 – α ) AD
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**5. 3 Congestion Control**

1. Ws = min (Wc, WR)

```
Slow start Congestion Avoidance Congestion Detection
```

1. If ACK Arrives
   Wc = Wc + 1
   1. IF ACK Arrives
      Wc = Wc +
      c

```
1
W
```

1. Time out
2. After one RTT
   Wc = 2 * WC
3. After one RTT
   Wc = Wc + 1
4. 3 duplicate ACK
   **5. 4 Token Bucket**

- Token bucket algorithm allows ideal hosts to accumulate credit for the future in the form of tokens.
- In regular interval, tokens are thrown into the bucket.
- Bucket has a maximum capacity.
- If there is a ready packet a token is removed from bucket and packet is sent.
- If there is no token in the bucket, the packet cannot be sent.

Let the capacity of token bucket is ‘C’ token and token enter into the bucket at rate of ‘r’ tokens per second.
The maximum number of packet that can be enter into the network during the time interval ‘t’ is

 

```
M aximum number of packet = C + rt
M aximum average rate for token bucket M = C + rt
t
M t = C + rt
Mt – rt = C
M – r t = C
```

```
t = C
M – r
```

C → token Bucket capacity
r → Token Arrival rate

**5.5 UDP**

1. UDP is message oriented connection less Datagram protocol.
2. It is unreliable Transport protocol.
3. It does not provide Flow control and Error control & congestion control.
4. It does not add anything to the services except process to process delivery of data.
5. Header is simple and fixed in size i.e. 8 byte.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

```
Note:
Unlike TCP, the checksum calculation is not mandatory in UDP. No error control or flow control is provided by UDP.
Hence UDP depends on IP and ICMP for error reporting.
```

**5. 5 .1 Optional inclusion of checksum**

The sender of UDP packet can choose not to calculate the checksum. In this case the checksum field is filled with all 0's
before being sent.

**5. 5 .2 Need of UDP**

[1] The application that required one request one reply. TCP is not suitable hence we use UDP.
[2] Application that required constant dataflow TCP is not suitable hence we use UDP.
[3] Application that required multimedia data transfer we cannot use TCP hence we use UDP.
[4] Application that required fastness and then reliability TCP is not suitable hence we use UDP.
[5] UDP used for management process such as SNMP (simple network management protocol).
[6] UDP is used for some route updating protocol such as RIP.
[7] For broadcasting & multicasting application TCP is no suitable hence we use UDP.
[8] UDP is normally used for interactive real time applications.
[9] UDP is suitable for a process with internal flow and error control mechanisms. For example, the Trivial File Transfer
protocol(TFTP) process include flow and error control. It can easily use UDP

### TCP UDP

```
Connection-oriented Connectionless
```

```
Reliability in delivery of message Not reliable
```

```
Sequence Number. No sequence number.
```

```
ACK number. No ACK number.
```

```
Overhead is high(Header size 20-60 Bytes) overhead is less(Header size = 8 Bytes)
```

```
Keep track of order (sequence) No order
```

```
Protocols: HTTP, FTP, SMTP, POP Protocol: DNS, SNMP, TFTP, DHCPtime protocol , All real
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

6

**MEDIUM ACESS**

**CONTROL[MAC]**

**6.1 Aloha**

Aloha was developed at university of Hawaii in 1970’s.
It was designed for wireless LAN but it can be used in any shared medium.
Each station sends equal size frame.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**6.2 CSMA (Carrier Sense multiple access)**

CSMA requires that each station, first sense the carrier before transmitting the data.
Vulnerable time for CSMA = Propagation time.

**6.3 Persistence methods in CSSMA**

Persistent
Non-persistent
P-persistent

**6.4 CSMA/CD (Carrier Sense multiple access/Collision Detection)**

1. Minimum size of frame to detect the collision in Ethernet (CSMA/CD)
   Td ≥ 2 * Pd + Td(Jam signal)
2. Backoff Algorithm
   Waiting time = K * Slot duration
   = K * RTT
   = K * 2 * Pd

K is any random number in between 0 to 2n -1.
n is collision number (Collision number is respect to data packet).

3. Efficiency in Ethernet (CSMA/CD)

1
1 6.44a

### 

### 

```
or η = usefulTotal timetime = Collision timeTd +Td+Pd
```

4. P(1–P)N –^1 → Probability of success for single station( Throughput of Host)

```
Pure Aloha Slotted Aloha
```

```
Any station transmits the data at any time. Any station can transmit the data at the beginning of any
time slot.
Vulnerable time in which collision may occur
= 2 * Tf ( Tf - Transmission time for single frame)
```

```
Vulnerable time in which collision may occur = Tf
```

```
Throughput of pure aloha = G * e-2G Throughput of slotted Aloha = G * e-G
```

```
Maximum throughput smax = 18.4 % (When G =
1/2)
```

```
Maximum throughput smax = 36.8 % (When G = 1)
```

```
The main advantage of pure aloha is it simplicity
in implementation
```

```
The main advantage of slotted aloha is that it reduces the
number of collisions to Half and double the throughput of
pure aloha
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

NP(1 – P)N–^1 → Probability of success for any station among all stations [Throughput of channel]

5. Ethernet Frame Structure:

```
Preamble SFD DA SA Length
Of Data
```

```
Data CRC
```

### 7B 1B 6B 6B 2B (46B – 1500B) 4B

### PL DLL DLL

Ethernet uses Manchester encoding technique for converting data bits into signal.
(Baud rate = 2 * bit rate)
Bit rate = 1/2 baud rate

### 

###  

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

7

**ROUTING ALGORITHMS,**

**SWITCHING & IP SUPPORT**

**PROTOCOL**

**7.1 Switching**

```
Circuit Switching Packet switching
```

```
(I) It has three phases-connection establishment,
Data transfer and Connection termination.
```

```
It has only one phase-Data transfer
```

```
(2) Physical path between source and destination No physical path
```

```
(3) All packets use same path Packet may follow different path (travel independently)
```

```
(4) Reserves the entire bandwidth in advance Does not reserve
```

```
(5) Bandwidth wastage No Bandwidth wastage
```

```
(6) No store and forward transmission Supports store and forward transmission
```

```
(7) Congestion can happen during connection
establishment phase
```

```
Congestion can happen during data transfer phase
```

```
Switching
```

```
Circuit Switching Packet Switching^
```

```
Virtual Circuit
Switching
```

```
Datagram
Switching
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

```
(8) It is reliable Not reliable
```

```
(9) Better for sending large messages Better for sending small messages
```

```
(10) Not fault tolerant technique Fault tolerant technique
```

```
(11) Circuit switching is implemented at physical layer. Packet switching is implemented at network layer
```

```
Total time= Setup time + Td + Pd + Tear down time
```

```
TT=S + Ld+X. +T
BV
```

```
For X Hop and N packet
Total time= X [T + P ] + X –1[P + Q ] + N – 1(T )d d rd d d
```

**7.2 Generalized Formula for optimal packet size(P)**

M = Message size
ℎ = Header size
p = Payload/Packet data size
No. of Hops = X

p =√𝑋𝑀−ℎ 1

So optimum packet size P = p + h

```
Datagram Switching Virtual circuit switching
```

```
(1) It is a connection less service. It is connection-oriented service.
```

```
(2) All the packets may follow different path. All the packet follows the same dedicated path.
```

```
(3) Data may appear out of order at the
destination since the packets may follow
different paths.
```

```
Data appears in order at the destination since all the
packets take the same dedicated path.
```

```
(4) It is not reliable since packets may be
discarded.
```

```
It is highly reliable.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**7.3 Routing Algorithm**

```
Distance vector Routing Link state Routing
```

1. 1980’s 1. 1990’s
2. Bandwidth required is very less because we sent
   only distance vector packet.
   2. Band width required is high because we sent
   entire link state packet
3. Local knowledge 3. Global knowledge
4. Bellman Ford algorithm 4. Dijkstra algorithm
5. Traffic is very less 5. Traffic is very high

```
(5) Cheap Costly
```

```
(6) No resource reservation is done. First packet reservebuffer) for the subsequent packets.s^ the resources (CPU, bandwidth and
```

```
(7) All the packets require a global header
which contains full information about the
destination.
```

```
Only first packet requires a global header which identifies
the path from one end to another end. All the following
packets require a local header which identifies the path
from hop to hop.
(8) The packets may be discarded at
intermediate switches if sufficient resources
are not available to process the packets.
```

```
The packets are never discarded at intermediate switches
and immediately forwarded since resources are reserved
for them.
```

```
(9) IP Networks uses datagram switching.
```

```
ATM (Asynchronous Transfer Mode) uses virtual circuit
switching.
```

```
(10) Datagram switching is normally
implemented at network layer.
```

```
Virtual circuit switching is normally implemented at data
link layer.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

6. Convergence is very low 6. Convergence is faster
7. Count to infinity Problem 7. No problem of count to infinity
8. Persistent Loops 8. Transient Loops

### 9. RIP 9. OSPF

The maximum Hop count allowed For RIP is 15 and Hop count of 16 is considered as Destination unreachable.

```
Note:
RIP uses UDP as its transport protocol with the port number – 530
```

**7.4 IP Support Protocol**

**7.4.1 ARP**

1. Address Resolution Protocol(ARP) is used to find the MAC(Media Access Control) address of a device from its IP address.
2. ARP request: ARP request is broadcasting
3. ARP response/reply: ARP reply is unicasting.
   **7. 4 .2 Internet Control Message Protocol (ICMP)**

```
ICMP messages
```

```
Error-reporting or
Feedback Message
```

```
Query or request and Reply
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**7.4.3 Internet Control Message Protocol (ICMP)**

**7.4.4 Internet Control Message Protocol (ICMP)**

### 

```
Feedback messages or Error Reporting
```

Destination Source quench (^) Time exceeded
unreachable
Parameter
problems
Redirection
Query or Request and reply
Timestamp request and reply Address-mask
request and reply
Echo request and reply
Router solicitation
and advertisement

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

8

**APPLICATION LAYER**

**PROTOCOL**

**8. 1 E-MAlL**

SMTP transfer the mail from sender’s mail server to receiver’s mail server.
While sending the mail ,SMTP is used two times-.
(i) Between the sender and sender’s mail server
(ii) Between the sender’s mail server and receiver’s mail server

**8.1.1 To receive or download the email,**

Another protocol is needed between the receiver mail server and receiver.
The most commonly used protocols are POP3 and IMAP4.

**8.1.2 SMTP(Simple mail transfer protocol)**

1. The objective of SMTP is to transfer the email reliably and efficiently.
2. It uses port number-25 at TCP.
3. In SMTP there are two components:

```
(i) User Agent (UA)
(ii) Mail transfer Agent (MTA)
```

4. User Agent prepares the message, creates the envelope and put the message in the envelope.
5. Mail transfer Agent transfer the mail across the internet i.e. Actual mail transfer is done through MTA.
6. To send mail, system must have a client MTA and to receive the mail. it must have a server MTA.

```
SMTP
```

```
(Gmail) (Yahoo)
```

```
Internet
```

```
SMTP Sender Mail
Server
```

```
(Push)
Receiver Mail
Server
```

```
Sender
```

```
(Pu
```

```
ll) PoP-3
or
IMAP-4
```

```
Receiver
```

```
Email [Electronic Mail]
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

7. SMTP is text based protocol.
8. With the help of SMTP & POP we can send only text messages.
9. SMTP can only handle the message containing 7 bit ASCII text.
10. SMTP cannot transfer other types of data like images, video, audio, etc.
11. SMTP cannot transfer binary files or executable files.
12. SMTP cannot transfer the text data for the language other than English (such as French, Japanese, and Chinese etc.).
13. Only SMTP is not sufficient to send binary files or to send videos or audio so we require MIME (Multipurpose Internet

```
mail extension).
```

14. MIME is a supplementary protocol that allows non-ASCII data to send through SMTP.
15. MIME is a set of software function that transforms non-ASCII data to ASCII data or viceversa.
16. MIME is used to convert non text data to text data and text data to non text data.
17. SMTP is stateless protocol. It does not maintain any information of user. If an e-mail is asked to be sent twice, then server

```
resends it without saying that e-mail has already been sent.
```

18. SMTP is a connection-oriented protocol.
19. SMTP uses persistent TCP connections, so it can send multiple e-mail at once.
20. SMTP is an “In-Band” protocol.
21. SMTP is used for Push the e-mail.
22. SMTP Pushes the mail from client to server on other hand, It needs a pull protocol(Download).
23. POP3 and IMAP4 are used for Pulling the e-mail.

**8.2 POP3( Post office Protocol version-3)**

1. It is a message access protocol.
2. It is a pull protocol.
3. POP 3 uses port number-110 at TCP.
4. POP 3 is a connection-oriented protocol.
5. POP 3 uses persistent TCP connection.
6. POP 3 is a stateful protocol.
7. POP3 is an “In-Band” protocol.
8. POP3 does not allow users to partially check the content of the mail before downloading.
9. POP3 does not allow user to organize the mail on the mail server.

**8.2.1 IMAP-4(Internet Mail Access Protocol version-4)**

1. IMAP-4 is similar to POP3 but it has more features. IMAP-4 is more powerful and more complex.
2. IMAP-4 provides the following extra functions.
3. A user checks the email header prior to downloading.
4. A user can search the content of the email for a specific string of characters prior to downloading.
5. A user can partially download the email.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

6. A user can create, delete, or rename the mail box on the mail server.
7. A user can create a hierarchy of mailbox in a folder for email storage.

**8.2. 2 Characteristics of IMAP**

1. IMAP is a pull protocol.
2. IMAP uses port number-143 at TCP.
3. IMAP is a connection-oriented protocol.
4. IMAP uses persistent TCP connection.
5. IMAP is a tasteful protocol.
6. IMAP is an “In-Band” Protocol.
   POP 3 IMAP
   (1) Mails can only be accessed from a single device. Mails can be accessed from multiple device.
   (2) Download the email from server to a single computer
   and the copy at the server is deleted.

```
The email message is stored on the mail server itself.
```

```
(3) User cannot organize the mails in the mail box of the
mail server.
```

```
User can organize mails on the mail server.
```

```
(4) It does not allow user to sync emails. It allows user to sync their emails.
(5) It is unidirectional i.e all the changes made on a device
does not effect the content present on the server.
```

```
It is bidirectional i.e all the chances made on server or
device are made on the other side too.
```

**8.3 File Transfer protocol (FTP)**

**8.3.1 FTP (File Transfer Protocol)**

1. File transfer protocol is a standard internet protocol for transferring files b/w computers over TCP/IP connection.
2. It uses port number - 20 & 21 on TCP.
3. It has two types of connection
   (i) Control connection (port number. - 21)
   (ii) Data connection (port number - 20)
4. Control connection remains connected during the entire interactive FTP session.
5. The data connection is opened and closed for each file transfer activity.
6. When user starts an FTP session, the control connection opens. While the control connection is open, the data connection
   can be opened and closed multiple times if several files are transferred.
7. FTP uses persistent TCP connections for control information.
8. FTP uses Non-persistent TCP connections for data information.
9. FTP is a connection-oriented protocol.
10. FTP is an “out of band” protocol as data and control information flow over different connection.
11. Some protocols send their request and data in the same TCP connection for this reason they are called as In-bound protocol.
12. HTTP & SMTP are In-Band protocol.
13. FTP is state full protocol.

**8.3.2 Transmission mode**

FTP can transfer a file across the data connection using one of the following three transmission modes.
(i) Stream mode
(ii) Block mode
(ii) Compressed mode

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**8.3.3 File Type**

FTP can transfer one of the following file types across the data connection:
(i) ASCII file
(ii) EBCDIC file (File format used by IBM)
(ii) Image file

**8.3.4 Data structure**

FTP can transfer a file across the data connection using one of the following interpretation of the structure of the data:
(i) File structure
(ii) Record structure
(iii) Page structure

**8.4 HTTP Protocol**

1. HTTP protocol is used mainly to access data on world wide web (www).
2. It is client server protocol using port number - 80 on TCP.
3. HTTP is “In-Band” protocol i.e. both request and data we will send only in one connection.
4. HTTP is a stateless protocol i.e. It does not maintain any information of user.
5. There are two types of HTTP protocol
   (i) Non persistent (1.0)
   (ii) Persistent (1.1)

**8.5 Non Persistent (1.0)**

| In a Non persistent connection one TCP connection is ade for each request/response. This strategy follow the following steps           |
| :------------------------------------------------------------------------------------------------------------------------------------- |
| (i) The client opens a TCP connection and sends a request.                                                                             |
| (ii) Server sends the response and closes the connection.                                                                              |
| (iii) In this strategy , If a file contains link to N-different pictures in different files(all located on same server) the connection |
| must be opened and closed N+1 times.                                                                                                   |

**8.6 Persistent (1.1)**

1. In a persistent connection the server leaves the connection open for more request after sending a response.
2. The server closes the connection at the request of client or time out has been reached.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**8.6.1 Important Table**

```
SHORT TRICK DNS HTTP SMTP POP IMAP FTP
Stateful/
Stateless
```

```
Stateless Stateless Stateless Stateful Stateful Stateful
```

```
Transport Protocol
Used UDP^ TCP^ TCP^ TCP^ TCP^ TCP^
Connectionless/
Connection
oriented
```

```
Connection
less
```

```
Connection
less
```

```
Connection
oriented
```

```
Connection
oriented
```

```
Connection
oriented
```

```
Connection
oriented
```

```
Persistent/Non-
persistent
```

```
Non-
persistent
```

```
HTTP 1.0 is
non persistent
HTTP 1.1 is
persistent.
```

```
Persistent Persistent Persistent
```

```
Control
connection is
persistent.
Data
connection is
non-
persistent.
```

```
Push/Pull - - Push Pull Pull Can’t
```

```
Port Number Used 53 80 25 110 143
```

```
20 for data
connection.
21 for control
connection.
In band/
Out-of-band In band^ In band^ In band^ In band^ In band^ Out-of-^ band^
```

```
Application Port Number. Transport Protocol
DNS 53 UDP
HTTP 80 TCP
FTP 20 (Data connection)^
21(Control connection)
```

### TCP

### SMTP 25 TCP

### POP 110 TCP

### SNMP 161, 162 UDP

### TFTP 69 UDP

### IMAP 143 TCP

```
Telnet 23 TCP
DHCP 67 (DHCP Server)^
68 (DHCP Client)
```

### UDP

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**8. 6 .2 Commands**

```
HTTP FTP SMTP
GET USER HELO
HEAD PASS MAIL FROM
PUT ACCT RCPT TO
POST CWD DATA
TRACE REIN QUIT
DELETE QUIT RSET
CONNECT PORT* VRFY
OPTIONS PASV NOOP
TYPE TURN
MODE EXPN
PROMPT HELP
STRU SEND FROM
SMOL FROM
SMAL FROM
```

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

9

**OSI AND TCP/IP PROTOCOL**

**STACK**

**9.1 Functions of Computer Network**

         

**9.2 OSI/ISO**

OSI : Open systems Interconnection model.
ISO : International Standards Organization. It is a multinational body dedicated to worldwide agreement on international
standard.

**9.2.1 OSI Mode**

- This model has been proposed by ISO.
- An open system is a set of protocols that allows any two different systems to communicate regardless of their underlying
  architecture (Hardware/Software).
- The purpose is to show how to facilitate communication between different systems without requiring changes to the
  logic of the underlying hardware & software.
- This model has got 7 separate but related layers.
  
  **9. 3 Functions of Physical layer

9. 3 .1 Physical Layer**

Physical Layer is responsible for movement of individuals bits from one Hop to next Hop.

```
 Error control
 Flow control
 Access control
 Multiplexing and Demultiplexing
:
:
```

```
 Encryption & Decryption
 Check pointing
 Routing
:
:
```

Functions

Mandatory Optional^

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**9.3.2 Functions of physical Layer**

1. It is used to define electrical, mechanical, functional and procedural characteristic of physical link.
   (physical Link)
   Copper → Electrical signal
   Fiber → Light signal
   Wireless comm. → Electromagnetic signal.
2. It defines transmission mode:
   a. Simplex
   b. Half duplex
   c. Full duplex
3. It defines topology configuration:
   - Bus topology
   - Star topology
   - Mesh Topology
   - Tree Topology
4. It is totally Hardware layer.
5. It defines link configuration:
   i Point to Point Link
   ii Broadcast Link
6. It defines Encoding.
7. Bits Synchronization.
8. Bit rate control.
   
   **9. 4 Data Link Layer**

Data link layer is responsible for moving frames From One Hop (Node) to Next Hop (Node).

**9. 4 .1 Function of data link layer**

1. Flow control
2. Error control
3. Access control
4. Framing
5. Physical Addressing

Data Link Layer is divided into two parts


### 

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**9. 5 Network Layer**

The network layer is responsible for the delivery of individual packet from source to destination.

**9. 5 .1 Function of Network Layer**

1. Host to Host connectively
2. Logical Addressing
3. Switching
4. Routing
5. Fragmentation
6. Congestion control:
   **9. 6 Transport Layer**

Transport Layer is responsible for process to process delivery. A process is an application program running on a host.

**9.6.1 Function of Transport Layer**

1. End to end connectively
2. Service point Addressing
3. Flow control
4. Error control
5. Segmentation and Reassembly
6. Congestion control
7. Connection Control
8. Multiplexing and Demultiplexing.
   **9. 7 Session Layer**

Session layer also known as network dialog controller. It establishes, maintains, synchronizes and terminates the interaction
b/w sender and receiver.

**9.7.1 Function of Session Layer**

1. Authentication & Authorization
2. Check point or synchronization
3. Dialog control

**9.8 Presentation Layer**

This layer take care of syntax and semantics of the information exchange in between two communicating systems.

**9. 8 .1 Function of Presentation Layer**

1. Character translation
2. Encryption/Decryption
3. Compression

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Computer Networks
```

**9. 9 Application Layer**

Application Layer is responsible for providing services to users. Users such as:

1. Mail services
2. File sharing
3. File transfer and many more
   **9. 10 TCP/IP Model**

This mode has got 5 different layer

Physical : No specific protocol

Data Link : No specific protocol

Network : ARP, RARP, ICMP, IGMP

Transport : TCP, UDP,SCTP

Application : DNS, SMTP, HTTP, FTP, POP,IMAP, SNMP , Telnet etc.
















**GENERAL**

**APTITUDE**

**GENERAL**

**APTITUDE**

```
Design Against Static Load
```

1. Percentages ..................................................................................................................... 12. 1 – 12. 5
2. Averages & Ages .............................................................................................................. 12. 6
3. Profit & Loss .................................................................................................................... 12. 7 – 12. 9
4. Ratio and Proportions ...................................................................................................... 12. 10
5. Time and Distance ........................................................................................................... 12. 11 – 12. 12
6. Time and Work ................................................................................................................ 12. 13 – 12. 14
7. Clocks ............................................................................................................................... 12. 15 – 12. 16
8. Calendars ......................................................................................................................... 12. 17 – 12. 19
9. Blood Relations ............................................................................................................... 12. 20
10. Directions ........................................................................................................................ 12. 21 – 12. 22
11. Data Interpretation .......................................................................................................... 12. 23 – 12. 24
12. Data Sufficiency .............................................................................................................. 12. 25

**INDEX**

GATE-O-PEDIA COMPUTER SCIENCE & INFORMATION TECHNOLOGY

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
Design Against Static Load
```

1

**PERCENTAGES**

**1.1. Understanding Percentages**

The word percent can be understood as follows:

```
Per cent  for every 100.
```

So, when percentage is calculated for any value, it means that that you calculate the value for every 100 of the reference
value.

Why Percentage?

Percentage is a concept evolved so that there can be a uniform platform for comparison of various things. (Since each value is
taken to a common platform of 100.)

Example:

- To compare three different students depending on the marks they scored we cannot directly compare their marks until
  we know the maximum marks for which they took the test. But by calculating percentages they can directly be
  compared with one another.
- Before going deeper into the concept of percentage, let u have a look at some basics and tips for faster calculations:

**1.2. Calculation of Percentage**

```
Percentage Value 100
Total value
```

```

^
```

Example: 50 is what % of 200?

Solution: Percentage^50100 25%
200

```
 
.^
```

**1.2.1. Calculation of Value:**

```
Percentage
Value total value
100
```

```

^
```

Example: What is 20% of 200?

Solution: Value^20200
100

```

^
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

Note: Percentage is denoted by “%”, which means “/100”.

Example: What is the decimal notation for 35%?

Solution: (^) 35%^35 0.35
100

### .^

For faster calculations we can convert the percentages or decimal equivalents into their respective fraction notations.

**1.3. Percentages – Fractions Conversions:**

The following is a table showing the conversions of percentages and decimals into fractions:

```
Percentage Decimal Fraction
10% 0.1 1
10
12.5% 0.125 1
8
16.66% 0.1666 1
6
20% 0.2 1
5
25% 0.25 1
4
30% 0.3 3
10
33.33% 0.3333
```

```
1
3
40% 0.4 2
5
50% 0.5 1
2
60% 0.6 3
5
62.5% 0.625 5
8
66.66% 0.6666 2
3
```

```
Similarly we can go for converting decimals more than 1 from the knowledge of the above cited conversions as follows:
```

We know that 12.5% 0.125 1
8

### ^

Then,

8 1  (^19)
1.125
88
 
 (i.e., the denominator will add to numerator once, denominator remaining the same.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

Also,

8 2  (^117)
2.125
88



 (here the denominator is added to numerator twice)
8 3  (^125)
3.125
88



 and so on.
Thus we can derive the fractions for decimals more than 1 by using those les than 1.
We will see how use of fractions will reduce the time for calculations:
Example: What is 62.5% of 320?
Solution: Value 55 320 since 62.5% 200
88
    






### .

**1.4. Percentage Change**

A change can be of two types – an increase or a decrease.

When a value is changed from initial value to a final value,

```
% change = (Difference between initial and final value/initial value) × 100
```

Example: If 20 changes to 40, what is the % increase?

Solution:  

```
40 20
% 100 100%
20
```

```

increase   .
```

```
Note:
```

1. If a value is doubled the percentage increase is 100.
2. If a value is tripled, the percentage change is 200 and so on.

**1.5. Percentage Difference**

```
% Difference = (Difference between values/value compared with) × 100.
```

Example: By what percent is 40 more than 30?

Solution: % difference =  

```
40 30
100 33.33%
30
```

```


```

(Here 40 is compared with 30. So 30 is taken as denominator)

Example: By what % is 60 more than 30?

Solution: % difference =  

```
60 30
100 100%
30
```

```

.
```

(Here is 60 is compared with 30.)

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

Hint: To calculate percentage difference the value that occurs after the word “than” in the question can directly be used as the
denominator in the formula.

**1.6. Important Points to Note**

1. When any value increases by

```
(a) 10%, it becomes 1.1 times of itself. (since 100+10 = 110% = 1.1)
```

(b) 20%, it becomes 1.2 times of itself.

(c) 36%, it becomes 1.36 times of itself.

(d) 4%, it becomes 1.04 times of itself.

Thus we can see the effects on the values due to various percentage increases.

2. When any value decreases by

```
(a) 10%, it becomes 0.9 times of itself. (Since 100 – 10 = 90% = 0.9)
```

(b) 20%, it becomes 0.8 times of itself

(c) 36%, it becomes 0.64 times of itself

(d) 4%, it becomes 0.96 times of itself.

Thus we can see the effects on a value due to various percentage decreases.

```
Note:
```

1. When a value is multiplied by a decimal more than 1 it will be increased and when multiplied by less than 1 it
   will be decreased.
2. The percentage increase or decrease depends on the decimal multiplied.

```
Example: 0.7  30% decrease, 0.67  33% decrease, 0. 956  4.4% decrease and so on.
```

```
Example: When the actual value is x, find the value when it is 30% decreased.
```

```
Solution: 30% decrease  0.7 x.
```

```
Example: A value after an increase of 20% became 600. What is the value?
```

```
Solution: 1.2x = 600 (since 20% increase)
```

```
 x = 500.
```

```
Example: If 600 is decrease by 20%, what is the new value?
```

```
Solution: New value = 0.8 × 600 = 480. (Since 20% decrease)
```

```
Thus depending on the decimal we can decide the % change and vice versa.
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

```
Example: When a value is increased by 20%, by what percent should it be reduced to get the actual value?
```

```
Solution: (It is equivalent to 1.2 reduced to 1 and we can use % decrease formula)
```

% decrease =  

```
1.2 – 1
100 16.66%
1.2
```

### .

3. When a value is subjected multiple changes, the overall effect of all the changes can be obtained by multiplying all the

```
individual factors of the changes.
```

```
Example: The population of a town increased by 10%, 20% and then decreased by 30%. The new population is what
% of the original?
```

```
Solution: The overall effect = 1.1 × 1.2 × 0.7 (Since 10%, 20% increase and 30% decrease)
```

```
= 0.924 = 92.4%.
```

```
Example: Two successive discounts of 10% and 20% are equal to a single discount of ___
```

```
Solution: Discount is same as decrease of price.
```

```
So, decrease = 0.9 × 0.8 = 0.72  28% decrease (Since only 72% is remaining).
```

```

```

 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

2

**AVERAGES & AGES**

**2.1. What is Average?**

The concept of average is equal distribution of the overall value among all the things or persons present there. So the formula

for finding the average is as follows:

Average, Total of all things,
Number of things,

```
A T
N
```

### 

Therefore, Total, T = AN

If any person joins a group with more value than the average of the group then the overall average increases. This is because

the value in excess than the average will also be distributed equally among all the members.

Similarly when any value less than the average joins the group the overall group decreases as the deficit is divided equally

among all the people present there.

Example:

Consider three people A, B and C with total of Rs. 30/-. Their average becomes Rs. 10/- for each. If another person D joins

them with Rs. 50/- then he has Rs. 40/- more than actual average of Rs. 10/-.

So this Rs. 40/- will get distributed among those four and each gets Rs. 10/-. Thus the average becomes Rs. 20/- each.

Example:

The average age of a class of 30 students is 12. If the teacher is also included the average becomes 13 years. Find the teacher’s

age.

Solution:

- When the teacher is included there are totally 31 members in the class and the average is increased by 1 year. This
  means that everyone got 1 extra year after distributing the extra years of the teacher.
- So extra years of the teacher are as follow: 31 × 1 = 31 years.
- Age of the teacher = actual avg + extra years = 12 + 31 = 43 years.
  

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

3

**PROFIT AND LOSS**

**3.1. What is Profit?**

When a person does a business transaction and gets more than what he had invested, then he is said to have profit. The profit

he gets will be equal to the additional money he gets other than his investment.

So profit can be understood as the extra money one gets other than what he had invested.

Example: A person bought an article for Rs. 100 and sold it for Rs. 120. Then he got Rs. 20 extra and so his profit is Rs. 20.

**3.2. What is Loss?**

When a person gets an amount less than what he had invested, then he is said to have a loss. The loss will be equal to the deficit
he got than the investment.

Example: A person bought an article at Rs. 100 and sold it for Rs. 90. Then he got a deficit of Rs. 10 and so his loss is Rs. 10.

**3.3. Cost Price (CP)**

- The money that the trader puts in his business is called Cost Price. The price at which the articles are bought is called
  Cost Price.
- In other words, Cost Price is nothing but the investment in the business.
  **3. 4 Selling Price (SP)**
- The price at which the articles are sold is called the Selling Price. The money that the trader gets from the business is
  called Selling Price.
- In other words, Selling Price is nothing but the returns from a business.
  **3. 5. Marked/Market/List Price (MP):**
- The price that a trader marks or lists his articles to is called the Marked Price.
- This is the only price known to the customer.
  **3. 6. Discount**

The waiver of cost from the Marked Price that the trader allows a customer is called Discount.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

```
Note:
```

1. Profit or loss percentage is to be applied always to the Cost Price only.
2. Discount percentage is to be applied always to the Marked Price only.
   **3. 7. Relationship Among CP, SP and MP:**

A trader adds his profit to the investment and sells it at that increased price.
Also he allows a discount on Marked Price and sells at the discounted price.
So, we can say that,

- SP = CP + Profit. (CP applied with profit is SP)
- SP = MP – Discount. (MP applied with discount is SP)
  **3. 8. Understanding Profit and Loss:**

So, by now we came to know that if CP is increased and sold it would result in profit and vice versa.

Also whatever increase is applied to CP, that increase itself is the profit.

For Rs. 10 profit, CP is to be increased by RS. 10 and the increased price becomes SP.

For 10% profit, CP is to be increased by 10% and it is the SP.

(From previous chapter we know that any value increased by 10% becomes 1.1 times.)

So, for 10% profit, CP increased by 10%  1.1CP = SP.

- SP = 1.1CPSP
  CP

```
= 1.1  10% profit
```

### • SP = 1.07CPSP

```
CP
```

```
= 1.07  7% profit
```

### • SP = 1.545CPSP

```
CP
```

```
= 1.545  54.5% profit and so on.
```

Similarly,

- SP = 0.9CPSP
  CP

```
= 0.9  10% loss (Since 10% decrease)
```

### • SP =0.7CPSP

```
CP
```

```
= 0.76  24% loss and so on.
```

So, to calculate profit % or loss %, it is enough for us to find the ratio of SP to CP.

```
Note:
```

1. If SP/CP > 1, it indicates profit.
2. If SP/CP < 1, it indicates loss.
   **3. 9. Multiple Profits or Losses**

A trader may sometimes have multiple profits or losses simultaneously. This is equivalent to having multiple changes and so
all individual changes are to be multiplied to get the overall effect.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

Examples: A trader uses a 800gm weight instead of 1 kg. Find his profit %.

Solution: (He is buying 800 gm but selling 1000 gm.

So, CP is for 800 gm and SP is for 1000 gm.)

1000 1.25 25%
800

```
SP  
CP
```

```
profit.
```

Examples: A trader uses 1 kg weight for 800 gm and increases the price by 20%. Find his profit/loss %.

Solution: 1 kg weight for 800 gm  loss (decrease)  800/1000 = 0.8

20% increase in price  profit (increase)  1.2

So, net effect = (0.8) × (1.2) = 0.96  4% loss.

Examples: A milk vendor mixes water to milk such that he gains 25%. Find the percentage of water in the mixture.

Solution: To gain 25%, the volume has to be increased by 25%.

So, for 1 lt of milk, 0.25 lt of water is added  total volume = 1.25 lt

% of water = 0.25 100 20%
1.25

```
.
```

Examples: A trader bought an item for Rs. 200. If he wants a profit of 22%, at what price must he sell it?

Solution: CP=200, Profit = 22%.

So, SP = 1.22CP = 1.22 × 200 = 244/-.

Examples: A person buys an item at Rs. 120 and sells to another at a profit of 25%. If the second person sells the I

tem to another at Rs. 180, what is the profit % of the second person?

Solution: SP of 1st person = CP of 2nd person = 1.25 × 120 = 150.

SP of 2nd person = 180.

Profit % = (^180) 1.2 20%
150
SP   
CP

### .

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

4

**RATIOS AND**

**PROPORTIONS**

**4.1. What is a Ratio?**

A ratio is a representation of distribution of a value present among the persons present and is shown as follows:

If a total is divided among A, B and C such that A got 4 parts, B got 5 parts and C got 6 parts then it is represented in ratio as
A:B:C = 4:5:6.

So, 4:5:6 means that the total value is divided into 4+5+6 = 15 equal parts and then distributed as per the ratio.

Example 1 : Divide Rs. 580 between A and B in the ratio of 14:15.

Solution: A:B = 14:15  580 is divided into 29 equal parts  each part = Rs. 20.

So A’s share = 14 parts = 14 × 20 = Rs. 280

B’s share = 15 parts = Rs. 300.

Example 2 : If A:B = 2:3 and B:C = 4:5 then find A:B:C.

Solution: To combine two ratios the proportions common for them shall be in equal parts. Here the common proportion is
B for the given ratios.

Making B equal in both ratios they become 8:12 and 12:15  A:B:C = 8:12:15.

Example 3: Three numbers are in the ratio of 3: 4 : 8 and the sum of these numbers is 975. Find the three numbers.

Solution: Let the numbers be 3x, 4x and 8x. Then their sum = 3x + 4 x + 8 x = 15x = 975  x = 65.

So the numbers are 3x = 195, 4x = 260 and 8x = 520.

Example 4: Two numbers are in the ratio of 4 : 5. If the difference between these numbers is 24, then find the numbers.

Solution: Let the numbers be 4x and 5x. Their difference = 5x – 4 x = x = 24 (given).

So the numbers are 4x = 96 and 5x = 120.

Example 5: Given two numbers are in the ratio of 3 : 4. If 8 is added to each of them, their ratio is changed to 5 : 6. Find two
numbers.

Solution: Let the numbers be a and b.

: 3 : 4^3
4

```
AB  A
B
```

. Also,

```
 
 
```

(^85)
86



A
B

### .

Solving we get, A=12 and B = 16.


**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

5

**TIME AND DISTANCE**

**5.1. Speed**

We have the relation between speed, time and distance as follows:

Speed = Distance
Time

So the distance covered in unit time is called speed.

This forms the basis for Time and Distance. It can be re-written as Distance = Speed X Time or

Time = Distance
Speed

### .

**5.1.1. Units of Speed**

The units of speed are kmph (km per hour) or m / s.

1 kmph =^5 m/s
18

1 m/s =^18 kmph
5

**5.1.2. Average Speed**

When the travel comprises of various speeds then the concept of average speed is to be applied.

aAverage Speed = Total distance covered
Total time of travel

Note: In the total time above, the time of rest is not considered.

Example 1 : If a car travels along four sides of a square at 100 kmph, 200 kmph, 300 kmph and 400 kmph find its average
speed.

Solution: Average Speed = Total distance
Total time

### .

Let each side of square be x km. Then the total distance = 4x km.

The total time is sum of individual times taken to cover each side.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

To cover x km at 100 kmph, time
100

```
 x.
```

For the second side time
200

```
 x.
```

Using this we can write average speed =^4 192 kmph

```
100 200 300 400
```

```
x
x x x x
```

```



```

```

```

### .

Example 2: A man if travels at^5
6

```
th of his actual speed takes 10 min more to travel a distance. Find his usual time.
```

Solution: Let s be the actual speed and t be the actual time of the man.

Now the speed is^5
6

```

s and time is (t^ +10) min. But the distance remains the same.^
```

So distance 1 = distance 2  s × t =^5
6

```

s ×^ (t+10) ^ t = 50 min.^
```

Example 3: If a person walks at 30 kmph he is 10 min late to his office. If he travels at 40 kmph then he reaches to his office
5 min early. Find the distance to his office.

Solution: Let the distance to his office be d. The difference between the two timings is given as 15 min =^1 h r
4

### .

Now if d km are covered at 30 kmph then time = d/30. Similarly second time = d/40.

So, –^1 30 km
30 40 4

```
dd  d.
```

```
Note: When two objects move with speeds s 1 and s 2
```

- In opposite directions their combined speed = s 1 + s 2
- In same direction their combined speed = s 1 ~ s 2.

Example 4: Two people start moving from the same point at the same time at 30 kmph and 40 kmph in opposite directions.
Find the distance between them after 3 hrs.

Solution: Speed = 30 + 40 = 70 kmph (since in opposite directions)

Time = 3 hrs

So distance = speed × time = 70 × 3 = 210 km.

Example 5: A starts from X to Y at 6 am at 40 kmph and at the same time B starts from Y to X at 50 kmph. When will they
meet if X and Y are 360 km apart?

Solution: Distance = 360 km, Speed = 40 + 50 = 90 kmph.

Time = distance =^360 = 4hrs from 6 am 10 am
speed 90

### .

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

6

**TIME AND WORK**

**6.1. Introduction**

If a person can complete a work in ‘n’ days then he can do^1
n

```
part of the work in one day.
```

The amount of work done be a person in 1 day is called his efficiency.

Example: A can do a work in 10 days. Then the efficiency of A is given by 1
10

### A .

Note: Number of days required to do a work = work to be done/work per day.

Example 1: If A can do a work in 10 days, B can do it in 20 days and C in 30 days in how many days will the three together
do it?

Solution: The efficiencies are 1 , 1 1
10 20 30

```
A  B  and C 
```

So work done per day by the three =^1 1  1  11    60 5.45
10 20 30 60 11

```
   No of days   days.
```

Example 2: If A and B can do a work in 10 days, B and C can do it in 20 days and C and A can do it in 40 days in what time
all the three can do it?

Solution: 1
10

### AB

### 1

```
20
```

### BC

### 1

```
40
```

### CA

Adding all the three we get (^2)   7 7 80
40 80 7
A B C       A B C No of days  days.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

```
Note: If all the people do not work for all the time then the principle below can be used:
mA + nB + oC = 1. (1 is the total work)
Here, m = no of days A worked
n = no of days B worked
o = no of days C worked
A, B, C = efficiencies
```

Example 3: If A can do a work in 12 days, B can do it in 18 days and C in 24 days. All the three started the work. A left after
two days and C left three days before the completion of the work. How many days are required to complete the
work?

Solution: Let the total no of days be x.

A worked only for 2 days, B worked for x days and C worked for x – 3 days.

So, mA + nB + oC = 1

(^21  1)  (^3) ^1  1
12 18 24
     
   xx       
 12 + 4x + 3(x-3) = 72
69
7
x days.
Note: The ratio of dividing wages = ratio of efficiencies = ratio of parts of work done
Example 4: A can do a work in 10 days and B can do it in 30 days and C in 60 days. If the total wages for the work is Rs. 1800
what is the share of A?
Solution: Ratio of wages =^1 :^1 :^1 6 : 2 : 1
10 30 60
 (Multiplying each term by LCM 60)
So total 9 equal parts in Rs. 1800  each part = Rs. 200  share of A = 6 parts = Rs. 1200.
Note: When pipes are used filling the tank they are treated similar to the men working but some outlet pipes emptying the
tank are present whose work will be considered negative.
Example 5: A pipe can fill a tank in 5 hrs but because of a leak a the bottom it takes 1 hr extra. In what time can the leak alone
empty the tank?
Solution: Let the filling pipe be A.
1
5

### A 

But with the leak L, –^1
6

```
AL ( A-L because leak is outlet)
```

So,^11 –^11
5 6 30

```
  
L
```

```
Leak can empty the tank in 30 hrs.

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

7

**CLOCKS**

**7.1. Introduction**

In a clock the most important hands are the minutes hand and the hours hand. Whatever may be the shape of the dial they
move in a circular track.

The total angle of 360 degrees in a watch is divided into 1 sectors, one for each hour.

So one hour sector =^360  30
12

```
^ degrees.^
```

For every one hour (60 min),

- The minutes hand moves through 360 deg.
- The hours hand moves through 30 deg.
  So for every minute,
- The minutes hand moves through 6 deg
- The hours hand moves through 0.5 deg.
  They move in same direction. So their relative displacement for every minute is 5.5 deg.

This 5.5 deg movement constitutes the movements of both the hands.

So for every minute both the hands give a displacement of 5.5 deg.

```
Note:
```

1. Between every two hours i.e., between 1 and 2, 2 and 3 and so on the hands of the clock coincide with each other for
   one time except between 11, 12 and 12, 1.
   In a day they coincide for 22 times.
2. Between every two hours they are perpendicular to each other two times except between 2, 3 and 3, 4 and 8, 9 and 9,
   10.
   In a day they will be perpendicular for 44 times.
3. Between every two hours they will be opposite to each other one time except between 5, 6 and 6, 7.
   In a day they will be opposite for 22 times.

Examples: At what time between 5 and 6 will the hands of the clock coincide?

Solution: At 5 the angle between the hands is 150 deg.

To coincide, they collectively have to travel this distance. Every minute they travel 5.5 deg.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

So no. of minutes required to coincide = 150 300 273
5.5 11 11

```
 min.
```

Examples: At what time between 6 and 7 will the hands be perpendicular?

Solution: At 6 the angle between the hands is 180 deg.

To form 90 deg they have to cover 90 deg (out of 180 if 90 is covered 90 will remain)

So no. of minutes required =^90180 16 4
5.5 11 11

```
min.
```

```
But they will be perpendicular for two times. The second one will happen after the minutes hand crosses the hours
hand and then for 90 deg.
```

So it has to travel 180 + 90 = 270 deg.

So time =^270540 491
5.5 11 11

```
min.
```

Examples: What is the angle between the hands of the clock at 3.45?

Solution: At 3, the angle between the hands = A = 90 deg.

In 45 min the hands will move angle of B = 45 × 5.5 deg (since 5.5 deg for 1 min)

B = 247.5 deg.

Required angle = A ~ B = 157.5 deg.

Examples: What is the angle between the hands at 4.40?

Solution: At 4 the angle between the hands, A = 120 deg.

In 40 min, B = 40 × 5.5 = 220 deg.

The required angle = A ~ B = 100 deg.

Examples: A clock loses 5 min for every hour and another gains 5 min for every hour. If they are set correct at 10 am on
Monday then when will they be 12 hrs apart?

Solution: For every hour watch A loses 5 min and watch B gains 5 min.

So for every hour they will differ by 10 min.

For 12 hrs (720 min) difference between them the time required =

(^72072)
10
 hrs
So they will be 12 hrs apart after 3 days i.e., at 10 am on Thursday.


**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

8

**CALENDARS**

**8.1. Calendars**

Here you mainly deal in finding the day of the week on a particular given date.

The process of finding this depends on the number of odd days.

Odd days are quite different from the odd numbers.

- Odd Days: The days more than the complete number of weeks in a given period are called odd days.
- Ordinary Year: An year that has 365 days is called Ordinary Year.
- Leap Year: The year which is exactly divisible by 4 (except century) is called a leap year.

```
Example: 1968, 1972, 1984, 1988 and so on are the examples of Leap Years.
1986, 1990, 1994, 1998, and so on are the examples of non leap years.
```

Note: The Centuries divisible by 400 are leap years.

Important Points:

- An ordinary year has 365 days = 52 weeks and 1 odd day.
- A leap year has 366 days = 52 weeks and 2 odd days.
- Century = 76 Ordinary years + 24 Leap years.
- Century contain 5 odd days.
- 200 years contain 3 odd days.
- 300 years contain 1 odd day.
- 400 years contain 0 odd days.
- Last day of a century cannot be Tuesday, Thursday or Saturday.
- First day of a century must be Monday, Tuesday, Thursday or Saturday.

Explanation:

```
100 years = 76 ordinary years + 24 leap years
= 76 odd days + 24 × 2 odd days
= 124 odd days = 17 weeks + 5 days
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

```
 100 years contain 5 odd days.
No. of odd days in first century = 5
 Last day of first century is Friday.
```

No. of odd days in two centuries = 3

```
 Wednesday is the last day.
```

No. of odd days in three centuries = 1

```
 Monday is the last day.
```

No. of odd days in four centuries = 0

```
 Sunday is the last day.
```

Since the order is continually kept in successive cycles, the last day of a century cannot be Tuesday, Thursday or
Saturday.

So, the last day of a century should be Sunday, Monday, Wednesday or Friday.

Therefore, the first day of a century must be Monday, Tuesday, Thursday or Saturday.

**8.2. Working Rules**

Working rule to find the day of the week on a particular date when reference day is given:

Step 1: Find the net number of odd days for the period between the reference date and the given date (exclude the

```
reference day but count the given date for counting the number of net odd days).
```

Step 2: The day of the week on the particular date is equal to the number of net odd days ahead of the reference

```
day (if the reference day was before this date) but behind the reference day (if this date was behind the
reference day).
```

Working rule to find the day of the week on a particular date when no reference day is given

Step 1: Count the net number of odd days on the given date

Step 2: Write:

For 0 odd days – Sunday

For 1 odd day – Monday

For 2 odd days – Tuesday

For 6 odd days - Saturday

Examples: If 11th January 1997 was a Sunday then what day of the week was on 10th January 2000?

Solution: Total number of days between 11th January 1997 and 10th January 2000

= ( 365 – 11) in 1997 + 365 in 1998 + 365 in 1999 + 10 days in 2000

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

= ( 50 weeks + 4 odd days) + (52 weeks + 1 odd day) + (52 weeks + 1 odd day) + (1 week + 3 odd days)

Total number of odd days = 4 + 1 + 1 + 3 = 9 days = 1 week + 2 days

Hence, 10th January, 2000 would be 2 days ahead of Sunday i.e. it was on Tuesday.

Examples: What day of the week was on 10th June 2008?

Solution: 10 th June 2008 = 2007 years + First 5 months up to May 2008 + 10 days of June

2000 years have 0 odd days.

Remaining 7 years has 1 leap year and 6 ordinary years2 + 6 = 8 odd days

So, 2007 years have 8 odd days.

No. of odd days from 1st January 2008 to 31st May 2008 = 3+1+3+2+3 = 12

10 days of June has 3 odd days.

Total number of odd days = 8+12+3 = 23

23 odd days = 3 weeks + 2 odd days.

Hence, 10th June, 2008 was Tuesday.

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

9

**BLOOD RELATIONS**

**9.1. Introduction**

The standard definitions of relations are given below

```
A/An  is related to a PERSON as 
```

```
Grandfather The father of his/her mother or father^
```

```
Grandmother The mother of his/her mother or father
```

```
Grandson The son of his/her daughter/son
```

```
Granddaughter The daughter of his/her daughters/son
```

```
Uncle The brother of his/her mother or father
```

```
Aunt The sister of his/her mother or father
```

```
Nephew The son of his/her brother or sister
```

```
Cousin The son or daughter of his/her aunt of uncle^
```

```
Niece The daughter of his/her brother or sister
```

```
Spouse as her husband or his wife
```

```
Father-in-law the father of his/her spouse
```

```
Mother-in-law the mother of his/her spouse
```

```
Sister-in-law the sister of his/her spouse
```

```
Brother-in-law the brother of his/her spouse
```

```
Son-in-law the spouse of his/her daughter
```

```
Daughter-in-law the spouse of his/her son
```

### 

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

10

**DIRECTIONS**

**10.1. Introduction**

Examples:

Example 1 : Ravi traveled 4 km straight towards south. He turned left and traveled 6 km straight, then turned right and traveled

```
4 km straight. How far is he from the starting point?
```

```
(a) 8 km (b) 10 km (c) 18 km (d) 12 km
```

Solution. 10 km. B is the finishing point and A is starting point. The distance of A from B is

Example 2. A is to the South-East of C, B is to the East of C and North-East of A. If D is to the North of A and North-West

```
of B. In which direction of C is D located?
```

```
(a) North-West (b) South-West (c) North-East (d) South-East
```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

Solution. North-East D is located to the North-East of C.

Example 3. A rat runs 20’ towards East and turns to right, runs 10’ and turns to right, runs 9’ and again turns to left, runs 5’

```
and then runs to left, runs 12’ and finally turns to left and runs 6’. Now, which direction is the rat facing?
```

```
(a) East (b) West
(c) North (d) South
```

Solution. North. The movements of the rat from A to G are as shown in the fig. It is clear, rat is walking in one direction

```
FG, i.e., North.
```

Example 4. From his house, Lokesh went 15 km to the North. Then he turned west and covered 10 km, then he turned South

```
and covered 5 km. Finally, turning to East, he covered 10 km. In which direction is he from his house?
```

```
(a) East (b) South
(c) North (d) West
```

Solution. North. Starting point is A and ending point is E. E is to the north of his house at A.

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

11

**DATA**

**INTERPRETATION**

**11.1. Data Interpretation**

 It deals with careful reading, understanding, organizing and interpreting the data provided so as to derive meaningful

```
conclusions.
```

 Mostly used tools for interpretation of a data are

```
 Ratio
 Percentage
 Rate
 Average
```

**11.2. Types of Data Interpretation:**

The numerical data pertaining to any event can be presented by any one or more of the following methods.

1. Tables
2. Line Graphs
3. Bar Graphs or Bar Charts
4. Pie Charts or Circle Graphs

**11.2.1. Tables**

It is the systematic presentation of data in tabular form to understand the given information and to make clear the problem in
a certain field of study. It has six elements namely:

- Title: It is the heading of the table.
- Stule: It is the section of the table containing row headings
- Column Captions: It is the heading of each column
- Body: It consists the numerical figures
- Footnotes: It is for further explanation of the table
- Source: It is the authority of the data

Example: Study the following table and answer the questions given below it.

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

```
Annual Income of Five Schools
Figures in ’00 rupees
```

```
Sources of Income School A School B School C School D School E
Tuition Fee 120 60 210 90 120
Term Fee 24 12 45 24 30
Donations 54 21 60 51 60
Funds 60 54 120 42 55
Miscellaneous 12 3 15 3 15
Total 270 150 450 210 280
```

Example: The income by way of donation to school D is what per-cent of its miscellaneous?

Solution: Required percentage = 27 %
300

### 5100

### 

**11.2.2. Line Graph**

A line graph indicates the variation of a quantity w.r.t two parameters calibrated on X and Y-axis respectively.

```
Note:
```

1. Any part of the line graph parallel to X-axis represents no change in the value of Y parameter w.r.t the value of X
   parameter.
2. The steepest or maximum part of the line graph indicates maximum percentage change of the value during the two
   consecutive period in which the related part lies.
3. If the steepest part is a rise slope, then it is the highest percentage growth.
4. If the steepest part is a decline slope, it will represent a maximum percentage fall of the value calibrated in the
   other axis.

**11.2.3. Bar Graph**

Bar graphs are diagrammatic representation of a discrete data.

Types of Bar Graphs:

- Simple Bar Graphs: A simple bar graph relates to only one variable. The values of the variables may relate to different
  years or different terms.
- Sub-divided Bar Graph: It is used to represent various parts of sub-classes of total magnitude of the given variable.
- Multiple Bar Graphs: In this type, two or more bars are constructed adjoining each other, to represent either different
  components of a total or to show multiple variables.

**11.2.4. Pie Chart**

In this method of representation, the total quantity is distributed over a total angle of 360 o which is one complete circle or pie.

```

```

**GATE WALLAH COMPUTER SCIENCE & INFORMATION TECHNOLOGY HANDBOOK**

```
General Aptitude
```

12

**DATA**

**SUFFICIENCY**

**12 .1. Introduction**

Data sufficiency questions are designed to measure your ability to analyze a quantities problem, recognize which given

information is relevant, and determine at what point there is sufficient information to solve a problem. In these questions, you

are to classify each problem according to the five or four fixed answer choice, rather than find a solution to the problem.

Each Data sufficiency question consists of a question, often accompanied by some initial information, and two statements,

labeled (1) and (2), which contain additional information. You must decide whether the information in each statement is

sufficient to answer the question or- if neither statement provides enough information –whether the information in the two

statements together is sufficient. It is also possible that the statements in combination do not give enough information answer

the question.

Begin by reading the initial information and the question carefully. Next, consider the first statement. Does the information

provided by the first statement is sufficient to answer the question? Go on the statement. Try to ignore the information given in

the first statement when you consider the second statement. Now you should be able to say, for each statement, whether it is

sufficient to determine the answer.

Next, consider the two statements in tandem. Do they, together, enable you to answer the question?

Give our answers as per the following statements

A Statement (1) alone is sufficient but

Statement (2) alone is not sufficient

B Statement (2) alone is sufficient but

Statement (1) alone is not sufficient

C Both statements together are sufficient

but neither statement alone is sufficient

D Each statement alone is sufficient

E Both statement together are still not sufficient.

```

```

**Thank**

**you**

**Thank**

**you**

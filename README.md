# Dayuri
A compiler for Dayuri Functional language


## Road Map 
All phases include the steps
+ parsing
+ desugar
+ ast
+ compile to python code

Current roadmap just have two steps

- Recognize simply typed lambda calculus type expression with just int as type
  + `int`
  + `int->int`
  + `int->(int->int)->int`

- Make simple upper level variable binding work with just int types
  + `some : int = 1;`
- Add new types definition but only with integer members
  + `type point2 = point2 (x:int) (y : int) ;`



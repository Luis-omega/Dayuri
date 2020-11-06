# Dayuri
A compiler for Dayuri Functional language


## Road Map 
All phases include the steps
+ parsing
  - Add to grammar the new sintax required
  - Add test cases
+ desugar
  - Transform the syntax tree in some kind of AST
+ ast
  - The true ast representation isn't a tree, is a bunch of python clasess.
+ ast2string
+ compile to python code
  - this isn't done right now



- [x] Recognize simply typed lambda calculus type expression with just int as type
  + `int`
  + `int->int`
  + `int->(int->int)->int`

- [ ] Add variable declaration
  + `some : int;`
  + `some1 : int->int; `

- [ ] Add basic values (int) and variable assignation
  + `some =1;`
  + `some2 : int =2;`
  + `some3 : int->int = 3;`

- [ ] Add type check for assignation
  + forbid `some : int->int = 3`

- [ ] Add Sum types with just int as members 
  + `type point2 = point2 (x:int) (y : int) ;`



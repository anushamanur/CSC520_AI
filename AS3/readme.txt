for 32b.pl

Instructions to run

$ swipl
?- consult("32b.pl").

Relations are defined as - 
value(X, isa, Y)

Subsets - 
value(X, ako, Y).



-------------------------------------------------------------
for 32d.pl

Instructions to run

$ swipl
?- consult("32d.pl").

Relations are defined as - 
value(X, isa, Y)

Subsets - 
value(X, ako, Y).

Property - 
hasproperty(X, property, Y).

eg -
hasproperty(X, legs, Y).

"property" can hold - 

legs
habitat
color
friend

-------------------------------------------------------------

for 33d.pl

Instructions to run

$ swipl
?- consult("33d.pl").

Relations are defined as - 
value(X, isa, database) -  checks if X database exists
value(X, user, Y) - X is a user in Y group
value(X, password, Y) - database X is password protected if Y=y and no if Y=n

To check access -
value(X, access, Y)  - does X have access to database Y

---------------------------------------------------------------- 

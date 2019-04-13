% Writing rules for prolog 2b


%Ron is a Bat.
edge(ron, isa, bat).

%Buckshot is a deer.
edge(buckshot, isa, deer).

%Junior is a deer.
edge(junior, isa, deer).

%Dexter is a Carnivore.
edge(dexter, isa, carnivore).

%Deer is a type of Herbivore.
edge(deer, ako, herbivore).

%Bat is another type of herbivore.
edge(bat, ako, herbivore).

% There are two types of animals: Carnivores and Herbivores.
edge(carnivore, ako, animal).
edge(herbivore, ako, animal).

%rel(SourceNode, RelationshipType, DestinationNode)
%if there is a direct edge
%rel(A, Slot, B):-
%	 edge(A, Slot, B).
% ako - subset
% isa - member


%rel(A, Slot, B):- 
%	edge(A, Slot, Z), 
%	rel(Z, ako, B).

%defining relation
value(Node, Slot, Value):-
edge(Node, Slot, Value).

value(Node, Slot, Value):-
edge(Node, isa, Node1),
value(Node1, Slot, Value).

value(Node, Slot, Value):-
edge(Node, ako, Node1),
value(Node1, Slot, Value).

value(Node, isa, Value):-
edge(Node,ako, Value).

value(Node, isa, Value):-
edge(Node, isa, Node1),
value(Node1, ako, Value). 
 

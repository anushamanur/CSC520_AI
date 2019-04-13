% Writing rules for prolog

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

%Animals’ habitat is land but Bat’s is Air.
property(animal, habitat, land).
property(bat, habitat,air).

%Skin color of a deer is yellow but Buckshot is black.
property(deer, color, yellow).
property(buckshot, color, black).

%Animals have 4 legs but Dexter and Ron have 2 legs.
property(animal, legs, 4).
property(dexter, legs, 2).
property(ron, legs, 2).

%Ron and Buckshot are friends of each other.
property(ron, friend, buckshot).
property(buckshot, friend, ron).

%Junior is a friend of Dexter but Dexter is not a friend of Junior.
property(junior, friend, dexter).


%rel(SourceNode, RelationshipType, DestinationNode)

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

%defining property
hasproperty(Object, Property, Value) :-
property(Object, Property, Value).
 
hasproperty(Object, Property, Value) :-
edge(Object, isa, Parent),
hasproperty(Parent, Property, Value),
\+ property(Object, Property, _).
 
hasproperty(Object, Property, Value) :-
edge(Object, ako, Parent),
hasproperty(Parent, Property, Value),
\+ property(Object, Property, _). 

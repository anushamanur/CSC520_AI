% Writing rules for prolog


edge(tom, user, client).
edge(mongodb, isa, database).
edge(mongodb, password, y).

%Examples added just for testing
edge(bbb, user, client).
edge(ccc, user, client).
edge(sql, isa, database).
edge(sql, password, n).

%relation
value(Node, Slot, Value):-
edge(Node, Slot, Value).


%Check access if user is part of client group and such a databse exists and is not passwprd protected
value(X, access, Z):-
value(X, user, client),
value(Z, isa, database),
value(Z, password, n).



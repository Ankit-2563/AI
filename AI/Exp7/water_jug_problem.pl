% Define the capacities of the two jugs and the goal amount.
capacity1(4).  % Capacity of the first jug
capacity2(3).  % Capacity of the second jug
goal(2).       % Goal: One of the jugs should have exactly 2 liters of water

% Check if the goal state is reached.
goal_state(state(X, _)) :- goal(G), X = G.
goal_state(state(_, Y)) :- goal(G), Y = G.

% Possible moves:
% 1. Fill Jug 1
move(state(_, Y), state(X2, Y), fill_jug1) :-
    capacity1(X2),
    X2 \= 0.  % Avoid filling if the jug is already full.

% 2. Fill Jug 2
move(state(X, _), state(X, Y2), fill_jug2) :-
    capacity2(Y2),
    Y2 \= 0.  % Avoid filling if the jug is already full.

% 3. Empty Jug 1
move(state(X, Y), state(0, Y), empty_jug1) :-
    X > 0.

% 4. Empty Jug 2
move(state(X, Y), state(X, 0), empty_jug2) :-
    Y > 0.

% 5. Pour water from Jug 1 to Jug 2
move(state(X, Y), state(X1, Y1), pour_jug1_to_jug2) :-
    capacity2(YMax),
    X > 0,
    Y < YMax,
    Transfer is min(X, YMax - Y),
    X1 is X - Transfer,
    Y1 is Y + Transfer,
    Y1 \= Y.  % Avoid pouring if no water is transferred.

% 6. Pour water from Jug 2 to Jug 1
move(state(X, Y), state(X1, Y1), pour_jug2_to_jug1) :-
    capacity1(XMax),
    Y > 0,
    X < XMax,
    Transfer is min(Y, XMax - X),
    X1 is X + Transfer,
    Y1 is Y - Transfer,
    X1 \= X.  % Avoid pouring if no water is transferred.

% Use Depth-First Search to explore states.
dfs(Path, State, [State|Path]) :-
    goal_state(State).

dfs(Path, State, Solution) :-
    move(State, NextState, _Action),
    \+ member(NextState, Path),        % Prevent revisiting visited states
    dfs([NextState|Path], NextState, Solution).

% Find a solution path from initial state
solve(Initial, Solution) :-
    dfs([Initial], Initial, RevSolution),
    reverse(RevSolution, Solution).

% Example query to run the program
% ?- solve(state(0, 0), Solution).

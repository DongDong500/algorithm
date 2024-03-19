# Greedy algorithms
A greedy algorithm always makes the choice that 
looks best at the moment. That is, it makes a locally optimal choice in the hope 
that this choice leads to a globally optimal solution.
Greedy algorithms do not always yield optimal solutions, but for many problems they do.

## Elements of the greedy strategy
A greedy algorithm obtains an optimal solution to a problem by making a sequence 
of choices. At each decision point, the algorithm makes the choice that seems best 
at the moment. This heuristic strategy does not always produce an optimal solution, 
but as in the activity-selection problem, sometimes it does. This section discusses 
some of the general properties of greedy methods.

* Greedy-choice property


The first key ingredient is the ***greedy-choice property***: you can assemble a globally 
optimal solution by making locally optimal (greedy) choices. In other words, when 
you are considering which choice to make, you make the choice that looks best in 
the current problem, without considering results from subproblems. 

* Optimal substructure


A problem exhibits ***optimal substructure*** if an optimal solution to the problem
 contains within it optimal solutions to subproblems. This 
property is a key ingredient of assessing whether dynamic programming applies, 
and it’s also essential for greedy algorithms.

* Greedy versus dynamic programming


Because both the greedy and dynamic-programming strategies exploit optimal substructure, you might be tempted to generate a dynamic-programming solution to 
a problem when a greedy solution suffices or, conversely, you might mistakenly 
think that a greedy solution works when in fact a dynamic-programming solution 
is required. To illustrate the subtle differences between the two techniques, let’s
investigate two variants of a classical optimization problem. 

* **0-1 knapsack problem**

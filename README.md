# Intelligent Algorithms #1 - Dijkstra's pathfinding algorithm

A full write-up about this topic can be found on [Issac Computer Science](https://isaaccomputerscience.org/concepts/dsa_search_dijkstra?topic=searching_sorting_pathfinding)

## Structured English:
```
Declare the visited list
Declare the unvisited list

For each node in graph:
  Add node to the unvisited list with distance of infinity and previous node of null
Set the start node's distance to 0 in the unvisited list

While the unvisited list is not empty:
  Set current node to the node with the lowest cost from the unvisited list
  Copy cost and previous values for current node from the unvisited list to the visited list
  Remove the current node from the unvisited list
        
  For each neighbour of current node:
    If neighbour is not in the visited list
      Calculate new cost = weight of edge + cost of current node
      If new cost is less than neighbour's cost in unvisited list
        Update the neighbour's cost to become the new cost
        Update the neighbour's previous node to become the current node

Return the visited list
```
Once you have visited all nodes, you will receive a data structure containing all of the optimum routes from your starting node to each node in the graph. 

Use this information to output the correct route from your starting node to the finishing node along with the total weight of the journey.

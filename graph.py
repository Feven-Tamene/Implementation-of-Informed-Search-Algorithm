graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151),
              ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Bucharest", 101)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101)]
}
 
# Straight-line distances to Bucharest (good heuristic — admissible)
heuristic_good = {
    "Arad": 366,
    "Zerind": 374,
    "Oradea": 380,
    "Sibiu": 253,
    "Fagaras": 176,
    "Rimnicu Vilcea": 193,
    "Pitesti": 100,
    "Timisoara": 329,
    "Lugoj": 244,
    "Bucharest": 0
}
 
# Misleading heuristic — overestimates and misdirects
heuristic_misleading = {
    "Arad": 100,       # too optimistic, misdirects early
    "Zerind": 50,      # makes Zerind look very close
    "Oradea": 30,      # makes Oradea look like the best path
    "Sibiu": 400,      # overestimates
    "Fagaras": 350,    # overestimates
    "Rimnicu Vilcea": 450,  # overestimates heavily
    "Pitesti": 300,    # overestimates
    "Timisoara": 200,
    "Lugoj": 150,
    "Bucharest": 0
}
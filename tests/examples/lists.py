#!/usr/bin/env python
import columnate

matrix = [
    [308, 0, "com.apple.Finder"],
    [84509, 0, "com.apple.metadata.mdwrite"]
]

string = columnate.lists(matrix)
print(string)

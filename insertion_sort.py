# -*- coding: utf-8 -*-
lst1 = [324, 54, 23, 12, 11, 7, 4, 5, 6, 9]
print(lst1)
def inssort(unsorted):
    sorted = []
    i = 0
    while i < len(unsorted):
        j = len(sorted)
        for e in unsorted:
            sorted.append(e)
            while j:
                

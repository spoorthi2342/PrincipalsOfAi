def fuzzy_union(set1,set2):
    union_set={}
    for element in set1:
        union_set[element]=max(set1[element],set2.get(element,0))
    for element in set2:
        if element not in union_set:
         union_set[element]=set2[element]
    return union_set

def fuzzy_intersection(set1,set2):
   intesection_set={}
   for element in set1:
      if element in set2:
         intesection_set[element]=min(set1[element],set2[element])
   return intesection_set

def display_fuzzy(fuzzy_set):
   print("{",end="")
   for element,membership in fuzzy_set.items():
      print(f"{element},{membership} ",end="")
   print("}")
set1={'a':0.4,'b':0.8,'c':0.2,'d':0.5,'e':0.1}
set2={'a':0.3,'b':0.5,'c':0.2,'g':0.8,'h':0.4}
         
print("fuszzy set 1")
display_fuzzy(set1)
print(end=" ")
print("fuzzy set 2")
display_fuzzy(set2)
print(end=" ")

print("union of fuzzy set is")
union_set=fuzzy_union(set1,set2)
display_fuzzy(union_set)
print(end=" ")
print("intersection of fuzzy ")
union_set=fuzzy_intersection(set1,set2)
display_fuzzy(union_set)



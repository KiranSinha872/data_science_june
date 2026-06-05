#TUPLES
#immutable

tp=(31,2,23,4)

#tp.sort() error bcz tuples are immutable
print(tp)
#a=sorted(tp)   sorted() makes a new list and doesnt interupt the main tuple
a=tuple(sorted(tp))  #tuple converts the list created by sorted() into a tuple
print(a)



#function 


p=(1,3,5,7,9,8,6,4,2,7,9,8,6,4,2)

#count() to count elements
print(p.count(7))

#index() to find the index of the element
print(p.index(7))

#len() to finc the length
print(len(p))

#sum() to find th  total
print(sum(p))


#max() min() to find the highest and lowest
print(max(p))
print(min(p))

#sorted() returns a list
print(sorted(p))
#List
#mutable


lst=[1,2,3,"kiran",[2,3],"c"]
#list takes time to execute
print(lst) #[1, 2, 3, 'kiran', [2, 3], 'c']


#to add elements or valkue we use append function
lst.append(3)
print(lst) #[1, 2, 3, 'kiran', [2, 3], 'c', 3]
lst.append([1,2,3])
print(lst) #new list added [1, 2, 3, 'kiran', [2, 3], 'c', 3, [1, 2, 3]]


#extend()
lst.extend([1,2,3])
print(lst) #1 ,2 ,3 added separately [1, 2, 3, 'kiran', [2, 3], 'c', 3, [1, 2, 3], 1, 2, 3]


#.insert(idx,ele)
#to add element anywhere
lst.insert(2,"hii")
print(lst)

#to remove last element
#.pop()
lst.pop()
print(lst)


# .remove() it removes the element of th first occurence
lst.remove(1)
print(lst)


# .index(ele)
#it returns the index of the element
print(lst.index("kiran")) #it returns an integer so we have to store it so we print it


#.count(ele)
#count the occurence of the element
print(lst.count(3))
print(lst.count("hell")) #if the element is not present it returns 0


#sort()
#it uses quick sort

#lst=lst.sort() error bcz lst contains integers strings together that cant be sorted
 
a=[1,4,2,5,6,7,2,3,4,9,1,56]
a.sort() #it returns none 
print(a)


#sum,min,max,sorted

k=[1,4,2,5,6,7,2,3,4,9,1,56]

#k.sum()  error 
#its not 

print(sum(k))
print(max(k))
print(min(k))
print(sorted(k)) #return a new list


# sorted() vs .sort()
#sorted return a new list.purani list same rehgi .so we have to store it somewhere like a var or print
#sort() return none so we have to us eit separately and print the list 
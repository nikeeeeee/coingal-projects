#Create a tuple with different data types
turplex = ("tuple", False,3.2, 1)
print(turplex)
#create a tuple
turplex = (4, 6, 2, 8, 3, 1)
print(turplex)
#tuples are immutable,so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = turplex + (9,)
print(tuplex)
#counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60,70, 50)
print(tuple1.count(50))
#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop]the start index is inclusive and stop index
_slice= tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isnt defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)
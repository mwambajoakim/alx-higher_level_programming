# <ins>Everything is Object</ins>

## Introduction
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
```
OK. But what about this?

```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```

## 00 - Function to get the type of an object?
- Write the name of the function in the file, without `()`.

## 01 - How do you get the variable identifier (which is the memory address in the CPython implementation)?
- Write the name of the function in the file, without ().

## 02 - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 100
```

## 03 - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = 89
```

## 04 - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a
```

## 05 - In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```

## 06 - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

## 07 - What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
## 08 - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

## 09 - What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

## 10 - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

## 11 - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

## 12 - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

## 13 - What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

## 14 - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

## 15 - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

## 16 - What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

## 17 - What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

## 18 - What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

## 19 - This function def copy_list(list=[]): returns a copy of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

## 20 - Is a a tuple? Answer with Yes or No.
```
a = ()
```

## 21 - Is a a tuple? Answer with Yes or No.
```
a = (1, 2)
```

## 22 - Is a a tuple? Answer with Yes or No.
```
a = (1)
```

## 23 - Is a a tuple? Answer with Yes or No.
```
a = (1, )
```

## 24 - What does this script print?
```
a = (1)
b = (1)
a is b
```

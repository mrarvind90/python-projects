# Scientific Computing with Python - freeCodeCamp

## About the Projects
This repository contains my solutions to the projects in "Scientific Computing with Python" course from freeCodeCamp.

## Project list:
- [Arithmetic Formatter](#arithmetic-formatter)
- [Time Calculator](#time-calculator)
- [Budget App](#budget-app)
- [Polygon Area Calculator](#polygon-area-calculator)
- [Probability Calculator](#probability-calculator)

## Arithmetic Formatter
A Python program that provides a function for formatting a list of arithmetic problems vertically and side-by-side. Optionally, it can display the answers alongside the problems.

### Example
Function Call:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)

You can try my code at [Replit](https://replit.com/@mrarvind90/arithmetic-formatter?v=1)

## Time Calculator
A Python program to add time to a 12-hour clock format, with optional day of the week support.

### Example
Function Call:

```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)

You can try my code at [Replit](https://replit.com/@mrarvind90/time-calculator?v=1)

## Budget App
A Python program to initialise a budget category object which allows depositing, withdrawing, as well as transferring funds to another budget category object.

Additionally, it can also return a formatted string representation of the category ledger as well as creating visual charts that depict the percentage of spending in each category.

### Example
Here is an example of the output when printing out the `Category` object:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
Here is an example of the output when printing out `Percentage spent by category` chart:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g 
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)

You can try my code at [Replit](https://replit.com/@mrarvind90/budget-app?v=1)


## Polygon Area Calculator
A Python project with a Rectangle class and a Square class, showcasing object-oriented programming. The Rectangle class handles width, height, area, perimeter, diagonal, picture representation, and fitting calculations. The Square class, a subclass of Rectangle, adds single-side handling and method access while maintaining string representation integrity.

### Example
Function Call:

```python
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area()) # Returns: 50

rect.set_height(3)
print(rect.get_perimeter()) # Returns: 26
print(rect) # Returns: Rectangle(width=10, height=3)

"""
Returns: 

**********
**********
**********

"""
print(rect.get_picture())


sq = shape_calculator.Square(9)
print(sq.get_area()) # Returns: 81

sq.set_side(4)
print(sq.get_diagonal()) # Returns: 5.656854249492381
print(sq) # Returns: Square(side=4)

"""
Returns: 

****
****
****
****

"""
print(sq.get_picture()) # Returns:

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

You can try my code at [Replit](https://replit.com/@mrarvind90/polygon-area-calculator?v=1)

## Probability Calculator
A Python program to calculate the probability of drawing M number of matching colors over N iteration


See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

You can try my code at [Replit](https://replit.com/@mrarvind90/probability-calculator?v=1)




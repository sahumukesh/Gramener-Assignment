# Gramener-Assignment
This is a repository for assignment in Data Science given by Gramener

# Python: 
```python
    1. Given two lists L1 = ['a', 'b', 'c'], L2 = ['b', 'd'], find common elements, 
    find elements present in L1 and not in L2?
    

Program:
L1 = ['a', 'b', 'c']
L2 = ['b', 'd']

def common_element(i, j):
	L1_set = set(L1)
	L2_set = set(L2)
	
	# Check Length
	if len(L1_set.intersection(L2_set)) > 0:
		return (L1_set.intersection(L2_set))
	else:
		return ("No Common Elements")
print list(set(L1) - set(L2))

Output:
['b']
['a', 'c']
```


```python
     2. How many Thursdays were there between 1990 - 2000?


Program:
# Since it was a Monday on 1st January 1990 and a Sunday on 31st December 2000
from datetime import date
f_date = date(1990, 1, 1)
l_date = date(2000, 12, 31)
delta = l_date - f_date
print(delta.days/7 + 1) # we add 1 to compensate for the remainder value

Output:
574
```
# Javascript:
```javascript
    1. Given the following Javascript array:
    var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop']
    write a Javascript function or expression that returns an array with just
    the zeroes removed.
    
Program:
<!DOCTYPE html>
<html>
<title>Web Page Design</title>
<script>
function removeElementsWithValue(arr, val) {
    var i = arr.length;
    while (i--) {
        if (arr[i] === val) {
            arr.splice(i, 1);
        }
    }
    return arr;
}

var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop'];
removeElementsWithValue(data, 0);
document.write(data);
</script>
<body>
</body>
</html>

Output:
1,2,stop,2,1,stop
```

# Use case 1 - National Achievement Survey
National Council of Education Research and Training conducts yearly National Achievement Survey. We have provided the data of Class VIII students from 2014. 

File: “gramener-usecase-nas.7z”
#### Questions to answer:

    1. What influences students performance the most?
    Answer: Please refer to the Use Case - 1/Question - #1 folder in this repository for the solution.
    2. How do boys and girls perform across states?
    Answer: Please refer to the Use Case - 1/Question - #2 folder in this repository for the solution.
    3. Do students from South Indian states really excel at Math and Science?
    Answer: Please refer to the Use Case - 1/Question - #3 folder in this repository for the solution.

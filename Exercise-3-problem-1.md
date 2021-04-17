## Problem 1 - Batch processing data files with a `for` loop (*2 points*)

This problem is meant to simulate a common problem dealing with data files: batch processing.

Batch processing involves using scripts to repeat a process with many data files, and one common task is generating a list of filenames that will be processed or saved to disk.

For this problem you will need to modify the code blocks below and add code to produce the desired outcomes. 

**Notice**: Closely follow the instructions! For example, you should be sure to use **exactly** the same variable names mentioned in the instructions.

**Your score on this problem will be based on following criteria:**

 - Creating and using variables to produce the desired text format
 - Successfully using a for loop to iterate over desired set of numbers
 - Successfully producing the desired filename(s)
 - Including comments that explain what most lines in the code do
 - Answering a couple questions at the end of the problem

### Part 1 (0.3 points)

- Create a new variable called `basename` that contains text `"Station"`.


```python
# YOUR CODE HERE
#
```


```python
# Test print of the variable
print(basename)
```


- Create a new variable `filenames` that is an empty list.


```python
# YOUR CODE HERE
#
```


```python
# Test print of the variable
print(filenames)
```

### Part 2 (1.7 points)

- Using a `for` loop iterate over the number range 0-20 and within the loop:
    - Create a variable `station` that contains the 1) text from `basename` variable, 2) the number, and 3) the file extension `.txt`  
    - Add the content of `station` to `filenames` list which should have following content in the end:

      ```
      ['Station_0.txt', 'Station_1.txt', 'Station_2.txt', 'Station_3.txt',
       'Station_4.txt', 'Station_5.txt', 'Station_6.txt', 'Station_7.txt',
       'Station_8.txt', 'Station_9.txt', 'Station_10.txt', 'Station_11.txt',
       'Station_12.txt', 'Station_13.txt', 'Station_14.txt', 'Station_15.txt',
       'Station_16.txt', 'Station_17.txt', 'Station_18.txt', 'Station_19.txt',
       'Station_20.txt']
      ```


```python
# YOUR CODE HERE
#
```


```python
# Test print of the results
print(filenames)
```


```python
# Check that the value of the last station is correct
# Note! This test assumes that you used the variable `station` inside the for-loop
assert station.lower().strip() == 'station_20.txt', 'The value of the last station is not correct'
```


```python
# Check that there are 21 values in the list
assert len(filenames) == 21, 'The length of the list "filenames" should be 21'
```

### Part 3 (0 points)

Here, we ask a few questions to make sure you have understand the concepts, etc. Answer shortly with a few sentences below.

You can also write any feedback or questions concerning this problem.

1. Is the concept of a loop clear to you? If not, what is difficult to understand?
2. Did you include comments in your code blocks? If not, please add them now :)
  
Write your answers below.

YOUR ANSWER HERE

### Done!

That's it! Now you are ready to continue with [Problem 2](Exercise-3-problem-2.ipynb).

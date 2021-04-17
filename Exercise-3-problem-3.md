## Problem 3 - Allocating locations (*4 points*)

### Overview

The following map shows the locations of the weather stations (as blue points) in Finland that are more than 70 years old [1].
In this problem we are interested to find out whether the station network was equally distributed across Finland
seventy years ago. We have divided Finland into four geographical zones (i.e. Northwest, Northeast, Southwest, Southeast) according the approximate center point of Finnish mainland located at `26.3, 64.5` (longitude, latitude in decimal degrees).

![FMI stations](img/FMI_stations_70_years_older.png)

[1]: The locations and the age of weather stations were obtained from: http://en.ilmatieteenlaitos.fi/observation-stations

Below, we have given you the coordinates of 34 weather stations.
The location of a single station is determined with a pair of latitude and longitude coordinates.
The coordinates of all the stations are separated into two lists (`lat` and `lon`) and the names of the stations are in `stations` list. From these lists, you would get e.g. the location of the first station by combining the latitude and longitude coordinates from coordinate lists, and the name of that station from `stations` list at index `0`.

### Problem statement

In this problem your job is to print the names of weather stations located in different zones. **Optionally** you should also report the share of weather stations that allocated to each zone that could be used to evaluate if certain zone was over/under-represented 70 years ago (This optional task does not affect your score on this problem).

To solve this problem, you should modify and fill in the missing parts in the programs below.

**Notice**: Closely follow the instructions! For example, you should be sure to use **exactly** the same variable names mentioned in the instructions.

**Your score on this problem will be based on following criteria:**

- Creating four lists for geographical zones in Finland (i.e. `nort_west`, `north_east`, `south_west`, `south_east`)
- Iterating over the values and determining to which geographical zone the station belongs
    - Hint: You should create a loop that iterates `n` times. Create a variable *`n`* that should contain the number of stations we have here.
    - You should use a conditional statement to find out if the latitude coordinate of a station is either North or South of the center point of Finland (`26.3, 64.5`) **AND** if the longitude location is West or East of that center point.
    - You should insert the name of the station into the correct geographical zone list
- Printing out the names of stations in each geographical zone
- (*Optional*) Calculating and printing the percentage of stations in each zone

### Data

Here, we provide you the data you should use to solve the problem 3.


```python
# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 
            'Juuka Niemelä', 'Jyväskylä airport', 'Kaarina Yltöinen', 'Kauhava airfield', 
            'Kemi Kemi-Tornio airport', 'Kotka Rankki', 'Kouvola Anjala', 
            'Kouvola Utti airport', 'Kuopio Maaninka', 'Kuusamo airport', 
            'Lieksa Lampela', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Rovaniemi Apukka', 'Salo Kärkkä', 'Savonlinna Punkaharju Laukansaari', 
            'Seinäjoki Pelmaa', 'Siikajoki Ruukki', 'Siilinjärvi Kuopio airport', 
            'Tohmajärvi Kemie', 'Utsjoki Nuorgam', 'Vaala Pelso', 'Vaasa airport', 
            'Vesanto Sonkari', 'Vieremä Kaarakkala', 'Vihti Maasoja', 'Ylitornio Meltosjärvi']

# Latitude coordinates of Weather stations  
lats = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4,
       60.39, 63.12, 65.78, 60.38, 60.7, 60.9, 63.14, 65.99,
       63.32, 63.44, 59.78, 61.47, 66.58, 60.37, 61.8, 62.94,
       64.68, 63.01, 62.24, 70.08, 64.501, 63.06, 62.92, 63.84,
       60.42, 66.53]

# Longitude coordinates of Weather stations 
lons = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67, 
       22.55, 23.04, 24.58, 26.96, 26.81, 26.95, 27.31, 29.23, 
       30.05, 21.07, 21.37, 21.79, 26.01, 23.11, 29.32, 22.49, 
       25.09, 27.8, 30.35, 27.9, 26.42, 21.75, 26.42, 27.22, 
       24.4, 24.65]

# Cutoff values that correspond to the centroid of Finnish mainland
# North - South
north_south_cutoff = 64.5

# East-West
east_west_cutoff = 26.3
```

### Part 1 (0.5 points)

- Create four empty lists for the geographical zones in Finland. Use **exactly** these variable names
   - `north_west`
   - `north_east`
   - `south_west`
   - `south_east`


```python
# YOUR CODE HERE
raise NotImplementedError()
```


```python
# This test print should work
print(north_west, south_west)

```

### Part 2 (0.5 points)

- Count the number of stations and store that value in variable: *`n`*


```python
# YOUR CODE HERE
raise NotImplementedError()
```


```python
# How many stations do we have?
print("In the data, there are", n, "stations.")
```

### Part 3 (0 points)

- Make a loop that iterates `n` times, and allocates stations to different geographical zones based on their coordinates. 


```python
# YOUR CODE HERE
raise NotImplementedError()
```

### Part 4  (2 points)

- In the following programs, you should print out the correct names for each geographical zone.
    - We have given you the correct number of stations as a hint for each zone, so it is easier for you to know whether you have correct answer. 


```python
# This test print should print out station names in North West
# Hint: there should be 4 stations in this class
print("The names of the Northwest stations are:\n", north_west)
```


```python
# This test print should print out station names in North Eest
# Hint: there should be 3 stations in this class
print("The names of the Northeast stations are:\n", north_east)
```


```python
# This test print should print out station names in South West
# Hint: there should be 16 stations in this class
print("The names of the Southwest stations are:\n", south_west)
```


```python
# This test print should print out station names in South East
# Hint: there should be 11 stations in this class
print("The names of the Southeast stations are:\n", south_east)
```

### Part 5 (*1 point*)

Here, we ask a few questions to make sure you have understand the concepts, etc. Answer shortly with a few sentences below.

You can also write any feedback or questions concerning this problem.

1. Is the concept of using the `and` operator and the difference between the `if`, `elif`, and `else` conditional statements clear to you? If not, what is difficult to understand?
2. Did you include comments in your code blocks? If not, please add them now :)

Write your answers below.

YOUR ANSWER HERE

### Part 6 (*optional*; 0 points)

- Print the percentage of stations in each geographical zone
    - Store the answers into variables:
        - `north_west_share`
        - `north_east_share`
        - `south_west_share`
        - `south_east_share`


```python
# YOUR CODE HERE
#
```

- Print the results following format: "Northwest contains 99 % of all stations." (this is an example not a correct answer)


```python
# Print the information (you don't need to modify this)
# .format() is a Python function that can be used to easily insert values inside a text-template such as below.
# .0f below is a specific operator that rounds the decimal values into whole numbers
print("Northwest contains{share: .0f} % of all stations.".format(share=north_west_share))
print("Northeast contains{share: .0f} % of all stations.".format(share=north_east_share))
print("Southwest contains{share: .0f} % of all stations.".format(share=south_west_share))
print("Southeast contains{share: .0f} % of all stations.".format(share=south_east_share))

```

### Done!

That's it! Now you have finished all the assignments for this week!

If you want, you can still continue with the *optional* (but fun!) [Problem 4](Exercise-3-problem-4.ipynb).

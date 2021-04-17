#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Classifying temperatures (*4 points*)
#
# ### Overview
#
# This problem is meant to introduce you to the very common and useful concept of data classification.
# In this problem your aim is to classify daily temperatures (in degrees Celsius) stored in the `temperatures` list into four different classes:
#
# - **Cold**: Temperatures of less than -2 degrees
# - **Slippery**: Temperatures equal to or warmer than -2 degrees, but less than +2 degrees
# - **Comfortable**: Temperatures equal to or warmer than +2 degrees, but less than +15 degrees
# - **Warm**: Temperatures equal to or warmer than +15 degrees
#
# To solve this problem, you should modify and fill in the missing parts in the following programs.
#
# **Notice**: Closely follow the instructions! For example, you should be sure to use **exactly** the same variable names mentioned in the instructions.
#
# **Your score on this problem will be based on following criteria:**
#
#  - Using a for loop to iterate over the temperature values
#  - Using conditional statements to find out if a value is within certain value range (class)
#  - Printing information for the user
#  - Including comments that explain what most lines in the code do
#  - Uploading your notebook to your GitHub repository for this week's exercise

# ### Data
#
# The data for this problem comprise a list of night-time, daytime and evening temperatures for April 2013 recorded at the Helsinki Malmi Airport. The list contains 90 values since there are 3 values for each day (April has 30 days). The first value of a given day represents night, the second one is for the daytime, and the third one is for the evening temperature.

temperatures = [
    -5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4, -2.5, -4.6,
    5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8, -0.1, -4.7, -5.6, 2.6,
    -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4, 1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8,
    3.3, 1.6, 1.5, 4.7, 4.0, 3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1,
    6.4, 3.8, 4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5, 4.8,
    11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6, -0.0, 7.3, 3.4,
    4.7, 9.3, 6.4, 5.4, 7.6, 5.2
]

# ### Part 1 (0.5 points)
#
# - Create four empty lists for the different temperature classes:
#
#     - `cold`
#     - `slippery`
#     - `comfortable`
#     - `warm`
#
# Be careful to use these **exact** names for your lists.


# YOUR CODE HERE


# Test print for all lists (they should be empty at this point)
print(cold, slippery, comfortable, warm)

# ### Part 2 (2 points)
#
# Iterate over the temperatures and add temperatures to the different temperature classes defined below:
#
# - **Cold**: Temperatures of less than -2 degrees
# - **Slippery**: Temperatures equal to or warmer than -2 degrees, but less than +2 degrees
# - **Comfortable**: Temperatures equal to or warmer than +2 degrees, but less than +15 degrees
# - **Warm**: Temperatures equal to or warmer than +15 degrees

# YOUR CODE HERE

# Test prints for all lists (now they should contain values)
print(cold, slippery, comfortable, warm)

# ### Part 3 (1.5 points)
#
# Please answer the following questions by modifying the Python programs below:
#
# - How many times was it slippery during the study period?

# Edit the variable to find correct answer
slippery_times = 'XXX'

# YOUR CODE HERE


# Print the answer
print("In April 2013 it was slippery", slippery_times, "times.")

#
# - How many times was it warm during the study period?

# Edit the variable to find correct answer
warm_times = 'XXX'

# YOUR CODE HERE

# Print the answer
print("In April 2013 it was warm", warm_times, "times.")

# - How many times was it cold during the study period?

# Edit the variable to find correct answer
cold_times = 'XXX'

# YOUR CODE HERE

# Print the answer
print("In April 2013 it was cold", cold_times, "times.")

# ### Part 4 (0 points)
#
# Here, we ask a few questions to make sure you have understand the concepts, etc. Answer shortly with a few sentences.
#
# You can also write any feedback or questions concerning this problem.
#
# 1. Is the concept of conditional statements clear to you? If not, what is difficult to understand?
# 2. Did you include comments in your code? If not, do it now :)
#
# Write your answers below.

# YOUR ANSWER HERE

# ### Done!
#
# That's it! Now you are ready to continue with [Problem 3](Exercise-3-problem-3.ipynb).

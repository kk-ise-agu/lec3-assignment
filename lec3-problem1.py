# Part 1
# Create a new variable called basename that contains text "Station"
#YOUR CODE HERE
basename = "Station"
#raise NotImplementedError()
print(basename)

# Create a new variable filenames that is an empty list.
#YOUR CODE HERE
filenames = []
#raise NotImplementedError()
print(filenames)

# Part 2
#Using a for loop iterate over the number range 0-20 and within the loop:
#
#Create a variable station that contains the 1) text from basename variable, 2) the number, and 3) the file extension .txt
#
#Add the content of station to filenames list which should have following content in the end:
#
#['Station_0.txt', 'Station_1.txt', 'Station_2.txt', 'Station_3.txt',
# 'Station_4.txt', 'Station_5.txt', 'Station_6.txt', 'Station_7.txt',
# 'Station_8.txt', 'Station_9.txt', 'Station_10.txt', 'Station_11.txt',
# 'Station_12.txt', 'Station_13.txt', 'Station_14.txt', 'Station_15.txt',
# 'Station_16.txt', 'Station_17.txt', 'Station_18.txt', 'Station_19.txt',
# 'Station_20.txt']

#YOUR CODE HERE
for i in range(21):
	filenames.append(basename+'_'+str(i)+'.txt')
print(filenames)
for station in filenames:
	print(station)

#Check that the value of the last station is correct.
#Note! This test assumes that you used the variable 'station' inside the for-loop
assert station.lower().strip()=='station_20.txt', 'The value of the last station is not correct'

#Check that there are 21 values in the list
assert len(filenames)==21, 'The length of the list "filenames" should be 21'

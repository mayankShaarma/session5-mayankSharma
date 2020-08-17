# ***Assignment 5***
## Session 5
### Session 5 - Functional Parameters

### Description of the module:
This is for session 5 assignment on some arguments and parameters for functions in Python and also to understand the concepts of * arguments, ** arguments, which are basically used for handling variable number of positional arguments and keyword / named arguments.

### Problem Statement

***Time It Function:***
Write a function which gives out average run time per call, such that it's definition is:
***def time_it(fn, *args, repetitions= 1, **kwargs):*** your code comes here.

We should be able to call it like this:

    time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitions=5)
    time_it(squared_power_list, 2, start=0, end=5, repetitions=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
    time_it(polygon_area, 15, sides = 3, repetitions=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
    time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100) # 100 is the base temperature given to be converted
    time_it(speed_converter, 100, dist='km', time='min', repetitions=200) #dist can be km/m/ft/yrd, time can be ms/s/min/hr/day, speed given by user is in kmph


### Implementation
It implements these functions (with exactly the same names)
> time_it
> squared_power_list
> polygon_area
> temp_converter
> speed_converter

### Function wise details:

**time_it:** This function takes in 1 or more positional arguments and 1 or more keyword arguments. The first positional argument is supposed to be a function name. Then the arguments for that function can be provided followed by repetitions and additional keyword arguments, if any.  
The function returns the average time taken by the function.

**squared_power_list:** This function takes exactly 1 positional argument. The position argument is the number for which powers would be calculated. All real numbers are accepted as valid inputs, including integers, floats and decimal types. Also, negative and 0 accepted as temperature by the function.  
The function also takes 2 keyword arguments start and end. The argument start denotes the lowest number to be used as power. The argument end denotes the highest number to be used as power. Both start and end, accept only positive integer values.  
The function returns the list with values from (number ** start) to (number ** end).

**polygon_area:** This function takes exactly 1 positional argument. The position argument is the side_length for the polygon for which area would be calculated. All positive real numbers are accepted as valid inputs, including integers, floats and decimal types.  
The function also takes 1 keyword argument - sides. The argument sides denotes the number of sides in the polygon. The argument - sides, accepts values from 3 to 6 only, i.e. for Triangle to Hexagon only.  
The function returns the area of the polygon with provided sides and side_length.

**temp_converter:** This function takes exactly 1 positional argument. The position argument is the temperature. All real numbers are accepted as valid inputs, including integers, floats and decimal types. Also, negative and 0 are accepted as temperature by the function.  
The function also takes 1 keyword argument - temp_given_in. The argument temp_given_in denotes the unit of the temperature provided. The argument - temp_given_in, accepts values 'f' and 'c' only. f stands for fahrenheit and c for celsius.  
The function returns the temperature in the unit other than the provided as temp_given_in.

**speed_converter:** This function takes exactly 1 positional argument. The position argument is the speed_given. The speed_given is assumed to be in km/hr. All real numbers are accepted as valid inputs, including integers, floats and decimal types. But, negative and 0 are NOT accepted as speed_given by the function.  
The function also takes 2 keyword arguments dist and time. The argument dist denotes the distance unit to be used for conversion. The argument time denotes the time unit to be used for conversion. Following are the accepted values for the keyword arguments:  
dist: 'km', 'm', 'ft', 'yrd'  
time: 'ms', 's', 'min', 'hr', 'day'  
The function returns the speed converted in the distance and time units as specified by the dist and time arguments.

### Test File:
Test cases have been implemented to assess the readme, naming standards, indentations, function wise valid and invalid cases.
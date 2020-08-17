from math import tan, pi
import decimal
from decimal import Decimal
import random
import decimal
import time

#1
#1 Timeit function which calculate Avg run time of functions
def time_it(fn, *args, repetitons= 1, **kwargs):
	'''
	Define time_it function
	'''
	avg_time = 0.0
	start = time.perf_counter()
	print(f'function called {fn}')
	print(f'positional Argument called *args {args}')
	print(f'loop repetitons defined {repetitons}')
	print(f'keyed Argument defined kwargs{kwargs}')
	for i in range(0,repetitons):
		fn(*args,**kwargs)
	end = time.perf_counter()
	avg_time = (end-start)/repetitons
	print(f'Avg time taken for {repetitons} runs is {avg_time}')
	return avg_time

#2
#2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
def squared_power_list(num, start=0, end=5):
	'''
	define the squared power list function
	'''
	if (not isinstance(num,int)) and (not isinstance(num,float)) and (not isinstance(num,Decimal)):
		raise TypeError("Invalid data type of input number given")

	if  not isinstance(start,int):
		raise TypeError("Only Integer allowed as a start")

	if not isinstance(end, int):
		raise TypeError("Only Integer allowed as end")

	if start<0:
		raise ValueError("Please provide positive start as value")

	if end<0:
		raise ValueError("please provide positive end as value")

	if end<start:
		raise ValueError("end should be greater then start")

	if (num < 0):
		raise ValueError("Input number should be positive as given ")

	power = []
	for i in range(start,end+1):
		power.append(num**i)
	print(f'squared_power_list define calculates as : {power}')
	return power

#3
# 15 is the side length. This polygon supports area calculations of upto a hexagon
def polygon_area(side_len, sides = 3):
	'''
	Define polygon_area function
	'''
	try:
		if not isinstance(sides,int):
			raise TypeError("Only Integer allowed as a start")

		if (not isinstance(side_len,int)) and (not isinstance(side_len,float)) and (not isinstance(side_len,Decimal)):
			raise TypeError("Please provide valid sides length")

		if side_len<0:
			raise ValueError("side length cannot be negative")

		poly_area =0.0
		if bool(side_len) and (side_len > 0):
			if sides < 0 or (sides < 3 or sides > 6):
				raise ValueError(f'ValueError: Invalid number of {sides}. Should not be negative and must be >=3 or =< 6')
			else:
				print(f'This polygon supports Area of calculations of upto a hexagon')
				poly_area = (sides * (side_len ** 2) / (4 * tan(pi / sides)) )
				return poly_area
		return poly_area
	finally:
		pass

#4
# 100 is the base temperature given to be converted only to 'Celsius' and 'Fahrenheit'
def temp_converter(base_temp, temp_given_in = 'f'):
	'''
	define temperature convertor
	'''
	try:
		if (not isinstance(base_temp,int)) and (not isinstance(base_temp,float)) and (not isinstance(base_temp,Decimal)):
			raise TypeError("Please provide valid input temp ")

		if temp_given_in not in ('c', 'f'):
			raise ValueError("provide the unit as c or f only")

		out_temp = 0.0
		if bool(base_temp):
			if temp_given_in == 'f':
				out_temp = ( (base_temp - 32) * (5 / 9) )
				print(f' base_temp given as {temp_given_in} and conversion to Celsius {out_temp}')
				return out_temp
			elif temp_given_in == 'c':
				out_temp = ( (base_temp * (9/5) ) + 32 )
				print(f' base_temp given as {temp_given_in} and conversion to Fahrenheit {out_temp}')
				return out_temp
			else:
				raise ValueError(f"Invalid input temp. Temp given {temp_given_in} Should be 'f' or 'c'")
		return out_temp
	finally:
		pass

#5 
#dist can be km/m/ft/yrd,
#time can be ms/s/m/hr/day,
#speed given by user is in kmph
def speed_converter(input_speed, dist='km', time='min'):
	'''
	define speed_Converter function
	'''
	try:
		if (not isinstance(input_speed,int)) and (not isinstance(input_speed,float)) and (not isinstance(input_speed,Decimal)):
			raise TypeError("please provide valid data type for Input speed")

		if (not isinstance(dist, str)):
			raise TypeError("input distance conversion should not be string")

		if (not isinstance(time, str)):
			raise TypeError("input time conversion should not be string")

		if time not in ('ms','s','min','hr','day'):
			raise ValueError("Time units can be only among [ms,s,min,hr,day]")

		if dist not in ('km','m','ft','yrd'):
			raise ValueError("Distance units can be only among [km, m, fr, yrd]")

		if input_speed<0:
			raise ValueError("speed cannot be negative")

		dist_dict ={'km' : 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.61 }
		time_dict = {'ms': 3.6e+6 , 's': 3600, 'min': 60, 'hr': 1, 'day': 1/24}

		if dist not in dist_dict:
			raise ValueError(f"Invalid : Distance given :{dist} not valid as per defined metric ")

		if time not in time_dict:
			raise ValueError(f"Invalid : Time given :{time} not valid as per defined metric ")

		result_speed=0.0
		if isinstance(input_speed,Decimal):
			result_speed = Decimal(input_speed) * Decimal(( dist_dict[dist] / time_dict[time] ))
			return result_speed
		
		if isinstance(input_speed,float):
			result_speed = float(input_speed) * float(( dist_dict[dist] / time_dict[time] ))
			return result_speed
		
		if isinstance(input_speed,int):
			result_speed = input_speed * ( dist_dict[dist] / time_dict[time] )
			print(f'Input Speed : {input_speed} kmph converted to  Distance {dist} and Time {time} as result :{result_speed}')
			print(f'Conversion Distance : {dist} as {dist_dict[dist]} and Time : {time} as {time_dict[time]}')
		return result_speed
	finally:
		pass
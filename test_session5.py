import pytest
import inspect
import re

from session5 import speed_converter
from session5 import temp_converter
from session5 import polygon_area
from session5 import squared_power_list

from decimal import Decimal
import session5
import copy
import random
import os
import math

CHECK_FOR_FUNCTIONS = [
'speed_converter',
'temp_converter',
'polygon_area',
'squared_power_list',
'time_it',
]


#1
def test_print():
	f1 = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
	assert isinstance(f1, float), "print function time avg"


### Test time_it Test Case ###
#2
def test_time_it():
	assert session5.time_it(print, 1000)> 0,'time_it not working as expected'

#3
def test_invalid_time_it():
	with pytest.raises(NameError):
		session5.time_it(printer, 1)


### tests for squared_power_list ###
#4
def test_squared_power_list():
	f2 = session5.time_it(squared_power_list, 2, start=0, end=5, repetitons=5)
	#2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
	assert isinstance(f2, float), "squared squared_power_list function Avg time is float"

#5
def test_squared_power_list_extra_args():
	with pytest.raises(TypeError):
		session5.squared_power_list(2,4, start=0, end=5)

#6
def test_squared_power_list_extra_kwargs():
	with pytest.raises(TypeError):
		session5.squared_power_list(2,start=0,end=5,interval=1)

#7
def test_squared_power_list_int_args():
	assert [1,2,4,8,16,32] == session5.squared_power_list(2,start=0,end=5), 'squared_power_list Not working as expected.!'

#8
def test_squared_power_list_float_args():
	assert [1.0,2.0,4.0,8.0,16.0,32.0] == session5.squared_power_list(2.0,start=0,end=5), 'squared_power_list Not working as expected.!'

#9
def test_squared_power_invalid_input_num():
	with pytest.raises(TypeError):
		session5.squared_power_list('2',start=0,end=5)

#10
def test_squared_power_list_invalid_start():
	with pytest.raises(TypeError):
		session5.squared_power_list(2,start='0',end=5)

#11
def test_squared_power_list_invalid_end():
	with pytest.raises(TypeError):
		session5.squared_power_list(2,start=0,end='5')

#12
def test_squared_power_list_negative_input():
	with pytest.raises(ValueError):
		session5.squared_power_list(-2, start=1, end=5)

#13
def test_squared_power_list_negative_start():
	with pytest.raises(ValueError):
		session5.squared_power_list(2, start=-1, end=5)

#14
def test_squared_power_list_negative_end():
	with pytest.raises(ValueError):
		session5.squared_power_list(2, start=0, end=-2)

### test for Polygon area calculation

#15
# 15 is the side length. This polygon supports area calculations of upto a hexagon
def test_time_it_polygon_area_float():
	f3 = session5.time_it(polygon_area, 15, sides = 3, repetitons=10)
	assert isinstance(f3, float), "print function time avg"

#16
def test_time_it_polygon_area_nonzero():
	assert session5.time_it(polygon_area,15,sides = 3,repetitons=10) > 0, 'time_it Function for Polygon_area should be greate then Zero.!'

#17
def test_polygon_area_extra_args():
	with pytest.raises(TypeError):
		session5.polygon_area(15,10,sides=4)

#18
def test_polygon_area_extra_kwargs():
	with pytest.raises(TypeError):
		session5.polygon_area(15,sides=4,base=5)

#19 
def test_polygon_area_int_result():
	assert int(session5.polygon_area(15,sides=4)) == 225, 'Polygon area calculation not happeing as expected.!'

#20
def test_polygon_area_float_result():
	assert round((session5.polygon_area(15,sides=4)),2) ==225.00, 'Polygon area calculation not happeing as expected.!'

#21
# def test_polygon_area_decimal_result():
# 	assert session5.polygon_area(Decimal('15'),sides=4) == Decimal('225'), 'Polygon area calculation not happeing as expected.!'

#22
def test_polygon_area_incorrect_side_len():
	with pytest.raises(TypeError):
		session5.polygon_area('2', sides=4)

#23
def test_polygon_area_incorrect_sides():
	with pytest.raises(TypeError):
		session5.polygon_area(15,sides='4')

#24
def test_polygon_area_negative_side_len():
	with pytest.raises(ValueError):
		session5.polygon_area(-5,sides=4)

#25
def test_polygon_area_sides_range_constraint_lessthen():
	with pytest.raises(ValueError):
		session5.polygon_area(15,sides=1)

#26
def test_polygon_area_sides_range_constraint_grt_then():
	with pytest.raises(ValueError):
		session5.polygon_area(15,sides=9)

### test time convertor of F and C ###
#27
def test_temp_converter():
	f4 = session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
	# 100 is the base temperature given to be converted
	assert isinstance(f4, float), "print function time avg"

#28
def test_temp_converter_extra_args():
	with pytest.raises(TypeError):
		session5.temp_converter(100, 0, temp_given_in='f')

#29
def test_temp_converter_extra_kwargs():
	with pytest.raises(TypeError):
		session5.temp_converter(100, temp_given_in='f', extra='c')

#30
def test_temp_converter_valid_args_int():
	assert session5.temp_converter(86, temp_given_in='f') == 30, 'temp_converter not working as expected.!'

#31
def test_temp_converter_valid_args_float():
	assert round((session5.temp_converter(86.0, temp_given_in='f')),2) == 30.00, 'temp_converter not working as expected.!'

#32
# def test_temp_converter_valid_args_decimal():
# 	assert session5.temp_converter(Decimal('86'), temp_given_in='f') == Decimal('30'), 'temp_converter not working as expected.!'

#33
def test_temp_converter_valid_args_fahrenheit():
	assert session5.temp_converter(140, temp_given_in='f') == 60, 'temp_converter not working as expected.!'

#34
def test_temp_converter_valid_args_celsius():
	assert session5.temp_converter(40, temp_given_in='c') == 104, 'temp_converter not working as expected.!'

#35
def test_temp_converter_invalid_input_value():
	with pytest.raises(TypeError):
		session5.temp_converter('100', temp_given_in='f')

#36
def test_temp_converter_invalid_input_temp():
	with pytest.raises(ValueError):
		session5.temp_converter(100, temp_given_in='k')

#37
def test_temp_converter_negative_input():
	assert session5.temp_converter(-4, temp_given_in='f') == -20, 'temp_converter not working as expected.!'

#38
def test_temp_converter_non_string_int():
	with pytest.raises(ValueError):
		session5.temp_converter(100, temp_given_in=0)

### test speed convertor ###
#dist can be km/m/ft/yrd,
#time can be ms/s/m/hr/day,
#speed given by user is in kmph

#39
def test_speed_converter():
	f5= session5.time_it(speed_converter, 100, dist='km', time='min', repetitons=200)
	assert isinstance(f5, float), "print function time avg"

#40
def test_speed_converter_extra_args():
	with pytest.raises(TypeError):
		session5.speed_converter(100, 20, dist='km', time='min')

#41
def test_speed_converter_extra_kwargs():
	with pytest.raises(TypeError):
		session5.speed_converter(200, dist='km', time='min', extra=1)


#42 #input speed kmph
def test_speed_converter_valid_args_given_int_speed():
	assert 60 == session5.speed_converter(3600, dist='km', time='min'), "speed_converter is not working as expected"

#43
def test_speed_converter_valid_args_given_float_speed():
	assert 60.00 == round((session5.speed_converter(3600.0, dist='km', time='min')),2), "speed_converter is not working as expected"

#44
# def test_speed_converter_valid_args_given_decimal_speed():
# 	assert Decimal('60') == session5.speed_converter(Decimal('3600'), dist='km', time='min'), "speed_converter is not working as expected"

#45
def test_speed_converter_invalid_value_speed_given():
	with pytest.raises(ValueError):
		session5.speed_converter(-300, dist='km', time='min')

#46
def test_speed_converter_invalid_value_dist():
	with pytest.raises(ValueError):
		session5.speed_converter(100, dist='miles', time='min')

#47
def test_speed_converter_invalid_value_time():
	with pytest.raises(ValueError):
		session5.speed_converter(100, dist='km', time='year')

#48
def test_speed_converter_invalid_type_speed_given():
	with pytest.raises(TypeError):
		session5.speed_converter('100', dist='km', time='min')

#49
def test_speed_converter_invalid_type_dist():
	with pytest.raises(TypeError):
		session5.speed_converter(100, dist=0, time='min')

#50
def test_speed_converter_invalid_type_time():
	with pytest.raises(TypeError):
		session5.speed_converter(100, dist='km', time=['min'])

#51
def test_speed_converter_name_error_dist():
	with pytest.raises(NameError):
		session5.speed_converter(100, dist=yrd, time='min')

#52
def test_speed_converter_name_error_time():
	with pytest.raises(NameError):
		session5.speed_converter(100, dist='km', time=hr)


### test README file ###
#53
def test_function_name_had_cap_letter():
	functions = inspect.getmembers(session5, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#54
def test_indentations():
	''' Returns pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(session5)
	spaces = re.findall('\n +.', lines)
	for space in spaces:
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

#55
def test_all_functions_exist():
	code_lines = inspect.getsource(session5)
	for word in CHECK_FOR_FUNCTIONS:
		assert word in code_lines, 'Have you heard of Pinocchio?'

#56
def test_readme_exists():
	assert os.path.isfile("README.md"), "README.md file missing!"

#57
def test_readme_contents():
	readme = open("README.md", "r")
	readme_words = readme.read().split()
	readme.close()
	assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

#58
def test_readme_file_for_formatting():
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	assert content.count("#") >= 10

#59
def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	for c in CHECK_FOR_FUNCTIONS:
		if c not in content:
			READMELOOKSGOOD = False
			pass
	assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
"""
lab4.py
Arjun Padaliya
1/30/2018
"""

def squared(num_list):
	"""
	Squares numbers in num_list
	num_list:list of numbers
	Returns:list of these numbers squared
	"""
	new_list=[]
	for num in num_list:
		sq_num=pow(num, 2)
		new_list.append(sq_num)
	return new_list

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and aren't title case
	title_list: list of strings
	Returns: list of strings that are titles
	"""
	for item in title_list:
		if not item.istitle():
			title_list.remove(item)
	return title_list


def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
	key: string that is the name of the inventory item
	value: integer that equals the number of that item currently on had
	Returns: updated dictionary where each inventory item is restocked
	"""
	new_inventory={}
	for item in inventory:
		new_inventory[item]=inventory[item]+10

	return new_inventory


def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: a dictionary with:
	key: string that is the name of the inventory item
	value: integer that equals the number of that item currently on had
	Returns: the same inventory_dict with any item had 0 quantity removed
	"""
	for k in inventory.copy():
		if inventory[k] == 0:
			inventory.pop(k)
	return inventory

def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	"""
	avg_grades={}
	for student_grade in grades: #get grades for every individual student
		#print (grades[student_grade])
		avg_grades[student_grade]=sum(grades[student_grade])/len(grades[student_grade])
	return avg_grades

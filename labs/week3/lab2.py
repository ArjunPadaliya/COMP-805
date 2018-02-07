"""
lab2.py
Arjun Padaliya
1/30/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	num_list:list of numbers
	Returns:list of these numbers squared
	"""
	for indx in range(0,len(num_list)):
		num_list[indx]=num_list[indx]**2

	return num_list

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
	for item in inventory:
		inventory[item]+=10

	return inventory


def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: a dictionary with:
	key: string that is the name of the inventory item
	value: integer that equals the number of that item currently on had
	Returns: the same inventory_dict with any item had 0 quantity removed
	"""
	new_list=[]

	for item in inventory:
		if inventory[item]==0:
			new_list.append(item)

	for keys in new_list:
		del inventory[keys]

	return inventory

def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
	key: string of students name
	value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	"""
	for student in grades: #get grades for every individual student
		total_marks=0 #initialize total_marks
		for marks in grades[student]: #iterate over list of marks of each student
			total_marks+=marks #sum up all the marks
		#update value of that student in dictionary (grades) by dividing total marks with available number of marks in list
		grades[student]=total_marks/len(grades[student])

	return grades

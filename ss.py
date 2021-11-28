#!/usr/bin/env python3

import os
import sys
import glob
import time
import random

input_file = sys.argv[1]

# set up dir for individual Secret Santa assignment files
if not os.path.exists('assignments'):
    os.makedirs('assignments')

# delete any previous assignment files
old_assignments = glob.glob('assignments/*.txt')
for txt_file in old_assignments:
        os.remove(txt_file)

# get lines of input file
with open(input_file, 'r') as f:
	lines = f.readlines()
	input_lines = [ele.strip() for ele in lines]

givers = []
receivers = []

# add participants to givers and receivers lists
for line in input_lines:
        # if comma in line, add both people
	if ',' in line:
		givers.append(line.split(',')[0])
		givers.append(line.split(',')[1])
		receivers.append(line.split(',')[0])
		receivers.append(line.split(',')[1])
        # otherwise just add the one person on the line
	else:
		givers.append(line)
		receivers.append(line)

# romantic partners dictionary
partners = {}

# iterate through each participant to fill partners dictionary
for person in givers:
        # exact match of person's name in line means no partner listed on same line
	if person in input_lines:
		partners[person] = ''
        # otherwise, find the line where the person is listed, set partner as value 
	else:
		for line in input_lines:
			if person in line.split(','):
				person_index = line.split(',').index(person)
				if person_index == 1:
					partner_index = 0
				else:
					partner_index = 1
				partners[person] = line.split(',')[partner_index]

# just for fun
print('\nAssigning partners...')
time.sleep(2)
print('\nbeep bop boop...\n')
time.sleep(2)

# function to assign Secret Santa partners
def assign(list1, list2):
	assignment_dict = {}
	for x in range(len(list1)):
		random_giver = random.choice(list1)
		random_receiver = random.choice(list2)
		assignment_dict[random_giver] = random_receiver
		list1.remove(random_giver)
		list2.remove(random_receiver)
	return assignment_dict

assignments = assign(givers, receivers)

# if anyone was assigned themselves or partner, try again
while any(pair[0] == pair[1] or partners[pair[0]] == pair[1] for pair in assignments.items()):
        # have to refill giver/receiver lists, as they got widdled down during assigning
	for line in input_lines:
		if ',' in line:
			givers.append(line.split(',')[0])
			givers.append(line.split(',')[1])
			receivers.append(line.split(',')[0])
			receivers.append(line.split(',')[1])
		else:
			givers.append(line)
			receivers.append(line)
        # re-assign partners
	assignments = assign(givers, receivers)

# make individual Secret Santa .txt files, named after giver, with receiver's name
for assignment in assignments.items():
    with open(f'assignments/{assignment[0]}.txt', 'w') as f:
        f.write(assignment[1])

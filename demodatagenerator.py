# -*- coding: utf-8 -*-
""" An example of how to use Hansoft's GraphQL API

Will generate example projects, groups and users.
Depends on:
-- qlient v. 1.0.0
"""
import sys
import math
import random
import datetime

from graphqlclient import HansoftGraphQLClient
from loremgenerator import LoremGenerator

URL = 'http://localhost:4000/graphql'
USER = 'Administrator'
PASSWORD = 'hpmadm'

SHARE_ADMINS = 0.1
SHARE_MAIN_MANAGERS = 0.1

client = HansoftGraphQLClient(URL, USER, PASSWORD)
lorem = LoremGenerator()

users = input("How many users? ")

try:
	users = int(users)
	if users < 1:
		users = 1
	elif users > 1000:
		users = 1000
except ValueError:
	print("Not a number.")
	sys.exit(0)

groups = input("How many groups? ")

try:
	groups = int(groups)
	if groups < 1:
		groups = 1
	elif groups > 1000:
		groups = 1000
except ValueError:
	print("Not a number.")
	sys.exit(0)

projects = input("How many projects? ")

try:
	projects = int(projects)
	if projects < 1:
		projects = 1
	elif projects > 1000:
		projects = 1000
except ValueError:
	print("Not a number.")
	sys.exit(0)

# Generate lorem data
start = datetime.datetime.now()
user_names = lorem.generateList(users, lorem.USER)
print("Generated user names in:", datetime.datetime.now()-start)

start = datetime.datetime.now()
group_names = lorem.generateList(groups, lorem.GROUP)
print("Generated group names in:", datetime.datetime.now()-start)

start = datetime.datetime.now()
project_names = lorem.generateList(projects, lorem.PROJECT)
print("Generated project names in:", datetime.datetime.now()-start)

# Create the users
created_users = 0
user_list = []
admin_list = []
target_admins = math.ceil(users * SHARE_ADMINS)
duplicates = 0
start = datetime.datetime.now()
for user in user_names:
	user_id = client.createNormalUser(user)
	if user_id == -1:
		# Duplicate - skip
		print("Skipping Duplicate:", user)
		continue
	if user_id == 0:
		sys.exit(0)
	client.enableLogin(user_id)
	user_list.append(user_id)
	if len(admin_list) < target_admins:
		client.enableAdmin(user_id)
		admin_list.append(user_id)
	created_users = created_users + 1
print("Added users in:", datetime.datetime.now()-start)

# Create the groups
created_groups = 0
group_list = []
target_members = math.ceil(users / groups )
duplicates = 0
start = datetime.datetime.now()
all_users_group = None
for group in group_names:
	group_id = client.createUserGroup(group)
	if group_id == -1:
		# Duplicate - skip
		print("Skipping Duplicate:", group)
		continue
	if group_id == 0:
		sys.exit(0)
	# Add the user to the group
	if not all_users_group:
		all_users_group = client.addUsersToGroup(group_id, user_list)
		print("All users are in group with id", all_users_group)
	else:
		members = 0
		users_to_add = []
		while members <= target_members:
			users_to_add.append(int(random.choice(user_list)))
			members = members + 1	
		client.addUsersToGroup(group_id, users_to_add)
	created_groups = created_groups + 1
print("Added groups in:", datetime.datetime.now()-start)

# Create the projects
created_projects = 0
projects_list = []
target_main_managers = math.ceil(users * SHARE_MAIN_MANAGERS)
duplicates = 0
start = datetime.datetime.now()
for project in project_names:
	project_id = client.createProject(project)
	if project_id == -1:
		# Duplicate - skip
		print("Skipping Duplicate:", group)
		continue
	if project_id == 0:
		sys.exit(0)
	projects_list.append(project_id)
	client.addGroupToProject(project_id, all_users_group)
	main_managers = 0
	for u in user_list[0:target_main_managers]:
		client.enableMainManager(project_id, u)
		main_managers = main_managers + 1

	created_projects = created_projects + 1
print("Added projects in:", datetime.datetime.now()-start)

print("*** DONE ***")
sys.exit(0)
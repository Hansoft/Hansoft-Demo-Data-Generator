# -*- coding: utf-8 -*-
""" An example of how to use generate users, groups and projects in Hansoft as demo data."""
import sys
import math
import random

from graphqlclient import HansoftGraphQLClient
from loremgenerator import LoremGenerator

URL = 'http://localhost:4000/graphql'
USER = 'Administrator'
PASSWORD = 'hpmadm'

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

# Create the users
created_users = 0
user_list = []
admin_list = []
target_admins = math.ceil(users * 0.1)
while created_users < users:
	# Create a new user
	user = lorem.generateUserName()
	user_id = client.createNormalUser(user)
	if user_id == -1:
		# Duplicate - try again
		continue
	if user_id == 0:
		sys.exit(0)
	client.enableLogin(user_id)
	user_list.append(user_id)
	if len(admin_list) < target_admins:
		client.enableAdmin(user_id)
		admin_list.append(user_id)
	created_users = created_users + 1

# Create the groups
created_groups = 0
group_list = []
target_members = math.ceil(users / groups )
while created_groups < groups:
	# Create a new user group
	group = lorem.generateGroupName()
	group_id = client.createUserGroup(group)
	if group_id == -1:
		# Duplicate - try again
		continue
	if group_id == 0:
		sys.exit(0)
	# Add the user to the group
	members = 0
	users_to_add = []
	while members <= target_members:
		users_to_add.append(int(random.choice(user_list)))
		members = members + 1	
	client.addUsersToGroup(group_id, users_to_add)
	created_groups = created_groups + 1
	
# Create the projects
created_projects = 0
projects_list = []
target_main_managers = math.ceil(users * 0.1)

while created_projects < projects:
	# Create a new project
	project = lorem.generateProjectName()
	project_id = client.createProject(project)
	if project_id == -1:
		# Duplicate - try again
		continue
	if project_id == 0:
		sys.exit(0)
	projects_list.append(project_id)
	main_managers = 0
	for u in user_list:
		# Add the user to the project
		client.addUserToProject(project_id, u)

		# Make main manager
		if main_managers < target_main_managers:
			client.enableMainManager(project_id, u)
			main_managers = main_managers + 1

	created_projects = created_projects + 1


print("*** DONE ***")

sys.exit(0)

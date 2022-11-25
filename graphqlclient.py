# -*- coding: utf-8 -*-
""" An example of how to use Hansoft's GraphQL API

Depends on:
-- qlient v. 1.0.0
"""
import requests

from qlient.http import HTTPClient
from qlient.http.backends import HTTPBackend

class HansoftGraphQLClient():
	def __init__(self, url, user, password):
		self.url = url
		if not self.login(user, password):
			print("Could not login")
			return
		self.setupAuthenticatedClient()
			
	def login(self, user, password):
		query = """mutation login($loginCredentials:LoginUserInput!){
		  login(loginUserInput:$loginCredentials){
		    access_token}
		}
		"""

		variables = {"loginCredentials": {
		    'username': user,
		    'password': password
		  }}
		  
		try:
			r = requests.post(self.url, json={'query': query, 'variables':variables})
			r.raise_for_status()
		except requests.HTTPError as http_err:
			print(f'HTTP error occured: {http_err}')
			return False
		except Exception as err:
			print(f'Other error occured: {err}')
			return False

		json = r.json()

		self.token = json["data"]["login"]["access_token"]	
		return True
		
	def setupBasicClient(self):
		self.client = HTTPClient(self.url)

	def setupAuthenticatedClient(self):
		session = requests.Session()
		session.headers["Authorization"] = f"Bearer {self.token}"
		self.client = HTTPClient(HTTPBackend(self.url, session=session))
		
	"""
	List
	"""
		
	def listUsers(self):
		response = self.client.query.users(["name"])
		users = []
		for p in response.data["users"]:
			users.append(p["name"])
		return users
		
	def listGroups(self):
		response = self.client.query.userGroups(["name"])
		groups = []
		for p in response.data["userGroups"]:
			groups.append(p["name"])
		return groups

	def listProjects(self):
		response = self.client.query.projects(["name"])
		projects = []
		for p in response.data["projects"]:
			projects.append(p["name"])
		return projects
		
	""""
	Create
	"""
		
	def createProject(self, name):
		projectPropertiesInput = {"name": name}
		r = self.client.mutation.createProject(projectPropertiesInput=projectPropertiesInput, _fields=["id", "name"])
		if r.errors:
			if r.errors[0]["message"] == "Project with that name already exists":
				return -1
			else:
				print(r.request.query)
				print(r.request.variables)
				print(r.errors)
				return 0
		else:
			return r.data["createProject"]["id"]
		
	def createNormalUser(self, name):
		userPropertiesInput = {"name": name, "password": "hpmadm"}
		r = self.client.mutation.createNormalUser(userPropertiesInput=userPropertiesInput, _fields=["id", "name"])
		if r.errors:
			if r.errors[0]["message"] == "User with that name already exists":
				return -1
			else:
				print(r.request.query)
				print(r.request.variables)
				print(r.errors)
				return 0

		else:
			return r.data["createNormalUser"]["id"]

	def createUserGroup(self, name):
		userGroupInput = {"name": name}
		r = self.client.mutation.createUserGroup(userGroupInput=userGroupInput, _fields=["id", "name"])
		if r.errors:
			if r.errors[0]["message"] == "User group with that name already exists":
				return -1
			else:
				print(r.request.query)
				print(r.request.variables)
				print(r.errors)
				return 0
		else:
			return r.data["createUserGroup"]["id"]
			
	"""
	Update
	"""
	def enableLogin(self, user_id):
		userPropertiesInput = {"id": user_id, "accessRights": {"isActiveAccount": True, "documentManagement": True, "dashboards": True, "dashboardPageShare": True, "avatarManagement": True}}
		r = self.client.mutation.updateNormalUser(userPropertiesInput=userPropertiesInput, _fields=["id", "name"])
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)

		else:
			return r.data["updateNormalUser"]["id"]

	def enableAdmin(self, user_id):
		userPropertiesInput = {"id": user_id, "accessRights": {"admin": True, "portfolioAllocation": True}}
		r = self.client.mutation.updateNormalUser(userPropertiesInput=userPropertiesInput, _fields=["id", "name"])
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)

		else:
			return r.data["updateNormalUser"]["id"]
			
	def addUserToGroup(self, group_id, user_id):
		userGroupInput = {"id": group_id, "userIDs": [user_id]}
		r = self.client.mutation.updateUserGroup(userGroupInput=userGroupInput, _fields=["id", "name"])
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)
		else:
			return r.data["updateUserGroup"]["id"]
			
	def addUsersToGroup(self, group_id, user_list):
		userGroupInput = {"id": group_id, "userIDs": user_list}
		r = self.client.mutation.updateUserGroup(userGroupInput=userGroupInput, _fields=["id", "name"])
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)
		else:
			return r.data["updateUserGroup"]["id"]
			
	def addUserToProject(self, project_id, user_id):
		r = self.client.mutation.addProjectUser(projectID=project_id, userID=user_id, _fields=["id", "name"])
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)
		else:
			return r.data["addProjectUser"]["id"]	
			
	def enableMainManager(self, project_id, user_id):
		accessRights = {"isMainManager": True, "canAccessProjectHistory": True}
		r = self.client.mutation.updateProjectUserAccessRights(projectID=project_id, userID=user_id, accessRights=accessRights)
		if r.errors:
			print(r.request.query)
			print(r.request.variables)
			print(r.errors)
		else:
			return True

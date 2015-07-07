
import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 										#current working directory 
sys.path.append(current_working_directory + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *																#imports all from module git, because exceptions file needs to be imported


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		join = os.path.join														#creates a git.Repo object to represent your repository.
		temp_dir = "/home/vac/clone_test/tester/testing/"

		def repo_check(temp_dir):												#code checks for .git in the folder	
			try :										
				repo = Repo(temp_dir)
				#self.view.insert(edit, 0, str(repo))
			except InvalidGitRepositoryError :									#exception handled when .git is not found
					forwd_slash_index = temp_dir.rfind('/', 0, len(temp_dir))   #finds index of last forward slash

					#self.view.insert(edit, 0, str(forwd_slash_index))
					
					temp_dir = temp_dir[0:forwd_slash_index]					#goes up one file level
					
					#self.view.insert(edit, 0, temp_dir)
					
					if forwd_slash_index == 0 :									#if file not versioned by git
						self.view.insert(edit, 0, "broken")
					else :														#recursive call to repo_check with upper file level
						repo_check(temp_dir)

		repo_check(temp_dir)													#function call to repo_check


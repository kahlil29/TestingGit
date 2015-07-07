
import sublime, sublime_plugin
import os
import sys

current_working_directory = os.getcwd() 										#current working directory 
sys.path.append(current_working_directory + "/lib/python3.4/site-packages")		#Tells sublime python interpreter where modules are store

from git import *

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
		repo = Repo('/home/vac/TestingGit')
		o = repo.remotes.origin
		o.pull()
		o.push()
		self.view.insert(edit, 0, "Complete")


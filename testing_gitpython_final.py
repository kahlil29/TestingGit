import sublime, sublime_plugin
import os
import sys

sys.path.append("/home/vac/.config/sublime-text-3/Packages/User/lib/python3.4/site-packages")


from git import Repo



class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")

		join = os.path.join

		repo = Repo("/home/vac/testing_git")
		repo_c = Repo.init("/home/vac/gitpython.git")

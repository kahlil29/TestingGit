import sublime, sublime_plugin
import os
import sys
sys.path.append('/home/Rohit/.config/sublime-text-3/Packages/User/lib/python3.4/site-packages')
import git 
from git import Repo
repo = git.Repo('/home/rohit/Documents/test')

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		repo = git.Repo('/home/rohit/Documents/test')
		pass

class myOpener(sublime_plugin.EventListener): 
	def on_post_save(self,view):
		sublime.message_dialog(str(repo.git.status()))
		sublime.message_dialog("Saved")
		sublime.message_dialog(str(repo.git.add('rohit1')))
		sublime.message_dialog(str(repo.git.commit(m='commiting for save')))

		sublime.message_dialog("and now it has been committed")
		sublime.message_dialog(str(repo.git.status()))
		pass
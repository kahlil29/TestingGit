

import  sublime,sublime_plugin, json, uuid, subprocess, os
from datetime import datetime
import time

import shutil

#Global list of thread objects
list_of_threads = []
new_list_of_threads = []



class Thread:

	def __init__(self, region,thread_key = None , comment_string = None,list_of_comments = [], is_resolved = False):
		#When reading from the file
		if ( thread_key == None):
			self.thread_key = str(uuid.uuid4())
		#when initializing from plugin
		else:
			self.thread_key = thread_key

		# region changing from string to sublime region object
		self.region = region

		self.is_resolved = is_resolved

		#When reading from the file
		if (comment_string == None):
			self.list_of_comments = list_of_comments
		#when initializing from plugin
		else:
			cobj = Comment(comment_string)
			list_of_comments.append(cobj)
			self.list_of_comments = list_of_comments

	#find thread object by region
	def find_thread(name_of_region): 
		for x in list_of_threads:
			if (x.thread_key == name_of_region):
				return x



	#Encode to JSON using Thread and comment Encoder and write to file
	@staticmethod
	def write_list_threads(plist_of_threads):
		with open('/home/User/Desktop/datafile.json', 'w') as f:
			json.dump([ThreadEncoder(indent = 1).default(x) for x in plist_of_threads], f, cls = ThreadEncoder, indent = 1)


	@staticmethod
	def WriteCreateThreadFolder(pcurrent_file_directory, plist_of_threads):

		thread_path = pcurrent_file_directory + '/Comments' #Checks if a Comments folder is present

		if os.path.exists(thread_path):
			shutil.rmtree(thread_path)
			os.makedirs(thread_path)

		for x in plist_of_threads:
			
			thread_path = pcurrent_file_directory + '/Comments' #Checks if a Comments folder is present

			thread_path = pcurrent_file_directory + '/' + 'Comments' + '/' + str(x.thread_key) #Creates a folder for a thread

			os.makedirs(thread_path)

			with open(thread_path + '/' + '1' + '.txt', 'w') as fl:
				fl.write( str(x.region) +"\n" + x.thread_key + "\n" + str(x.is_resolved))
			for y in x.list_of_comments:
				with open(thread_path + '/' + y.timestamp + '.txt', 'w') as fl:
					fl.write(y.username + '\n' + y.comment_key + '\n' + y.comment_string + "\n" +y.timestamp)



	#Reading thread from file
	@staticmethod
	def read_thread():
		with open('/home/aaron/Desktop/datafile.json', 'r') as fl:
			new_list_of_threads = json.load(fl)
			return(new_list_of_threads)


	#Coverting JSON data from string back to Thread and Comment Class objects
	@staticmethod
	def converting_from_file_to_new_list_of_threads(pnew_list_of_threads):
		pnewer_list_of_threads = [Thread( sublime.Region(int(list(x["region"].split(','))[0]),int(list(x["region"].split(','))[1])),
			list_of_comments = [ Comment(y["comment_string"],y["comment_key"],y["username"],y["timestamp"]) for y in x["list_of_comments"] ],
			is_resolved = x["is_resolved"]) for x in pnew_list_of_threads]
		return pnewer_list_of_threads


	#add thread to list of thread objects
	def add_thread(self, plist_of_threads):
		plist_of_threads.append(self)


	#add new comment to thread
	def add_comment(self, comment_string):
		cobj = Comment(comment_string)
		self.list_of_comments.append(cobj)



def read_multiple_files(pcurrent_file_directory): #reading from multiple files directly into sublime Data Structure

		for root, dirs, files in os.walk(pcurrent_file_directory + '/' + 'Comments'):
			local_list_of_comments = []
			for name in files:

				if (name !=  '1.txt'):
					with open(os.path.join(root,name), 'r') as fl:
						content = fl.readlines()
						c = Comment(str(content[2])[0:-1],str(content[1])[0:-1],str(content[0])[0:-1],str(content[3])[0:-1])
						local_list_of_comments.append(c)

			for name in files:
				if (name == '1.txt'):
					with open(os.path.join(root,name), 'r') as fl:
						content = fl.readlines()
						reg = str(content[0])[1:-2]
						t = Thread( (sublime.Region(int(list(reg.split(','))[0]),int(list(reg.split(','))[1]))), 
							thread_key = str(content[1])[0:-1],  comment_string = None, list_of_comments = local_list_of_comments, 
							is_resolved = str(content[2])[0:-1])
						t.add_thread(list_of_threads)
		return list_of_threads



class Comment:

	def __init__(self, comment_string = None, comment_key = None, username = None, timestamp =None):

		#while adding comment for for first time in thread
		if(comment_key == None):

			#getting username from terminal
			git_uname = subprocess.Popen("git config user.name", shell=True, stdout=subprocess.PIPE).stdout.read()
			self.username = str(git_uname.decode("utf-8"))[0:-1]


			self.comment_key = str(uuid.uuid4())

			self.comment_string = comment_string

			#getting timestamp and doing string manipulation to truncate
			timestamp_string = str(datetime.now())
			self.timestamp = timestamp_string[0:timestamp_string.rfind(".")]


		#while adding comment from  .comments file
		else:
			self.username = username
			self.comment_key = comment_key
			self.comment_string = comment_string
			self.timestamp = timestamp





class ThreadEncoder(json.JSONEncoder):

	def default(self, obj):

		#getting rid of "" marks
		changed_region = str(obj.region)[1:-2]

		#Encoding into JSON
		if isinstance(obj, Thread):
			return {"thread_key":obj.thread_key, "region":changed_region, "is_resolved":obj.is_resolved, 
			"list_of_comments":[CommentEncoder(indent = 1).default(x) for x in obj.list_of_comments]}
		return json.JSONEncoder.default(self, obj)



#similar to ThreadEncoder function
class CommentEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Comment):
			return {"username":obj.username,"comment_key":obj.comment_key, 
					"comment_string":obj.comment_string, "timestamp":obj.timestamp}
		return json.JSONEncoder.default(self, obj)

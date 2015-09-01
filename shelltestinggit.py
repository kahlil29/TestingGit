import subprocess
import os


pwd = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE).stdout.read()
print pwd
cwd = pwd[:-1]	#get the directory without file name and extra new line char to use in popen
pwd = cwd
print cwd
print subprocess.Popen("git status", cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()
current_file = str(os.path.abspath(__file__))		#directory including filename for add
print subprocess.Popen("git add "+current_file, cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("git status", cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("git commit -m\"commit to git staging area\"", cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("git pull origin master", cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()
print subprocess.Popen("git push origin master", cwd = pwd, shell=True, stdout=subprocess.PIPE).stdout.read()


# a = str("helloworld")
# a = a [:-2]
# print a

# #print subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE).stdout.read()
# print subprocess.Popen("git add --all", cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# print subprocess.Popen("git commit -m\"2nd commit to check subp\"", cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# print subprocess.Popen("git pull origin master", cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# #print subprocess.Popen("git push origin master", cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# print subprocess.Popen("git status", cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# a = "check.txt"

# subprocess.Popen("subl "+a, cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
# current_file = str(os.path.abspath(__file__))		#directory including filename for add
# print subprocess.Popen("git add "+current_file, cwd = r'/home/kahlil/TestingGit', shell=True, stdout=subprocess.PIPE).stdout.read()
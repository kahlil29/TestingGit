from git import Repo
import os
join = os.path.join

repo = Repo("/home/vac/testing_git")
repo_c = Repo.init("/home/vac/gitpython.git")
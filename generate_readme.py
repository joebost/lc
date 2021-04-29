import os
from fnmatch import fnmatch

class ProblemData:
  def __init__(self, file):
    open_file = open(file, 'r')
    self.file_path = file
    self.problem_number = open_file.readline().rstrip().strip("# ")
    self.problem_link = open_file.readline().rstrip().strip("# ")
    date_strs = [line.rstrip().strip("## ") for line in open_file.readlines() if "##" in line]
    print(date_strs)
    # TODO
    open_file.close()

  def print(self):
    print(self.problem_number + " " + self.problem_link)

repo_url = "https://github.com/joebost/lc/blob/main/"
exclude = set((".git", "README", "template.py", "update.py"))
solution_files = {}

# get all files
for path, subdirs, files in os.walk("."):
  for file in files:
    if fnmatch(file, "*.py") and file not in exclude:
      file_path = os.path.join(path, file)
      solution_files[file_path] = ProblemData(file_path)
      solution_files[file_path].print()


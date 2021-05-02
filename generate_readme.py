import os
from datetime import datetime
from fnmatch import fnmatch

REPO_URL = "https://github.com/joebost/lc/blob/main/"
EXCLUDE_FILES = set((".git", "README", "template.py", "generate_readme.py"))
class Problem:
  def __init__(self, file):
    open_file = open(file, "r")
    self.file_path = file
    self.name = file.split("/")[-1].replace(".py", "").replace("-", " ").capitalize()
    self.type = file.split("/")[1].capitalize()
    self.problem_number = open_file.readline().rstrip().strip("# ")
    self.problem_link = open_file.readline().rstrip().strip("# ")
    open_file.close()

  def to_markdown_title(self):
    title = "[" + self.name + "](" + self.problem_link + ") - " + self.type + " [(solution)](" + REPO_URL + self.file_path.strip("./") + ")"
    return title

class ReadMe:
  def __init__(self):
    self.months = {}

  def add_problem(self, file : str, date : datetime):
    month = date.strftime("%B %Y")
    if month not in self.months:
      self.months[month] = []
    if file in self.months[month]:
      return
    else:
      self.months[month].append(file)

  def print(self):
    for month in self.months.keys():
      print(month + "\n")
      for problem in self.months[month]:
        print(problems[problem].to_markdown_title())

def get_solution_file_paths():
  solution_files = []
  for path, subdirs, files in os.walk("."):
    for file in files:
      if fnmatch(file, "*.py") and file not in EXCLUDE_FILES:
        file_path = os.path.join(path, file)
        solution_files.append(file_path)
  return solution_files

def create_problems(solution_files):
  problems = {}
  for file in solution_files:
    problems[file] = Problem(file)
  return problems

def add_solved_dates_to_readme(solution_files, readme : ReadMe):
  for file in solution_files:
    open_file = open(file, "r")
    date_strs = set([line.rstrip().strip("## ") for line in open_file.readlines() if "##" in line])
    for date_str in date_strs:
      date = datetime.strptime(date_str, "%m/%d/%y")
      readme.add_problem(file, date)

def write_to_readme(readme : ReadMe, problems):
  open_file = open("README.md", "w")
  open_file.truncate(0)
  for month in readme.months.keys():
    line = "[" + month + "](#" + month.lower().replace(" ", "-") + ")\n\n"
    open_file.write(line)

  for month in readme.months.keys():
    month_title = "### " + month + "\n"
    open_file.write(month_title)
    for problem in readme.months[month]:
      problem_title = "1. " + problems[problem].to_markdown_title() + "\n"
      open_file.write(problem_title)
  open_file.close()


solution_files = get_solution_file_paths()
problems = create_problems(solution_files)
readme = ReadMe()

add_solved_dates_to_readme(solution_files, readme)
write_to_readme(readme, problems)


# get all files

      # date_strs = [line.rstrip().strip("## ") for line in open_file.readlines() if "##" in line]
      # self.dates = [datetime.strptime(d, "%m/%d/%y") for d in date_strs]




"""
Expected output:

Table of Contents
April 2021
May 2021

April 2021
1. Two Sum (code) 2x
13. Problem2 (code)

May 2021
"""

"""
Algorithm
for each file
create a Problem object
members should be
- name
- number
- lc link
- code link

in each file search for dates
create new date -> problem mapping
have a group for each month, add problems
create object for problem within a month
"""

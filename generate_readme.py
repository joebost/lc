import os
from datetime import datetime
from fnmatch import fnmatch
import attr

REPO_URL = "https://github.com/joebost/lc/blob/main/"
EXCLUDE_FILES = set((".git", "README", "template.py", "generate_readme.py", ".venv", ".vscode"))

@attr.s(kw_only=True, frozen=True, auto_attribs=True)
class Problem:
  problem_name: str;
  problem_type: str;
  problem_number: int;
  problem_link: str;
  solution_link: str;
  file_path: str;

def create_problem(file_path: str) -> Problem:
  open_file = open(file_path, "r")
  problem_name = file_path.split("/")[-1].split(".")[0].replace("-", " ").capitalize()
  problem_type = file_path.split("/")[1].capitalize()
  problem_number = open_file.readline().rstrip().strip("# ")
  problem_link = open_file.readline().rstrip().strip("# ")
  solution_link = REPO_URL + file_path.strip("./")
  open_file.close()

  return Problem(
    problem_name=problem_name,
    problem_type=problem_type,
    problem_number=problem_number,
    problem_link=problem_link,
    solution_link=solution_link,
    file_path=file_path,
  )

def problem_markdown_title(problem: Problem) -> str:
  return "[" + problem.problem_name + "](" + problem.problem_link + ") - " + problem.problem_type + " [(solution)](" + problem.solution_link + ")"

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

def get_all_problem_files():
  problem_files = []
  for path, dirs, files in os.walk("."):
    [dirs.remove(d) for d in list(dirs) if d in EXCLUDE_FILES]
    for file in files:
      if file not in EXCLUDE_FILES and file.endswith((".py", ".sh")):
        file_path = os.path.join(path, file)
        problem_files.append(file_path)
  return problem_files

def create_problems(solution_files):
  problems = {}
  for file in solution_files:
    problems[file] = create_problem(file)
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
      problem_title = "1. " + problem_markdown_title(problems[problem]) + "\n"
      open_file.write(problem_title)
  open_file.close()

def main():
  all_problem_files = get_all_problem_files()
  problems = create_problems(all_problem_files)
  readme = ReadMe()

  add_solved_dates_to_readme(all_problem_files, readme)
  write_to_readme(readme, problems)

if __name__ == "__main__":
  main()
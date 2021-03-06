import sys

from app.scripts.helpers import *
from app.structures.models.user import *
from app.structures.models.course import *
from app.structures.models.gradebook import *

if __name__ == "__main__":
  username = raw_input("Username: ")
  
  user = getUser(username)

  if user == None:
    print "Could not find the user you specified"
    sys.exit(1)

  for i, c in enumerate(user.courseStudent):
    print "%d) %s" % (i, c.name)

  index = int(raw_input("Pick a course: "))

  course = user.courseStudent[index]

  for i, a in enumerate(course.assignments):
    print "%d) %s" % (i, a.name)

  index = int(raw_input("Pick an assignment: "))

  assignment = course.assignments[index]

  for i, p in enumerate(assignment.problems):
    print "%d) %s" % (i, p.name)

  index = int(raw_input("Pick a problem: "))

  problem = assignment.problems[index]

  subNum = problem.getSubmissionNumber(user)

  subPath = problem.getFilePath(user, subNum)

  print subPath
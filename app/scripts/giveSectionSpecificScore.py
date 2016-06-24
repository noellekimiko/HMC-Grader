import sys

from app.scripts.helpers import *
from app.helpers.autograder import *

from app.structures.models.user import *

from datetime import datetime

if __name__ == "__main__":
  courseName = raw_input("Course Name: ")
  semester = raw_input("Course Semester: ")

  course = getCourse(semester, courseName)

  if course == None:
    print "Could not find the course you specified"
    sys.exit(1)

  for i, a in enumerate(course.assignments):
    print "%d) %s" % (i, a.name)

  index = int(raw_input("Pick an assignment: "))

  assignment = course.assignments[index]

  for i, p in enumerate(assignment.problems):
    print "%d) %s" % (i, p.name)

  index = int(raw_input("Pick a problem: "))

  problem = assignment.problems[index]
  
  for i, sec in enumerate(problem.rubric):
    print "%d) %s" % (i, sec)

  section = raw_input("Pick a section (Type the name): ")

  ##### REPLACE THESE LINES TO CUSTOMIZE DIRECTLY #####
  comments = raw_input("Set the comments: ")
  score = float(raw_input("Set the score: "))
  #####################################################

  students = User.objects.filter(courseStudent=course)

  for s in students:
    print s.username
    sub = problem.getLatestSubmission(s)
    if sub == None:
      continue

    #set the grade
    sub.grade.scores[section] = score
    sub.grade.save()
    sub.comments = comments
    sub.status = SUBMISSION_GRADED
    sub.save()

import sys

from app.scripts.helpers import *
from app.helpers.autograder import *

from app.structures.models.user import *
from app.userViews.student.submitFiles import createSubmission

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

  comments = "Yay for extra credit"
  section = "Points"
  score = 5

  students = User.objects.filter(courseStudent=course)

  for s in students:
    print "Student: " + s.username
    sub = problem.getLatestSubmission(s)
    if sub == None:
      continue

    #set the grade
    sub.status = SUBMISSION_GRADED
    sub.save()

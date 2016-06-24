import sys

from app.scripts.helpers import *
from app.structures.models.user import *
from app.structures.models.course import *

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

  students = User.objects.filter(courseStudent=course)

  for s in students:
    print s.username
    sub = problem.getLatestSubmission(s)
    if sub == None:
      continue

    # Modify the latest submission
    if sub.grade.totalScore() == 0.0:
      sub.status = SUBMISSION_TESTED
      sub.save()
    else:
      continue
    

#
# re-grader!
#

import sys, re

from app.scripts.helpers import *
from app.helpers.autograder import *
from app.structures.models.user import *
from app.structures.models.course import *

if __name__ == "__main__":

  #courseName = raw_input("Course Name: ")
  courseName = u"CS60"  # Green section!


  #I'm not sure how to actually find this secret 'semester' information... aargh!
  # someday it will be done better ;-)
  #semester = raw_input("Course Semester: ")
  semester = u"Spring 16"    # don't know if the u is needed, but I'm going with it!

  course = getCourse(semester, courseName)

  if course == None:
    print "Could not find the course you specified"
    sys.exit(1)
  else:
    print "DID find the course - nice work!"
    print "courseName is", courseName
    print "semester is", semester

  # Assignments
  # for i, a in enumerate(course.assignments):
  #   print "%d) %s" % (i, a.name)
  # index = int(raw_input("Pick an assignment: "))
  assignment = course.assignments[3]

  # Problems
  # for i, p in enumerate(assignment.problems):
  #   print "%d) %s" % (i, p.name)
  # index = int(raw_input("Pick a problem: "))
  problem = assignment.problems[2]

  # File
  # for i, f in enumerate(problem.getStrictFiles()):
  #   print "%d) %s" % (i, f)
  # index = int(raw_input("Pick a file: "))
  fileToSearch = problem.getStrictFiles()[0]

  # safety!! (copy elsewhere)
  #print "Exiting..."
  #sys.exit(1)
  # safety!!

  # Students
  students = User.objects.filter(courseStudent=course)
  #print >> sys.stderr, '# of students:', len(students)
  studentsToRegrade = []
  for s in students:
    print "Student: " + s.username
    subNum = problem.getSubmissionNumber(s)

    if subNum != 0:
      filePath = problem.getFilePath(s, subNum)
      # 
      # this is the line you would want to change per desired function name
      #
      RACKET_TEST_REGEX = r"\(check-equal"
      with open(filePath + "/" + fileToSearch, 'r') as studentFile:
        text = studentFile.read()
        # searchResult = re.findall(RACKET_TEST_REGEX, text,re.MULTILINE)
        # if len(searchResult) >= 8:

        if "map" in text:
          print "true"
        else:
          studentsToRegrade += [s.username]

  # safety!! (copy elsewhere)
  print "studentsToRegrade:", studentsToRegrade
  print "Exiting..."
  sys.exit(1)
  # safety!!

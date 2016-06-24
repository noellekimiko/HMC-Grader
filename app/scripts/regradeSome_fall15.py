#
# ./app/scripts/regradeSome_fall15.py
#

import sys

from app.scripts.helpers import *
from app.helpers.autograder import *

from app.structures.models.user import *
from app.userViews.student.submitFiles import createSubmission

from datetime import datetime

# constants from app/structures/models/course.py
#Some constants for doing submission status stuff
def sub_lookup( num ):
  if num == 0: return "SUBMISSION_UNGRADED"
  if num == 1: return "SUBMISSION_TESTING"
  if num == 2: return "SUBMISSION_TESTED"
  if num == 3: return "SUBMISSION_GRADING"
  if num == 4: return "SUBMISSION_GRADED"
  return "NO IDEA! num = " + str( num )
"""
SUBMISSION_UNGRADED = 0
SUBMISSION_TESTING = 1
SUBMISSION_TESTED = 2
SUBMISSION_GRADING = 3
SUBMISSION_GRADED = 4
"""

if __name__ == "__main__":

  # 
  # check these first!
  #  
  #   courseName and semester
  # 
  courseName = u"CS5GR"     #raw_input("Course Name: ")
  courseName = u"CS5G"      #raw_input("Course Name: ")
  courseName = u"CS5B"      #raw_input("Course Name: ")
  semester = u"Fall 15"     #raw_input("Course Semester: ")

  # remember to check the section
  # below section = index, but for a few they're not the same

  course = getCourse(semester, courseName)

  if course == None:
    print "Could not find the course you specified"
    sys.exit(1)
  else:
    print "DID find the course you were looking for..."
    print "course: ", courseName
    print "semester: ", semester

  for i, a in enumerate(course.assignments):
    print "%d) %s" % (i, a.name)

  index = int(raw_input("Pick an assignment: "))

  assignment = course.assignments[index]

  for i, p in enumerate(assignment.problems):
    print "%d) %s" % (i, p.name)

  index = int(raw_input("Pick a problem: "))

  problem = assignment.problems[index]

  #comments = "Autograded..."  # move this down
  #section = "hw4pr0"
  #score = 0

  students = User.objects.filter(courseStudent=course)

  for s in students:
    print "Student: " + s.username,
    sub = problem.getLatestSubmission(s)

    if sub == None:
      # for the next run...
      #print " SHOULD NOT BE HERE! "
      print "unsubmitted!"
      continue
      """
      print "... creating submission...", 
      sub, _ = createSubmission(problem, s)
      sub.isLate = False
      sub.save()
      problem.save()

      # in case I forget...
      comments = "Unsubmitted..."
      score = 0

      # place this inside the above if sub == None block
      # in order to ONLY grade the no-submissions
      sub.grade.scores[section] = score
      sub.grade.save()
      sub.comments = comments
      sub.status = SUBMISSION_GRADED
      sub.save()
      print "... grading done."
      """

    else:
      print "status: ", sub_lookup( sub.status ),
      num = sub.status
      if num == 0: 
        print "REGRADING..."
        regradeSubmission.delay(sub)
      if num == 1: 
        print "REGRADING..."
        regradeSubmission.delay(sub)
      if num == 2:
        print "nothing..."
      if num == 3:
        print "nothing..."
      if num == 4:
        print "nothing..."

 
#    elif sub.status == SUBMISSION_GRADED:
#      # if you want to not touch the already-graded ones...
#      print "Already graded"
#      continue    # not really needed, but...
#      # end of if you don't want to touch the already-graded ones...
#      #print "... it was submitted...",
#      #print "continuing...",
#      # want to change the score?
#      """
#      score = 5
#      section = "hw4pr0"
#      sub.grade.scores[section] = score
#      score = 0
#      section = "hw4pr1"
#      sub.grade.scores[section] = score
#      sub.grade.save()
#      #comments = "Thank you for this thoughtful reponse to the reading here!"  # move this down
#      sub.comments = "Nice response to the reading!"
#      sub.status = SUBMISSION_GRADED
#      sub.save()
#      """
#      #continue
#
#      """
#    elif sub.status == SUBMISSION_TESTED:
#      print "autograded - finalizing",
#      comments = "This problem was auto-graded... (please see tests)"  # move this down
#      sub.comments = comments
#      sub.status = SUBMISSION_GRADED
#      sub.save()
#      print "complete"
#      continue
#      """
#
#    else:
#      print "... it was submitted... but NOT autograded",
#      score = 25
#      section = "total"   # is this possibly correct?
#      sub.grade.scores[section] = score
#      sub.grade.save()
#      comments = "Because this was auto-graded, all points for this problem are in hw6pr1..."  # move this down
#      comments = "Very nice... 5/5 here."  # move this down
#      comments = "Lab problem (auto-graded): VPython!!"  # move this down
#      comments = "We're grading the milestones as labs. Final-project grading is this evening..."  # move this down
#      comments = "Great!"  # move this down
#      comments = "Lab problem: full credit for coming to lab. \n(Join us next week, too!) \n"  # move this down
#      sub.comments = comments
#      sub.status = SUBMISSION_GRADED
#      sub.save()
#      print "... grading done."
#

  pass



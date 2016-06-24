import sys

from app.scripts.helpers import *
from app.helpers.autograder import *

from app.structures.models.user import *
from app.userViews.student.submitFiles import createSubmission

from datetime import datetime

if __name__ == "__main__":
  courseName = u"IST338"  #raw_input("Course Name: ")
  courseName = u"CS 5"  #raw_input("Course Name: ")
  semester = u"Spring 15"    #raw_input("Course Semester: ")

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

  comments = "Autograded..."  # move this down
  section = "hw9pr1"
  score = 25

  students = User.objects.filter(courseStudent=course)

  for s in students:
    print "Student: " + s.username,
    sub = problem.getLatestSubmission(s)
    if sub == None:
      # for the next run...
      #print " SHOULD NOT BE HERE! "
      continue
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

    elif sub.status == SUBMISSION_GRADED:
      # if you want to not touch the already-graded ones...
      print "Already graded"
      continue    # not really needed, but...
      # end of if you don't want to touch the already-graded ones...
      #print "... it was submitted...",
      #print "continuing...",
      # want to change the score?
      score = 5
      section = "hw4pr0"
      sub.grade.scores[section] = score
      score = 0
      section = "hw4pr1"
      sub.grade.scores[section] = score
      sub.grade.save()
      #comments = "Thank you for this thoughtful reponse to the reading here!"  # move this down
      sub.comments = "Nice response to the reading!"
      sub.status = SUBMISSION_GRADED
      sub.save()
      print "... grading done."
      #continue

    else:
      print "... it was submitted...",
      print "continuing...",
      score = 25
      sub.grade.scores[section] = score
      sub.grade.save()
      comments = "Keep coming to lab!"  # move this down
      sub.comments = comments
      sub.status = SUBMISSION_GRADED
      sub.save()
      print "... grading done."


  pass



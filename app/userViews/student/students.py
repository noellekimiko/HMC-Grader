# -*- coding: utf-8 -*-

#import the app and the login manager
from app import app

from flask import g, request, render_template, redirect, url_for, flash, send_file, abort
from flask import jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required

from flask.ext.mongoengine import DoesNotExist

from werkzeug import secure_filename

from app.structures.models.user import *
from app.structures.models.gradebook import *
from app.structures.models.course import *

from app.structures.forms import SubmitAssignmentForm, AttendanceForm
from app.helpers.autograder import gradeSubmission

from app.helpers.filestorage import *
from app.plugins.latework import getLateCalculators

import os, datetime, shutil

from app.helpers.gradebook import getStudentAssignmentScores, getStudentAuxScores

@app.route('/assignments/<cid>')
@login_required
def studentAssignments(cid):
  '''
  Function Type: View Function
  Template: student/assignments.html
  Purpose: Display to a student user all of the assignments which they can
  submit homework to.

  Inputs:
    cid: The object ID for the course the student is viewing

  Template Parameters:
    course: The Course object given by <cid>

  Forms Handled: None
  '''
  try:
    c = Course.objects.get(id=cid)
    #For security purposes we send anyone who isnt in this class to the index
    if not ( c in current_user.courseStudent):
      abort(403)

    return render_template("student/assignments.html", course=c)
  except Course.DoesNotExist:
    #If the course can't be found then 404
    abort(404)



@app.route('/assignments/view/<pid>/<subnum>')
@login_required
def viewProblem(pid,subnum):
  '''
  Function Type: View Function
  Template: student/viewsubmission.html
  Purpose: Allow a student to view their submission and feedback from the
  autograder and the student graders.

  Inputs:
    pid: The object ID of the problem that this submission belongs to
    subnum: Which submission by the student should be viewed

  Template Parameters:
    course: The course which contains the problem
    assignment: The assignment group containing the problem
    problem: The problem object specified by <pid>
    subnum: The number of the current submission
    submission: The Submission object for this submission

  Forms Handled: None
  '''
  try:
    p = Problem.objects.get(id=pid)
    c, a = p.getParents()
    #For security purposes we send anyone who isnt in this class to the index
    if not ( c in current_user.courseStudent):
      abort(403)

    submission = p.getSubmission(current_user, subnum)

    return render_template("student/viewsubmission.html", \
                            course=c, assignment=a, problem=p,\
                             subnum=subnum, submission=submission)
  except (Problem.DoesNotExist, Course.DoesNotExist, AssignmentGroup.DoesNotExist):
    #If either p can't be found or we can't get its parents then 404
    abort(404)
  return redirect(url_for('studentAssignments', cid=cid))

'''
Backend upload/download functions
'''

@app.route('/assignments/send/<pid>/<uid>/<subnum>/<filename>')
@login_required
def sendFiles(pid, uid, subnum, filename):
  '''
  Function Type: Callback-Download
  Purpose: Downloads the file specified for the user.

  Inputs:
    pid: The object ID of the problem that the file belongs to
    uid: The object ID of the user the file belongs to
    subnum: The submission number that the file belongs to
    filename: The filename from the submission to download
  '''
  try:
    p = Problem.objects.get(id=pid)
    c,a = p.getParents()
    #For security purposes we send anyone who isnt in this class to the index
    if not ( c in current_user.courseStudent or c in current_user.gradingCourses()):
      abort(403)

    u = User.objects.get(id=uid)

    s = p.getSubmission(u, subnum)

    filepath = getSubmissionPath(c, a, p, u, subnum)

    return send_file(os.path.join(filepath, filename))
  except (Problem.DoesNotExist, Course.DoesNotExist, AssignmentGroup.DoesNotExist):
    #If either p can't be found or we can't get its parents then 404
    abort(404)

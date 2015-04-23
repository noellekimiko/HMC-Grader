# coding=utf-8

from app import app
import os, shutil, re

def cleanPath(path):
  '''
  Function Type: Helper
  Purpose: Replaces spaces with underscores and removes dots from filepaths so
  that the paths are clean and easier to type.
  '''
  path = path.replace(" ", "_")
  path = path.replace(".", "")
  return path

#
# Functions for creating filepaths
#

def getPhotoDir():
  path = os.path.join(app.config['STORAGE_HOME'], "photos")
  return path


def getUserPhotoDir():
  return os.path.join(getPhotoDir(), 'user')

def getUserPhotoPath(user):
  path = os.path.join(getUserPhotoDir(), user.photoName)
  return path

def getPagePhotoDir(page):
  return os.path.join(getPhotoDir(), 'pages', str(page.id))

def getPagePhotoPath(page, name):
  path = os.path.join(getPagePhotoDir(page), name)
  return path

def getCoursePath(course):
  path = os.path.join(app.config['STORAGE_HOME'], "submissions")
  path = os.path.join(path, course.semester, course.name)
  #Make sure the filepath is clean
  path = cleanPath(path)

  return path

def getAssignmentPath(course, assignment):
  path = os.path.join(getCoursePath(course), assignment.name)
  #Make sure the filepath is clean
  path = cleanPath(path)

  return path

def getProblemPath(course, assignment, problem):
  #Course path
  path = os.path.join(getAssignmentPath(course, assignment), problem.name)
  #Make sure the filepath is clean
  path = cleanPath(path)

  return path

def getSubmissionPath(course, assignment, problem, user, subnum):
  #Course path
  path = os.path.join(getProblemPath(course, assignment, problem), user.username)
  #Join submission number
  path = os.path.join(path, str(subnum))
  #Make sure the filepath is clean
  path = cleanPath(path)

  return path

def getTestPath(course, assignment, problem):
  #Course path
  path = getProblemPath(course, assignment, problem)

  #Join test directory
  path = os.path.join(path, '.test')

  return path

def getCommentPath():
  path = os.path.join(app.config['STORAGE_HOME'], "comments")
  return path

#
# Function for moving a problem if it gets renamed
#

def moveProblemPath(course, assignment, problem, newName):
  path = getProblemPath(course, assignment, problem)
  newPath = os.path.join(getAssignmentPath(course, assignment), newName)
  newPath = cleanPath(newPath)

  shutil.move(path, newPath)

#
# Functions for making sure a file exists
#

def ensurePathExists(path):
  if not os.path.isdir(path):
    os.makedirs(path)

def removePath(path):
  shutil.rmtree(path)

#
# Functions for makeing sure that we are putting data in the right mount point
#

def checkMounted():
  '''
  Reads /proc/mounts to see if mntPoint is listed as mounted
  '''
  if not app.config['STORAGE_MOUNTED']:
    return

  with open('/proc/mounts', 'r') as mounts:
    if re.search(app.config['STORAGE_HOME'], mounts.read()):
      return
    else:
      raise Exception("""
Your request has been terminated because the backing filesystem is not mounted.
Please try again in a few minutes. If this error persists please contact an administrator""")

# coding=utf-8

#import the app
from app import app

from flask import g, request, render_template, redirect, url_for, flash, abort, jsonify
from flask.ext.login import current_user, login_required

from app.models.course import *
from app.models.pages import *

from app.forms import ProblemOptionsForm, AddTestForm

from werkzeug import secure_filename

@app.route('/page/view/id/<pgid>')
@login_required
def viewPage(pgid):
  page = Page.objects.get(id=pgid)
  return render_template('pages/viewpage.html', page=page)


@app.route('/page/edit/id/<pgid>')
@login_required
def editPage(pgid):
  if len(current_user.gradingCourses()) == 0:
    abort(403)
  page = Page.objects.get(id=pgid)
  return render_template('pages/editpage.html', page=page)

@app.route('/page/save/<pgid>', methods=['POST'])
@login_required
def savePage(pgid):
  try:
    if len(current_user.gradingCourses()) == 0:
      abort(403)
    page = Page.objects.get(id=pgid)
    content = request.get_json()
    page.text = content['text']
    page.title = content['title']
    page.generalView = content['generalView']
    page.studentView = content['studentView']
    page.grutorView = content['grutorView']
    page.grutorEdit = content['grutorEdit']
    page.save()
    return jsonify(res=True)
  except Exception as e:
    return jsonify(res=str(e))

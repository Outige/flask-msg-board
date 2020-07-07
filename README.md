# Flask Message Board

## `About`

This is a message board application that allows a user to send messages to various message boards. As well as update and delete messages made.

---

## `Technologies`

* flask
* jinja2
* sqlite
* html
* css
* bootstrap
* deploying website
* wsgi production server
* virtualenv
* CRUD

---

## `Inspiration`

* <a href="https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=1221s">Learn Flask for Python - Full Tutorial</a>

---

## `Setting up heroku`

### Before creating app:
$ touch Procfile  
&nbsp; &nbsp; &nbsp; &nbsp; in Procfile: &nbsp; `web: gunicorn wsgi:app`
$ touch runtime.txt  
&nbsp; &nbsp; &nbsp; &nbsp; in runtime.txt: &nbsp; `python-3.8.2`
$ pip3 freeze > requirements.txt

### Creating app:
* Make sure the directory is GIT
* Make commit
$ heroku login  
$ heroku create tieg-app2  
* Go to: heroku dash board > tieg-app2 > Settings > Add build pack > (+) Python  
$ git push heroku master

### Error checking:
$ heroku logs --app=message-board-flask --tail
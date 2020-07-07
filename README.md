# Flask Message Board

## `About`

This is a message board application that allows a user to send messages to various message boards. As well as update and delete messages made.  
<a href="https://tieg-app2.herokuapp.com/" target="_blank">Click here to see the deployed app</a>

---

## `Technologies`

* flask
* jinja2
* sqlite
* html
* css
* bootstrap
* deploying website
* heroku
* wsgi production server
* virtualenv
* CRUD

---

## `Inspiration`

* <a href="https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=1221s" target="_blank">Learn Flask for Python - Full Tutorial</a>
* <a href="https://www.youtube.com/watch?v=YnrEGDdJfSk" target="_blank">Bootstrap tutorial 9 - Tables
</a>

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

---

## `Todo`

* Favicon
* Better CSS
* update/delete better re-routing
* User functions
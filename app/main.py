from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    board = db.Column(db.String(32), nullable=False, default='DEFAULT')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return str(self.id) + ": " + self.message + ", " + self.board + "\n"

def get_boards(messages):
    boards = set()
    for message in messages:
        boards.add(message.board)
    return boards


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    print(request.method)
    messages = Message.query.order_by(Message.date_created).all()
    boards = get_boards(messages)
    filter = request.args.get('filter')
    if not filter or filter == '':
        filter = 'All'

    if request.method == 'GET':
        return render_template('index.html', messages=messages, boards=boards, filter=filter)
    elif request.method == 'POST':
        message = request.form['message']
        board = request.form['board']

        if message == '':
            return render_template('error.html', error="Message body can't be empty", status=400)
        if board == '':
            return render_template('error.html', error="Message board can't be empty", status=400)
        if board == 'All':
            return render_template('error.html', error="'All' is a reserved message board", status=400)
        new_message = Message(message=message, board=board)
        
        try:
            db.session.add(new_message)
            db.session.commit()
            messages = Message.query.order_by(Message.date_created).all()
            boards = get_boards(messages)
            filter = request.form['board']
            return render_template('index.html', messages=messages, boards=boards, filter=filter)
        except:
            return render_template('error.html', error="Something went wrong, we were unable to send your message", status=500)
    elif request.method == 'PUT':
        return 'PUT'
    else:
        return render_template('error.html', error="Something went wrong", status=500)


@app.route('/message/delete/<int:id>/filter/<string:filter>')
def delete(id, filter):
    message = Message.query.get_or_404(id)

    try:
        db.session.delete(message)
        db.session.commit()
        
        messages = Message.query.order_by(Message.date_created).all()
        boards = get_boards(messages)
        return render_template('index.html', messages=messages, boards=boards, filter=filter)
    except:
        return render_template('error.html', error="Something went wrong, we were unable to delete your message", status=500)

@app.route('/update/<int:id>/filter/<string:filter>')
def update(id, filter):
    messages = Message.query.order_by(Message.date_created).all()
    boards = get_boards(messages)
    # FIXME: would like to pass the filter somehow, probably in URL from the get
    return render_template('index.html', messages=messages, boards=boards, filter=filter, id=id)
    # return render_template('index.html', messages=messages, boards=boards)#, filter=filter)
    # return render_template('error.html', error="Something went wrong, we were unable to update your message", status=500)

@app.route('/message/update/<int:id>/filter/<string:filter>', methods=['POST'])
def update_message(id, filter):
    # return 'PUT'

    message = Message.query.get_or_404(id)
    message_text = request.form['message']
    board = request.form['board']
    if message_text == '':
        return render_template('error.html', error="Message body can't be empty", status=400)
    if board == '':
        return render_template('error.html', error="Message board can't be empty", status=400)
    if board == 'All':
        return render_template('error.html', error="'All' is a reserved message board", status=400)

    try:
        message.message = message_text
        message.board = board # FIXME: check on the board and message
        db.session.commit()

        messages = Message.query.order_by(Message.date_created).all()
        boards = get_boards(messages)
        return render_template('index.html', messages=messages, boards=boards, filter=filter)
    except:
        return render_template('error.html', error="Something went wrong, we were unable to update your message", status=500)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
import random
number = random.randrange(0, 9)
app = Flask(__name__)

def make_bold(function):
    pass

@app.route('/')
def hello_world():
    return '<h1><b>Guess a number between 0 and 9<b><h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<user_number>')
def is_correct(user_number):
    if int(user_number) == number:
        return '<h1 style= "color: green">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif int(user_number) < number:
        return '<h1 style= "color: red">Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style= "color: purple">too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    

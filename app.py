from flask import Flask, render_template, request, session, redirect
from python import reverser, is_a_multiple 

app = Flask(__name__)
app.secret_key = "k1a2n3"

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html",
        name="Yison Tech Hub") 
    else:
        word = request.form['word']
        result = reverser(word)
        return render_template("index.html", res = result)

@app.route("/about")
def about_us():
    return "welcome to the about page"

@app.route("/kannyiri")
def Myself():
    pass

@app.route("/game-of-multiples", methods=["POST", "GET"])
def multiple_game():

    session["start"] = True

    if request.method == "POST":
        session["user"] = request.form["name"]
        session["multiple"] = request.form['multiple']

        session["start"] = False

        return render_template("multiples.html", start=session["start"])
    else:
        return render_template("multiples.html", start=session["start"])

@app.route("/play", methods=["POST", "GET"])
def play():
    
    if request.method == "POST":
        total = 0

        if'score' in session.keys():
            total = int(session['score'])
        else:
            session['score'] = 0

        multiple = int(session['multiple'])
        num = int(request.form['number'])

        if is_a_multiple(num, multiple):
            session['score'] = total + num
            return render_template('multiples.html', score=session['score'])
        else:
            return render_template('game_over.html', score=session['score'] , user=session['user'])
    else:
        return render_template('multiples.html')

@app.route('/reset-game', methods=['POST'])
def reset():
    del session['score']
    del session['user']
    del session['multiple']
    del session['start']

    return redirect("/game-of-multiples")
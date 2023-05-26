from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lofi beats to code, debug, and cry to'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['user_name'] = request.form['user_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['options'] = request.form['options']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def show_results():
    return render_template('result.html')

@app.route('/home', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)

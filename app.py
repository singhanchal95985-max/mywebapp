from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add():
    note = request.form['note']
    notes.append(note)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    notes.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
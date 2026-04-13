from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#New route for part 1
@app.route('/part1')
def part1():
    return render_template('part1.html')

if __name__ == '__main__':
    app.run(debug=True)
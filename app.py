from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#New route for part 1
@app.route('/part1')
def part1():
    return render_template('part1.html')

#New route for part 2
@app.route('/part2')
def part2():
    return render_template('part2.html')

#New route for part 3
@app.route('/part3')
def part3():
    return render_template('part3.html')

if __name__ == '__main__':
    app.run(debug=True)
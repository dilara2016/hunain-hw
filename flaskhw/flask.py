from flaskhw.flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        year = int(request.form['year'])
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result = f"{year} is a leap year!"
        else:
            result = f"{year} is not a leap year."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

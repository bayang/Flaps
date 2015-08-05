from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        myfilename = f.filename
        myfileurl = url_for('static', filename=myfilename)
        return render_template('index.html', myfilename=myfilename,
                               myfileurl=myfileurl)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

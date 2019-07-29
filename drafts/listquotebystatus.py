import os
from flask import render_template
from flask import Flask
from flask import request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)


@app.route('/quotess/')
@app.route('/quotess/<status>')
def state(status=None):
    print(status)
    return render_template('quote.html', status=status, list=["open", "close", "pending"])


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            # to run in heroku uncomment this line and comment the port=5000 line
            # port=int(os.environ.get('PORT')),
            port=5000,
            debug=True)

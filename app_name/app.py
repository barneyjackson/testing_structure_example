from flask import Flask

import helpers
import db

app = Flask(__name__)


@app.route('/')
def index():
    db.create_db()
    helpers.helper_f()
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)

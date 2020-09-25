from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

from os import getenv
from dotenv  import load_dotenv

load_dotenv()

app_settings = getenv('APP_SETTINGS',None)
assert app_settings

app = Flask(__name__)
app.config.from_object(app_settings)
print(app_settings)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
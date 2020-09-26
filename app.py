from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

from os import getenv
from dotenv  import load_dotenv



load_dotenv()

app_settings = getenv('APP_SETTINGS',None)
assert app_settings

app = Flask(__name__)
app.config.from_object(app_settings)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app_settings)
db = SQLAlchemy(app)

from models import Result

@app.route('/', methods=['GET','POST'])
def index():
    errors = []
   # Result = {}
    if request.method == "POST":
          try:
              url = request.form['content']
              new_country = Result(pais=url)
              db.session.add(new_country)
              db.session.commit()
              return redirect('/')
          except:
              errors.append(
                  "imposible de obtener url.Favorcito de hacer bien la buscaqueda carnal"
              )
    contenido = Result.query.order_by(Result.country_id).all()
    return render_template('index.html',errors=errors,contenido=contenido)

if __name__ == "__main__":
    app.run(debug=True)
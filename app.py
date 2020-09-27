from flask import Flask,render_template,url_for,request,redirect,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

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
ma = Marshmallow(app)

from models import Result,ResultSchema

@app.route('/', methods=['GET','POST'])
def index():
    errors = []
   # Result = {}
    if request.method == "POST":
          try:
              url = request.form['content']
              new_country = Result(country=url)
              db.session.add(new_country)
              db.session.commit()
              return redirect('/')
          except:
              errors.append(
                  "imposible de obtener url.Favorcito de hacer bien la buscaqueda carnal"
              )
    key = 1          
    contenido = Result.query.order_by(Result.country_id).all()
    contenido_schema = ResultSchema(many=True)
    salida = contenido_schema.dump(contenido)
    #return render_template('index.html',errors=errors,jsonify(salida))

    return render_template('index.html',errors=errors)
         
@app.route('/sopa', methods=['GET','POST'] )
def sabor():
    contenido = Result.query.order_by(Result.country_id).all()
    contenido_schema = ResultSchema(many=True)
    salida = contenido_schema.dump(contenido)
    return jsonify({'data':salida})

@app.route('/download/pdf', methods=['GET','POST'])
def create_pdf():
    return "holaS"

if __name__ == "__main__":
    app.run(debug=True)
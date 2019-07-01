from flask import Flask
from views import page


app = Flask(__name__)
app.config['SECRET_KEY'] = 'eununcavouesquecerasenha'
app.register_blueprint(page)

if __name__ == '__main__':
    app.run(debug=True)

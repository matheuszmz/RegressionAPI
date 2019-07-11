from flask import Flask

from views import page

#app CONFIG
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '8FD1C2279CE9EE931E1BA1D2772C6'
app.register_blueprint(page)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

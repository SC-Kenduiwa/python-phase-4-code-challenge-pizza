from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('server/config.py')

@app.route('/')
def index():
    return f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI')}"

if __name__ == "__main__":
    app.run()

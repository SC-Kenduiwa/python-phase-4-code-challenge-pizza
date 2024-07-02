from flask import Flask

app = Flask(__name__)
config_path = 'server/config.py'
print(f"Attempting to load configuration from: {config_path}")

try:
    app.config.from_pyfile(config_path)
    print("Configuration loaded successfully.")
except Exception as e:
    print(f"Failed to load configuration: {e}")

print("SQLALCHEMY_DATABASE_URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))
print("SQLALCHEMY_TRACK_MODIFICATIONS:", app.config.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
print("SECRET_KEY:", app.config.get('SECRET_KEY'))

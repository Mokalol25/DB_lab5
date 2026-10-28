import yaml
from flask import Flask

from app.my_project.auth.route.user_route import user_bp
from app.my_project.auth.route.server_route import server_bp

app = Flask(__name__)

with open('app/config/app.yml', 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)
    app.config['DB_CONFIG'] = config['db']

@app.route('/')
def home():
    return {"message": "Flask server is running!"}, 200

app.register_blueprint(user_bp)
app.register_blueprint(server_bp)

if __name__ == '__main__':
    app.run(debug=True)
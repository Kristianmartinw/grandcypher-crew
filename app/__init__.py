import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from .models import db, User
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.archetype_routes import archetype_routes
from .api.archetype_values_routes import archetype_value_routes
from .api.character_routes import character_routes
from .api.charge_attack_routes import charge_attack_routes
from .api.element_routes import element_routes
from .api.party_routes import party_routes
from .api.race_routes import race_routes
from .api.skill_routes import skill_routes
from .api.specialty_routes import specialty_routes
from .api.support_skill_routes import support_skill_routes

from .seeds import seed_commands

from .config import Config

app = Flask(__name__)


login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(archetype_routes, url_prefix='/api/archetypes')
app.register_blueprint(archetype_value_routes, url_prefix='/api/archetype_values')
app.register_blueprint(character_routes, url_prefix='/api/characters')
app.register_blueprint(charge_attack_routes, url_prefix='/api/charge_attacks')
app.register_blueprint(element_routes, url_prefix='/api/elements')
app.register_blueprint(party_routes, url_prefix='/api/parties')
app.register_blueprint(race_routes, url_prefix='/api/races')
app.register_blueprint(skill_routes, url_prefix='/api/skills')
app.register_blueprint(specialty_routes, url_prefix='/api/specialties')
app.register_blueprint(support_skill_routes, url_prefix='/api/support_skills')
db.init_app(app)
Migrate(app, db)

CORS(app)

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')

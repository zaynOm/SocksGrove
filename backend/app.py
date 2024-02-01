# backend/app.py
from app import app, db
from app.routes.user_routes import user_bp


with app.app_context():
    db.create_all()

    # adding user routes bluprint to the app
    app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

def create_app():
    
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from rowingconditions import routes

        from rowingconditions.plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app
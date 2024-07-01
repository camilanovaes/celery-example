from app import create_app

flask = create_app()
app = flask.extensions["celery"]

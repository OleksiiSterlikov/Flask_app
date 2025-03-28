""" Main module """

#!/user/bin/env python
from app import create_app, db

app = create_app()

@app.shell_context_processor
def make_context():
    """Objects exposed here will be automatically available from the shell"""
    return dict(app=app, db=db)

if __name__ == "__main__":
    app.run()


from backend import app
from flask_ngrok import run_with_ngrok

if "__main__" == __name__:
    run_with_ngrok(app)
    app.run() # 127.0.0.1(localhost)

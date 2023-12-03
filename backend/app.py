import sys
sys.path.append('.')
from flask import Flask
from routes import index as routes_index

app = Flask(__name__)

# Register the routes
app.register_blueprint(routes_index.routes)

if __name__ == "__main__":
    app.run(debug=True)
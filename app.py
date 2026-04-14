from flask import Flask
from routes import inventory_routes

app = Flask(__name__)

# IMPORTANT LINE (YOU MISSED THIS)
app.register_blueprint(inventory_routes)

@app.route("/")
def home():
    return {"message": "Inventory API running"}

if __name__ == "__main__":
    app.run(debug=True)
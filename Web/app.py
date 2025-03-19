from flask import Flask, render_template, request, jsonify
from prediction import predict

app = Flask("__name__")

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")

@app.route("/model")
def model():
    return render_template("model.html")

@app.route("/files")
def files():
    return render_template("files.html")

@app.route('/predict', methods = ["POST"])
def predict_text():
    try:
        data = request.get_json()
        text_input = data["text"]

        prediction = predict([text_input])

        return jsonify({"Prediction": prediction[0]})

    except Exception as e:
        return jsonify({"Error" : str(e)})

if __name__ == "__main__":
    app.run(debug = True)
app.py


# from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
# from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from prediction import predict  # Import the predict function from prediction.py
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch

# # Initialize the Flask app
# app = Flask("__name__")

# # Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)

# # Set a secret key for session management
# app.secret_key = 'your_secret_key'

# # Dummy user database (username or email as key)
# users_db = {
#     'admin@example.com': {'password': generate_password_hash('admin123'), 'email': 'admin@example.com'},
#     'user@example.com': {'password': generate_password_hash('user123'), 'email': 'user@example.com'}
# }

# # Dummy User class for user management in Flask-Login
# class User:
#     def __init__(self, username, email):
#         self.id = username
#         self.email = email

#     def is_authenticated(self):
#         return True

#     def is_active(self):
#         return True

#     def is_anonymous(self):
#         return False

#     def get_id(self):
#         return self.id

# # Load user function required by Flask-Login
# @login_manager.user_loader
# def load_user(username):
#     if username in users_db:
#         return User(username, users_db[username]['email'])
#     return None

# @app.route("/sign", methods=["GET", "POST"])
# def sign():
#     if request.method == "POST":
#         email = request.form["email"]
#         if email:
#             # Store email in session
#             session['email'] = email
#             return redirect(url_for('sign_password'))
#         else:
#             flash("Please enter a valid email.")
#             return redirect(url_for('sign'))
#     return render_template("sign.html")

# @app.route("/sign_password", methods=["GET", "POST"])
# def sign_password():
#     if request.method == "POST":
#         email = session.get('email')
#         password = request.form['password']

#         # Check the password with the stored one
#         user_data = users_db.get(email)
#         if user_data and check_password_hash(user_data['password'], password):
#             user = User(email, user_data['email'])
#             login_user(user)
#             flash("Login successful!", "success")
#             return redirect(url_for('home'))  # Redirect to home or dashboard
#         else:
#             flash("Invalid email or password. Please try again.", "danger")
#             return redirect(url_for('sign'))
#     return render_template("sign.html")

# @app.route("/")
# @login_required  # Protect home route, requires login
# def home():
#     return render_template("index.html", user_name=current_user.id)

# @app.route("/model")
# @login_required  # Protect model route, requires login
# def model():
#     # Handle the model-related functionality here
#     return render_template("model.html")

# @app.route('/files')
# @login_required  # Protect files route, requires login
# def files():
#     return render_template("files.html")

# @app.route('/predict', methods=["POST"])
# def predict_text():
#     try:
#         # Get JSON data from the frontend
#         data = request.get_json()

#         # Ensure the "text" key is provided in the request data
#         if "text" not in data:
#             return jsonify({"Error": "Text input missing"}), 400

#         text_input = data["text"]  # Extract the text from the request

#         # Call your prediction function (the one defined in prediction.py)
#         prediction = predict([text_input])  # Assuming predict function accepts a list of texts

#         # Return the prediction result
#         return jsonify({"Prediction": prediction[0]})

#     except Exception as e:
#         return jsonify({"Error": str(e)}), 500


# # Route for logout
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash("You have been logged out.", "info")
#     return redirect(url_for('sign'))

# if __name__ == "__main__":
#     app.run(debug=True)

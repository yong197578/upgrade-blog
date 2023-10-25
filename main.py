from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post')
def post():
    return render_template("post.html")


users = {}


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register_username = request.form["email"]
        register_password = request.form["password"]
        users[register_username] = register_password
        return render_template("login.html")
    return render_template("register.html")


@app.route('/login', methods=["POST"])
def login():
    username = request.form["login_email"]
    password = request.form["login_pw"]
    if username in users and users[username] == password:
        return render_template("index.html")


print(users)

if __name__ == "__main__":
    app.run(debug=True)


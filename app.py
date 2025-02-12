from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greeting():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("greeting.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)

# Git Repo: https://github.com/tylerlisk/Simple-Flask-App
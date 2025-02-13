from flask import Flask, render_template, request

app = Flask(__name__)

user_feedback = {}

@app.route("/", methods=["GET", "POST"])
def greeting():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("index.html", name=name)

@app.route("/<user>/feedback_form", methods=["GET", "POST"])
def feedback(user):
    if request.method == "POST":
        feedback = request.form.get("feedback")
        user_feedback[user] = feedback
        return render_template("feedback.html", user_feedback=user_feedback)
    return render_template("feedback_form.html", name=user)

if __name__ == "__main__":
    app.run(debug=True)



# Git Repo: https://github.com/tylerlisk/Simple-Flask-App
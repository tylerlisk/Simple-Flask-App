from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = "my_secret_key"
user_feedback = {}

@app.route("/", methods=["GET", "POST"])
def greeting():
    name = None
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("index.html", name=name)

@app.route("/<user>/feedback_form", methods=["GET", "POST"])
def feedback_form(user):
    if request.method == "POST":
        feedback = request.form.get("feedback")
        user_feedback[user] = feedback
        flash(f"Thank you for your feedback {user}!", "success")
        return redirect(url_for("feedback"))
    
    return render_template("feedback_form.html", name=user)

@app.route("/feedback")
def feedback():
    return render_template("feedback.html", user_feedback=user_feedback)

if __name__ == "__main__":
    app.run(debug=True)



# Git Repo: https://github.com/tylerlisk/Simple-Flask-App
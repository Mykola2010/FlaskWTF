from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, SelectField, SelectMultipleField, RadioField

app = Flask(__name__)
app.config["SECRET_KEY"] = "AprioriKS"

@app.get("/search/")
def flask_form():
    return render_template("search.html")

@app.get("/auth/")
def flask_auth_form():
    return render_template("auth.html")

@app.get("/dosearch/")
def flask_form_do():
    search = request.args.get("search")
    return f"Find by {search}"

@app.post("/postsearch/")
def post_search():
    email = request.form.get("email")
    return f"Register by {email}"

class SubscriptionForm(FlaskForm):
    name = StringField("Name")
    email = EmailField("Email")
    submit = SubmitField("Send")

@app.get("/subscribe/")
def get_subs():
    form = SubscriptionForm()
    return render_template("subs.html", form=form)

@app.post("/subscribe/")
def post_subs():
    form = SubscriptionForm()
    return form.name.data

if __name__ == '__main__':
    app.run(port=33333)
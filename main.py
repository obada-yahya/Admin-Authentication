from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email


app = Flask(__name__)
app.secret_key = "obada yahya"


class MyForm(FlaskForm):
    email = EmailField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=3, max=12)])
    submit = SubmitField(label="submit")


@app.route("/", methods=["POST", "GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email)
        print(password)
        if email == "admin@gmail.com" and password == "123456789":
            return render_template("secret.html")
        else:
            return render_template("failed.html")
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

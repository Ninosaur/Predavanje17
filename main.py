from flask import Flask, render_template,request, make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():

    year = datetime.datetime.now().year

    poruka = "ovo je poruka iz main.py"

    gradovi = ["Zagreb", "Rijeka", "Split"]

    user = "Ivo Ivić"



    return render_template("index.html", year=year, poruka=poruka, gradovi=gradovi, user=user)




@app.route("/about", methods=["GET", "POST"])
def about():

    if request.method == "GET":
        user_name = request.cookies.get("user_name")

        return render_template("about.html", name=user_name)
    elif request.method == "POST":

        name = request.form.get("contact-name")
        prezime = request.form.get("contact-prezime")
        grad = request.form.get("grad")
        adresa = request.form.get("contact-adresa")
        email = request.form.get("contact-email")
        message = request.form.get("contact-message")

        print(name)
        print(prezime)
        print(grad)
        print(adresa)
        print(email)
        print(message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", name)

        return response








@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("contact-name")
    email = request.form.get("contact-email")
    message = request.form.get("contact-message")

    print(name)
    print(email)
    print(message)

    return render_template("success.html")


if __name__ == "__main__":
    app.run(use_reloader=True)



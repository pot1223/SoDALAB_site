from flask import Blueprint, render_template

soda = Blueprint(
    "soda",
    __name__,
    template_folder="templates",
    static_folder = "static",
)


@soda.route("/")
def index():
    return render_template("soda/home.html")

@soda.route("/people")
def people():
    return render_template("soda/people.html")

@soda.route("/public")
def public():
    return render_template("soda/public.html")

@soda.route("/gallery")
def gallery():
    return render_template("soda/gallery.html")

@soda.route("/intro")
def intro():
    return render_template("soda/intro.html")

@soda.route("/domain")
def domain():
    return render_template("soda/domain.html")

@soda.route("/prof")
def prof():
    return render_template("soda/prof.html")
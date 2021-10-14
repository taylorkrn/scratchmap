from flask import Blueprint
from flask import render_template, request, Blueprint
from scratchmap.models import Scratched_Map

main = Blueprint('main', __name__)

#Homepage - Should display possible Map_Types from most popular to least popular (Need to create Map model first)
@main.route("/")
@main.route("/home")
def home():

    #pagination
    page = request.args.get('page',1, type=int)
    #Database query
    maps = Scratched_Map.query.order_by(Scratched_Map.date_created.desc()).paginate(page=page, per_page=4)
    return render_template('home.html', maps=maps)

#About page - Currently empty
@main.route("/about")
def about():
    return render_template('about.html', title='About')

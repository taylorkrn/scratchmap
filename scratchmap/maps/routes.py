from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from scratchmap import db
from scratchmap.models import Scratched_Map
from scratchmap.maps.forms import ScratchedMapForm, MapForm


maps = Blueprint('maps', __name__)

#Create a new Map
@maps.route("/map/new", methods=['GET', 'POST'])
@login_required
def new_map():
    form = MapForm()
    if form.validate_on_submit():
        s_map = Scratched_Map(title=form.title.data, map_type=form.map_type.data, author=current_user)
        db.session.add(s_map)
        db.session.commit()
        flash('Your scratch map has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_map.html', title='New Map',
                            form=form, legend='New Map')

#View a Scratched Map
@maps.route("/map/<int:map_id>")
def s_map(map_id):
    #get_or_404 means get s_map or return 404
    s_map = Scratched_Map.query.get_or_404(map_id)
    return render_template('s_map.html', title=s_map.title, s_map=s_map)

#Update a Scratched Map
@maps.route("/map/<int:map_id>/update", methods=['GET', 'POST'])
@login_required
def update_map(map_id):
    #get_or_404 means get map or return 404
    s_map = Map.query.get_or_404(map_id)
    if s_map.author != current_user:
        abort(403)
    form = ScratchMapForm()

    if form.validate_on_submit():
        s_map.title = form.title.data
        s_map.visited = form.visited.data
        s_map.wish_list = form.wish_list.data
        db.session.commit()
        flash('Your scratch map has been updated!', 'success')
        return redirect(url_for('maps.s_map', map_id= s_map.id))
    elif request.method == 'GET':
        form.title.data = s_map.title
        form.visited.data = s_map.visited
        form.wish_list.data = s_map.wish_list
    return render_template('create_map.html', title='Update Map',
                            form=form, legend='Update Map')

#Delete a Scratched Map
@maps.route("/map/<int:map_id>/delete", methods=['POST'])
@login_required
def delete_map(map_id):
    #get_or_404 means get map or return 404
    s_map = Scratched_Map.query.get_or_404(map_id)
    if s_map.author != current_user:
        abort(403)
    db.session.delete(s_map)
    db.session.commit()
    flash('Your scratch map has been deleted!', 'success')
    return redirect(url_for('main.home'))

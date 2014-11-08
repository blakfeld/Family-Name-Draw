from random import randint
from flask import render_template, request
from app import app, db
from models import Family

"""
Hacky workaround -- if this was more serious
    I wouldn't do this. But I, for example, should
    not be allowed to draw my parents, and others
    should not be allowed to draw spouses or children.
"""
cant_draw = {
    'Kory': ['Krissa', 'Mike'],
    'Krissa': ['Mike', 'Kory'],
    'Mike': ['Krissa', 'Kory'],
    'Ben': ['Jo Marie'],
    'Jo Marie': ['Ben'],
    'Jennifer': ['Moe'],
    'Moe': ['Jennifer'],
    'Christine': ['Justin'],
    'Justin': ['Christine']
}


@app.route('/')
@app.route('/index')
def index():
    family_members = Family.get_all_members()
    member_names = [x.name for x in family_members]
    return render_template('index.html',
                           family_members=member_names)

@app.route('/drawName', methods=['POST'])
def draw_name():
    name = request.form['username']
    if not Family.member_exists(name):
        return "Not a Member of My Family. This Isn't For You :)"
    if Family.check_has_chosen(name):
        return "You've already picked someone!"

    user = Family.get_member_by_name(name)
    family_members = Family.get_all_available_members(name)
    member_names = [x.name for x in family_members]
    draw_random = randint(0, len(member_names))
    member = Family.get_member_by_name(member_names[draw_random])
    while member.name in cant_draw[user.name]:
        draw_random = randint(0, len(member_names) - 1)
        member = Family.get_member_by_name(member_names[draw_random])
    member.chosen = True
    user.has_chosen = True
    db.session.commit()

    return member.name

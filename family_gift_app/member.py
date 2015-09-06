"""
member.py -- A model for a family member in the database.
"""


class Member(object):
    def __init__(self, id, name, chosen, has_chosen, chosen_by, cannot_choose):
        self.id = id
        self.name = name
        self.chosen = chosen
        self.has_chosen = has_chosen
        self.chosen_by = chosen_by

        if not isinstance(cannot_choose, list):
            self.cannot_choose = cannot_choose.split(',')
        else:
            self.cannot_choose = cannot_choose

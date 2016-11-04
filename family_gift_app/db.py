"""
db.py -- Class for interacting with my database.
"""

import sqlite3 as sqlite

from member import Member


class FamilySQLiteDB(object):
    def __init__(self, db_name):
        """
        Constructor

        Args:
            db_name (str):      The name/path of the database to connect to.
        """

        self.db_conn = sqlite.connect(db_name)
        self.cursor = self.db_conn.cursor()
        self.members_db = 'family_members'

    def _serailze_to_member(self, db_tuple):
        """
        Take a tuple returned from the database, and serialize it into
            something nicer.
        """

        return Member(*db_tuple)

    def get_all_members(self):
        """
        Get all from the family members database
        """

        with self.db_conn:
            self.cursor.execute('SELECT * FROM family_members;')
            rows = self.cursor.fetchall()

        members = [self._serailze_to_member(r) for r in rows]

        return members

    def get_member_by_id(self, id):
        """
        Get a memember by an id

        Args:
            id (int):       Database ID to query on.
        """

        with self.db_conn:
            self.cursor.execute('SELECT * FROM family_members WHERE id = ?',
                                (id,))

            rows = self.cursor.fetchall()

            member = self._serailze_to_member(rows[0])

            return member

    def get_member_by_name(self, name):
        """
        Get a member by their name.

        Args:
            name (str):     The name to query.
        """

        with self.db_conn:
            self.cursor.execute('SELECT * FROM family_members WHERE name =?',
                                (name,))

            rows = self.cursor.fetchall()

            member = self._serailze_to_member(rows[0])

            return member

    def get_available_members(self, current_user):
        """
        Get all members where chosen = 0

        Args:
            current_user (str):     The requesting user, to ensure they dont
                                        get themselves back.
        """

        current_member = self.get_member_by_id(current_user)

        with self.db_conn:
            # This is hacky as fuck. I love it.
            self.cursor.execute('SELECT * FROM family_members WHERE chosen = 0 AND id != ? AND cannot_choose NOT LIKE ?',
                                (current_user,
                                 '%{0}%'.format(current_member.name)))

            rows = self.cursor.fetchall()

            members = [self._serailze_to_member(r) for r in rows]

            return members

    def update_chosen(self, chooser_id, chosen_id):
        """
        Update all the fields that have to do with choosing and being
            chosen.

        Args:
            chooser_id (int):       The id of the record doing the choosing.
            chosen_id (int):        The id of the record that was chosen.
        """

        chooser = self.get_member_by_id(chooser_id)
        chosen = self.get_member_by_id(chosen_id)
        with self.db_conn:
            self.cursor.execute('UPDATE family_members SET has_chosen = 1 where id = ?',
                                (chooser_id, ))

            self.cursor.execute('UPDATE family_members SET chosen = 1, chosen_by = ? WHERE id = ?',
                                (chooser.name, chosen_id))

            self.db_conn.commit()


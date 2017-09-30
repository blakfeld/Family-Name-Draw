from __future__ import absolute_import, print_function

import json
import os

import filelock


class FamilyMembers(object):
    def __init__(self, data_fpath, cwd=None):
        self.data_fpath = data_fpath
        self.cwd = cwd or os.path.join(
            os.path.dirname(self.data_fpath),
            'data.working.json'
        )

        lock_file = os.path.join(os.path.dirname(self.data_fpath), 'data.lock')
        self.lock = filelock.FileLock(lock_file)

        if not os.path.isfile(self.cwd):
            self._reset_data()

    def _reset_data(self):
        with self.lock:
            data = {}
            with open(self.data_fpath, 'r') as f:
                data = json.loads(f.read())

            with open(self.cwd, 'w') as f:
                f.write(json.dumps(data, indent=4))

    def _read_data_file(self):
        with self.lock:
            with open(self.cwd, 'r') as f:
                return json.loads(f.read())

    def _write_data_file(self, data):
        with self.lock:
            with open(self.cwd, 'w') as f:
                f.write(json.dumps(data, indent=4))

    def get_all(self):
        return self._read_data_file()

    def get_by_name(self, name):
        data = self._read_data_file()
        return {
            'data': filter(lambda x: x['name'].lower() == name.lower(), data['data'])
        }

    def update(self, new_data):
        self._write_data_file(new_data)

    def reload(self):
        self._reset_data()

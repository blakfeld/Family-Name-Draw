DROP TABLE IF EXISTS family_members;
CREATE TABLE family_members(
    id INTEGER Primary Key,
    name TEXT,
    chosen INTEGER,
    has_chosen INTEGER,
    chosen_by TEXT,
    cannot_choose TEXT
);

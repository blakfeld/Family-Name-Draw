#!/bin/bash


DB_NAME="family_gift_app.db"

rm $DB_NAME

touch $DB_NAME

sqlite3 $DB_NAME < schema.sql
sqlite3 $DB_NAME < data.sql

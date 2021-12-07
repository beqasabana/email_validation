from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "Insert INTO emails (email) VALUES(%(email)s);"
        email_id = connectToMySQL('email_schema').query_db(query, data)
        return email_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        emails_from_db = connectToMySQL('email_schema').query_db(query)
        emails = []
        for email in emails_from_db:
            emails.append(cls(email))
        return emails

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email):
            flash("Invalid Email Address!")
            is_valid = False
        return is_valid
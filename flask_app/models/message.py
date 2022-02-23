from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
import math
from flask import flash

db = 'private_wall_schema'

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

        self.sender = data['sender']
        self.receiver = data['receiver']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def get_user_messages(cls,data):
        query = """
        SELECT users.first_name as sender, users2.first_name as receiver, messages.* FROM users
        LEFT JOIN messages ON users.id = messages.sender_id
        LEFT JOIN users as users2 ON users2.id = messages.receiver_id
        WHERE users2.id =  %(id)s;"""
        results = connectToMySQL(db).query_db(query,data)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages

    @classmethod
    def save_message(cls,data):
        query = """
        INSERT INTO messages (content,sender_id,receiver_id)
        VALUES (%(content)s,%(sender_id)s,%(receiver_id)s);"""
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def destroy_message(cls,data):
        query = """
        DELETE FROM messages
        WHERE messages.id = %(id)s;"""
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['content']) < 1:
            is_valid = False
            flash("Please enter a message.","message")
        if len(message['content']) > 1:
            is_valid = True
            flash("Message sent successfully!","message")
        return is_valid
from flask import current_app
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    #should goal_id be showing up in the tasks table?

    def is_complete(self):
        if self.completed_at is None:
            is_complete = False
        else:
            is_complete = True
        return is_complete

    # def validate_input(self):
    #     if self.title is None or self.description is None or self.completed_at is None:
    #         return False
    #     return True

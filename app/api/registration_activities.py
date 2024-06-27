from flask_restx import Resource, reqparse, inputs
from datetime import date
from app.models import Announcement
from app.api.nsmodels import ongoing_activities


@ongoing_activities.route("/ongoing_activities")
class RegistrationActivitiesApi(Resource):
    
   
    @ongoing_activities.doc(responses={200: 'OK'})
    def get(self):
        current_date = date.today()

        active_contests = Announcement.query.filter(
            Announcement.registration_start < current_date,
            Announcement.registration_end >= current_date
        ).all()

        ongoing_activities = Announcement.query.filter(
            Announcement.start_date < current_date,
            Announcement.end_date >= current_date
        ).all()

        active_contests_data = [
            {"id": contest.id, "name": contest.name} for contest in active_contests
        ]
        ongoing_activities_data = [
            {"id": activity.id, "name": activity.name} for activity in ongoing_activities
        ]

        registration_activities = {
            "active_contests": active_contests_data,
            "ongoing_activities": ongoing_activities_data
        }

        return registration_activities, 200

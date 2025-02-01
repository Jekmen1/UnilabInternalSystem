from flask_restful import Resource
from app.models.user import Region, City, University, School
from app.models.roles import Role
from flask import request


class ListsApi(Resource):
    def get_locations(self):
        regions = Region.query.all()
        locations = []

        for region in regions:
            region_data = {
                "id": region.id,
                "name": region.region_name,
                "cities": [
                    {
                        "id": city.id,
                        "name": city.city_name
                    }
                    for city in City.query.filter_by(region_id=region.id).all()
                ]
            }
            locations.append(region_data)

        return {"locations": locations}, 200

    def get_universities(self):
        city_id = request.args.get("city_id", type=int)

        universities = University.get_universities(city_id)
        return {"universities": universities}, 200


    def get_roles(self):
        roles = Role.get_roles()
        filtered_roles = []
        for role in roles:
            if role.name.lower() != "admin":
                filtered_roles.append({"id": role.id, "name": role.name})
        return {"roles": filtered_roles}, 200


    def get_schools(self):
        city_id = request.args.get("city_id", type=int)

        schools = School.get_schools(city_id)
        return {"schools": schools}, 200
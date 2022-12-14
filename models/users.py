from flask import jsonify, request, abort
from sqlalchemy import Column, String, Integer, Date

from database.basemodel import BaseRepository, BaseModel


class ResUser(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    joindate = Column(Date)


class UserRepository(BaseRepository):
    model = ResUser

    def get_users(self, ROWS_PER_PAGE):
        page = request.args.get('page', 1, type=int)
        data_list = []
        query = self.session.query(ResUser.user_id, ResUser.name, ResUser.age, ResUser.joindate)
        res = query.limit(ROWS_PER_PAGE).offset(page)
        paginated_res = res

        for idx, item in enumerate(paginated_res):
            data_list.append({
                "user_id": (paginated_res[idx].user_id),
                "name": (paginated_res[idx].name),
                "age": (paginated_res[idx].age),
                "joindate": str(paginated_res[idx].joindate)

            })

        results = {"data": data_list}
        return jsonify(results)

    def get_users_by_id(self, user_id):
        data_list = []
        query = self.session.query(ResUser.user_id, ResUser.name, ResUser.age, ResUser.joindate).filter(
            ResUser.user_id == user_id)
        res = query.all()
        if len(res) < 1:
            abort(400, description=f'Invalid user id {user_id}')
        else:

            for idx, item in enumerate(res):
                data_list.append({
                    "user_id": (res[idx].user_id),
                    "name": (res[idx].name),
                    "age": (res[idx].age),
                    "joindate": str(res[idx].joindate)

                })

            results = {"data": data_list}
            return jsonify(results)

    def get_users_from_db_by_range_limit(self, limit, ages1, ages2):
        data_list = []
        page = request.args.get('page', 1, type=int)
        query = self.session.query(ResUser.user_id, ResUser.name, ResUser.age, ResUser.joindate) \
            .filter(ResUser.age.between(ages1, ages2))

        res = query.limit(limit).offset(page)
        paginated_res = res

        for idx, item in enumerate(paginated_res):
            data_list.append({
                "user_id": (paginated_res[idx].user_id),
                "name": (paginated_res[idx].name),
                "age": (paginated_res[idx].age),
                "joindate": str(paginated_res[idx].joindate)

            })

        results = {"data": data_list}
        return jsonify(results)

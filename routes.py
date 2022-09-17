from views.users import GetUsers, GetUsersByID

routes = [
    (GetUsers,"/user/get/limit/<int:limit>"),
    (GetUsersByID,"/user/get/id/<int:user_id>")
]

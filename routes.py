from views.users import GetUsers, GetUsersByID, GetUsersByRangeandLimit

routes = [
    (GetUsers, "/user/get"),
    (GetUsersByID, "/user/get/id"),
    (GetUsersByRangeandLimit, "/user/get/ranges")
]

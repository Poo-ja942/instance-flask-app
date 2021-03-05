from flask_restful import Resource
import logging as login


class Task(Resource):

    def get(self):
        login.debug("get method")
        return {"inside":"get"}

    def post(self):
        login.debug("post method")
        return {"inside":"post"}

    def put(self):
        login.debug("put method")
        return {"inside":"put"}

    def delete(self):
        login.debug("delete method")
        return {"inside":"delete"}
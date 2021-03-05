from flask_restful import Resource
import logging as login


class TaskById(Resource):

    def get(self,taskId):
        login.debug("get method")
        return {"inside":"get Task-Id {}", format(taskId)}

    def post(self, taskId):
        login.debug("post method")
        return {"inside":"post Task-Id {}", format(taskId)}

    def put(self, taskId):
        login.debug("put method")
        return {"inside":"put Task-Id {}", format(taskId)}

    def delete(self, taskId):
        login.debug("delete method")
        return {"inside":"delete Task-Id {}", format(taskId)}
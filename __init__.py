from flask_restful import Api
from .Task import Task
from .TaskById import TaskById
from app import app

restData = Api(app)

restData.add_resource(Task,"/App-api/task")
restData.add_resource(TaskById,"/api/task/id/<string:taskId>/")

from flask import Flask, request, jsonify,app
import logging as login
login.basicConfig(level="DEBUG")


app = Flask(__name__)

if __name__=='__main__':
    login.debug('PLEASE CHAL JAOOO NA')
    from api import *
    app.run(debug=True)
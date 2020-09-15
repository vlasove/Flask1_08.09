from flask import Flask 
from flask_restplus import Api, Resource
from environment.instance import enviroment_config


class Server:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            version='1.0 unstable',
            title= 'Simple Items API',
            description= 'Simple description for Items API',
            doc=enviroment_config['swagger-url']
            )


    def run(self):
        self.app.run(
            port=enviroment_config["port"],
            debug=enviroment_config["debug"]
        )

server = Server()
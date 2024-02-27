from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from

app = Flask(__name__)
api = Api(app)

# 创建一个简单的 API
class HelloWorld(Resource):
    @swag_from("demo.yml")
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

# 配置 Swagger
swagger = Swagger(app)

if __name__ == '__main__':
    app.run(debug=True)
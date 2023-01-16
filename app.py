from flask import Flask
from flasgger import Swagger
from api.route.posts import posts_api
from api.route.auth import auth_api
from api.schema.http import HTTP
from api.schema.encryption import Encryption

import config as conf

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Flask Api'
}
swagger = Swagger(app)
app.register_blueprint(posts_api,url_prefix='/posts')
app.register_blueprint(auth_api,url_prefix='/auth')


if __name__ == "__main__":
    HTTP.create_table()
    print(HTTP.get_all_active_user())
    app.run(debug=conf.DEBUG, host=conf.HOST,port=conf.PORT) 
import pymysql
from root import create_app
from root.config import config

from root import csrf

environment = config['development']
app = create_app(environment)

# run server
if __name__ == "__main__":
    csrf.init_app(app)

    app.run(port = "3000")
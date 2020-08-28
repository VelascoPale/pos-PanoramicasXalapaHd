import pymysql
from root import create_app
from root.config import config

from root import csrf

environment = config['deploy']
app = create_app(environment)

# run server
if __name__ == "__main__":

    #app.run()

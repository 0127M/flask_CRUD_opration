
class Config(object):

    SECRET_KEY='admin@123'#we can change this secret key

    SQLALCHEMY_DATABASE_URI='mysql://root:root@localhost/student_info'
    SQLALCHEMY_TRACK_MODIFICATIONS=False #this will print anusual logs

class DevlopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True#


class ProductionConfig(Config):
    DEBUG=False#we don't want to represent the logs

app_config={
    'development':DevlopmentConfig, #here we have to create a dict bcz we have to call key for 
    'production':ProductionConfig
}


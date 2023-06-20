from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        mysql_user = os.environ.get('HBNB_MYSQL_USER')
        mysql_password = os.environ.get('HBNB_MYSQL_PWD')
        mysql_host = os.environ.get('HBNB_MYSQL_HOST')
        mysql_db = os.environ.get('HBNB_MYSQL_DB')
        hbnb_env = os.environ.get('HBNB_ENV')

        if hbnb_env == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(mysql_user, mysql_password, mysql_host, mysql_db), pool_pre_ping=True)

    def all(self, cls=None):
        obj_list = ["User", "State", "City", "Amenity", "Place", "Review"]
		obj_dict = {}

        if cls is None:
            for i in obj_list:
                for instance in session.query(i).all():
                     key = instance.__class__.__name__ + '.' + instance.id
                     obj_dict[key] = instance
        else:
            for instance in session.query(i).all():
                key = instance.__class__.__name__ + '.' + instance.id
                obj_dict[key] = instance
         return obj_dict

    def new(self, obj):
        self.__session.add(obj)
	
    def save(self):
        self.__session.commit()
	
    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database create the current database session """
        from model.state import state
        from model.city import City
        from model.place import Place
        from model.user import User
        from model.review import Review
        from model.amenity import Amenity
        Base.metadata.create_all(bind=self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

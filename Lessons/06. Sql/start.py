from lib.settings import *
from lib.DB_Manager import db_manager


user_manager = db_manager(HOSTNAME, USERNAME, PASSWORD)
user_manager.menu()

"""
Connection setup of database, used in conjunction with .env
"""

import pymongo
import os
CONNECTION_STRING = os.environ.get('CONDOMINIUM_DB_CONNECTION')
DATABASE = pymongo.MongoClient(CONNECTION_STRING).condominium
import api
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime


sid = 10701

rix = api.RixCloud("user", "pass")

cred = credentials.Certificate("db-rix.json")
firebase_admin.initialize_app(cred)

ref = db.reference('/traffic', url='https://<your_db>.firebaseio.com/')
traffic = rix.get_traffic(sid)
ref.push({"ctime": datetime.utcnow().ctime(), "upload": traffic['upload'], "download": traffic['download']})

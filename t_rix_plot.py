import matplotlib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from bashplotlib.histogram import plot_hist

cred = credentials.Certificate("db-rix.json")
firebase_admin.initialize_app(cred)

ref = db.reference('/traffic_v2', url="https://<your_db_name>.firebaseio.com/")
data = ref.get()

up = [value['upload'] for value in data.values()]
down = [value['download'] for value in data.values()]
up_delta = [up[i] - up[i - 1] for i in range(1, len(up))]
down_delta = [down[i] - down[i - 1] for i in range(1, len(down))]
index = list(range(1, len(up)))
plot_hist(up)


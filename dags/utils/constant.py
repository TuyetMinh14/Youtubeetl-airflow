from airflow.models import Variable
import json


DAG_ID = Variable.get("DAG_ID")
YOUTUBE_API_KEY = Variable.get("YOUTUBE_API_KEY")

client_list = json.loads(Variable.get("client_list"))
# smtp_variable = json.loads(Variable.get("smtp_variable"))

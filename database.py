import sqlalchemy
from sqlalchemy import create_engine, text
db_connection_string = "mysql+pymysql://dg7v3vphfa5ip7x0z0t2:pscale_pw_6grJWALZoGJNafvNhP1mvToA1NIpTzms4VxUroRSSX9@aws.connect.psdb.cloud/bcfprojects?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from projects"))
    print("type(result):", type(result))
    result_all = result.all()
    print("type(result.all())", type(result_all))
    print("result_all():", result_all)
    # projects = []
    # for row in result.all():
      # projects.append(row)
    # return projects

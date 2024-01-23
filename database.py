import sqlalchemy
from sqlalchemy import create_engine, text
#db_connection_string = "mysql+pymysql://bh194304n4kk1cn1fvxt:pscale_pw_VoGIj8rjKvF3SCi8829bwfjWTXtnS0oG1O8zdI8sPdD@aws.connect.psdb.cloud/bcfprojects?charset=utf8mb4"
#engine = create_engine(db_connection_string, connect_args={
  #"ssl": {
    #"ssl_ca": "/etc/ssl/cert.pem"}})
#connection = engine.connect()
#result = connection.execute("SELECT * FROM PROJECTS")

#def load_projects_from_db():
  #with engine.connect() as conn:
    #result = conn.execute(text("select * from projects"))
#for row in result:
  #print(row)
    # projects = []
    # for row in result.all():
      # projects.append(row)
    # return projects

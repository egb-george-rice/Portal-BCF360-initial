import sqlalchemy, os
from sqlalchemy import create_engine, text

my_secret = os.environ['DB_CONNECTION_STRING']


engine = create_engine(my_secret, connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from proj24"))
    projects = []
    for (row) in result.all():
      projects.append(row)
    return projects

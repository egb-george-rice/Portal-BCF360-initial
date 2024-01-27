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
    columns = result.keys()  
    result_dict = [dict(zip(columns, row)) for row in result.fetchall()]
    projects = []  
    for row in result_dict:
      projects.append(row)
    return projects
    
def load_project_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from proj24 where proj_id = :val"), {"val": id})
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      columns = result.keys()  
      result_dict = [dict(zip(columns, row)) for row in rows]
      return result_dict[0]
    
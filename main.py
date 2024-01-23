from flask import Flask, render_template, jsonify
#from database import load_projects_from_db

app = Flask(__name__)

PROJECTS = [
  {
    'project_id': 1,
    'project_county': 'Kern',
    'project_state': 'CA',
    'project_acres': '40',
    'project_description': 'This is Project 1',
    'project_image': 'County website'
  },
  {
    'project_id': 2,
    'project_county': 'Cumberland',
    'project_state': 'NC',
    'project_description': 'This is Project 2',
    'project_image': 'County website'
  },
  {
    'project_id': 3,
    'project_county': 'Franklin',
    'project_state': 'NC',
    'project_acres': '1000',
    'project_description': 'This is Project 3',
    'project_image': 'County website'
  },
  {
    'project_id': 4,
    'project_county': 'Scotland',
    'project_state': 'NC',
    'project_acres': '1500',
    'project_description': 'This is Project 4',
    'project_image': 'County website'
  }
]

@app.route("/")

def hello_bcf():
  #projects = load_projects_from_db()
  return render_template("home.html", projects=PROJECTS, company='Bright Clean Future')

@app.route("/api/projects")
def list_projects():
  #projects = load_projects_from_db()
  return jsonify(PROJECTS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
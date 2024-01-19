from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
  {
    'project_id': 1,
    'project_name': 'Project 1', 'project_county': 'Franklin', 'project_state': 'NC',
    'project_description': 'This is project 1', 'project_acres': '100',    'project_image': 'https://picsum.photos/200/300',
    'project_link': 'https://www.google.com'
  },
  {
  'project_id': 2,
  'project_name': 'Project 2',
  'project_description': 'This is project 2', 'project_county': 'Anson', 'project_state': 'NC', 'project_image': 'https://picsum.photos/200/300',
  'project_link': 'https://www.google.com'
  }, 
  {
  'project_id': 3,
  'project_name': 'Project 3',
  'project_description': 'This is project 3', 'project_county': 'Cabarras', 'project_state': 'NC', 'project_acres': '300', 'project_image': 'https://picsum.photos/200/300',
  'project_link': 'https://www.google.com'
  }
]

@app.route("/")

def hello_bcf():
  return render_template("home.html", projects=PROJECTS, company='Bright Clean Future')

@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  
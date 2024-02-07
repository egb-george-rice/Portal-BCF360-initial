from flask import Flask, render_template, jsonify
from database import load_projects_from_db, load_project_from_db, add_interest_to_db

app = Flask(__name__)

@app.route("/")

def hello_bcf():
  projects = load_projects_from_db()
  return render_template("home.html", projects=projects)

@app.route("/login")
def login():
  return render_template("login.html", boolean=True)

@app.route("/logout")
def logout():
  return "<p>Logout</p>"

@app.route("/sign-up")
def signin():
  return render_template("sign-up.html")

@app.route("/api/projects")
def list_projects():
  projects = load_projects_from_db()
  return jsonify(projects)

@app.route("/projects/<id>/interest")
def project_interest(id):
  project = load_project_from_db(id)
  add_interest_to_db(id, project)
  return render_template("interest.html", project=project)

@app.route("/projects/<id>/add_watch")
def project_watch(id):
  projects = load_project_from_db()
  return jsonify(projects)

@app.route("/projects/<id>")
def show_project(id):
  project = load_project_from_db(id)
  if not project:
    return "Not Found", 404
    
  return render_template("projectpage.html", project=project)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
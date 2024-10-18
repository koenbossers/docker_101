from pathlib import Path

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/lister/<folder>")
def list_folder(folder):
    folder_contents = list(Path(f"/{folder}").glob("**/*"))
    return f"Folder {folder} contains: {folder_contents}"

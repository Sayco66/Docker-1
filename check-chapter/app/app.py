from flask import Flask
import requests
import datetime
import os


app = Flask(__name__)

chapter = os.environ.get("CHAPTER_VALUE","1089")

@app.route("/")
def hello():
    return "Hello world"


@app.route("/check_chapter")
def check_chapter():
    r = requests.get("http://www.volonte-d.com/", verify=False)
    is_new_chapter_released = f"chapitre {chapter}" in str(r.content).lower()

    return f"{chapter} released: {is_new_chapter_released}"

@app.route("/write_datetime")
def write_datetime():
    now = datetime.datetime.now()

    with open("project/file.txt", "a") as f:
        f.write(f"{now}\n")

    return f"{now}"

@app.route("/write_env")
def write_env():
    env_var = os.environ.get("MSG_TO_WRITE", "Valeur par défaut")
    with open("project/env.txt", "a") as f:
        f.write(f"{env_var}\n")

    return f"{env_var}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
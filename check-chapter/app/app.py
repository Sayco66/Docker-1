from flask import Flask
import requests
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


@app.route("/check_chapter")
def check_chapter():
    chapter_id = 1088
    r = requests.get("http://www.volonte-d.com/", verify=False)
    is_new_chapter_released = f"chapitre {chapter_id}" in str(r.content).lower()
    now = datetime.datetime.now()

    return f"{chapter_id} released: {is_new_chapter_released}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
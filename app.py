from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://picsum.photos/id/1/200/300",
    "https://picsum.photos/id/2/200/300",
    "https://picsum.photos/id/3/200/300",
    "https://picsum.photos/id/4/200/300",
    "https://picsum.photos/id/5/200/300",
    "https://picsum.photos/id/6/200/300",
    "https://picsum.photos/id/7/200/300",
    "https://picsum.photos/id/8/200/300",
    "https://picsum.photos/id/9/200/300",
    "https://picsum.photos/id/10/200/300",
    "https://picsum.photos/id/11/200/300",
    "https://picsum.photos/id/12/200/300"
]


@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == "__main__": app.run(host="0.0.0.0")

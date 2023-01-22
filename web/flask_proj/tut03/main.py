
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import random

app = Flask(__name__)


def hello():
    plt.plot([random.randint(0, 10) for _ in range(10)])
    plt.show()


@app.route('/')
def hello2():
    fig, ax = plt.subplots(1, 1)
    ax.plot([random.randint(0, 10) for _ in range(10)])
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # print(data)
    # return f"<img src='data:image/png;base64,{data}'/>"
    return render_template('hello.html', image=f'data:image/png;base64,{data}')


if __name__ == '__main__':
    # hello()
    app.run()

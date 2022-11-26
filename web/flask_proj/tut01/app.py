from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    print(request.method)
    print(request.headers)
    print(request.cookies)
    print(request.args)

    cnt = int(request.cookies.get('visit', 0))
    cnt += 1
    messgae = 'you"ve visited this page {} times.'.format(cnt)
    resp = make_response(messgae)
    resp.set_cookie('visit', str(cnt))
    return resp


if __name__ == '__main__':
    app.run(debug=True)

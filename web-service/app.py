import os
from flask import Flask, render_template
from nameko.standalone.rpc import ClusterRpcProxy

nameko_username = os.environ.get('nameko_username')
nameko_password = os.environ.get('nameko_password')
nameko_host = os.environ.get('nameko_host', "rabbitmq")

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)

CONFIG = {'AMQP_URI': f"amqp://{nameko_username}:{nameko_password}@{nameko_host}"}


@app.route('/', methods=['GET'])
def user():
    return "request /user or /book for microservice"

@app.route('/user', methods=['GET'])
def user():
    with ClusterRpcProxy(CONFIG) as rpc:
        user_data = rpc.user.user()
    return render_template('user.html', template=user_data.get('data'))

@app.route('/book', methods=['GET'])
def book():
    with ClusterRpcProxy(CONFIG) as rpc:
        user_data = rpc.book.book()
    return render_template('book.html', template=user_data.get('data'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

from flask import Flask, render_template


app = Flask(__name__)
HOST, PORT = "127.0.0.1", 5000


def main():
    app.run(HOST, PORT)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    main()
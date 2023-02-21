from flask import Flask

app = Flask(__name__)

dicts = {
    "14.02.2023": {
        "alpha":[3454, 454, 45],
        "beta":[44, 454, 458, 745]
    },
    "15.02.2023": {
        "alpha":[3454, 454, 45],
        "beta":[44, 454, 458, 745]
    },
    "16.02.2023": {
        "alpha":[3454, 454, 45],
        "beta":[44, 454, 458, 745]
    },
}
@app.route("/")
def index():
    return dicts

if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
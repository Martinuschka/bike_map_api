from mysql.connector import connect, Error
from flask import Flask, request


app = Flask(__name__)


@app.route("/bike_map_api", methods=["POST"])
def post_measurements():
    data = request.get_json()
    insert_data(data["vibration"], data["latitude"], data["longitude"], data["speed"], data["timestamp"])
    return data


def db_connect():
    try:
        return connect(host="IP", user="USER", password="PW", database="DB")
    except Error as e:
        print(e)


def insert_data(vibration, latitude, longitude, speed, timestamp):
    connection = db_connect()
    print("Connection: ", connection)
    query = f"INSERT INTO measurements values (0,'{vibration}','{latitude}','{longitude}','{speed}','{timestamp}');"
    try:
        connection.cursor().execute(query)
        connection.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

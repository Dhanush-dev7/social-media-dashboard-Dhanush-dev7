from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

@app.route("/db-test")
def db_test():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    conn.close()

    return jsonify({
        "status": "success",
        "tables": tables
    })

if __name__ == "_main_":
    app.run(debug=True)

@app.route("/metrics")
def get_metrics():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query ="""
    SELECT p.content_type, m.likes, m.comments, m.reach, m.impressions
    FROM metrics m
    JOIN posts p ON m.post_id = p.id
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

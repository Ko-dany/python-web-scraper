from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio

from functions.communitech_scraper import communitech_scraper

app = Flask(__name__)
CORS(app)

db = {}

def function_keyword(keyword):
    return f"I got the data: {keyword}"

@app.route("/api/data")
def get_data():
    data = {
        "message":"Hello from Flask!"
    }
    return jsonify(data)

@app.route("/search", methods=["POST"])
def search_keyword():
    data = request.get_json()
    keyword = data.get("keyword")
    if keyword:
        try:
            # response_message = function_keyword(keyword)
            job_list = asyncio.run(communitech_scraper(keyword))
            return jsonify(job_list)
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), 500
    else:
        return jsonify({
            "message": "We didn't receive the keyword..."
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
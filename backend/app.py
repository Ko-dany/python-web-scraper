from flask import Flask, request, jsonify, redirect, send_file
from flask_cors import CORS
import asyncio
import os

from functions.communitech_scraper import communitech_scraper
from functions.export import export_to_file

app = Flask(__name__)
CORS(app)

db = {}

@app.route("/")
# API Address Test
def index():
    return "Hi!"


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
            job_list = asyncio.run(communitech_scraper(keyword))
            # print(job_list)
            db[keyword] = job_list 
            return jsonify(job_list)
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), 500
    else:
        return jsonify({
            "message": "We didn't receive the keyword..."
        }), 400

# @app.route("/export", methods=["POST"])
# def export():
#     data = request.get_json()
#     keyword = data.get("keyword")

#     if not keyword or keyword not in db:
#         return jsonify({"error": "Invalid keyword or keyword not found"}), 400

#     try:
#         export_to_file(keyword, db[keyword])
        
#         return send_file(
#             f"{keyword}.csv",
#             mimetype='text/csv',
#             as_attachment=True,
#             download_name=f"{keyword}.csv" 
#         )
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#     finally:
#         if os.path.exists(f"{keyword}.csv"):
#             os.remove(f"{keyword}.csv")

if __name__ == '__main__':
    app.run(debug=True)
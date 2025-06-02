from flask import Flask, render_template, request, jsonify
import requests

application = Flask(__name__)

# Your Yelp API Key
API_KEY = "6r8GwPsBifuem8BpM8Bv8VsRD91__dBXj85NZ2sw4CCO_OqI_PROUK3DJSmxlIyVLy5ZO4CenKiVaKHzdQ9FvR9kqT0t_MTbgVPVcRS4YLuwls8fDg7jjQRF--08aHYx"
YELP_URL = "https://api.yelp.com/v3/businesses/search"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Route to load HTML frontend
@application.route("/")
def home():
    return render_template("travel_search_page.html")

# Route to handle search API calls
@application.route("/api/search", methods=["POST"])
def search():
    try:
        # Parse JSON request
        if request.is_json:
            data = request.get_json()
        else:
            return jsonify({"error": "Request must be JSON"}), 400

        location = data.get("location", "").strip()
        if not location:
            return jsonify({"error": "Location not provided"}), 400

        print(f"🔍 Received search for location: {location}")

        # Query Yelp API
        params = {
            "location": location,
            "term": "attractions",
            "limit": 10,
            "sort_by": "rating"
        }

        response = requests.get(YELP_URL, headers=HEADERS, params=params)

        if response.status_code == 200:
            businesses = response.json().get("businesses", [])
            results = [
                {
                    "name": b["name"],
                    "rating": b["rating"],
                    "image_url": b.get("image_url", ""),
                    "address": ", ".join(b["location"].get("display_address", [])),
                    "url": b.get("url", "#")
                } for b in businesses
            ]
            return jsonify(results)
        else:
            print("❌ Yelp API error:", response.status_code, response.text)
            return jsonify({"error": "Failed to fetch data from Yelp"}), 500

    except Exception as e:
        print("🔥 Server error:", str(e))
        return jsonify({"error": "Server error occurred"}), 500

# Run the Flask app
if __name__ == "__main__":
    application.run(debug=True)


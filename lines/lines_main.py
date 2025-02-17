from fastapi import FastAPI
import requests

API_KEY = "9a7bf8bccf9841f085539c5421466861" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

lines_app = FastAPI()

# Create route for lines that loops through data and returns the information.
@lines_app.get("/lines")
def get_lines():
    response = requests.get(ENDPOINT_URL + f"/lines?api_key={API_KEY}")
    list_of_lines = []
    lines = response.json()["data"]
    for line in lines:
        list_of_lines.append(
            {
            "id": line["id"],
            "text_color": line["attributes"]["text_color"],
            "short_name": line["attributes"]["short_name"],
            "long_name": line["attributes"]["long_name"],
            "color": line["attributes"]["color"]
            })
    return{"lines": list_of_lines}


# Create a new route /lines/{line_id}
@lines_app.get("/lines/{line_id}")
def get_line(line_id: str):
    response = requests.get(ENDPOINT_URL + f"/lines/{line_id}?api_key={API_KEY}") # Send a request to the endpoint
    line_data = response.json()["data"]
    line = {
        "id": line_data["id"],
        "text_color": line_data["attributes"]["text_color"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
    }
    return {"lines":line}

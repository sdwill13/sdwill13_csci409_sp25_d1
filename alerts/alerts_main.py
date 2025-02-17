from fastapi import FastAPI, Depends
import requests, httpx

API_KEY = "9a7bf8bccf9841f085539c5421466861" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS
MBTA_BASE_URL = "https://api-v3.mbta.com/alerts/" #Added for alerts

alerts_app = FastAPI()

# Dependency to fetch all alerts
async def get_all_alerts(route: str = None, stop: str = None):
    params = {}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(MBTA_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()


# Dependency to fetch a specific alert by ID
async def get_alert_by_id(alert_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/{alert_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@alerts_app.get("/alerts")
async def read_alerts(route: str = None, stop: str = None, alerts=Depends(get_all_alerts)):
    return alerts


@alerts_app.get("/alerts/{alert_id}")
async def read_alert(alert_id: str, alert=Depends(get_alert_by_id)):
    return alert

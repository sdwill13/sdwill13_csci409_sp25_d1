from fastapi import FastAPI, Depends
import requests, httpx

API_KEY = "9a7bf8bccf9841f085539c5421466861" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS
MBTA_BAXE_URL = "https://api-v3.mbta.com/vehicles/" #Added for vehicles

vehicles_app = FastAPI()


# Dependency to fetch all vehicles
async def get_all_vehicles(route: str = None, revenue: str = None):
    params = {}
    if route:
        params["filter[route]"] = route
    if revenue:
        params["filter[stop]"] = revenue

    async with httpx.AsyncClient() as client:
        response = await client.get(MBTA_BAXE_URL, params=params)
        response.raise_for_status()
        return response.json()


# Dependency to fetch a specific vehicle by ID
async def get_vehicle_by_id(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

# Create /vehicles route
@vehicles_app.get("/vehicles")
async def read_vehicles(route: str = None, revenue: str = None, vehicles=Depends(get_all_vehicles)):
    return vehicles


# Create /vehicles/{id} route
@vehicles_app.get("/vehicles/{id}")
async def read_vehicle(id: str, vehicle=Depends(get_vehicle_by_id)):
    return vehicle
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import RedirectResponse
from alerts import alerts_main
from gateway.api_router import RedirectRoutesPortalException, RedirectLinesPortalException, \
    RedirectAlertsPortalException, RedirectVehiclesPortalException, call_api_gateway
from lines import lines_main
from routes import routes_main
from vehicles import vehicles_main


# App
app = FastAPI()
app.mount("/routes", routes_main.route_app)
app.mount("/lines", lines_main.lines_app)
app.mount("/alerts", alerts_main.alerts_app)
app.mount("vehicles", vehicles_main.vehicles_app)


# Router
router = APIRouter()

@router.get("/{portal_id}")
def access_portal(portal_id:int):
    return{'message': 'Home for Various Routes'}



@app.exception_handler(RedirectRoutesPortalException)
def exception_handler_routes(request: Request, exc: RedirectRoutesPortalException):
    return RedirectResponse(url='http://localhost:127.0.0.1:8000/routes')
@app.exception_handler(RedirectLinesPortalException)
def exception_handler_routes(request: Request, exc: RedirectLinesPortalException):
    return RedirectResponse(url='http://localhost:127.0.0.1:8000/lines')
@app.exception_handler(RedirectAlertsPortalException)
def exception_handler_routes(request: Request, exc: RedirectAlertsPortalException):
    return RedirectResponse(url='http://localhost:127.0.0.1:8000/alerts')
@app.exception_handler(RedirectVehiclesPortalException)
def exception_handler_routes(request: Request, exc: RedirectVehiclesPortalException):
    return RedirectResponse(url='http://localhost:127.0.0.1:8000/vehicles')

from flask import Flask, request, jsonify, Blueprint
from datetime import date

planet_bp = Blueprint("planet", __name__)

@planet_bp.route("/", methods=["GET"])
def planetCalendars():
    
    data = request.get_json()
    planet = data.get("planet")

    planet = planet.lower().strip()
    
    orbitalPeriods = {
        "mercury": 87.97,
        "venus": 224.70,
        "earth": 365.25,
        "mars": 686.98,
        "jupiter": 4332.59,
        "saturn": 10759.22,
        "uranus": 30688.5,
        "neptune": 60182.0,
        "pluto": 90560.0
    }
    dayLengths = {  # in Earth hours
        "mercury": 1407.6,
        "venus":   -5832.5,
        "earth":   23.9345,
        "mars":    24.6229,
        "jupiter": 9.9250,
        "saturn":  10.6562,
        "uranus":  -17.24,
        "neptune": 16.11,
        "pluto":   153.2928
    }
    
    if planet not in orbitalPeriods:
        raise ValueError(f"Unknown planet: {planet}")
    
    today = date.today()
    jan1 = date(today.year, 1, 1)
    earth_days_since_jan1 = (today - jan1).days + 1

    earth_hours_since_jan1 = earth_days_since_jan1 * 24
    planet_day_length_hours = abs(dayLengths[planet])
    planet_days = earth_hours_since_jan1 / planet_day_length_hours

    planet_days = abs(planet_days)

    period = orbitalPeriods[planet]
    day_len = dayLengths[planet]
    days_per_year = period / (abs(day_len) / 24)
    ouput = f"{planet.title()} Calendar System:\n~{round(days_per_year)} days/year\n{abs(round(day_len, 2))} hour days\n{planet.title()} days since Earth Jan 1: {round(planet_days)}"
    if(planet != "earth"):
        ouput += f" (Earth: {earth_days_since_jan1})"

    print(ouput)

    return jsonify({
        "planet_title": planet.title(),
        "days_per_year": round(days_per_year),
        "day_length_hours": round(abs(day_len), 2),
        "planet_days_since_jan_1": round(planet_days),
        "earth_days_since_jan_1": earth_days_since_jan1 if planet != "earth" else None
    })

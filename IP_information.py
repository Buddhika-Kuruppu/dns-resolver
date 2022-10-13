import requests
import socket

hostname = input("Please enter website address:\n")

#def get_ip():
    #response = requests.get('https://api64.ipify.org?format=json').json()
    #return response["ip"]
    
def get_location():
    ip_address = socket.gethostbyname(hostname)
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "version": response.get("version"),
        "postal": response.get("postal"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "utc_offset": response.get("utc_offset"),
        "country_calling_code": response.get("country_calling_code"),
        "asn": response.get("asn"),
        "org": response.get("org")  
    }
    return location_data

print(get_location())
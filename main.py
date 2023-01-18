import csv
import requests

def add_coordinates(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
        
    for row in rows:
        location = row['lieu_de_naissanceLabel']
        url = f'https://nominatim.openstreetmap.org/search?q={location}&format=json'
        response = requests.get(url)
        data = response.json()
        lat = data[0]['lat']
        lng = data[0]['lon']
        row['latitude'] = lat
        row['longitude'] = lng

    with open(csv_file, 'w', newline='') as file:
        fieldnames = list(rows[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

add_coordinates('catData.csv')
import csv
from geopy.distance import distance

def first_5000_rows_metropolitan_France(file_name):
    nb_line = 50000 
    # Point de référence connu dans la France métropolitaine (par exemple, la Tour Eiffel)
    reference_point = (48.8583700, 2.2944810)
    threshold_distance = 100000
    # ouvrir le fichier csv en mode lecture
    with open(file_name, 'r', encoding="utf8") as file:
        reader = csv.reader(file)
        # lire les 5000 premières lignes
        rows = [row for row in reader][:nb_line]

    # créer un nouveau fichier csv avec les 5000 premières lignes
    with open('data/first_' + str(nb_line) + '_' + file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows:
            try:
                latitude = float(row[49])
                longitude = float(row[50])
                gps_coordinates = (latitude, longitude)
                # vérifier si les coordonnées GPS sont dans la France métropolitaine
                if distance(reference_point, gps_coordinates).km < threshold_distance:
                    writer.writerow(row)
            except:
                # si il y a une erreur dans la ligne telle que des données manquantes ou
                # un format de données incorrect, la ligne sera ignorée
                pass


first_5000_rows_metropolitan_France('DataSetInitCoquelicot.csv')

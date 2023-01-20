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

# import os
# import csv
# import random
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="geoapiExercises")

# # Chemin du dossier d'images
# folder_path = input("Entrez le chemin du dossier d'images : ")

# # Liste pour stocker les informations des images
# images_data = []

# # Parcours des images dans le dossier
# for i, image_name in enumerate(os.listdir(folder_path)):
#     # Génération aléatoire de nom de plante
#     plant_name = 'Plante ' + str(random.randint(1, 100))
#     # Génération aléatoire de date
#     date = str(random.randint(1, 30)) + '/' + str(random.randint(1, 12)) + '/' + str(random.randint(2000, 2020))
#     # Génération aléatoire de latitude et longitude
#     lat = random.uniform(-90, 90)
#     lon = random.uniform(-180, 180)
#     # Trouver l'adresse a partir des coordonnées
#     location = geolocator.reverse((lat,lon), exactly_one=True)
#     # Si l'adresse est valide
#     if location is not None:
#         # extraire les coordonnées
#         latitude, longitude = location.latitude, location.longitude
#     else:
#         latitude, longitude = None, None
#     # Chemin de l'image
#     image_path = "https://riidley.github.io/DataVizHAMSEK/Projet/" + os.path.join(folder_path, image_name)
#     # Ajout des informations de l'image à la liste
#     images_data.append([i, plant_name, image_path, date, latitude, longitude])

# # Ecriture des données dans un fichier CSV
# with open('images_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['ID', 'nom_plante', 'chemin', 'date','latitude','longitude'])
#     writer.writerows(images_data)

# print("Fichier CSV créé avec succès!")


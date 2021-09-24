# Challenge 1 : Air quality 

## Objectives 

The goal of this challenge is to estimate a pollution pike at day 2 and day 3. 

### Station localization 

Données brutes à disposition
Zone d’étude :

    POLYGON ((3.01025390625 42.946622264045786, 3.2522964477539062 42.946622264045786, 3.2522964477539062 43.07841776257431, 3.01025390625 43.07841776257431, 3.01025390625 42.946622264045786))

```
​Coordonnées   Latitude      Longitude
Point 1       42.94662      3.010253        
Point 2       43.078417     3.252296

Lat/long des sondes AIR (identification de la zone d’étude) :
Station       Latitude      Longitude        Nom Station
868           43.01492      3.05215          Piscine
869           43.01404      3.06448          Capitainerie
```

## Dataset 

The following dataset (**put a link**) contained these fields:
 * Données brutes de station qualité de l’air : Concentration de particules fines  (Données anonymisées)
 * Données météos : vent, pluie
 * Données Trafic maritime de la zone étudiée  
 * Données de coordonnées de la zone d’étude
 * Données de coordonnées des stations qualité d’AIR

## Threshholds for pollution detection 

Alert thresholds for measurements PM10, NO2 et SO2 

- Premier seuil (seuil de pré-alerte) :

    PM 10 et PM25 >= 50 μg/mᴲ (en moyenne sur 24h),
    NO₂ >= 200 μg/mᴲ (en moyenne sur une heure)
    SO₂ >= 300 μg/mᴲ (en moyenne sur une heure)

- Deuxième seuil (seuil d’alerte) :

    PM 10 et PM 25 >= 80 μg/mᴲ (sur les dernières 24h)
    NO₂ >= 300 μg/mᴲ (sur la dernière heure)
    SO₂ >= 500 μg/mᴲ (sur la dernière heure)


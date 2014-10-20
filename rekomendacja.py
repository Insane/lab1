from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0, "Hunter":1.0,"Metallica":10.0}
        }
 
def manhattan(rating1, rating2):
    klucze1 = rating1.keys()
    klucze2= rating2.keys()
    d = 0
    flaga=False
    for klucz in klucze1:
        if klucz in rating2.keys():
            flaga=True
            d=d+abs(rating2[klucz]-rating1[klucz])
    if flaga:
         return d
    else:
         return -1       

def test_manhattan(rating1,rating2,d):
     if manhattan(rating1,rating2) == d:
        True
     else:
         False
        
def najblizszy_sasiad(username, users):
    distances = []
    for uzytkownik in users:
        if uzytkownik!=username:
            odleglosc=manhattan(users[username],users[uzytkownik])
            distances.append((odleglosc,uzytkownik))     
    return sorted(distances)

def recommend(username,users):
    nearest=najblizszy_sasiad(username, users)[0][1]
    recommendations = []
    rating_of_nearest= users[nearest] 
    userRating = users[username]
    for artist in rating_of_nearest:
        if not artist in userRating:
            recommendations.append((artist,rating_of_nearest[artist]))       
    
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

print ("Rekomendacje to: %s" %recommend("Ania",users))
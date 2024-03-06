import requests
from bs4 import BeautifulSoup
from .models import Club

def scrape_clubs():
    URL = 'https://madridlux.com/en/clubs'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    # searching for the website and saving the html into soup

    clubs_data = []
    club_containers = soup.find_all('div', class_='clubs-list-large__item')
    # adding to club containers all the html divs/container containing clubs

    # now for each container take the improtant information like the name, location, music type
    for container in club_containers:
        # name
        name_tag = container.find('h3', class_='clubs-list-large__name')
        name = name_tag.text.split('Club ', 1)[-1].strip() if name_tag else 'No Name Found'
        # address
        location_icon = container.find('i', class_='i-lg-location')
        address_tag = location_icon.find_parent('li') if location_icon else None
        address = address_tag.get_text(strip=True) if address_tag else 'No Address Found'
        # music
        music_type = container.find_all('li')[1].get_text(strip=True) if len(container.find_all('li')) > 1 else 'No Music Type Found'

        # all of it saved into a clean dictionary
        clubs_data.append({
            'name': name,
            'location': address,
            'music_type': music_type,
        })

    return clubs_data

# now we just need to input that information into our database so it can be used afterwards
def save_club_data(clubs_data):
    # for each club check if already in database, if or not it implements it or changes the info
    for club_data in clubs_data:
        try:
            club, created = Club.objects.get_or_create(
                name=club_data['name'],
                defaults={
                    'location': club_data['location'],
                    'music_type': club_data['music_type'],
                }
            )
            if not created:
                club.location = club_data['location']  # Updated 'address' to 'location'
                club.music_type = club_data['music_type']
                club.save()
        except Exception as e:
            print(f"Error saving club {club_data['name']}: {e}")

# save_club_data(scrape_clubs())

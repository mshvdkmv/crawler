import requests, json
import pickle
TOKEN = 'oK0jD065025D3iN4NZFkw64w171DBYy9HJOe0BFDC-huWjb229LOOsXCHe2AuHgo'
BASE_URL = 'https://api.genius.com'


def get_song_info(song_id):
    headers = {'Authorization': 'Bearer ' + TOKEN}
    search_url = BASE_URL + '/songs/' + str(song_id)
    response = requests.get(search_url, headers=headers).json()

    return response


def get_artist_and_song_url(song_id):
    status = -5
    name, link, release_date = '', '', ''
    info = get_song_info(song_id)
    status = info['meta']['status']
    print(song_id)
    if status == 200:
        link = info['response']['song']['path']
        name = info['response']['song']['primary_artist']['name']
        release_date = info['response']['song']['release_date']
    return status, name, link, release_date


def build_artist_dict(start, end):
    artist_dict = dict()
    while start <= end:
        status, name, link, date = get_artist_and_song_url(start)
        if status == 200:
            if name in artist_dict.keys():
                artist_dict[name].append((link, date))
            else:
                artist_dict[name] = list()
                artist_dict[name].append((link, date))
        start += 1
    return artist_dict


def main():
<<<<<<< HEAD
    ad = build_artist_dict(350001, 400000)
=======
    ad = build_artist_dict(28000, 56000)
>>>>>>> d6c81dd0fd0316cf08de4a6704aa55f35115fbcc
    with open('results.p', 'wb') as f:
        pickle.dump(ad, f)


if __name__ == "__main__":
    main()


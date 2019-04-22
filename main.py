import requests, json
import pickle
TOKEN = 'ujcJqpQBid1pt6rJDkPKQHMMn5boncVwUTgBGh2DfPUi_MXs824FG9y72YRcr8Km'
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
    counter = 1
    filename = 'data.p'
    save(filename, artist_dict)
    while start <= end:
        if counter == 1000:
            counter = 1
            previous_results = load(filename)
            merged = merge_two_dicts(previous_results, artist_dict)
            save(filename, merged)
        status, name, link, date = get_artist_and_song_url(start)
        if status == 200:
            if name in artist_dict.keys():
                artist_dict[name].append((link, date))
            else:
                artist_dict[name] = list()
                artist_dict[name].append((link, date))
        start += 1
        counter += 1
    return artist_dict, start


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


def load(name):
    with open(name, 'rb') as f:
        data_new = pickle.load(f)
    return data_new


def save(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)


def main():
    ad, index = build_artist_dict(150000, 200000)
    filename = str(index) + '.p'
    with open(filename, 'wb') as f:
        pickle.dump(ad, f)


if __name__ == "__main__":
    main()


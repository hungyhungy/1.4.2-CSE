import csv
import sys
import random

def read_csv(filename):
    song_list = []
    with open(filename, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            song_list.append(row)
    return song_list

def play_song(song):
    print(f"Playing: {song['track_name']} by: {song['track_artist']}")
    song['played_count'] += 1
    user_input = input("Press anything to stop / 'x' to quit / 'z' to go to home / 'd' to show Data: ")
    if user_input.lower() == 'x':
        sys.exit()
    elif user_input.lower() == 'z':
        check()
    elif user_input.lower() == 'd':
        display_data()

def check():
    while True:
        play_method = input('What Play method would you like, (S)huffle, (A)rtist, (Al)bum, (Y)ear: ')
        if play_method.lower() not in ['s', 'a', 'al', 'y']:
            print('Please enter a valid input.')
        elif play_method.lower() == 's':
            play_songs('shuffle')
        elif play_method.lower() == 'al':
            play_songs('track_album_name')
        elif play_method.lower() == 'a':
            artist_name = input("What's the artist's name?: ")
            play_songs('artist', artist_name=artist_name)
        elif play_method.lower() == 'y':
            play_songs('track_album_release_date')

def play_songs(sorting_method, artist_name=None):
    for item in song_list:
        item[new_key] = 0

    if sorting_method == 'shuffle':
        random.shuffle(song_list)
        for song in song_list:
            play_song(song)
    elif sorting_method == 'artist':
        artist_list = [s for s in song_list if s['track_artist'] == artist_name]
        if artist_list:
            random.shuffle(artist_list)
            for song in artist_list:
                play_song(song)
        else:
            print(f"\nNo songs found for artist: {artist_name}\n")
    else:
        song_list.sort(key=lambda x: x[sorting_method])
        for song in song_list:
            play_song(song)

def display_data():
    sorted_for_data = list(filter(lambda x: x['played_count'] > 0, song_list))
    for song in sorted_for_data:
        print(f"\nYou played {song['track_name']} {song['played_count']} times\n")

if __name__ == "__main__":
    new_key = 'played_count'
    song_list = read_csv('spotify_songs.csv')
    play_songs(check())

import spotipy

spotify = spotipy.Spotify\
    (client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials\
        (client_id='', client_secret=''))

def get_artists_from_playlist(playlist_url):
    artists = {}
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_url)
    for song in playlist_tracks['items']:
        if song['track']:
            print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']]=song['track']['artists'][0]['name']
    return artists
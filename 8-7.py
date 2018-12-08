def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('michael buble', 'nobody but me')
print(album)

album = make_album('john legenc', 'evolver')
print(album)

album = make_album('the beatles', 'abbey road')
print(album)
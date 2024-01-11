import os


def main():
    if os.path.exists("/Users/luna/real-version/songs"):
        print("kjs;jdafkbnskahj;felbfnsmd")
        pass
    else:
        os.mkdir("/Users/luna/real-version/songs/")

    songs = []
    parent_dir = "/Users/luna/real-version/test/songs/"

    song_to_be_added = []

    song_name = input("Enter the song name: ")
    song_artist = input("Enter the artist: ")
    song_rating = int(input("Enter the rating (0-9): "))
    songs.append([song_name, song_artist, str(song_rating)])
    print(songs)

    os.mkdir(parent_dir + song_name)


if __name__ == "__main__":
    main()

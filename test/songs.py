import os


def main():
    if os.path.exists("/Users/luna/real-version/test/songs"):
        print("kjs;jdafkbnskahj;felbfnsmd")
        pass
    else:
        os.mkdir("/Users/luna/real-version/test/songs/")

    songs = []
    parent_dir = "/Users/luna/real-version/test/songs/"

    song_to_be_added = []

    song_name = input("Enter the song name: ")
    song_artist = input("Enter the artist: ")
    song_rating = int(input("Enter the rating (0-9): "))
    songs.append([song_name, song_artist, str(song_rating)])
    print(songs)

    os.mkdir(parent_dir + song_name)
    os.chdir("/Users/luna/real-version/test/songs/helloworld/")
    with open(song_name, "w") as f:
        f.write("hsdfaiuhgvhjbkalfhidsubkjsaewfigdsbjk\n")


if __name__ == "__main__":
    main()

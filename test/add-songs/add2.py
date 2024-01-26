import random
from pprint import pprint

songs = [["song1", 1], ["song2", 5], ["song3", 5], ["song4", 9], ["song5", 2]]


def choose_song():
    # extracting songs and their corresponding weights
    song_names, weights = zip(*songs)

    # inverting the weights
    inverted_weights = [max(weights) - weight for weight in weights]

    # using the weights for a weighted random selection
    chosen_song = random.choices(song_names, weights=inverted_weights)[0]

    return chosen_song


def main():
    songs = [[0], [0], [0], [0], [0]]
    for i in range(1000):
        chosen_song = choose_song()
        if chosen_song == "song1":
            songs[0][0] += 1
        elif chosen_song == "song2":
            songs[1][0] += 1
        elif chosen_song == "song3":
            songs[2][0] += 1
        elif chosen_song == "song4":
            songs[3][0] += 1
        elif chosen_song == "song5":
            songs[4][0] += 1
    pprint(songs)


if __name__ == "__main__":
    main()

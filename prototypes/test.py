def main():
    with open("paste.txt", "w") as f:
        f.write("# G STRING")
        for i in range(0, 25):
            f.write(
                f"""
g_{i}_button = NoteButton(note_button_coords[{i}], note_button_coords[0], note_button_width, note_button_height, RED, "{i}", BLACK, "g", "g-{i}")
list_of_note_buttons.append(g_{i}_button)\n"""
            )
        f.write("# D STRING")
        for i in range(0, 25):
            f.write(
                f"""
d_{i}_button = NoteButton(note_button_coords[{i}], note_button_coords[1], note_button_width, note_button_height, ORANGE, "{i}", BLACK, "d", "d-{i}")
list_of_note_buttons.append(d_{i}_button)\n"""
            )
        f.write("# A STRING")
        for i in range(0, 25):
            f.write(
                f"""
a_{i}_button = NoteButton(note_button_coords[{i}], note_button_coords[2], note_button_width, note_button_height, YELLOW, "{i}", BLACK, "a", "a-{i}")
list_of_note_buttons.append(a_{i}_button)\n"""
            )
        f.write("# E STRING")
        for i in range(0, 25):
            f.write(
                f"""
e_{i}_button = NoteButton(note_button_coords[{i}], note_button_coords[3], note_button_width, note_button_height, GREEN, "{i}", BLACK, "e", "e-{i}")
list_of_note_buttons.append(e_{i}_button)\n"""
            )


if __name__ == "__main__":
    main()

import sys

from datetime import datetime
import pygame


def main():

    with open("logfile.txt", "a") as f:

        f.write(f"{datetime.now()}: App started\n")
        RED = (255, 0, 0)
        ORANGE = (255, 165, 0)
        YELLOW = (255, 255, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        MAGENTA = (255, 0, 255)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        class Button:
            def __init__(self, x, y, width, height, color, text, text_color):
                self.rect = pygame.Rect(x, y, width, height)
                self.color = color  # tuple of 3 ints (0 <= x <= 255)
                self.text = text  # string
                self.text_color = text_color  # tuple of 3 ints (0 <= x <= 255)

            def draw(self, screen):
                pygame.draw.rect(screen, self.color, self.rect)
                global font
                font = pygame.font.Font(
                    "/System/Library/Fonts/Supplemental/Arial.ttf", 28
                )
                text = font.render(self.text, True, self.text_color)
                text_rect = text.get_rect(center=self.rect.center)
                screen.blit(text, text_rect)

            def is_clicked(self, pos):
                return self.rect.collidepoint(pos)

        class NoteButton(Button):
            def __init__(
                self, x, y, width, height, color, text, text_color, string, description
            ):
                super().__init__(x, y, width, height, color, text, text_color)
                self.string = string  # char
                self.description = description  # string

            def get_string(self):
                return self.string

        pygame.init()

        screen_width = 1280
        screen_height = 720

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Main menu")
        f.write(f"{datetime.now()}: Caption is now 'Main Menu'\n")

        # BUTTONS
        def make_main_menu_buttons():
            list_of_buttons = []

            global make_tab_button
            make_tab_button_width = 200
            make_tab_button_height = 100
            make_tab_button_x_pos = (screen_width - make_tab_button_width) // 2
            make_tab_button_y_pos = 0
            make_tab_button = Button(
                make_tab_button_x_pos,
                make_tab_button_y_pos,
                make_tab_button_width,
                make_tab_button_height,
                RED,
                "Make tab",
                WHITE,
            )
            list_of_buttons.append(make_tab_button)

            global view_songs_button
            view_songs_button_width = 200
            view_songs_button_height = 100
            view_songs_button_x_pos = (
                screen_width - make_tab_button_width) // 2
            view_songs_button_y_pos = 105
            view_songs_button = Button(
                view_songs_button_x_pos,
                view_songs_button_y_pos,
                view_songs_button_width,
                view_songs_button_height,
                ORANGE,
                "View songs",
                BLACK,
            )
            list_of_buttons.append(view_songs_button)

            global visualisation_button
            visualisation_button_width = 200
            visualisation_button_height = 100
            visualisation_button_x_pos = (
                screen_width - visualisation_button_width
            ) // 2
            visualisation_button_y_pos = 210
            visualisation_button = Button(
                visualisation_button_x_pos,
                visualisation_button_y_pos,
                visualisation_button_width,
                visualisation_button_height,
                YELLOW,
                "Visualisation",
                BLACK,
            )
            list_of_buttons.append(visualisation_button)

            global show_song_button
            show_song_button_width = 200
            show_song_button_height = 100
            show_song_button_x_pos = (screen_width - show_song_button_width) // 2
            show_song_button_y_pos = 315
            show_song_button = Button(
                show_song_button_x_pos,
                show_song_button_y_pos,
                show_song_button_width,
                show_song_button_height,
                GREEN,
                "Show song!",
                BLACK,
            )
            list_of_buttons.append(show_song_button)

            global main_menu_button
            main_menu_button = Button(0, 660, 100, 60, BLUE, "Home", WHITE)
            # list_of_buttons.append(main_menu_button)

            f.write(
                f"{datetime.now()}: Called function make_main_menu_buttons()\n")
            return list_of_buttons

        def make_note_buttons():
            # w = 46
            # h = 46
            # gap = 5

            # maths to programmatically determine the x and y coords of every button
            # because the note buttons are squares they are essentially on a square grid
            # you can generate the grid with logic in the list comprehension and then use it for x and y

            note_button_coords = [i for i in range(0, 1280, 51)]

            note_button_width = 46
            note_button_height = 46
            list_of_note_buttons = []

            # G STRING
            g_0_button = NoteButton(note_button_coords[0], note_button_coords[0], note_button_width, note_button_height, RED, "0", BLACK, "g", "g-0",)
            list_of_note_buttons.append(g_0_button)

            g_1_button = NoteButton(
                note_button_coords[1],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "1",
                BLACK,
                "g",
                "g-1",
            )
            list_of_note_buttons.append(g_1_button)

            g_2_button = NoteButton(
                note_button_coords[2],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "2",
                BLACK,
                "g",
                "g-2",
            )
            list_of_note_buttons.append(g_2_button)

            g_3_button = NoteButton(
                note_button_coords[3],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "3",
                BLACK,
                "g",
                "g-3",
            )
            list_of_note_buttons.append(g_3_button)

            g_4_button = NoteButton(
                note_button_coords[4],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "4",
                BLACK,
                "g",
                "g-4",
            )
            list_of_note_buttons.append(g_4_button)

            g_5_button = NoteButton(
                note_button_coords[5],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "5",
                BLACK,
                "g",
                "g-5",
            )
            list_of_note_buttons.append(g_5_button)

            g_6_button = NoteButton(
                note_button_coords[6],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "6",
                BLACK,
                "g",
                "g-6",
            )
            list_of_note_buttons.append(g_6_button)

            g_7_button = NoteButton(
                note_button_coords[7],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "7",
                BLACK,
                "g",
                "g-7",
            )
            list_of_note_buttons.append(g_7_button)

            g_8_button = NoteButton(
                note_button_coords[8],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "8",
                BLACK,
                "g",
                "g-8",
            )
            list_of_note_buttons.append(g_8_button)

            g_9_button = NoteButton(
                note_button_coords[9],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "9",
                BLACK,
                "g",
                "g-9",
            )
            list_of_note_buttons.append(g_9_button)

            g_10_button = NoteButton(
                note_button_coords[10],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "10",
                BLACK,
                "g",
                "g-10",
            )
            list_of_note_buttons.append(g_10_button)

            g_11_button = NoteButton(
                note_button_coords[11],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "11",
                BLACK,
                "g",
                "g-11",
            )
            list_of_note_buttons.append(g_11_button)

            g_12_button = NoteButton(
                note_button_coords[12],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "12",
                BLACK,
                "g",
                "g-12",
            )
            list_of_note_buttons.append(g_12_button)

            g_13_button = NoteButton(
                note_button_coords[13],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "13",
                BLACK,
                "g",
                "g-13",
            )
            list_of_note_buttons.append(g_13_button)

            g_14_button = NoteButton(
                note_button_coords[14],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "14",
                BLACK,
                "g",
                "g-14",
            )
            list_of_note_buttons.append(g_14_button)

            g_15_button = NoteButton(
                note_button_coords[15],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "15",
                BLACK,
                "g",
                "g-15",
            )
            list_of_note_buttons.append(g_15_button)

            g_16_button = NoteButton(
                note_button_coords[16],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "16",
                BLACK,
                "g",
                "g-16",
            )
            list_of_note_buttons.append(g_16_button)

            g_17_button = NoteButton(
                note_button_coords[17],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "17",
                BLACK,
                "g",
                "g-17",
            )
            list_of_note_buttons.append(g_17_button)

            g_18_button = NoteButton(
                note_button_coords[18],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "18",
                BLACK,
                "g",
                "g-18",
            )
            list_of_note_buttons.append(g_18_button)

            g_19_button = NoteButton(
                note_button_coords[19],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "19",
                BLACK,
                "g",
                "g-19",
            )
            list_of_note_buttons.append(g_19_button)

            g_20_button = NoteButton(
                note_button_coords[20],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "20",
                BLACK,
                "g",
                "g-20",
            )
            list_of_note_buttons.append(g_20_button)

            g_21_button = NoteButton(
                note_button_coords[21],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "21",
                BLACK,
                "g",
                "g-21",
            )
            list_of_note_buttons.append(g_21_button)

            g_22_button = NoteButton(
                note_button_coords[22],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "22",
                BLACK,
                "g",
                "g-22",
            )
            list_of_note_buttons.append(g_22_button)

            g_23_button = NoteButton(
                note_button_coords[23],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "23",
                BLACK,
                "g",
                "g-23",
            )
            list_of_note_buttons.append(g_23_button)

            g_24_button = NoteButton(
                note_button_coords[24],
                note_button_coords[0],
                note_button_width,
                note_button_height,
                RED,
                "24",
                BLACK,
                "g",
                "g-24",
            )
            list_of_note_buttons.append(g_24_button)

            # D STRING
            d_0_button = NoteButton(
                note_button_coords[0],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "0",
                BLACK,
                "d",
                "d-0",
            )
            list_of_note_buttons.append(d_0_button)

            d_1_button = NoteButton(
                note_button_coords[1],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "1",
                BLACK,
                "d",
                "d-1",
            )
            list_of_note_buttons.append(d_1_button)

            d_2_button = NoteButton(
                note_button_coords[2],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "2",
                BLACK,
                "d",
                "d-2",
            )
            list_of_note_buttons.append(d_2_button)

            d_3_button = NoteButton(
                note_button_coords[3],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "3",
                BLACK,
                "d",
                "d-3",
            )
            list_of_note_buttons.append(d_3_button)

            d_4_button = NoteButton(
                note_button_coords[4],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "4",
                BLACK,
                "d",
                "d-4",
            )
            list_of_note_buttons.append(d_4_button)

            d_5_button = NoteButton(
                note_button_coords[5],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "5",
                BLACK,
                "d",
                "d-5",
            )
            list_of_note_buttons.append(d_5_button)

            d_6_button = NoteButton(
                note_button_coords[6],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "6",
                BLACK,
                "d",
                "d-6",
            )
            list_of_note_buttons.append(d_6_button)

            d_7_button = NoteButton(
                note_button_coords[7],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "7",
                BLACK,
                "d",
                "d-7",
            )
            list_of_note_buttons.append(d_7_button)

            d_8_button = NoteButton(
                note_button_coords[8],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "8",
                BLACK,
                "d",
                "d-8",
            )
            list_of_note_buttons.append(d_8_button)

            d_9_button = NoteButton(
                note_button_coords[9],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "9",
                BLACK,
                "d",
                "d-9",
            )
            list_of_note_buttons.append(d_9_button)

            d_10_button = NoteButton(
                note_button_coords[10],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "10",
                BLACK,
                "d",
                "d-10",
            )
            list_of_note_buttons.append(d_10_button)

            d_11_button = NoteButton(
                note_button_coords[11],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "11",
                BLACK,
                "d",
                "d-11",
            )
            list_of_note_buttons.append(d_11_button)

            d_12_button = NoteButton(
                note_button_coords[12],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "12",
                BLACK,
                "d",
                "d-12",
            )
            list_of_note_buttons.append(d_12_button)

            d_13_button = NoteButton(
                note_button_coords[13],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "13",
                BLACK,
                "d",
                "d-13",
            )
            list_of_note_buttons.append(d_13_button)

            d_14_button = NoteButton(
                note_button_coords[14],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "14",
                BLACK,
                "d",
                "d-14",
            )
            list_of_note_buttons.append(d_14_button)

            d_15_button = NoteButton(
                note_button_coords[15],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "15",
                BLACK,
                "d",
                "d-15",
            )
            list_of_note_buttons.append(d_15_button)

            d_16_button = NoteButton(
                note_button_coords[16],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "16",
                BLACK,
                "d",
                "d-16",
            )
            list_of_note_buttons.append(d_16_button)

            d_17_button = NoteButton(
                note_button_coords[17],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "17",
                BLACK,
                "d",
                "d-17",
            )
            list_of_note_buttons.append(d_17_button)

            d_18_button = NoteButton(
                note_button_coords[18],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "18",
                BLACK,
                "d",
                "d-18",
            )
            list_of_note_buttons.append(d_18_button)

            d_19_button = NoteButton(
                note_button_coords[19],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "19",
                BLACK,
                "d",
                "d-19",
            )
            list_of_note_buttons.append(d_19_button)

            d_20_button = NoteButton(
                note_button_coords[20],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "20",
                BLACK,
                "d",
                "d-20",
            )
            list_of_note_buttons.append(d_20_button)

            d_21_button = NoteButton(
                note_button_coords[21],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "21",
                BLACK,
                "d",
                "d-21",
            )
            list_of_note_buttons.append(d_21_button)

            d_22_button = NoteButton(
                note_button_coords[22],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "22",
                BLACK,
                "d",
                "d-22",
            )
            list_of_note_buttons.append(d_22_button)

            d_23_button = NoteButton(
                note_button_coords[23],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "23",
                BLACK,
                "d",
                "d-23",
            )
            list_of_note_buttons.append(d_23_button)

            d_24_button = NoteButton(
                note_button_coords[24],
                note_button_coords[1],
                note_button_width,
                note_button_height,
                ORANGE,
                "24",
                BLACK,
                "d",
                "d-24",
            )
            list_of_note_buttons.append(d_24_button)

            # A STRING
            a_0_button = NoteButton(
                note_button_coords[0],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "0",
                BLACK,
                "a",
                "a-0",
            )
            list_of_note_buttons.append(a_0_button)

            a_1_button = NoteButton(
                note_button_coords[1],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "1",
                BLACK,
                "a",
                "a-1",
            )
            list_of_note_buttons.append(a_1_button)

            a_2_button = NoteButton(
                note_button_coords[2],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "2",
                BLACK,
                "a",
                "a-2",
            )
            list_of_note_buttons.append(a_2_button)

            a_3_button = NoteButton(
                note_button_coords[3],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "3",
                BLACK,
                "a",
                "a-3",
            )
            list_of_note_buttons.append(a_3_button)

            a_4_button = NoteButton(
                note_button_coords[4],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "4",
                BLACK,
                "a",
                "a-4",
            )
            list_of_note_buttons.append(a_4_button)

            a_5_button = NoteButton(
                note_button_coords[5],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "5",
                BLACK,
                "a",
                "a-5",
            )
            list_of_note_buttons.append(a_5_button)

            a_6_button = NoteButton(
                note_button_coords[6],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "6",
                BLACK,
                "a",
                "a-6",
            )
            list_of_note_buttons.append(a_6_button)

            a_7_button = NoteButton(
                note_button_coords[7],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "7",
                BLACK,
                "a",
                "a-7",
            )
            list_of_note_buttons.append(a_7_button)

            a_8_button = NoteButton(
                note_button_coords[8],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "8",
                BLACK,
                "a",
                "a-8",
            )
            list_of_note_buttons.append(a_8_button)

            a_9_button = NoteButton(
                note_button_coords[9],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "9",
                BLACK,
                "a",
                "a-9",
            )
            list_of_note_buttons.append(a_9_button)

            a_10_button = NoteButton(
                note_button_coords[10],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "10",
                BLACK,
                "a",
                "a-10",
            )
            list_of_note_buttons.append(a_10_button)

            a_11_button = NoteButton(
                note_button_coords[11],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "11",
                BLACK,
                "a",
                "a-11",
            )
            list_of_note_buttons.append(a_11_button)

            a_12_button = NoteButton(
                note_button_coords[12],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "12",
                BLACK,
                "a",
                "a-12",
            )
            list_of_note_buttons.append(a_12_button)

            a_13_button = NoteButton(
                note_button_coords[13],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "13",
                BLACK,
                "a",
                "a-13",
            )
            list_of_note_buttons.append(a_13_button)

            a_14_button = NoteButton(
                note_button_coords[14],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "14",
                BLACK,
                "a",
                "a-14",
            )
            list_of_note_buttons.append(a_14_button)

            a_15_button = NoteButton(
                note_button_coords[15],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "15",
                BLACK,
                "a",
                "a-15",
            )
            list_of_note_buttons.append(a_15_button)

            a_16_button = NoteButton(
                note_button_coords[16],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "16",
                BLACK,
                "a",
                "a-16",
            )
            list_of_note_buttons.append(a_16_button)

            a_17_button = NoteButton(
                note_button_coords[17],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "17",
                BLACK,
                "a",
                "a-17",
            )
            list_of_note_buttons.append(a_17_button)

            a_18_button = NoteButton(
                note_button_coords[18],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "18",
                BLACK,
                "a",
                "a-18",
            )
            list_of_note_buttons.append(a_18_button)

            a_19_button = NoteButton(
                note_button_coords[19],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "19",
                BLACK,
                "a",
                "a-19",
            )
            list_of_note_buttons.append(a_19_button)

            a_20_button = NoteButton(
                note_button_coords[20],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "20",
                BLACK,
                "a",
                "a-20",
            )
            list_of_note_buttons.append(a_20_button)

            a_21_button = NoteButton(
                note_button_coords[21],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "21",
                BLACK,
                "a",
                "a-21",
            )
            list_of_note_buttons.append(a_21_button)

            a_22_button = NoteButton(
                note_button_coords[22],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "22",
                BLACK,
                "a",
                "a-22",
            )
            list_of_note_buttons.append(a_22_button)

            a_23_button = NoteButton(
                note_button_coords[23],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "23",
                BLACK,
                "a",
                "a-23",
            )
            list_of_note_buttons.append(a_23_button)

            a_24_button = NoteButton(
                note_button_coords[24],
                note_button_coords[2],
                note_button_width,
                note_button_height,
                YELLOW,
                "24",
                BLACK,
                "a",
                "a-24",
            )
            list_of_note_buttons.append(a_24_button)

            # E STRING
            e_0_button = NoteButton(
                note_button_coords[0],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "0",
                BLACK,
                "e",
                "e-0",
            )
            list_of_note_buttons.append(e_0_button)

            e_1_button = NoteButton(
                note_button_coords[1],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "1",
                BLACK,
                "e",
                "e-1",
            )
            list_of_note_buttons.append(e_1_button)

            e_2_button = NoteButton(
                note_button_coords[2],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "2",
                BLACK,
                "e",
                "e-2",
            )
            list_of_note_buttons.append(e_2_button)

            e_3_button = NoteButton(
                note_button_coords[3],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "3",
                BLACK,
                "e",
                "e-3",
            )
            list_of_note_buttons.append(e_3_button)

            e_4_button = NoteButton(
                note_button_coords[4],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "4",
                BLACK,
                "e",
                "e-4",
            )
            list_of_note_buttons.append(e_4_button)

            e_5_button = NoteButton(
                note_button_coords[5],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "5",
                BLACK,
                "e",
                "e-5",
            )
            list_of_note_buttons.append(e_5_button)

            e_6_button = NoteButton(
                note_button_coords[6],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "6",
                BLACK,
                "e",
                "e-6",
            )
            list_of_note_buttons.append(e_6_button)

            e_7_button = NoteButton(
                note_button_coords[7],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "7",
                BLACK,
                "e",
                "e-7",
            )
            list_of_note_buttons.append(e_7_button)

            e_8_button = NoteButton(
                note_button_coords[8],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "8",
                BLACK,
                "e",
                "e-8",
            )
            list_of_note_buttons.append(e_8_button)

            e_9_button = NoteButton(
                note_button_coords[9],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "9",
                BLACK,
                "e",
                "e-9",
            )
            list_of_note_buttons.append(e_9_button)

            e_10_button = NoteButton(
                note_button_coords[10],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "10",
                BLACK,
                "e",
                "e-10",
            )
            list_of_note_buttons.append(e_10_button)

            e_11_button = NoteButton(
                note_button_coords[11],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "11",
                BLACK,
                "e",
                "e-11",
            )
            list_of_note_buttons.append(e_11_button)

            e_12_button = NoteButton(
                note_button_coords[12],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "12",
                BLACK,
                "e",
                "e-12",
            )
            list_of_note_buttons.append(e_12_button)

            e_13_button = NoteButton(
                note_button_coords[13],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "13",
                BLACK,
                "e",
                "e-13",
            )
            list_of_note_buttons.append(e_13_button)

            e_14_button = NoteButton(
                note_button_coords[14],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "14",
                BLACK,
                "e",
                "e-14",
            )
            list_of_note_buttons.append(e_14_button)

            e_15_button = NoteButton(
                note_button_coords[15],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "15",
                BLACK,
                "e",
                "e-15",
            )
            list_of_note_buttons.append(e_15_button)

            e_16_button = NoteButton(
                note_button_coords[16],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "16",
                BLACK,
                "e",
                "e-16",
            )
            list_of_note_buttons.append(e_16_button)

            e_17_button = NoteButton(
                note_button_coords[17],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "17",
                BLACK,
                "e",
                "e-17",
            )
            list_of_note_buttons.append(e_17_button)

            e_18_button = NoteButton(
                note_button_coords[18],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "18",
                BLACK,
                "e",
                "e-18",
            )
            list_of_note_buttons.append(e_18_button)

            e_19_button = NoteButton(
                note_button_coords[19],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "19",
                BLACK,
                "e",
                "e-19",
            )
            list_of_note_buttons.append(e_19_button)

            e_20_button = NoteButton(
                note_button_coords[20],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "20",
                BLACK,
                "e",
                "e-20",
            )
            list_of_note_buttons.append(e_20_button)

            e_21_button = NoteButton(
                note_button_coords[21],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "21",
                BLACK,
                "e",
                "e-21",
            )
            list_of_note_buttons.append(e_21_button)

            e_22_button = NoteButton(
                note_button_coords[22],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "22",
                BLACK,
                "e",
                "e-22",
            )
            list_of_note_buttons.append(e_22_button)

            e_23_button = NoteButton(
                note_button_coords[23],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "23",
                BLACK,
                "e",
                "e-23",
            )
            list_of_note_buttons.append(e_23_button)

            e_24_button = NoteButton(
                note_button_coords[24],
                note_button_coords[3],
                note_button_width,
                note_button_height,
                GREEN,
                "24",
                BLACK,
                "e",
                "e-24",
            )
            list_of_note_buttons.append(e_24_button)

            # SPECIAL BUTTONS
            rest_button = NoteButton(
                note_button_coords[0],
                note_button_coords[4],
                note_button_width,
                note_button_height,
                MAGENTA,
                "R",
                BLACK,
                None,
                "Adds a rest to all strings",
            )
            list_of_note_buttons.append(rest_button)

            hammer_on_button = NoteButton(
                note_button_coords[1],
                note_button_coords[4],
                note_button_width,
                note_button_height,
                MAGENTA,
                "H",
                BLACK,
                None,
                "Adds a hammer on to the current string",
            )
            list_of_note_buttons.append(hammer_on_button)

            pull_off_button = NoteButton(
                note_button_coords[2],
                note_button_coords[4],
                note_button_width,
                note_button_height,
                MAGENTA,
                "P",
                BLACK,
                None,
                "Adds a pull off to the current string",
            )
            list_of_note_buttons.append(pull_off_button)

            slide_up_button = NoteButton(
                note_button_coords[3],
                note_button_coords[4],
                note_button_width,
                note_button_height,
                MAGENTA,
                "/",
                BLACK,
                None,
                "Adds a slide up to the current string",
            )
            list_of_note_buttons.append(slide_up_button)

            slide_down_button = NoteButton(
                note_button_coords[4],
                note_button_coords[4],
                note_button_width,
                note_button_height,
                MAGENTA,
                "\\",
                BLACK,
                None,
                "Adds a slide down to the current string",
            )
            list_of_note_buttons.append(slide_down_button)

            f.write(f"{datetime.now()}: Called function make_note_buttons()\n")
            return list_of_note_buttons

        make_main_menu_buttons()
        make_note_buttons()

        # this list will be used within the game loop
        # the program initialises the buttons by calling the list in the game loop

        # this is the main menu state (FIRST LOAD)
        buttons = make_main_menu_buttons()

        # note_buttons is used in the tab maker
        # initialised to empty list, no notes should be on the main menu
        note_buttons = []

        # there are screens represented by integers
        # the app checks what screen it is by looking at the valuse of `current_screen`
        # e.g 1 = main menu, 2 = tab creator with the fret buttons etc
        # ALWAYS STORES A STRING VALUE NAMED AFTER THE SCREEN THE USER IS ON
        current_screen = "main menu"
        running = True

        while running:
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # check if the left mouse button is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()

                    # MAIN MENU
                    if current_screen == "main menu":
                        for button in buttons:
                            if button.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked {button.text}\n")
                        if make_tab_button.is_clicked(pos):
                            # need this to be able to back out if desired
                            buttons = [main_menu_button]

                            # if the user is on screen 1 and make_tab_button is pressed
                            # change to tab maker screen
                            current_screen = "tab maker"

                            # change window title to tab maker
                            # makes app more immersive due to the added attention to detail
                            pygame.display.set_caption("Tab maker")
                            f.write(f"{datetime.now()}: Caption is now 'Tab maker'\n")
                            f.write(f"{datetime.now()}: User will be prompted to enter song details\n")
                            buttons = [main_menu_button]
                            questions = [
                                "Enter song name:",
                                "Enter song artist:",
                                "Enter rating:",
                            ]
                            answers = []
                            current_question = 0

                            # iterate through questions while taking the user input
                            for i, question in enumerate(questions):
                                input_box = pygame.Rect(100, 100, 140, 32)
                                color_inactive = pygame.Color("lightskyblue3")
                                color_active = pygame.Color("dodgerblue2")
                                color = color_inactive
                                active = True
                                text = ""

                                while True:
                                    try:
                                        # log the question the user is currently on
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                return
                                            # get mouse position and make text box active
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                active = True
                                                if input_box.collidepoint(event.pos):
                                                    active = not active
                                                else:
                                                    active = False
                                                # python's syntax for ternary operator
                                                color = color_active if active else color_inactive
                                            # if the user presses a key...
                                            if event.type == pygame.KEYDOWN:
                                                # and the text box is active...
                                                if active:
                                                    # if the user presses return
                                                    if event.key == pygame.K_RETURN:
                                                        if (text.strip()):  # check if the text is not empty or only spaces
                                                            answers.append(
                                                                text.strip())
                                                            # debugging
                                                            print(f"Answer: { text.strip()}\n")
                                                            # debugging
                                                            print(answers)

                                                            # stops when the user has entered three things
                                                            if len(answers) == 3:
                                                                print("user has added 3")
                                                                pygame.quit()

                                                            # increments the iterating variable to move on to the next question
                                                            current_question += 1

                                                            # clear the text box ready for the user's next answer
                                                            text = ""
                                                            break
                                                    elif (
                                                        event.key == pygame.K_BACKSPACE
                                                    ):
                                                        text = text[:-1]
                                                    else:
                                                        text += event.unicode

                                        # if this isn't here, the text above the text box won't update
                                        # and the text in the text box won't appear to clear upon pressing Enter
                                        # even though it actually does get rendered correctly
                                        screen.fill(WHITE)

                                        # render and display the question
                                        question_surface = font.render(
                                            questions[current_question],
                                            True, (0, 0, 0),
                                        )
                                        screen.blit(
                                            question_surface,
                                            (input_box.x, input_box.y - 30),
                                        )

                                        txt_surface = font.render(
                                            text, True, color)
                                        width = max(
                                            200, txt_surface.get_width() + 10)
                                        input_box.w = width
                                        screen.blit(
                                            txt_surface,
                                            (input_box.x + 5, input_box.y + 5),
                                        )
                                        pygame.draw.rect(
                                            screen, color, input_box, 2)

                                        # required for the code to work
                                        pygame.display.flip()
                                        clock.tick(60)
                                    # don't want to deal with an actual error message
                                    except IndexError:
                                        print("index error")
                                        sys.exit()
                                    except pygame.error:
                                        print("pygame.error")
                                        sys.exit()
                            # note_buttons = make_note_buttons()

                        if view_songs_button.is_clicked(pos):
                            current_screen = "view songs"
                            pygame.display.set_caption("View songs")
                            f.write(f"{datetime.now()}: Caption is now 'View songs'\n")
                            buttons = [main_menu_button]
                            note_buttons = []

                        if visualisation_button.is_clicked(pos):
                            current_screen = "visualisation"
                            pygame.display.set_caption("Visualisation")
                            f.write(f"{datetime.now()}: Caption is now 'Visualisation'\n")
                            buttons = [main_menu_button]

                        if show_song_button.is_clicked(pos):
                            current_screen = "show song"
                            pygame.display.set_caption("Show song")
                            f.write(f"{datetime.now()}: Caption is now 'Show song'\n")
                            buttons = [main_menu_button]

                    # TAB MAKER
                    elif current_screen == "tab maker":
                        # runs number of times `note_buttons` is long
                        # then moves on to `if main_menu_button.is_clicked(pos):`
                        for i in note_buttons:
                            if i.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked {i.text}, string: {i.description}\n")
                        if main_menu_button.is_clicked(pos):
                            f.write(f"{datetime.now()}: Clicked main menu button\n")
                            # if user clicks the switch button when it's already screen 2
                            # change to main menu
                            current_screen = "main menu"

                            # change window title to main menu
                            pygame.display.set_caption("Main menu")
                            f.write(f"{datetime.now()}: Caption is now 'Main menu'\n")
                            buttons = make_main_menu_buttons()
                            note_buttons = []

                    # VIEW SONGS
                    elif current_screen == "view songs":
                        for i in buttons:
                            if i.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked {i.text}\n")
                            if main_menu_button.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked main menu button\n")
                                current_screen = "main menu"
                                pygame.display.set_caption("Main menu")
                                f.write(f"{datetime.now()}: Caption is now 'Main menu'\n")
                                buttons = make_main_menu_buttons()

                    # VISUALISATION
                    elif current_screen == "visualisation":
                        for i in buttons:
                            if i.is_clicked(pos):
                                f.write(
                                    f"{datetime.now()}: Clicked {i.text}\n")
                            if main_menu_button.is_clicked(pos):
                                f.write(
                                    f"{datetime.now()}: Clicked main menu button\n")
                                current_screen = "main menu"
                                pygame.display.set_caption("Main menu")
                                f.write(
                                    f"{datetime.now()}: Caption is now 'Main menu'\n"
                                )
                                buttons = make_main_menu_buttons()

                    # SHOW SONG
                    elif current_screen == "show song":
                        for i in buttons:
                            if i.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked {i.text}\n")
                            if main_menu_button.is_clicked(pos):
                                f.write(f"{datetime.now()}: Clicked main menu button\n")
                                current_screen = "main menu"
                                pygame.display.set_caption("Main menu")
                                f.write(f"{datetime.now()}: Caption is now 'Main menu'\n")
                                buttons = make_main_menu_buttons()

            # draw buttons at the end of each frame
            # i's purpose is to facilitate this iteration and acess the button in the list and render it
            # WHILE the game loop is running, the buttons in the list are drawn on the screen
            # which is why they persist on the screen
            all_buttons = buttons + note_buttons
            for i in all_buttons:
                i.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        f.write(f"{datetime.now()}: App exited\n")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()

# snpkggqckczaflcezdjtehnyknbkhpkdmodxfldftocvwgovxhscwuqhabujsdpjslxfoveqdavqxkhgnzrajmzsmjvqcrabipcnfujxjjcadavqxkhgnzralxhzoltepxozcldqhytclhxhxhscwuqhabujhqmsuduidkkmlxhzoltepxozfldftocvwgovxhscwuqhabujrlfdvgqzynjlssbzvudjycgpahlplqkatuntssbzvudjycgpjfvdafwpgldfjmzsmjvqcrabsdpjslxfoveqssbzvudjycgprlfdvgqzynjlxhscwuqhabujlxhzoltepxozxfzfsnvrzshorlfdvgqzynjlxhscwuqhabujhqmsuduidkkmdavqxkhgnzraknbkhpkdmodxmezlmpqkkbwumezlmpqkkbwussbzvudjycgpxfzfsnvrzshoxhscwuqhabujcvwhvwmyrgkklhnhcbrwnpyrxhscwuqhabujuummvyrlidhaknbkhpkdmodxjfvdafwpgldfssbzvudjycgplhnhcbrwnpyrktgaksqebkgzxhscwuqhabujphypaxcvwizplxhzoltepxozlhnhcbrwnpyrxhscwuqhabujflcezdjtehnyssbzvudjycgpjfvdafwpgldfjfvdafwpgldfjmzsmjvqcrabrqoirjhmjmbdxhscwuqhabujehpmcwojanxsjlkkwmsfiwsu

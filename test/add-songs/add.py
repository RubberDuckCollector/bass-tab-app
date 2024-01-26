import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    questions = ["What is your name?", "How old are you?", "Where are you from?"]
    answers = []
    current_question = 0

    for question in questions:
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color("lightskyblue3")
        color_active = pygame.Color("dodgerblue2")
        color = color_inactive
        active = False
        text = ""

        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                if (
                                    text.strip()
                                ):  # check if the text is not empty or only spaces
                                    answers.append(text.strip())
                                    print(f"Answer: {text.strip()}\n")
                                    print(answers)
                                    if len(answers) == 3:
                                        print("user has added 3")
                                        pygame.quit()
                                    current_question += 1
                                    text = ""
                                    break
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode

                screen.fill((30, 30, 30))

                # render and display the question
                question_surface = font.render(
                    questions[current_question], True, (255, 255, 255)
                )
                screen.blit(question_surface, (input_box.x, input_box.y - 30))

                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width() + 10)
                input_box.w = width
                screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                pygame.draw.rect(screen, color, input_box, 2)

                pygame.display.flip()
                clock.tick(60)
            except IndexError:
                print("index error")
                sys.exit()
            except pygame.error:
                print("pygame.error")
                sys.exit()

    pygame.quit()


if __name__ == "__main__":
    main()

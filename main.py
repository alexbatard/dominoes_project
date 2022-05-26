import pygame
import sys
from dominoes.constants import WIDTH, HEIGHT, BLACK, WHITE, AMBER, ROWS,\
     SQUARE_SIZE
from gui.constants import SMALL_FONT, DOMINOES_TEXT, DOMINOES_RECT,\
     SELECT_MODE_TEXT, SELECT_MODE_RECT, BUTTON,\
     SELECT_COMPUTER_DIFFICULTY_TEXT, SELECT_COMPUTER_DIFFICULTY_RECT,\
     BACKGROUND, NAME_TEXT_BOX_1, NAME_TEXT_BOX_2, ENTER_PLAYER_NAMES_TEXT,\
     ENTER_PLAYER_NAMES_RECT, PLAYER1_TEXT, PLAYER1_RECT, PLAYER2_TEXT,\
     PLAYER2_RECT, PRESS_ENTER_TEXT, PRESS_ENTER_RECT
from dominoes.game import Game
from gui.button import Button

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set window dimensions
pygame.display.set_caption("Main menu")  # set window caption

FPS = 60  # frames per second


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main_menu():  # main menu screen
    pygame.display.set_caption('Main menu')

    while True:
        # WIN.fill(TEAL)
        WIN.blit(BACKGROUND, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(pos=(WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Play")

        QUIT_BUTTON = Button(pos=(2 * WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Quit")

        WIN.blit(DOMINOES_TEXT, DOMINOES_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeTextColor(menu_mouse_pos)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(menu_mouse_pos):
                    gamemode_menu()

                if QUIT_BUTTON.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def gamemode_menu():
    pygame.display.set_caption("Gamemode selection")

    while True:
        WIN.blit(BACKGROUND, (0, 0))

        gamemode_mouse_pos = pygame.mouse.get_pos()

        TWO_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 3),
                                    font=SMALL_FONT,
                                    image=BUTTON,
                                    base_color=BLACK,
                                    hovering_color=WHITE,
                                    text_input="2 Players")

        THREE_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, 5 * HEIGHT / 12),
                                      font=SMALL_FONT,
                                      image=BUTTON,
                                      base_color=BLACK,
                                      hovering_color=WHITE,
                                      text_input="3 Players")

        FOUR_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 2),
                                     font=SMALL_FONT,
                                     image=BUTTON,
                                     base_color=BLACK,
                                     hovering_color=WHITE,
                                     text_input="4 Players")

        COMPUTER_BUTTON = Button(pos=(WIDTH / 2, 7 * HEIGHT / 12),
                                 font=SMALL_FONT,
                                 image=BUTTON,
                                 base_color=BLACK,
                                 hovering_color=WHITE,
                                 text_input="Computer")

        BACK_BUTTON = Button(pos=(WIDTH / 2, 11 * HEIGHT / 12),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Back")

        WIN.blit(SELECT_MODE_TEXT, SELECT_MODE_RECT)

        for button in [
                TWO_PLAYERS_BUTTON, THREE_PLAYERS_BUTTON, FOUR_PLAYERS_BUTTON,
                COMPUTER_BUTTON, BACK_BUTTON
        ]:
            button.changeTextColor(gamemode_mouse_pos)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if TWO_PLAYERS_BUTTON.checkForInput(gamemode_mouse_pos):
                    two_players_name_menu()

                if COMPUTER_BUTTON.checkForInput(gamemode_mouse_pos):
                    computer_difficulty_menu()

                if BACK_BUTTON.checkForInput(gamemode_mouse_pos):
                    main_menu()

        pygame.display.update()


def computer_difficulty_menu():
    pygame.display.set_caption("Computer difficulty selection")

    while True:
        WIN.blit(BACKGROUND, (0, 0))

        computer_difficulty_mouse_pos = pygame.mouse.get_pos()

        EASY_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 3),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Easy")

        INTERMEDIATE_BUTTON = Button(pos=(WIDTH / 2, 5 * HEIGHT / 12),
                                     font=SMALL_FONT,
                                     image=BUTTON,
                                     base_color=BLACK,
                                     hovering_color=WHITE,
                                     text_input="Intermediate")

        HARD_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Hard")

        BACK_BUTTON = Button(pos=(WIDTH / 2, 11 * HEIGHT / 12),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Back")

        WIN.blit(SELECT_COMPUTER_DIFFICULTY_TEXT,
                 SELECT_COMPUTER_DIFFICULTY_RECT)

        for button in [
                EASY_BUTTON, INTERMEDIATE_BUTTON, HARD_BUTTON, BACK_BUTTON
        ]:
            button.changeTextColor(computer_difficulty_mouse_pos)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(computer_difficulty_mouse_pos):
                    gamemode_menu()

        pygame.display.update()


def two_players_name_menu():
    pygame.display.set_caption("Name selection")
    player1_name_input = ''
    player2_name_input = ''
    is_text_box_1_active = False
    is_text_box_2_active = False
    text_box_1_color = BLACK
    text_box_2_color = BLACK

    while True:
        WIN.blit(BACKGROUND, (0, 0))

        name_mouse_pos = pygame.mouse.get_pos()
        player1_name_text = SMALL_FONT.render(player1_name_input, True, WHITE)
        player2_name_text = SMALL_FONT.render(player2_name_input, True, WHITE)

        BACK_BUTTON = Button(pos=(WIDTH / 2, 11 * HEIGHT / 12),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Back")

        NAME_TEXT_BOX_1.w = max(150, player1_name_text.get_width() + 9)
        NAME_TEXT_BOX_2.w = max(150, player2_name_text.get_width() + 9)

        if is_text_box_1_active:
            text_box_1_color = AMBER
            text_box_2_color = BLACK
        elif is_text_box_2_active:
            text_box_1_color = BLACK
            text_box_2_color = AMBER
        else:
            text_box_1_color = BLACK
            text_box_2_color = BLACK

        pygame.draw.rect(WIN, text_box_1_color, NAME_TEXT_BOX_1)
        pygame.draw.rect(WIN, text_box_2_color, NAME_TEXT_BOX_2)

        WIN.blit(player1_name_text,
                 (NAME_TEXT_BOX_1.x + 5, NAME_TEXT_BOX_1.y + 10))
        WIN.blit(player2_name_text,
                 (NAME_TEXT_BOX_2.x + 5, NAME_TEXT_BOX_2.y + 10))
        WIN.blit(ENTER_PLAYER_NAMES_TEXT, ENTER_PLAYER_NAMES_RECT)
        WIN.blit(PRESS_ENTER_TEXT, PRESS_ENTER_RECT)
        WIN.blit(PLAYER1_TEXT, PLAYER1_RECT)
        WIN.blit(PLAYER2_TEXT, PLAYER2_RECT)

        for button in [BACK_BUTTON]:
            button.changeTextColor(name_mouse_pos)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_TEXT_BOX_1.collidepoint(event.pos):
                    is_text_box_1_active = True
                    is_text_box_2_active = False
                elif NAME_TEXT_BOX_2.collidepoint(event.pos):
                    is_text_box_1_active = False
                    is_text_box_2_active = True
                else:
                    is_text_box_1_active = False
                    is_text_box_2_active = False

                if BACK_BUTTON.checkForInput(name_mouse_pos):
                    gamemode_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if is_text_box_1_active:
                        player1_name_input = player1_name_input[:-1]
                    if is_text_box_2_active:
                        player2_name_input = player2_name_input[:-1]
                elif event.key == pygame.K_RETURN:
                    global PLAYER1_NAME
                    global PLAYER2_NAME
                    PLAYER1_NAME = player1_name_input
                    PLAYER2_NAME = player2_name_input
                    play()
                else:
                    if is_text_box_1_active and NAME_TEXT_BOX_1.w < 2 * WIDTH\
                       / 5 - NAME_TEXT_BOX_1.x:
                        player1_name_input += event.unicode
                    if is_text_box_2_active and NAME_TEXT_BOX_2.w < 2 * WIDTH\
                       / 5 - NAME_TEXT_BOX_1.x:
                        player2_name_input += event.unicode

        pygame.display.update()


def play():  # main game loop
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    game = Game(WIN)

    while True:  # event loop
        clock.tick(FPS)  # set FPS
        play_mouse_pos = pygame.mouse.get_pos()
        game.update()

        PLAYER1_NAME_TEXT = SMALL_FONT.render(PLAYER1_NAME, True, BLACK)
        PLAYER2_NAME_TEXT = SMALL_FONT.render(PLAYER2_NAME, True, BLACK)
        PLAYER1_NAME_RECT = PLAYER1_NAME_TEXT.get_rect(
            center=(WIDTH / 2, SQUARE_SIZE // 2 + SQUARE_SIZE * (ROWS - 3)))
        PLAYER2_NAME_RECT = PLAYER2_NAME_TEXT.get_rect(
            center=((WIDTH / 2, SQUARE_SIZE // 2 + SQUARE_SIZE * 2)))

        DRAW_BUTTON = Button(pos=(13 * WIDTH / 15, 18.5 * HEIGHT / 21),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Draw")

        END_TURN_BUTTON = Button(pos=(13 * WIDTH / 15, 19.5 * HEIGHT / 21),
                                 font=SMALL_FONT,
                                 image=BUTTON,
                                 base_color=BLACK,
                                 hovering_color=WHITE,
                                 text_input="End turn")

        NEXT_TURN_BUTTON = Button(pos=(13 * WIDTH / 15, 20.5 * HEIGHT / 21),
                                  font=SMALL_FONT,
                                  image=BUTTON,
                                  base_color=BLACK,
                                  hovering_color=WHITE,
                                  text_input="Next turn")

        for event in pygame.event.get():  # check if event happened
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if END_TURN_BUTTON.checkForInput(play_mouse_pos):
                    game.resetTurn()

                elif NEXT_TURN_BUTTON.checkForInput(play_mouse_pos):
                    game.restoreTurn()
                    game.changeTurn()

                elif DRAW_BUTTON.checkForInput(play_mouse_pos):
                    pass

                else:
                    row, col = get_row_col_from_mouse(play_mouse_pos)
                    game.select(row, col)

        WIN.blit(PLAYER1_NAME_TEXT, PLAYER1_NAME_RECT)
        WIN.blit(PLAYER2_NAME_TEXT, PLAYER2_NAME_RECT)

        DRAW_BUTTON.changeTextColor(play_mouse_pos)
        DRAW_BUTTON.update(WIN)

        if game.turn is not None:
            END_TURN_BUTTON.changeTextColor(play_mouse_pos)
            END_TURN_BUTTON.update(WIN)
        else:
            NEXT_TURN_BUTTON.changeTextColor(play_mouse_pos)
            NEXT_TURN_BUTTON.update(WIN)

        pygame.display.update()


if __name__ == "__main__":
    main_menu()

# When 2, 3 or 4 players are playing on the same computer,
# the current player needs to press a button to start his turn.
# His dominoes are then displayed on the screen (under the board).
# When he presses the same button, his turn ends and
# his dominoes are hidden.
# This allows the game to display both players' dominoes,
# but not at the same time, and to set a time limit for 1 turn.

# the game must also display the back of the opponent's dominoes
# so that the other player knows the number of dominoes his oppenent has left
# without seeing the opponent's dominoes'.

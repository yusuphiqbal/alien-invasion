import pygame


class Ship:
    """
    A class to manage the ship.
    """

    def __init__(self, ai_game):
        """
        Initialize the ship and set it's starting position.
        :param ai_game:
        """

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag.
        self.moving_right = False

    def update(self):
        """
        Update the ship's position based on the movement flag.
        :return:
        """

        if self.moving_right:
            self.rect.x += 1

    def blit_me(self):
        """
        Draw the ship at it's current location
        :return:
        """

        self.screen.blit(self.image, self.rect)

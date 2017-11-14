import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf

def run_game():

    # Initialize game and create a screen project.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    # Make a group of bullets in.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens:
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            # Get rid of bullets that have disappeared.
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
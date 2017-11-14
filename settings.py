class Settings():
    """"A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings:
        #-----------------
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings:
        #---------------
        self.ship_speed_factor = 1.5
        self.ship_limit_factor = 3

        # Bullet Settings:
        #-----------------
        self.bullet_speed_factor = 1.618
        self.bullet_width = 2.618
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10000

        # Alien settings:
        #----------------
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


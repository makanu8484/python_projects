class Settings():

    def __init__(self):
        """Screen settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (248, 248, 255)
        #Ship settings
        self.ship_speed_factor = 1.5

        #Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 48, 48
        self.bullets_allowed = 10
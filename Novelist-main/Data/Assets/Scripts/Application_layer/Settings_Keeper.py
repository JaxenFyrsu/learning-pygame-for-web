from os import path
from pygame import display, Surface, FULLSCREEN, RESIZABLE

from ..Universal_computing.Pattern_Singleton import SingletonPattern


class SettingsKeeper(SingletonPattern):
    """
    Reading settings from "settings" file and keep it.
    """

    def __init__(self):
        # Path settings:
        script_root_path = path.abspath(__file__)
        self.user_settings_path = path.join(script_root_path, "user_settings")

        # Read settings configuration file:
        settings = {}
        try:
            with open(self.user_settings_path, "r", encoding="utf-8") as settings_file:
                for line in settings_file:
                    setting_type, value = line.strip().split("=")
                    settings[setting_type] = value
        except FileNotFoundError:
            pass  # Handle missing settings file gracefully

        # Set default values if not found in the file
        width, height = settings.get("screen_size", "800x600").split("x")
        self.screen_size = (int(width), int(height))
        
        self.general_volume = int(settings.get("general_volume", "50"))
        self.music_volume = int(settings.get("music_volume", "50"))
        self.sound_volume = int(settings.get("sound_volume", "50"))
        self.screen_type = settings.get("screen_type", "windowed")
        self.text_language = settings.get("text_language", "eng")
        self.voice_acting_language = settings.get("voice_acting_language", "eng")

        # Display settings:
        self.screen = self.set_windows_settings()
        self.frames_per_second = 60

    def get_windows_settings(self) -> Surface:
        """
        Get "display.set_mode(...)" pygame.Surface with actual settings.
        :return: pygame.Surface
        """
        return self.screen

    def set_windows_settings(self) -> Surface:
        """
        Generate or set new display mode.
        :return: pygame.display.Surface
        """
        if self.screen_type == "full_screen":
            # Get screen size using pygame
            screen: Surface = display.set_mode((0, 0), FULLSCREEN)
        elif self.screen_type == "windowed":
            screen: Surface = display.set_mode(self.screen_size, RESIZABLE)

        # Create the display surface using the desired size and flags
        return screen

    def update_settings(self):
        """
        Update game settings.
        """
        self.screen = self.set_windows_settings()
        self.save_settings()

    def save_settings(self):
        """
        Save new settings to "user_settings" file.
        """
        with open(self.user_settings_path, "w", encoding="utf-8") as settings_file:
            settings_file.write(
                f"# game_settings:\n"
                f"screen_size={self.screen_size[0]}x{self.screen_size[1]}\n"
                f"screen_type={self.screen_type}\n"
                f"general_volume={self.general_volume}\n"
                f"music_volume={self.music_volume}\n"
                f"sound_volume={self.sound_volume}\n"
                f"text_language={self.text_language}\n"
                f"voice_acting_language={self.voice_acting_language}"
            )

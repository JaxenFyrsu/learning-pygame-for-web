import pygbag.aio as asyncio
import logging
from os import path

# Replace pygame imports with potential browser alternatives
# (These are placeholders and might need adjustments)
# from browser_display import set_caption, set_icon  # Hypothetical replacements

from pygame import display

from Assets.Scripts.Application_layer.Assets_load import image_load
from Assets.Scripts.Application_layer.Settings_Keeper import SettingsKeeper
from Assets.Scripts.Application_layer.Game_Master import GameMaster
from Assets.Scripts.Logging_Config import logging_config, text_for_logging


async def run():
    """
    Initialization.
    """
    app_name: str = "Visual Novel"

    icon_set: dict[str] = {
        "Windows": "win_icon",
        "Mac_OS": "mac_icon",
        "linux": "nix_icon"
    }

    # Set game settings:
    start_settings: SettingsKeeper = SettingsKeeper()
    type_of_system: str = start_settings.system_type
    # Path to icons (might need adjustment for web)
    path_to_icons: str = path.join(*[
        'User_Interface', 'Icons'
    ])

    # Browser alternatives for window settings (replace as needed)
    await display.set_caption(app_name)
    await display.set_icon(await image_load(  # Assuming image_load works in web env
        art_name=icon_set[type_of_system],
        file_format='png',
        asset_type=path_to_icons
    ))

    # Start game:
    gameplay: GameMaster = GameMaster()
    await gameplay()  # Make GameMaster asynchronous if needed


async def main():
    logging_config(
        log_path="logg_file.txt",
        log_level=30
    )
    try:
        await run()
    except Exception as error:
        logging.critical(
            text_for_logging(
                log_text="The program launch ended with an error!",
                log_error=error
            )
        )
        raise error


if __name__ == '__main__':
    asyncio.run(main())

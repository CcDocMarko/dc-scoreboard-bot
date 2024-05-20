from nextcord import Color, Embed
from nextcord.ext.commands import Bot
from nextcord import Intents
import nextcord
import logging

intents = Intents.all()

logging.basicConfig(level=logging.INFO)

bot = Bot(command_prefix="/", strip_after_prefix=True, intents=intents)


@bot.event
async def on_ready():
    channel_id = 1011284358826577990  # cea-agents-anything-goes
    channel = bot.get_channel(channel_id)

    if channel is None:
        logging.error(f"Failed to get channel with ID {channel_id}")
        await bot.close()
        return

    embed = Embed(title="ScoreBoard", url="https://login.theccdocs.com/custom/score_board/index.php",
                  description="Agents Appointment Score", color=Color.random())

    try:
        await channel.send(embed=embed)
        logging.info("Message sent successfully.")
    except nextcord.HTTPException as http_error:
        logging.error(f"HTTP error occurred: {http_error}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    await bot.close()


bot.run(token="MTAzNDkzMjQzNDI2MjgzOTM2Nw.G_eJ5h.TlRvvV2CVLQbQCDnIkmC4eiH0Dh9MWiVhuiZ38")
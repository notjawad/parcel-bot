import aiohttp
import glob
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()


class ParcelBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$', intents=discord.Intents.all())
        self.session = None
        self.initial_extensions = [i.replace('\\', '.').replace('.py', '') for i in glob.glob('cogs/*') if
                                   i.endswith('.py')]

    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print('Ready!')


bot = ParcelBot()
bot.run(os.getenv('bot_token'))

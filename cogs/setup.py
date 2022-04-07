from discord.ext import commands
from utils.database import Database
from utils.parcel_web import *


class Setup(commands.Cog):
    """
    A class that houses all commands related to setting up the bot
    """

    def __init__(self, client):
        self.client = client
        self.db = Database().db

    @commands.command(name='auth', aliases=['register', 'signup', 'login'])
    async def authenticate(self, ctx, account_token: str):
        """
        Links Parcel app account using account token
        """
        get_tokens = await self.db['tokens'].find_one({
            "discord_user_id": ctx.author.id
        })
        if get_tokens:
            await ctx.reply('You\'re already logged in!')
        elif check_token(account_token):
            await self.db['tokens'].insert_one({
                'discord_user_id': ctx.author.id,
                'parcel_account_token': account_token,
                'show_delivered': 'yes'
            })
            await ctx.reply('You\'re now logged in! 👋🏼')
        else:
            await ctx.reply('Your token is invalid 👎🏼')

    @commands.command(name='logout', aliases=['signout', 'deactivate'])
    async def remove_account(self, ctx):
        """
        Unlinks your Parcel app account from the bot
        """
        get_tokens = await self.db['tokens'].find_one({
            "discord_user_id": ctx.author.id
        })
        if get_tokens:
            await self.db['tokens'].delete_one({
                'discord_user_id': ctx.author.id
            })
            await ctx.reply('You\'ve been logged out 👋🏼')
        else:
            await ctx.reply('You\'re not logged in')

    @commands.command(name='mode')
    async def change_mode(self, ctx):
        """
        Toggles between showing delivered packages or not
        """
        get_accounts = await self.db['tokens'].find_one({
            "discord_user_id": ctx.author.id
        })

        if not get_accounts:
            await ctx.reply('You\'re not logged in')
        else:
            show_delivered = get_accounts['show_delivered']
            if show_delivered == 'yes':
                await self.db['tokens'].update_one({'discord_user_id': ctx.author.id},
                                                   {'$set': {'show_delivered': 'no'}})
                await ctx.reply('I will no longer show you delivered packages 🚚')
            else:
                await self.db['tokens'].update_one({'discord_user_id': ctx.author.id},
                                                   {'$set': {'show_delivered': 'yes'}})
                await ctx.reply('I will now show all packages, including delivered packages ✅')


async def setup(client):
    await client.add_cog(Setup(client))

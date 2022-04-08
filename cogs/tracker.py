import discord
from discord.ext import commands
from utils.database import Database
from utils.parcel_web import *


def emojify(status):
    if 'delivered' in status.lower():
        return '✅'
    elif 'departed' in status.lower():
        return '🛫'
    elif 'in possession' in status.lower():
        return '🛂'
    elif 'arrived' in status.lower():
        return '🛬'
    elif 'awaiting item' in status.lower():
        return '🕑'
    elif 'out for delivery' in status.lower():
        return '🚚'
    elif 'expects item for mailing' in status.lower():
        return '📥'
    else:
        return ''


class Tracker(commands.Cog):
    """
    A class that houses all package tracking commands
    """

    def __init__(self, client):
        self.client = client
        self.db = Database().db

    @commands.group(aliases=['parcel', 'delivery'])
    async def packages(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('No subcommand was given')

    @packages.command(name='get') # TODO: finish this command
    async def get_package(self, ctx, package_name):
        """
        Returns information about the supplied package name
        """
        get_tokens = await self.db['tokens'].find_one({
            "discord_user_id": ctx.author.id
        })

        if get_tokens:
            ...

        else:
            await ctx.reply('Please login before using this command')

    @packages.command(name='all')
    async def all_packages(self, ctx):
        """
        Returns all your packages
        """
        get_tokens = await self.db['tokens'].find_one({
            "discord_user_id": ctx.author.id
        })

        if get_tokens:
            data = fetch_packages(get_tokens['parcel_account_token'])
            show_delivered = get_tokens['show_delivered']
            packages = []

            for i in data:
                packages.extend(
                    {
                        'tracking_number': package[0],
                        'package_description': package[1],
                        'package_carrier': package[2],
                        'package_status': f'{package[4][0][0]} {package[4][0][1]}',
                        'package_zipcode': package[4][0][2],
                        'package_city': package[4][0][3]} for package in i if len(package) > 10)
            embed = discord.Embed()

            if show_delivered != 'yes':
                for delivery in packages:
                    if 'delivered' not in delivery['package_status'].lower():
                        embed.add_field(
                            name=f"{delivery['package_description']} - {emojify(delivery['package_status'])}",
                            value=delivery['package_status'])
            else:
                for delivery in packages:
                    embed.add_field(name=f"{delivery['package_description']} - {emojify(delivery['package_status'])}",
                                    value=delivery['package_status'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply('Please login before using this command')


async def setup(client):
    await client.add_cog(Tracker(client))

import discord
from discord.ext import commands
import asyncio
import os
#intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.command()
async def fetch_attachments(ctx, channel_id: int):
    channel = bot.get_channel(channel_id)
    if channel is None:
        await ctx.send("Invalid channel ID.")
        return

    attachment_links = []

    async for message in channel.history(limit=None):
        for attachment in message.attachments:
            attachment_links.append(attachment.url)

    with open('attachments.txt', 'w') as f:
        for link in attachment_links:
            f.write(f"{link}\n")

    await ctx.send(f"Saved {len(attachment_links)} attachment links to attachments.txt.")

bot.run(os.environ['Token'],bot=False)

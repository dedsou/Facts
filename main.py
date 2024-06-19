import discord
from discord.ext import commands
import asyncio
import os
#intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', self_bot=True)



# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to fetch attachment links and send as file
@bot.command()
async def fa(ctx, channel_name: str):
    # Find channel by name (replace 'Your Server Name' and 'your-channel' with actual server and channel names)
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    
    if not channel:
        await ctx.send(f"Channel '{channel_name}' not found.")
        return
    
    # Fetch attachment links
    attachment_links = []
    async for message in channel.history(limit=None):
        for attachment in message.attachments:
            attachment_links.append(attachment.url)
    
    # Save links to a text file
    filename = f'{channel_name}_attachments.txt'
    with open(filename, 'w') as f:
        for link in attachment_links:
            f.write(link + '\n')
    
    # Send the file to the user who requested it
    with open(filename, 'rb') as f:
        file = discord.File(f, filename=filename)
        await ctx.author.send(f"Here are the attachment links from #{channel_name}:", file=file)
    
    # Delete the file after sending
    import os
    os.remove(filename)

bot.run(os.environ['Token'],bot=False)

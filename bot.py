#region variables
#region imports
import discord
from os import environ, path
if path.exists("./vars.py"):
    from vars import token
else:
    token = environ.get("BOT_TOKEN")
#endregion
#region global variables
intents = discord.Intents()
intents.members = True
client = discord.Client(intents=intents)
#endregion
#endregion

#region client commands

#endregion

#region client events
#region client error
@client.event
async def on_error(eventname: str) -> None:
    """Emitted when the client encounters an error"""
    print(f"An error occured in the {eventname} event")
#endregion
#region client ready
@client.event
async def on_ready() -> None:
    """Emitted when the client is ready"""
    print(f"{client.user.name} is ready")
#endregion
#region client guildJoin
@client.event
async def on_guild_join(guild: discord.Guild) -> None:
    """Emitted when the client creates a guild or has been added to a guild"""
#endregion
#region client guildRemove
@client.event
async def on_guild_remove(guild: discord.Guild) -> None:
    """Emitted when the client is removed from a guild"""
#endregion
#region client memberJoin
@client.event
async def on_member_join(member: discord.Member) -> None:
    """Emitted when a member joins a guild"""
#endregion
#region client memberRemove
@client.event
async def on_member_remove(member: discord.Member) -> None:
    """Emitted when a member leaves a guild"""
#endregion
#region client memberUpdate
@client.event
async def on_member_update(oldMember: discord.Member, newMember: discord.Member) -> None:
    """Emitted when a member updates their profile"""
#endregion
#region client reactionAdd
@client.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.Member) -> None:
    """Emitted when a reaction is added to a message"""
#endregion
#region client reactionRemove
@client.event
async def on_reaction_remove(reaction: discord.Reaction, user: discord.Member) -> None:
    """Emitted when a reaction is removed from a message"""
#endregion
#region client message
@client.event
async def on_message(message: discord.Message) -> None:
    """Emitted when a message is sent"""
#endregion
#endregion

client.run(token)
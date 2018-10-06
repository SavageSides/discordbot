import discord
import datetime
import random
import json
import asyncio
import time
from discord.ext import commands

TOKEN = "NDk3OTAzNTUxNTcwMzc4NzUy.Dpl8pw.tGwO2ifPXb4_s1jCqcgYRrs9qIQ"

client = commands.Bot(command_prefix="-")
client.remove_command('help')

@client.event
async def on_ready():
    print("Still in phase one on the codes!")
    await client.change_presence(game=discord.Game(name=f"{len(set(client.get_all_members()))} members || -help", type=3))
    

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    try:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Help Page <:check:497917407277350912>", value="``Following Commands Below``")
        embed.add_field(name="<:locks:497941110342287370> | Moderation", value="-kick @User <reason> \n -ban @User <reason> \n -unban <uername or id> \n  -warn @User \n -clearwarns @User \n -warnings @User \n -clear <amount> \n -mute @User <reason> \n -unmute @User <reason>", inline=False)
        embed.add_field(name="<:settings:497936701025550345> | Config", value="-setwelcome <message> \n -setgoodbye <message> \n -setchannel <channel_name> \n -configs <shows all of the configs>", inline=True)
        embed.add_field(name="<:money:497965184309002250> | Economy", value="-daily \n -work \n -bal \n -gamble <amount> \n -pay @User <amount>", inline=False)
        embed.add_field(name="Producers:", value="Rev#5076 - One of my friends who made the pictures for this bot!", inline=True)
        embed.add_field(name="Links Etc.", value="[Click here for the Bot Invite:](https://discordapp.com/api/oauth2/authorize?client_id=497903551570378752&permissions=2146958839&scope=bot) \n [Server Invite Link for help:](https://discord.gg/S9PY2x)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/496858852117970957/497951527114244096/PokeParkBanne2r.png")
        await client.send_message(author, embed=embed)
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:questions:497935217743364116> | Message Recieved?", value="You should have gotten a help message!", inline=False)
        await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:ex:497918019536683018> | Error:", value="We can't send you a help message because you need to do this: \n 1.) Enable for everyone can talk to you", inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="Invite Link!", value="[Click here for the Bot Invite:](https://discordapp.com/api/oauth2/authorize?client_id=497903551570378752&permissions=2146958839&scope=bot)")
    await client.say(embed=embed)



@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason = None):
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(color=0x1434a3)
                embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -kick @Desired User**", inline=False)
                await client.say(embed=embed)
                return
            await client.kick(user)
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Kick was scucessful! <:check:497917407277350912>", value="``Following Data Below:``", inline=False)
            embed.add_field(name="Author:", value=f"{author.mention}")
            embed.add_field(name="User:", value=f"{user.mention}")
            embed.add_field(name="Channel:", value=f"{channel.mention}")
            embed.add_field(name="User ID:", value=f"``{user.id}``")
            embed.add_field(name="Author ID:", value=f"``{author.id}``")
            embed.add_field(name="Date:", value=f"``{timestamp}``")
            embed.add_field(name="Reason:", value=f"**{reason}**")
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
            embed.add_field(name="Missing Permissions:", value="**Kick Members**")
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value="**I can't kick this user because I have a lower role or lower permission**")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, reason = None):
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(color=0x1434a3)
                embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -ban @Desired User**", inline=False)
                await client.say(embed=embed)
                return
            await client.ban(user)
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Ban was scucessful! <:check:497917407277350912>", value="``Following Data Below:``", inline=False)
            embed.add_field(name="Author:", value=f"{author.mention}")
            embed.add_field(name="User:", value=f"{user.mention}")
            embed.add_field(name="Channel:", value=f"{channel.mention}")
            embed.add_field(name="User ID:", value=f"``{user.id}``")
            embed.add_field(name="Author ID:", value=f"``{author.id}``")
            embed.add_field(name="Date:", value=f"``{timestamp}``")
            embed.add_field(name="Reason:", value=f"**{reason}**")
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
            embed.add_field(name="Missing Permissions:", value="**Ban Members**")
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value="**I can't ban this user because I have a lower role or lower permission**")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, *, reason = None):
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    bot = ctx.message.author.bot
    try:
        if ctx.message.author.server_permissions.mute_members:
            if user is None:
                embed = discord.Embed(color=0x1434a3)
                embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -mute @Desired User**", inline=False)
                await client.say(embed=embed)
                return
            if bot == user:
                embed = discord.Embed(color=0x1434a3)
                embed.add_field(name="Wrong UUsage <:ex:497918019536683018>", value="You need to define a user \n **Example: -mute @Desired User**", inline=False)
                await client.say(embed=embed)
                return
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await client.add_roles(user, MutedRole)
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Mute was scucessful! <:check:497917407277350912>", value="``Following Data Below:``", inline=False)
            embed.add_field(name="Author:", value=f"{author.mention}")
            embed.add_field(name="User:", value=f"{user.mention}")
            embed.add_field(name="Channel:", value=f"{channel.mention}")
            embed.add_field(name="User ID:", value=f"``{user.id}``")
            embed.add_field(name="Author ID:", value=f"``{author.id}``")
            embed.add_field(name="Date:", value=f"``{timestamp}``")
            embed.add_field(name="Reason:", value=f"**{reason}**")
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
            embed.add_field(name="Missing Permissions:", value="**Mute Members**")
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value="**I can't mute this user because I have a lower role or lower permission**")
        await client.say(embed=embed)
        return

@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None, *, reason = None):
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    try:
        if ctx.message.author.server_permissions.mute_members:
            if user is None:
                embed = discord.Embed(color=0x1434a3)
                embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -unmute @Desired User**", inline=False)
                await client.say(embed=embed)
                return
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await client.remove_roles(user, MutedRole)
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Unmute was scucessful! <:check:497917407277350912>", value="``Following Data Below:``", inline=False)
            embed.add_field(name="Author:", value=f"{author.mention}")
            embed.add_field(name="User:", value=f"{user.mention}")
            embed.add_field(name="Channel:", value=f"{channel.mention}")
            embed.add_field(name="User ID:", value=f"``{user.id}``")
            embed.add_field(name="Author ID:", value=f"``{author.id}``")
            embed.add_field(name="Date:", value=f"``{timestamp}``")
            embed.add_field(name="Reason:", value=f"**{reason}**")
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
            embed.add_field(name="Missing Permissions:", value="**Mute Members**")
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value="**I can't unmute this user because I have a lower role or lower permission**")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unban(ctx):
    ban_list = await client.get_bans(ctx.message.server)
    # Show banned users
    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Ban List: <:ex:497918019536683018>", value="ATM the ban list is empty.", inline=False)
        await client.say(embed=embed)
        return
    try:
        await client.unban(ctx.message.server, ban_list[-1])
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Unbanned <:check:497917407277350912>", value="Unbanned user: `{}`".format(ban_list[-1].name), inline=False)
        await client.say(embed=embed)
    except discord.Forbidden:
        embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value="**I don't have the permissions to unban this user.**")
        return
    except discord.HTTPException:
        await client.say("Unban failed.")
        return

@client.command(pass_context=True)
async def warn(ctx, user: discord.Member = None, *, reason = None):
    with open("warnings.json", "r") as f:
        warnings = json.load(f)
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    if ctx.message.author.server_permissions.mute_members:
        if user is None:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -warn @Desired User**", inline=False)
            await client.say(embed=embed)
            return
        if author == user:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong Usage: <:ex:497918019536683018>", value="Wrong usage. You can't warn your self. Agianst my policys.", inline=False)
            await client.say(embed=embed)
            return
        if not ctx.message.server.id in warnings:
            warnings[ctx.message.server.id] = {}
        if not user.id in warnings[ctx.message.server.id]:
            warnings[ctx.message.server.id][user.id] = 0
        warnings[ctx.message.server.id][user.id] += 1
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Warn was scucessful! <:check:497917407277350912> :warning:", value="``Following Data Below:``", inline=False)
        embed.add_field(name="Author:", value=f"{author.mention}")
        embed.add_field(name="User:", value=f"{user.mention}")
        embed.add_field(name="Channel:", value=f"{channel.mention}")
        embed.add_field(name="Author ID:", value=f"``{author.id}``")
        embed.add_field(name="Date:", value=f"``{timestamp}``")
        embed.add_field(name="Reason:", value=f"**{reason}**")
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Mute Members**")
        await client.say(embed=embed)
    with open("warnings.json", "w") as f:
        json.dump(warnings, f, indent=4)

@client.command(pass_context=True)
async def clearwarns(ctx, user: discord.Member = None, *, reason = None):
    with open("warnings.json", "r") as f:
        warnings = json.load(f)
    author = ctx.message.author
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    warns = warnings[ctx.message.server.id][user.id]
    if ctx.message.author.server_permissions.mute_members:
        if author == user:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong Usage: <:ex:497918019536683018>", value="Wrong usage. You can't warn your self. Agianst my policys.", inline=False)
            await client.say(embed=embed)
            return
        if user is None:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -warn @Desired User**", inline=False)
            await client.say(embed=embed)
            return
        if warnings[ctx.message.server.id][user.id] == 0:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Uncaught Error: <:ex:497918019536683018>", value=f"**{user.mention} Has 0 warns.**")
            await client.say(embed=embed)
            return
        if not ctx.message.server.id in warnings:
            warnings[ctx.message.server.id] = {}
        if not user.id in warnings[ctx.message.server.id]:
            warnings[ctx.message.server.id][user.id] = 0
        warnings[ctx.message.server.id][user.id] -= warns
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Removed Warnings was scucessful! <:check:497917407277350912> :warning:", value="``Following Data Below:``", inline=False)
        embed.add_field(name="Author:", value=f"{author.mention}")
        embed.add_field(name="User:", value=f"{user.mention}")
        embed.add_field(name="Channel:", value=f"{channel.mention}")
        embed.add_field(name="Author ID:", value=f"``{author.id}``")
        embed.add_field(name="Date:", value=f"``{timestamp}``")
        embed.add_field(name="Reason:", value=f"**{reason}**")
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Mute Members**")
        await client.say(embed=embed)
    with open("warnings.json", "w") as f:
        json.dump(warnings, f, indent=4)

@client.command(pass_context=True)
async def warnings(ctx, member: discord.Member):
    with open("warnings.json", "r") as f:
        warnings = json.load(f)
    if member is None:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong Usage <:ex:497918019536683018>", value="You need to define a user \n **Example: -warn @Desired User**", inline=False)
        await client.say(embed=embed)
        return
    if not member.id in warnings[ctx.message.server.id]:
        warnings[ctx.message.server.id][member.id] = 0
    warns = warnings[ctx.message.server.id][member.id]
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="Shown Warnings Scucess <:check:497917407277350912>", value=f"``Following Data Below``", inline=False)
    embed.add_field(name="Warns:", value=f"**{warns}**", inline=False)
    await client.say(embed=embed)
    with open("warnings.json", "w") as f:
        json.dump(warnings, f, indent=4)

@client.command(pass_context=True)
async def purge(ctx, amount=None):
    author = ctx.message.author
    channel = ctx.message.channel
    timestamp = datetime.datetime.utcnow()
    if ctx.message.author.server_permissions.manage_messages:
        if amount is None:
            embed = discord.Embed(color=0x1434a3)
            embed.add_field(name="Wrong Usage: <:ex:497918019536683018>", value="Please specify a amount \n **Example: -purge 5**", inline=False)
            await client.say(embed=embed)
            return
        channel = ctx.message.channel
        author = ctx.message.author
        messages = []
        async for message in client.logs_from(channel, limit=int(amount)):
            messages.append(message)
        await client.delete_messages(messages)
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Purge was scucessful! <:check:497917407277350912>", value="``Following Data Below:``", inline=False)
        embed.add_field(name="Author:", value=f"{author.mention}")
        embed.add_field(name="Channel:", value=f"{channel.mention}")
        embed.add_field(name="Author ID:", value=f"``{author.id}``")
        embed.add_field(name="Date:", value=f"``{timestamp}``")
        embed.add_field(name="Amount:", value=f"**{amount}**")
        msg = await client.say(embed=embed)
        await asyncio.sleep(3)
        await client.delete_message(msg)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Manage Messages**")
        await client.say(embed=embed)



@client.command(pass_context=True)
async def setwelcome(ctx, *, text = None):
    with open("serverconfig.json", "r") as f:
        welcome = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if not ctx.message.server.id in welcome :
            welcome[ctx.message.server.id] = {}
            welcome[ctx.message.server.id]["welcome"] = "default"
        welcome[ctx.message.server.id]["welcome"] = text
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:settings:497936701025550345> | Set Welcome Message:", value=f"*{text}*", inline=True)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Manage Server**")
        await client.say(embed=embed)
    with open("serverconfig.json", "w") as f:
        json.dump(welcome,f)

@client.command(pass_context=True)
async def setgoodbye(ctx, *, text = None):
    with open("serverconfig.json", "r") as f:
        goodbye = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if not ctx.message.server.id in goodbye:
            goodbye[ctx.message.server.id] = {}
            goodbye[ctx.message.server.id]["goodbye"] = "Set a message quickly"
        goodbye[ctx.message.server.id]["goodbye"] = text
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:settings:497936701025550345> | Set Goodbye Message:", value=f"*{text}*", inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Manage Server**")
        await client.say(embed=embed)
    with open("serverconfig.json", "w") as f:
        json.dump(goodbye, f, indent = 4)

@client.command(pass_context=True)
async def setchannel(ctx, channel_name = None):
    with open("serverconfig.json", "r") as f:
        channel = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if not ctx.message.server.id in channel:
            channel[ctx.message.server.id] = {}
            channel[ctx.message.server.id]["channel"] = "Dafult"
        channel[ctx.message.server.id]["channel"] = channel_name
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:house1:497950213101584394> | Set Welcome-Goodbye Channel", value=f"*{channel_name}*", inline=False)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong permissions <:ex:497918019536683018>", value="``Following Description Below:``", inline=False)
        embed.add_field(name="Missing Permissions:", value="**Manage Server**")
        await client.say(embed=embed)
    with open("serverconfig.json", "w") as f:
        json.dump(channel, f, indent = 4)

    
@client.command(pass_context=True)
async def configs(ctx):
    with open("serverconfig.json", "r") as f:
        config = json.load(f)
    channels = config[ctx.message.server.id]["channel"]
    goodbyes = config[ctx.message.server.id]["goodbye"]
    welcomes = config[ctx.message.server.id]["welcome"]
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="Welcome Message:", value=f">  *{welcomes}*", inline=False)
    embed.add_field(name="Goodbye Message:", value=f">  *{goodbyes}*", inline=True)
    embed.add_field(name="Channel:", value=f">  *{channels}*", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/496858852117970957/497935804484812821/d2afa50822966fe0.png")
    await client.say(embed=embed)
    with open("serverconfig.json", "w") as f:
        json.dump(config,f)

@client.event
async def on_member_join(member):
    with open("serverconfig.json", "r") as f:
        welcome = json.load(f)
    server = member.server
    channel = welcome[member.server.id]["channel"]
    welcomes = welcome[member.server.id]["welcome"]
    channels = discord.utils.get(server.channels, name=channel)
    await client.send_message(channels, f"{member.mention} {welcomes}")
    await client.change_presence(game=discord.Game(name=f"{len(set(client.get_all_members()))} members || -help", type=3))
    with open("serverconfig.json", "w") as f:
        json.dump(welcome,f)

@client.event
async def on_member_remove(member):
    with open("serverconfig.json", "r") as f:
        welcome = json.load(f)
    server = member.server
    channel = welcome[member.server.id]["channel"]
    welcomes = welcome[member.server.id]["goodbye"]
    channels = discord.utils.get(server.channels, name=channel)
    await client.send_message(channels, f"{member.mention} {welcomes}")
    await client.change_presence(game=discord.Game(name=f"{len(set(client.get_all_members()))} members || -help", type=3))
    with open("serverconfig.json", "w") as f:
        json.dump(welcome,f)

    
        
    
#Economy


@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
async def work(ctx):
    with open("coins.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    coinsc = random.randint(100, 700)
    if not ctx.message.server.id in coins:
       	coins[ctx.message.server.id] = {}
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coins[ctx.message.server.id][author.id] += coinsc
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="<:money:497965184309002250> | Work Pay Amount", value=f"${coinsc}", inline=False)
    embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
    await client.say(embed=embed)
    with open("coins.json", "w") as f:
        json.dump(coins, f, indent=4)
@work.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        author = ctx.message.author
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Cool Down:", value="I use this so we don't have a spam raid or slow me down. Use this in 2 Minutes!")
        embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def bal(ctx):
    with open("coins.json", "r") as f:
        coins = json.load(f)
    author = ctx.message.author
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coinss = coins[ctx.message.server.id][author.id]
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="<:money:497965184309002250> | Your Coin Balance:", value=f"${coinss}", inline=False)
    embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
    await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(5, 10, commands.BucketType.user)
async def gamble(ctx, amount: int):
    with open("coins.json", "r") as f:
        coins = json.load(f)
    choices = random.randint(0, 1)
    amountt = coins[ctx.message.server.id][ctx.message.author.id]
    if coins[ctx.message.server.id][ctx.message.author.id] <= 1:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Wrong!", value=f"You dont have enough! Required: ``2``. Your balance: ``{amountt}``.", inline=False)
        await client.say(embed=embed)
        return
    if amount > coins[ctx.message.server.id][ctx.message.author.id]:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Not Enough!", value="You don't have sufficiant coins.", inline=False)
        await client.say(embed=embed)
        return
    if amount <= 0:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Not Enough", value="You cannot gamble anything less then ``0``!", inline=False)
        await client.say(embed=embed)
        return
    if choices == 0:
        coins[ctx.message.server.id][ctx.message.author.id] += amount * 2
        won = amount * 2
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:money:497965184309002250> | You won!", value=f"${won}", inline=False)
        await client.say(embed=embed)
    else:
        coins[ctx.message.server.id][ctx.message.author.id] -= amount
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="<:money:497965184309002250> | You lost", value=f"${amount}", inline=False)
        await client.say(embed=embed)
    with open("coins.json", "w") as f:
        json.dump(coins, f, indent=4)
@gamble.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        author = ctx.message.author
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Cool Down:", value="I use this so we don't have a spam raid or slow me down. Use this in 10 Seconds!")
        embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 864000, commands.BucketType.user)
async def daily(ctx):
    with open("coins.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    coinsc = random.randint(100, 700)
    if not ctx.message.server.id in coins:
       	coins[ctx.message.server.id] = {}
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coins[ctx.message.server.id][author.id] += coinsc
    embed = discord.Embed(color=0x1434a3)
    embed.add_field(name="<:money:497965184309002250> | Daily Pay Amount", value=f"${coinsc}", inline=False)
    embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
    await client.say(embed=embed)
    with open("coins.json", "w") as f:
        json.dump(coins, f, indent=4)
@daily.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        author = ctx.message.author
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Cool Down:", value="I use this so we don't have a spam raid or slow me down. Use this in 24 Hours!")
        embed.set_footer(icon_url=author.avatar_url, text="Economy Commands!")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def pay(ctx, member:discord.Member=None, *, amount: int):
    with open("coins.json", "r") as f:
        coins = json.load(f)
        author = ctx.message.author
    if amount > coins[ctx.message.server.id][ctx.message.author.id]:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Error:", value="**You don't have enough coins!**", inline=False)
        await client.say(embed=embed)
        return
    if author == member:
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Error:", value="**Don't add money to your self**", inline=False)
        await client.say(embed=embed)
        return
    if not ctx.message.server.id in coins:
        coins[ctx.message.server.id] = {}
    if not member.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][member.id] = 0
        coins[ctx.message.server.id][member.id] += amount
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Paying Command", value=f"Added **{amount} to **{member.name}** ", inline=False)
        await client.say(embed=embed)
    else:
        coins[ctx.message.server.id][member.id] += amount
        coins[ctx.message.server.id][ctx.message.author.id] -= amount
        embed = discord.Embed(color=0x1434a3)
        embed.add_field(name="Paying Command", value=f"Added **{amount}** to **{member.name}** ", inline=False)
        await client.say(embed=embed)
    with open("coins.json", "w") as f:
        json.dump(coins, f, indent=4)


    
    

    

            
client.run(TOKEN)

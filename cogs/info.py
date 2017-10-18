import discord
from discord.ext import commands

class Info:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['info'])
	async def whois(self, ctx, member: discord.Member = None):
		if member == None:
			memberholder = ctx.message.author.id
			member = ctx.guild.get_member(memberholder)
			emb = discord.Embed(colour=self.bot.embed_colour)
			emb.set_author(name="Whois for {***REMOVED***".format(member.display_name),
							icon_url=member.avatar_url)
			emb.set_thumbnail(url=member.avatar_url)
			emb.add_field(name="**ID**", value=member.id)
			emb.add_field(name="**Roles**", value=", ".join([r.name for r in member.roles]))
			emb.add_field(name="**Status**", value="**Playing** {***REMOVED***".format(member.game.name if member.game else ""))
			emb.add_field(name="**Color**", value=str(member.color))
			emb.add_field(name="**Joined on**", value=member.joined_at.date())
			emb.add_field(name="**Avatar url**", value="[Here]({***REMOVED***)".format(member.avatar_url))
			try:
				await ctx.send(embed=emb)
			except:
				await ctx.send("Too much info...")
		else:S
			emb = discord.Embed(colour=self.bot.embed_colour)
			emb.set_author(name="Whois for {***REMOVED***".format(member.display_name),
							icon_url=member.avatar_url)
			emb.set_thumbnail(url=member.avatar_url)
			emb.add_field(name="**ID**", value=member.id)
			emb.add_field(name="**Roles**", value=", ".join([r.name for r in member.roles]))
			emb.add_field(name="**Status**", value="**Playing** {***REMOVED***".format(member.game.name if member.game else ""))
			emb.add_field(name="**Color**", value=str(member.color))
			emb.add_field(name="**Joined on**", value=member.joined_at.date())
			emb.add_field(name="**Avatar url**", value="[Here]({***REMOVED***)".format(member.avatar_url))
			try:
				await ctx.send(embed=emb)
			except:
				await ctx.send("Too much info...")

def setup(bot):
	bot.add_cog(Info(bot))
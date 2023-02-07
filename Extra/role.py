import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from colorama import Fore

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Add eine Rolle zu einem User")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, target: Option(discord.Member, "Who should i add a Role?", required=True), role: Option(discord.Role, "Which Role should i add?", required=True)):
        if role in target.roles:
            await ctx.respond(f"{target.mention} already has the {role.mention} Role.", ephemeral=True)
        else:
            await ctx.respond(f"The Role {role.mention} was added to {target.mention}.", ephemeral=True)
            await target.add_roles(role)

    @slash_command(description="Remove eine Rolle von einem User")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, target: Option(discord.Member, "Who should i remove a Role?", required=True), role: Option(discord.Role, "Which Role should i remove?", required=True)):
        if role in target.roles:
            await target.remove_roles(role)
            await ctx.respond(f"The Role {role.mention} got Remove from {target.mention}.", ephemeral=True)
        else:
            await ctx.respond(f"{target.mention} already has the {role.mention} Role.", ephemeral=True)

    @slash_command(description="Create a Role")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, name: Option(str, "Whats the name of the Role?", required=True), color: Option(str, "What Color should the Role have?", required=False)):

        colorlol = int(f"0x{color}", 16)

        if color == None:
            await ctx.guild.create_role(name=name, color=colorlol)
            await ctx.respond(f"Your Role with the Name {name} got created.")
        else:
            await ctx.guild.create_role(name=name, color=colorlol)
            await ctx.respond(f"Your Role {name} got Succefully Created with the Color ({color})!")

    
def setup(bot):
    bot.add_cog(Role(bot))

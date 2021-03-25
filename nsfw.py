    @commands.command(no_pm=True)
    @commands.guild_only()
    async def boobs(self, ctx):
        """Shows some boobs."""
        try:
            rdm = random.randint(0, await self.settings.ama_boobs())
            search = ("http://api.oboobs.ru/boobs/{}".format(rdm))
            result = await self.get(search)
            tmp = random.choice(result)
            boob = "http://media.oboobs.ru/{}".format(tmp["preview"])
        except Exception as e:
             await ctx.send("Error getting results.\n{}".format(e))
             return
        if ctx.channel.is_nsfw():
            emb = discord.Embed(title="Boobs")
            emb.set_image(url=boob)
            await ctx.send(embed=emb)

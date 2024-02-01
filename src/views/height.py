from asyncio import TimeoutError


class HeightInput:
    def __init__(self, interaction, bot, type):
        self.interaction = interaction
        self.user = interaction.user
        self.channel = interaction.channel
        self.bot = bot
        self.selected_values = None
        self.type = type
        self.msg = None

    async def send(self):
        self.msg = await self.interaction.followup.send(
            f"Dale capo, decime la altura {self.type}", ephemeral=False
        )

        def check(msg):
            return (
                msg.author == self.user
                and msg.channel == self.channel
                and msg.content.isdigit()
            )

        try:
            msg = await self.bot.wait_for("message", timeout=30.0, check=check)
        except TimeoutError:
            await self.interaction.followup.send(
                "Mirá capo, tardaste mucho en responder", ephemeral=True
            )
            return
        else:
            height = int(msg.content)
            self.selected_values = height
            await self.msg.delete()
            await msg.delete()

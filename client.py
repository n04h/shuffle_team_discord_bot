import discord
import environ

class MyClient(discord.Client):
    async def on_message(self, message):
        # 自分のメッセージは無視
        if message.author == self.user:
            return

        # 自分へメンションの場合
        if self.user in message.mentions:
            await self.shuffle(message)

    async def shuffle(self, message):
      msg = message.content.split()
      await message.channel.send(msg[1])

client = MyClient()
client.run(environ.TOKEN)

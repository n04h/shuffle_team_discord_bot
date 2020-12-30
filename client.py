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
      vc = self.get_join_voice_channel(message)

      if vc is None:
        await message.channel.send('ボイスチャンネルを特定できませんでした。')
      else:
        await message.channel.send(vc.name)

    def get_join_voice_channel(self, message):
      # VCを全取得してジョインしてるチャンネルを探す
      vcs = message.guild.voice_channels
      for vc in vcs:
        members = vc.members
        for member in members:
          if member.id == message.author.id:
            return vc
      return None

    def get_channel_users(self, channel):
      # チャンネルのユーザー一覧を返す
      aa = 1

client = MyClient()
client.run(environ.TOKEN)

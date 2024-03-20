import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def teamrandom(ctx, *players: str):
    # Chuyển đổi tuple thành danh sách
    players_list = list(players)

    # Kiểm tra xem có ít nhất 4 người chơi không
    if len(players_list) < 4:
        await ctx.send("Phải có ít nhất 4 người chơi để tạo đội.")
        return

    # Xáo trộn thứ tự người chơi
    random.shuffle(players_list)

    # Chia thành các đội
    teams = [players_list[i:i+2] for i in range(0, len(players_list), 2)]

    # Gửi thông điệp về việc sắp xếp đội
    response = "Các đội được tạo:\n"
    for i, team in enumerate(teams, start=1):
        response += f"Team {i}: {' và '.join(team)}\n"

    await ctx.send(response)

# Khởi động bot với token của bạn
bot.run('MTIxMzc4MjUzNzAzODQ2Mjk5Ng.GbtFNf.E_Ve5T3WGq8Mm29_YL4BuzvEmEfNZSPtb3kkbU')

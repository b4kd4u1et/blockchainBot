import asyncio
import sys
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from bitcoinrpc import BitcoinRPC

rpc_user = os.getenv("rpc_user")
rpc_url = os.getenv("rpc_url")
rpc_password = os.getenv("rpc_password")
#rpc = BitcoinRPC.from_config(os.getenv("rpc_url"), (os.getenv("rpc_user"), os.getenv("rpc_password")))


token = os.getenv("BITCOIN_BOT_TOKEN")
dp = Dispatcher()
bot = Bot(token)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("/getnewaddress - for new address\n/getbalance - for balance info")

@dp.message(Command("getnewaddress"))
async def getNewAddress(message: Message):
    res = os.system(f"curl --user {rpc_user}:{rpc_password} --data-binary '{{\"jsonrpc\": \"1.0\", \"id\": \"curltest\", \"method\": \"getnewaddress\", \"params\":[]}}' -H 'content-type: text/plain;' {rpc_url}")
    await message.answer(str(res))

@dp.message(Command("getbalance"))
async def getBalance(message: Message):
    res = os.system(f"curl --user {rpc_user}:{rpc_password} --data-binary '{{\"jsonrpc\": \"1.0\", \"id\": \"curltest\", \"method\": \"getbalance\", \"params\":[]}}' -H 'content-type: text/plain;' {rpc_url}")
    await message.answer(str(res))

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())

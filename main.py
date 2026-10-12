import asyncio
from aiobale import Client, Dispatcher, F
from aiobale.types import Message
from aiobale.filters import IsGift

dp = Dispatcher()

client = Client(dp, session_file="my_bot")

@dp.message(IsGift())
async def gift_handler(msg: Message):
    try:
        wallet = await client.get_wallet()
        result = await client.open_gift(msg, wallet.wallet.token)
        print(f"[+] Gift successfully opened: {result}")
    except Exception as e:
        print(f"[-] Error opening gift: {e}")

async def main():
    print("[*] Bot activated and scanning messages...")
    await client.start()

if __name__ == "__main__":
    asyncio.run(main())

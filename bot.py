import asyncio


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    from loader import bot, db
    from handlers import dp
    db.create_db()
    asyncio.run(main())

import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("Users table creating...")
    await db.create_table_users()
    print("Created!")

    print("Adding users...")

    await db.add_user("Jill", "jilldev", 789456123)
    await db.add_user("John", "johndev", 122345678)
    await db.add_user("Tom", "tomdev", 789489156)
    await db.add_user("jerry", "jerrydev", 123156489)
    await db.add_user("Bek", "bekdev", 786425689)
    print("Added!")

    users = await db.select_all_users()
    print(f"All users: {users}")

    user = await db.select_user(id=5)
    print(f"User: {user}")

asyncio.run(test())

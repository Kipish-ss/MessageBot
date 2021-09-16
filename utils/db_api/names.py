import aiosqlite
from data.config import PATH


async def update_user_name(new_name: str, user_id: int) -> str:
    async with aiosqlite.connect(PATH) as conn:
        query = "UPDATE user_list SET name = ? WHERE id = ?"
        await conn.execute(query, (new_name, user_id))
        await conn.commit()
    text = f"Your name was successfully updated to {new_name}."
    return text


async def get_user_name(user_id: int) -> str:
    try:
        async with aiosqlite.connect(PATH) as conn:
            query = "SELECT name FROM user_list WHERE id = ?"
            async with conn.execute(query, (user_id,)) as cursor:
                name_tuple = await cursor.fetchone()
        name = name_tuple[0]
    except Exception as err:
        print(err)

    return name


async def get_other_names() -> list:
    async with aiosqlite.connect(PATH) as conn:
        query = "SELECT name FROM user_list"
        cursor: aiosqlite.Cursor
        async with conn.execute(query) as cursor:
            names: list = await cursor.fetchall()
    name_list = []
    for name in names:
        name_list.append(name[0])
    return name_list

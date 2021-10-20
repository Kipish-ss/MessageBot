import aiosqlite
from data.config import DB


async def update_count(user_id: int) -> None:
    async with aiosqlite.connect(DB) as conn:
        query = "UPDATE user_list SET msg_count = msg_count + 1 WHERE id = ?"
        await conn.execute(query, (user_id,))
        await conn.commit()


async def get_msg_count(user_id: int = None, user_name: str = None) -> int:
    async with aiosqlite.connect(DB) as conn:
        if user_id is not None:
            param = user_id
            query = "SELECT msg_count FROM user_list WHERE id = ?"
        else:
            param = user_name
            query = "SELECT msg_count FROM user_list WHERE name = ?"
        cursor: aiosqlite.Cursor
        async with conn.execute(query, (param,)) as cursor:
            msg_count_tpl = await cursor.fetchone()
            if msg_count_tpl is not None:
                msg_count = msg_count_tpl[0]
            else:
                msg_count = None
        return msg_count


async def reset_count(user_id: int) -> None:
    async with aiosqlite.connect(DB) as conn:
        query = "UPDATE user_list SET msg_count = 0 WHERE id = ?"
        await conn.execute(query, (user_id,))
        await conn.commit()


async def reset_for_all():
    async with aiosqlite.connect(DB) as conn:
        query = "UPDATE user_list SET msg_count  = 0"
        await conn.execute(query)
        await conn.commit()


async def get_top(length) -> list:
    async with aiosqlite.connect(DB) as conn:
        query = "SELECT msg_count FROM user_list"
        cursor: aiosqlite.Cursor
        async with conn.execute(query) as cursor:
            counts = await cursor.fetchall()
    count_list: list[int] = []
    top_list = []
    for tup in counts:
        count_list.append(tup[0])
    count_list = sorted(count_list, reverse=True)
    for i in range(length):
        top_list.append(count_list[i])
    return top_list

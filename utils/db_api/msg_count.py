import aiosqlite
from data.config import PATH


async def update_count(user_id: int) -> None:
    async with aiosqlite.connect(PATH) as conn:
        query = "UPDATE user_list SET msg_count = msg_count + 1 WHERE id = ?"
        await conn.execute(query, (user_id,))
        await conn.commit()


async def get_msg_count(user_id: int = None, user_name: str = None) -> int:
    async with aiosqlite.connect(PATH) as conn:
        if user_id is not None:
            param = user_id
            query = "SELECT msg_count FROM user_list WHERE id = ?"
        else:
            param = user_name
            query = "SELECT msg_count FROM user_list WHERE name = ?"
        cursor: aiosqlite.Cursor
        async with conn.execute(query, (param,)) as cursor:
            msg_count_tpl = await cursor.fetchone()
            msg_count = msg_count_tpl[0]
    return msg_count


async def reset_count(user_id: int) -> str:
    async with aiosqlite.connect(PATH) as conn:
        query = "UPDATE user_list SET msg_count = 0 WHERE id = ?"
        await conn.execute(query, (user_id,))
        await conn.commit()
    text = "Your message count is now 0. Type messages to increase it."
    return text

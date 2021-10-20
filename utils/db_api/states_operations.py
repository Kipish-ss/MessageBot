import sqlite3
import aiosqlite
from data.config import DB
from states import States


def get_state(user_id: int) -> int:
    with sqlite3.connect(DB) as conn:
        query = "SELECT state FROM user_list WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(query, (user_id,))
        state_tuple = cursor.fetchone()
        if state_tuple is not None:
            state = state_tuple[0]
        else:
            state = States.start.value
    return state


async def set_state(user_id: int, state: int) -> None:
    async with aiosqlite.connect(DB) as conn:
        query = "UPDATE user_list SET state = ? WHERE id = ?"
        await conn.execute(query, (state, user_id))
        await conn.commit()

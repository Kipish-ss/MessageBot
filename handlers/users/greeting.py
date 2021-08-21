from utils.db_api.names import get_user_name


async def greet_user(user_name: str = '', user_id: int = None, is_present=False) -> str:
    if is_present:
        user_name = await get_user_name(user_id)
        response = f"Welcome back, {user_name}!\nIf you'd like to change your name, " \
                   f"use /update_name command.\n" \
                   f"Use /message_count command to get your message count " \
                   f"or type a message to increase your count."
    else:
        response = f'Nice to meet you, {user_name}! Type a message to increase your message count ' \
                    f'or use /message_count command to get your current count. Use /update_name' \
                   f' command to change your name.'
    return response

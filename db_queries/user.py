
from psycopg2.extras import DictRow

from core.db_settings import  execute_query
from typing import Optional

def get_user_by_telegram_id(telegram_id) -> Optional[DictRow]:

    query = "SELECT * FROM users WHERE telegram_id=%s"
    user:Optional[DictRow] = execute_query(query =query, params=(telegram_id,), fetch='one')

    if user:
        return user
    return None






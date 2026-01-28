from handlers.registration_handler import regis_handlers
from core.db_settings import execute_query
import logging

logger = logging.getLogger(__name__)

def insert_user():

    user_data = regis_handlers()
    if user_data:
        query = "INSERT INTO users (First_name, Last_name, phone_number) VALUES (%s, %s, %s)"
        try:
            execute_query(query=query,params=user_data)
            print('Foydalanuchi bazaga yozildi')
        except Exception as e:
            print(f"Xato yuz berdi: {e}")
            logger.error(f"INSERT xatosi: {e}")
    else:
        print('Foydalanuvchi bazaga yozilmadi')
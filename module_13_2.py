from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api =''
bot =Bot(token=api)
db =Dispatcher(bot,storage=MemoryStorage())

@db.message_handler(commands='start')
async def all_message(message):
    print ("Привет! Я бот помогающий твоему здоровью.")

@db.message_handler()
async def all_message(message):
    print ("Введите команду '/start', чтобы начать общение.")


if __name__=='__main__':
    executor.start_polling(db,skip_updates=True)
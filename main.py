# 8555467956:AAGHMCC_3vJ8PqdFNn1tadO4YgOc-FO0hRw



from translate import Translator
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F

from aiogram import Router
from aiogram.types import Message, CallbackQuery



from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "8555467956:AAGHMCC_3vJ8PqdFNn1tadO4YgOc-FO0hRw"

# All handlers should be attached to the Rout           er (or Dispatcher)



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(F.text.contains("Salom"))
async def meet(message: Message) -> None:
      await message.answer(f"Salom senga ham, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text.contains( "Yordam" or "Tushunmadim"))
async def help_sos(message: Message) -> None:
    await message.answer(f"Qanday Yordam Kerak?, \n\n Agar siz bu botdan qanday foydalanishni bilmayorgan bo'lsangiz, mana bu bot haqida: \n Bu bot translate bo'lib faqat o'zbek tilidan ingiliz tiliga tarjima qiladi, va yaqin orada bir necha tillar ham qo'shilishi mumkin!")


@dp.message(F.text.contains(not ""))
async def command_start_handler(message: Message) -> None:
      await message.answer(f"Bu translate va faqat so'z tarjima qiladi boshqa narsa emas!")
      
      






@dp.message()
async def echo_handler(message: Message) -> None:
    
    matn = message.text

    from translate import Translator
    
    def translated(translation_language, translated_language, text):
            translator = Translator(to_lang=translation_language, from_lang=translated_language)
            translation = translator.translate(text)
            return translation
        
    result = translated(translated_language=f'uz', translation_language=f'en', text=matn )
    print(result)
    await message.answer(result)




    
    
    
        # Send a copy of the received message
    # await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
        # But not all the types is supported to be copied so need to handle it
    # await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
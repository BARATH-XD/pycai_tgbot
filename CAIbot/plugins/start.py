from CAIbot import bot
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types import CallbackQuery



START_TEXT = """
I Already Awake!  🍌!

• Read the help menu for about my futures /help.
"""

buttons = [
        [
            InlineKeyboardButton(
                "➕ Add Me", url="t.me/tttofubot?startgroup=true"),
            InlineKeyboardButton(
                "🆘 Help", callback_data='help_back'),]]



@bot.on_message(filters.command("start"))
async def start(_, message):
     await message.reply_text(START_TEXT,
     reply_markup=InlineKeyboardMarkup(buttons),)

@bot.on_message(filters.command("help"))
async def help(_, message):
     await message.reply_text(HELP_TEXT,
     reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
     

HELP_TEXT = """
Click the button below to know my commands!
"""

HELP_BUTTON = [[
        InlineKeyboardButton('👮 Admin', callback_data='admin_help'),
        InlineKeyboardButton('👥 UserInfo', callback_data='userinfo_help'),
        ],[
        InlineKeyboardButton('🤗 Fun', callback_data='fun_help'),
        InlineKeyboardButton('👻 Misc', callback_data='misc_help'),
        ],[
        InlineKeyboardButton('🔍 Tagging', callback_data='tagging_help'),
        InlineKeyboardButton('☀ Mornings', callback_data='mornings_help'),
        ],[
        InlineKeyboardButton('🧚 Nekos', callback_data='nekos_help'),
        InlineKeyboardButton('❌ M-Action', callback_data='m-action_help'),
        ],[
        InlineKeyboardButton('🏡 Home', callback_data='home')]]


#defining callback
@bot.on_callback_query(filters.regex("home"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(START_TEXT,
                                    reply_markup=InlineKeyboardMarkup(buttons),)

@bot.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)

@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()

BUTTON = [[InlineKeyboardButton("🔙 Back", callback_data="help_back"),
            InlineKeyboardButton("🗑 Close", callback_data='close'),]]



USERINFO_TEXT = """
User info:
• /id - userid & chatid.
• /info - user information.
"""

@bot.on_callback_query(filters.regex("userinfo_help"))
async def userinfohelp(_, query: CallbackQuery):
     await query.message.edit_caption(USERINFO_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
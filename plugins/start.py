from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕️YouTube Downloader⭕️", url="https://t.me/Musicworldanu/2206")],
        [InlineKeyboardButton("➕ Add me to your Group ➕", url="https://t.me/youtube_Downloder_4k_bot?startgroup=true")],
        
        [
            InlineKeyboardButton("👥 Official Group", url="https://t.me/anujasu"),
            InlineKeyboardButton("📣 Official Channel", url="https://t.me/musicworldanu"),
        
        ],
        [
            InlineKeyboardButton(
            "🎯 Owner", url="https://t.me/Anujasupulsara")]
    ])
    welcomed = f"**✨ Welcome** <b>{message.from_user.first_name}</b>\n\n **💭 ⭕️YouTube Downloader⭕️ allows you to youtube video Download📥**\n **on groups through the new Telegram's Youtube link❕**\n\n **💡 All you have to do is send us the youtube link you want to download📥**\n\n **❔Then select the quality of the Video or Song that you want to get** \n\n\n **🎯. /help 👈 For more information**"
    ytdl_img = "[Youtube-Downloader-4k-Bot](https://telegra.ph/file/617f8b2060de2356722d8.jpg)"
    await message.reply_text(ytdl_img,welcomed, reply_markup=joinButton)
    raise StopPropagation

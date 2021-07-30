from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import num_of_subscribers, percent, ok, cancel
from states import video

from loader import dp, bot, db

num = "0"
per = "0"
id_video = "0"


async def ask_subscribers(user_id):
    text = "📈Пожалуйста, выбери какое у тебя количество подписчиков :\n\n" \
           "Please choose how many subscribers do you have :"
    await bot.send_message(user_id, text, reply_markup=num_of_subscribers.num_of_subs)


@dp.callback_query_handler(text=["< 100", "< 500", "< 1 000", "< 2 500", "< 5 000", "< 10 000", "< 20 000", "20000+"])
async def ask_percent(call: types.CallbackQuery):
    global num
    num = call.data
    await call.message.edit_reply_markup()
    text = "📊Спасибо, теперь, пожалуйста, выбери свой % :\n\n" \
           "Thanks, now please choose your % :"
    await call.message.edit_text(text, reply_markup=percent.percent_btn)


@dp.callback_query_handler(text=["10%+", "< 10%", "< 5%", "< 2,5%", "< 1%", "< 0.5%"])
async def ask_video(call: types.CallbackQuery):
    global per
    per = call.data
    await call.message.edit_reply_markup()
    text = "✔Благодарю, теперь отправь мне, пожалуйста, видеозапись экрана подтверждающую ваши слова ( покажи свою " \
           "страницу с количеством подписчиков и %) \n\n" \
           "Thank you, now please send me a video recording of the your screen for confirming your words (show your " \
           "page with the number of subscribers and %) "
    await call.message.edit_text(text, reply_markup=cancel.cancel_btn)
    await video.Video.video_state.set()


@dp.message_handler(content_types=['video'], state=video.Video.video_state)
async def catch_video(message: types.Message, state: FSMContext):
    global id_video
    await state.finish()
    id_video = message.video.file_id
    if message.chat.username is None:
        await message.answer("❌Что бы я смог отправлять тебе предложения для sfs от меня, тебе необходимо в настройках "
                             "телеграмма указать свой username. Как сделаешь нажми на кнопку 'OK'\n\n"
                             "So that I can send you suggestions for sfs from me, you need in the settings telegram "
                             "specify your username. How do you click on the 'OK' button", reply_markup=ok.ok_btn)
    else:
        if db.check_verification(message.chat.id) == 1:
            await message.answer("✔Ваш аккаунт успешно обновлен!\n\n"
                                 "Your account has been successfully updated!")
            db.update_account(message.chat.id, num, per)
        else:
            await message.answer("🎊Спасибо, теперь каждый день ты будешь получать новые предложения для sfs от меня!\n\n"
                                 "Thank you, now every day you will receive new offers for sfs from me!")
            video_id = message.video.file_id
            db.add_user(message.chat.id, message.chat.username, num, per, video_id)


@dp.message_handler(state=video.Video.video_state)
async def send(message: types.Message):
    await message.answer("❌Мне нужно видео! Иначе ты не сможешь верифицироваться\n\n"
                         "I need a video! Otherwise, you will not be able to verify", reply_markup=cancel.cancel_btn)


@dp.callback_query_handler(text='OK')
async def check_username(call: types.CallbackQuery):
    if call.message.chat.username is None:
        await call.message.edit_reply_markup()
        await call.message.edit_text("❌У вас нет username. Попробуйте еще раз!\n\n"
                                     "You don't have a username. Try again!", reply_markup=ok.ok_btn)
    else:
        await call.message.edit_reply_markup()
        if db.check_verification(call.message.chat.id) == 1:
            await call.message.edit_text("Ваш аккаунт успешно обновлен!\n\n"
                                         "Your account has been successfully updated!")
            db.update_account(call.message.chat.id, num, per)
        else:
            await call.message.edit_text(
                "🎊Спасибо, теперь каждый день ты будешь получать новые предложения для sfs от меня!\n\n"
                "Thank you, now every day you will receive new offers for sfs from me!")
            db.add_user(call.message.chat.id, call.message.chat.username, num, per, id_video)


@dp.callback_query_handler(text='Cancel', state="*")
async def undo_action(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.edit_text("Действие отменено")

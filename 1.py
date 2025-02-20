from Token import my_token
import telebot
import pandas as pd
import os


bot = telebot.TeleBot(my_token)

DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Отправь мне файл Excel.")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        if message.document.mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            file_name = message.document.file_name
            file_path = os.path.join(DOWNLOAD_DIR, file_name)

            with open(file_path, 'wb') as f:
                f.write(downloaded_file)

            bot.reply_to(message, f"Файл '{file_name}' успешно загружен.")

            try:
                df_excel = pd.read_excel(file_path)
                table_string = df_excel.to_string()


                formatted_table = f"```\n{table_string}\n```"

                chunk_size = 4000
                for i in range(0, len(formatted_table), chunk_size):
                    chunk = formatted_table[i:i + chunk_size]
                    bot.send_message(message.chat.id, chunk, parse_mode="Markdown")

            except FileNotFoundError:
                bot.send_message(message.chat.id, f"Ошибка: Файл '{file_path}' не найден.")
            except Exception as e:
                bot.send_message(message.chat.id, f"Ошибка при чтении Excel файла (Pandas): {e}")

        else:
            bot.reply_to(message, "Извини, я принимаю только файлы Excel (.xlsx).")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обработке файла: {e}")

bot.infinity_polling()


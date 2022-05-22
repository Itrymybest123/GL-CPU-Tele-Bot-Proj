from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hi"):
        return "Hello there"

    if user_message in ("what do you do?"):
        return "I test garbage"

    if user_message in ("time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "Huh?"
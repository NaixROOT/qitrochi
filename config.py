import os

def get_config(config_file):
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            lines = f.read().splitlines()
        if len(lines) >= 2:
            return lines[:2]
        else:
            return prompt_config(config_file)
    else:
        return prompt_config(config_file)

def prompt_config(config_file):
    print("Заполните поля ниже.")
    print("🔎 Если вы незнаете где взять данные напишите в лс @ghosvx")
    api_id = input("Введите API ID: ")
    api_hash = input("Введите API Hash: ")
    with open(config_file, 'w') as f:
        f.write(api_id + '\n')
        f.write(api_hash + '\n')
    print("Готово! Эти данные не надо будет вводить в будущем.")
    return api_id, api_hash

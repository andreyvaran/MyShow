from collections import ChainMap

global_settings = {
    'theme': 'светлая',
    'language': 'английский',
    'notifications': True
}

user_settings = {
    'language': 'русский',
    'notifications': False
}

session_settings = {
    'theme': 'темная'
}

# Сначала указываем самые приоритетные настройки
app_settings = ChainMap(session_settings, user_settings, global_settings)

print(app_settings)
print("Итоговая конфигурация:")
for key, value in app_settings.items():
    print(f"{key}: {value}")

print("\nТема:", app_settings['theme'])

session_settings['language'] = 'французский'
print(app_settings)

print("\nОбновленная языковая настройка в сессии:", app_settings['language'])

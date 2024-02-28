import subprocess
import re
import time
import datetime

# Функция для пинга одного адреса
def ping(address):
    # Выполнение команды ping
    response = subprocess.run(['ping', '-n', '1', '-w', '1000', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Проверка на наличие ошибок
    if response.returncode != 0:
        return "Ping request could not find host. Please check the name and try again."

    # Декодирование результата
    output = response.stdout

    # Поиск времени отклика
    match = re.search('Average = (\d+)ms', output)
    if match:
        latency = int(match.group(1))
        if latency > 10:
            return f"High latency: {latency} ms"
        else:
            return f"Latency OK: {latency} ms"
    else:
        return "Packet lost"

# Список IP-адресов для мониторинга
addresses = ['10.61.100.1', '10.61.100.16']

# Цикл мониторинга
while True:
    with open('ping_log.txt', 'a') as log_file:
        for address in addresses:
            result = ping(address)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} - {address} - {result}\n"
            print(log_entry)
            log_file.write(log_entry)
    time.sleep(60)  # Пауза между проверками

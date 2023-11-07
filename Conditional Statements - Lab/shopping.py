# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.

budget = float(input())
num_video = int(input())
num_processor = int(input())
num_ram = int(input())

video_card = 250
processor = (num_video * video_card) * 0.35
ram = (num_video * video_card) * 0.1
total = (num_video * video_card) + (num_ram * ram) + (num_processor * processor)

if num_video > num_processor:
    total = total * 0.85
else:
    total = total
if budget >= total:
    print(F"You have {budget - total:.2F} leva left!")
else:
    print(F"Not enough money! You need {total - budget:.2F} leva more!")




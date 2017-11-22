def get_answer():
	answer = {"Привет": "И тебе привет!", "Как дела": "Лучше всех", "Пока": "Увидимся"}
	question = input()
	print(answer[question].lower())
get_answer()
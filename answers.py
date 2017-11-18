def get_answer():
	answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	question = input()
	print(answer[question].lower())
get_answer()
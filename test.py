from main import Question

questions = 'file/questions.txt'
answers = 'file/nswers.txt'
choices = 'file/choices.txt'
one = Question(questions,answers,choices)
one.get_anything()
one.show_hello()
while one.active:
    try:
        one.pop_up()
        one.show_question()
        one.check_choice()
    except IndexError:
        one.active = False
one.check_print_mistake()
one.show_grade()

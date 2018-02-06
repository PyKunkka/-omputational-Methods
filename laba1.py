import math
from tkinter import *


class MainWindow:
    def __init__(self):

        # for first exercise
        self.label_name_ex_1 = Label(root, text='-' * 40 + 'Задача 1' + '-' * 40).place(x=8, y=10)
        self.label_for_denominator_1 = Label(root, text='Введіть дріб:').place(x=10, y=40)
        self.label_for_enumerator_1 = Label(root, text='Введіть число для кореня:').place(x=10, y=80)
        self.label_equal_l_1 = Label(root, text='=').place(x=240, y=39)
        self.label_equal_2_1 = Label(root, text='=').place(x=240, y=79)

        self.entry_add_denum_1 = Entry(root, width=22)
        self.entry_add_denum_1.place(x=100, y=42)

        self.entry_add_sqrt_1 = Entry(root, width=10)
        self.entry_add_sqrt_1.place(x=170, y=82)

        self.entry_add_answer_for_first_num_1 = Entry(root, width=10)
        self.entry_add_answer_for_first_num_1.place(x=260, y=42)

        self.entry_add_answer_for_second_num_1 = Entry(root, width=10)
        self.entry_add_answer_for_second_num_1.place(x=260, y=82)

        self.btn_show_result_1 = Button(root, text='Вивести результат')
        self.btn_show_result_1.place(x=340, y=58)

        # for second exercise

        self.label_name_ex_2 = Label(root, text='-' * 40 + 'Задача 2' + '-' * 40).place(x=8, y=120)
        self.label_for_number_2 = Label(root, text='Введіть число:').place(x=10, y=150)
        self.label_for_absolute_error_2 = Label(root, text='Введіть абсолютну похибку:').place(x=10, y=190)

        self.entry_add_for_number_2 = Entry(root, width=20)
        self.entry_add_for_number_2.place(x=110, y=151)

        self.entry_add_for_absolute_error_2 = Entry(root, width=8)
        self.entry_add_for_absolute_error_2.place(x=180, y=191)

        self.btn_show_result_2 = Button(root, text='Вивести результат')
        self.btn_show_result_2.place(x=340, y=170)

        # for third exercise

        self.label_name_ex_3 = Label(root, text='-' * 40 + 'Задача 3' + '-' * 40).place(x=8, y=230)
        self.label_for_exact_value_3 = Label(root, text='Введіть число:').place(x=10, y=260)
        self.label_for_absolute_error_3 = Label(root, text='Введіть відносну похибку:').place(x=10, y=300)

        self.entry_add_for_exact_value_3 = Entry(root, width=12)
        self.entry_add_for_exact_value_3.place(x=160, y=261)

        self.entry_add_for_absolute_error_3 = Entry(root, width=9)
        self.entry_add_for_absolute_error_3.place(x=180, y=300)

        self.btn_show_result_3 = Button(root, text='Вивести результат')
        self.btn_show_result_3.place(x=340, y=280)


# Functions for first exercise


def calculate_radical_number(number):  # обрахунок кореня числа, за умови, що число додатнє.
    try:
        if number >= 0:
            return math.sqrt(number)
        else:
            return "Your number is not positive."
    except ValueError:
        return "Format Error"


def calculate_division_number(number):  # ділення числа, при умові, що знаменник не 0, інакше 0
    div_numbers = number.split('/')
    try:
        return float(div_numbers[0]) / float(div_numbers[1])
    except ValueError:
        return "Format error"
    except ZeroDivisionError:
        return "Error, division by 0."


def calculation_abs_num(number, answer_number):  # обчислення абсолютної похибки та округлення
    return abs(number - answer_number)


def calculate_delta_num(number):  # обчислення заокруглених значень з надлишком "на вхід йде str"
    res = 0
    for i in range(2, len(number)):
        if number[i] != '0':
            res = round(float(number), i)
            break
    return res


def calculate_border_relative_oversight(delta_num, answer_number):  # обчислення граничних відносних похибок
    return delta_num / answer_number


def calculation_relative_oversight(absolute_oversight, mod_approximate_number):  # обрахунок відносної похибки
    return absolute_oversight / mod_approximate_number * 100


def out_answer(number, answer_number_1, number2, answer_number_2
               , real_oversight_1, real_oversight_2):                                   # виведення результату
    div_numbers = number.split('/')
    if real_oversight_1 < real_oversight_2:
        return 'Оскільки delta_1 < delta_2, то рівність ' + str(div_numbers[0]) \
                + '/' + str(div_numbers[1]) + '=' + str(answer_number_1) + ' є більш точною.'
    else:
        return 'Оскільки delta_1 > delta_2, то рівність ' + 'sqrt(' + str(number2) + ')'\
                + '=' + str(answer_number_2) + ' є більш точною.'


# Functions for second exercise

def out_abs_oversight(num, delt_num):
    return delt_num/num


# Functions for third exercise

def calculate_delta_as_number(number, delta_as_percent):
    try:
        return number*delta_as_percent / 100
    except ValueError:
        return "Value error."


def calculate_true_numbers(number, approximate_number):
    str_app_num = str(approximate_number)
    res = 0
    for i in range(2, len(str_app_num)):
        if str_app_num[i] != 0:
            res = round(number, i)
            break
    return res


def show_result_for_fisrt_ex(number_1, answer_number1, number_2, answer_number2):
    win = Tk()
    win.title('Відповідь до задачі №1.')
    text = Text(win)
    text.pack()
    text.insert(1.0, 'Введені значення для операції ділення: ' + number_1 + ' = ' + answer_number1 + '\n')
    text.insert(2.0, 'Введені значення для кореня: ' + number_2 + ' = ' + answer_number2 + '\n')

    ans_div = calculate_division_number(number_1)
    ans_sqrt = calculate_radical_number(float(number_2))
    text.insert(3.0, 'В результаті ділення виразу: ' + str(ans_div) + '\n')
    text.insert(4.0, 'В результаті внесення під корінь: ' + str(ans_sqrt) + '\n')

    ans_abs_num_for_div = calculation_abs_num(ans_div, float(answer_number1))
    ans_abs_num_for_sqrt = calculation_abs_num(ans_sqrt, float(answer_number2))

    text.insert(5.0, 'В ході обчислення гран. та абс. похибки для ділення: ' + str(ans_abs_num_for_div) + '\n')
    text.insert(6.0, 'В ході обчислення гран. та абс. похибки для кореня: ' + str(ans_abs_num_for_sqrt) + '\n')

    ans_delta_num_div = calculate_delta_num(str(ans_abs_num_for_div))
    ans_delta_num_sqrt = calculate_delta_num(str(ans_abs_num_for_sqrt))

    text.insert(7.0, 'Заокруглені результати ділення (дельта): ' + str(ans_delta_num_div) + '\n')
    text.insert(8.0, 'Заокруглені результати кореня (дельта): ' + str(ans_delta_num_sqrt) + '\n')

    ans_hranichna_vidnosna_pohibka_div = calculate_border_relative_oversight(ans_delta_num_div, float(answer_number1))
    ans_hranichna_vidnosna_pohibka_sqrt = calculate_border_relative_oversight(ans_delta_num_sqrt, float(answer_number2))

    text.insert(9.0, 'Дельта, що ділиться на введену відповідь, ділення: '
                + str(ans_hranichna_vidnosna_pohibka_div) + '\n')
    text.insert(10.0, 'Дельта, що ділиться на введену відповідь, корінь: '
                + str(ans_hranichna_vidnosna_pohibka_sqrt) + '\n')

    real_oversight_div = calculation_relative_oversight(ans_delta_num_div, float(answer_number1))
    real_oversight_sqrt = calculation_relative_oversight(ans_delta_num_sqrt, float(answer_number2))

    text.insert(11.0, 'Гранична відносна похибка, ділення: ' + str(real_oversight_div) + '\n')
    text.insert(12.0, 'Гранична відносна похибка, корінь: ' + str(real_oversight_sqrt) + '\n')

    answer_for_laba = out_answer(number_1, float(answer_number1), float(number_2)
                                 , float(answer_number2), real_oversight_div, real_oversight_sqrt)

    text.insert(13.0, answer_for_laba)


def show_result_for_second_ex(number1, number2):
    win_2 = Tk()
    win_2.title('Відповідь до задачі №2.')
    text_2 = Text(win_2)
    text_2.pack()
    text_2.insert(1.0, 'Введене число: ' + number1 + '\n')
    text_2.insert(2.0, 'Дельта (вірні цифри): ' + number2 + '\n')
    text_2.insert(3.0, 'Абсолютна похибка: ' + str(out_abs_oversight(float(number1), float(number2))) + '\n')
    text_2.insert(4.0, 'Відносна похибка: ' + str(out_abs_oversight(float(number1), float(number2))*100) + '\n')


def show_result_for_third_ex(number1, number2):
    win_3 = Tk()
    win_3.title('Відповідь до задачі №3.')
    text_3 = Text(win_3)
    text_3.pack()
    text_3.insert(1.0, 'Введене число: ' + number1 + '\n')
    text_3.insert(2.0, 'Введена відносна похибка: ' + number2 + '\n')
    ans = calculate_delta_as_number(float(number1), float(number2))
    text_3.insert(3.0, 'Дельта: ' + str(ans) + '\n')
    text_3.insert(4.0, 'Заокругливши: ' + str(calculate_true_numbers(float(number1), ans)) + '\n')


root = Tk()
window = MainWindow()
window.btn_show_result_1.bind('<Button-1>', lambda event: show_result_for_fisrt_ex(
                                                                    window.entry_add_denum_1.get()
                                                                    , window.entry_add_answer_for_first_num_1.get()
                                                                    , window.entry_add_sqrt_1.get()
                                                                    , window.entry_add_answer_for_second_num_1.get()))
window.btn_show_result_2.bind('<Button-1>', lambda event: show_result_for_second_ex(
                                                                    window.entry_add_for_number_2.get()
                                                                    , window.entry_add_for_absolute_error_2.get()))
window.btn_show_result_3.bind('<Button-1>', lambda event: show_result_for_third_ex(
                                                                    window.entry_add_for_exact_value_3.get()
                                                                    , window.entry_add_for_absolute_error_3.get()))

root.title('Елементи теорії похибок')
root.minsize(width=480, height=370)
root.maxsize(width=480, height=370)
root.mainloop()

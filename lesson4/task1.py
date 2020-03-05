from sys import argv

script_name, work_hours, pay_hours, overpay = argv

def savary():
    try:
        return (int(work_hours) * int(pay_hours)) + int(overpay)
    except TypeError:
        return 'Ввод только числовых параметров'
    except ValueError:
        return 'Некорректные значения,проверьте правильность параметров'


print(savary())

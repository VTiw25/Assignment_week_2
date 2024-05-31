from django.shortcuts import render

def calculator_view(request):
    result = None
    if request.method == "POST":
        number1 = float(request.POST.get('number1'))
        number2 = float(request.POST.get('number2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 != 0:
                result = number1 / number2
            else:
                result = "Error: Division by zero"

    return render(request, 'calculator/calculator.html', {'result': result})

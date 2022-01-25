def arithmetic_arranger(problems, *solver):
    prob_count = 0
    iteration = 0
    top_num = ""
    op_list = ""
    bot_num = ""
    width = ""
    solved_num = ""

    for problem in problems:
        prob_count +=  1

    for problem in problems:
        iteration += 1
        # Number of Problems Check
        if prob_count > 5:
            return ("Error: Too many problems.")

        separated_prob = problem.split()

        num1 = separated_prob[0]
        if len(num1) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        for characters1 in num1:
            if characters1.isdigit():
                continue
            else:
                return ("Error: Numbers must only contain digits.")

        operation = separated_prob[1]
        if operation == str('*'):
            return ("Error: Operator must be '+' or '-'.")
        if operation == str('/'):
            return ("Error: Operator must be '+' or '-'.")

        num2 = separated_prob[2]
        if len(num2) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        for characters2 in num2:
            if characters2.isdigit():
                continue
            else:
                return ("Error: Numbers must only contain digits.")

        # Solver
        if operation == str('+'):
            num3 = int(num1) + int(num2)
        if operation == str('-'):
            num3 = int(num1) - int(num2)

        # Width Calculator
        if int(num1) > int(num2):
            max_length = len(num1)
        else:
            max_length = len(num2)
        full_width = max_length + 2
        dashed_width = '-' * full_width
        
        # Final Lines
        if iteration < prob_count:
            top_num += num1.rjust(full_width) + '    '
            bot_num += operation + ' ' + num2.rjust(max_length) +  '    '
            width += dashed_width + '    '
            solved_num += str(num3).rjust(full_width) + '    '
        else:
            top_num += num1.rjust(full_width)
            bot_num += operation + ' ' + num2.rjust(max_length)
            width += dashed_width
            solved_num += str(num3).rjust(full_width)

    # Printing
    if solver:
        arranged_problems =  (top_num + "\n" + bot_num + "\n" + width + "\n" + solved_num)
    else:
        arranged_problems =  (top_num + "\n" + bot_num + "\n" + width)

    return arranged_problems
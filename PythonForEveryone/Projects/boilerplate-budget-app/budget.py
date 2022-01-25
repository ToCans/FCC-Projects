from typing import final
import unittest

class Category:

    name = ''
    balance = 0
    spent_balence = 0
    
    def __init__(self,cat):
        self.name = cat
        self.ledger = []

    def deposit(self,dep_amount,dep_desc=""):

        self.ledger.append({"amount": dep_amount, "description": dep_desc})
        self.balance = self.balance + dep_amount
        
    def withdraw(self,wit_amount,wit_desc=""):
        flag = self.check_funds(wit_amount)
        if flag == True:
            wit_amount = -wit_amount
            self.spent_balance = self.spent_balence + abs(wit_amount)
            self.balance = self.balance + wit_amount
            self.ledger.append({"amount": wit_amount, "description": wit_desc})
            return flag
        else:
            return flag

    def get_balance(self):
        return self.balance

    def transfer(self, trans_amount, cat):
        flag = self.check_funds(trans_amount)
        if flag == True:
            self.ledger.append({"amount": -trans_amount, "description": "Transfer to " + cat.name })
            cat.ledger.append({"amount": trans_amount, "description": "Transfer from " + self.name})
            self.balance = self.balance - trans_amount
            cat.balance = cat.balance + trans_amount
            return flag
        else:
            return flag

    def check_funds(self,fund_amount):
        if fund_amount > self.balance:
            flag = False
        else:
            flag = True
        return flag

    # Making Table
    def __str__(self):
        title_line_len = 30
        ast_num = ((title_line_len - len(self.name))/2)
        title_line = (int(ast_num)*'*'+self.name+int(ast_num)*'*'+"\n")
        output = title_line

        for item in self.ledger:

            # Ledger Splitting
            item = str(item)
            item = item.split(":")

            # Amount Stripping
            part1 = str(item[1])
            part1 = part1.split(",")
            amount = part1[0].strip()
            amount = float(amount)
            amount = '%.2f'%amount
            amount_len = len(amount)

            if amount_len > 7:
                amount = amount[0:7]
                amount_len = 7
            
            # Description Stripping
            part2 = item[2].strip()
            part2 = str(part2).strip('}')
            description = part2[1:-1]
            description_len = len(description)

            if description_len > 23:
                description = description[0:23]
                description_len = 23

            #Calculating Lengths
            padding_len = title_line_len - amount_len - description_len
            padding = padding_len*" "
            line = description+padding+str(amount)+"\n"

            output = output + line

        total= ("Total: "+str(self.balance))
        output = output + total
        return output
                

def create_spend_chart(categories_list):
    total_spent = 0
    longest_title = 0
    #category_spent = []

    # Find Total Balance First
    for category in categories_list:
        if len(category.name) > longest_title:
            longest_title = len(category.name)
        total_spent = total_spent + category.spent_balance

    # Chart Parameters
    top_chart = "Percentage spent by category"
    # Hundred 
    hundred_line = "\n100| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent) > 0.999:
            hundred_line = hundred_line + "o  "
        else: 
            hundred_line = hundred_line + "   "
    # Ninety 
    ninety_line = "\n 90| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.9:
            ninety_line = ninety_line + "o  "
        else: 
            ninety_line = ninety_line + "   " 
    # Eighty 
    eighty_line = "\n 80| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.8:
            eighty_line = eighty_line + "o  "
        else: 
            eighty_line = eighty_line + "   " 
    # Seventy 
    seventy_line = "\n 70| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.7:
            seventy_line = seventy_line + "o  "
        else: 
            seventy_line = seventy_line + "   " 
    # Ninety 
    sixty_line = "\n 60| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.6:
            sixty_line = sixty_line + "o  "
        else: 
            sixty_line = sixty_line + "   " 
    # Fifty 
    fifty_line = "\n 50| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.5:
            fifty_line = fifty_line + "o  "
        else: 
            fifty_line = fifty_line + "   " 
    # Fourty 
    fourty_line = "\n 40| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.4:
            fourty_line = fourty_line + "o  "
        else: 
            fourty_line = fourty_line + "   " 
    # Thirty
    thirty_line = "\n 30| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.3:
            thirty_line = thirty_line + "o  "
        else: 
            thirty_line = thirty_line + "   " 
    # Twenty 
    twenty_line = "\n 20| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.2:
            twenty_line = twenty_line + "o  "
        else: 
            twenty_line = twenty_line + "   " 
    # Ten 
    ten_line = "\n 10| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.1:
            ten_line = ten_line + "o  "
        else: 
            ten_line = ten_line + "   " 
    # Zero 
    zero_line = "\n  0| "
    for category in categories_list:
        if ((category.spent_balance)/total_spent)>0.0:
            zero_line = zero_line + "o  "
        else: 
            zero_line = zero_line + "   " 

    # Hashline
    hash_line = "\n    "
    for category in categories_list:
        hash_line = hash_line + "---"
    hash_line = hash_line + "-"
    
    # Category Titles
    category_line = "\n     "
    category_counter = 0
    while category_counter < longest_title:
        for category in categories_list:
            if category_counter >= len(category.name):
                category_line = category_line + "   "
            else:
                letter = category.name[category_counter]
                category_line = category_line + letter + "  "
        category_counter = category_counter + 1
        if category_counter < longest_title:
            category_line = category_line + "\n     "
    
    final_output = top_chart+hundred_line+ninety_line+eighty_line+seventy_line+sixty_line+fifty_line+fourty_line+thirty_line+twenty_line+ten_line+zero_line+hash_line+category_line
    return(final_output)
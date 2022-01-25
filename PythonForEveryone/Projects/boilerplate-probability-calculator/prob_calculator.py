import copy
import random
from unittest.case import expectedFailure
# Consider using the modules imported above.

class Hat:
    
    def __init__(self,**args):
        # Working
        self.contents = []
        for color,value in args.items():
            for iteration in range(value):
                self.contents.append(color)


    def draw(self,num_balls_drawn):
        # Working
        drawn_ball_output = []
        drawing_sample = 0

        for i in self.contents:
            drawing_sample += 1

        if num_balls_drawn > drawing_sample:
            return self.contents

        else:
            while num_balls_drawn > 0:
                index = random.randrange(0,drawing_sample)
                drawn_ball = self.contents.pop(index)
                drawn_ball_output.append(drawn_ball)
                num_balls_drawn -= 1
                drawing_sample -= 1
            return drawn_ball_output

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0
    failures = 0
		
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        colors_drawn = hat_copy.draw(num_balls_drawn)
        
        for key in expected_balls.keys():
            count = 0
            for index in range(len(colors_drawn)):
                if colors_drawn[index] == key:
                    count += 1
            if count < expected_balls[key]:
                failures += 1
                break
                

    successful_experiments = 1 - (failures/num_experiments)


    return successful_experiments

    

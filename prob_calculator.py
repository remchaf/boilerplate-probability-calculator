import copy
import random
import re
# Consider using the modules imported above.


class Hat:
    contents = None
    colors = ['red', 'orange', 'black', 'blue', 'green', 'yellow', 
                'pink', 'striped', 'test']
    variables = None

    def __init__(self, green=0, blue=0, red=0, orange=0, black=0, yellow=0, pink=0, striped=0, test=0):
        self.variables = (red, orange, black, blue, green, yellow, pink, striped, test)
        self.contents = list()

        for i in range(len(self.colors)):
            if not self.variables[i]:
                continue
            self.contents.extend(
                [self.colors[i] for x in range(self.variables[i])])

    def __str__(self) -> str:
        return (self.contents)

    def draw(self, n) :
        if n >= len(self.contents) :
            return self.contents
        
        ls = list()
        for i in range(n) :
            idx = random.randrange( len(self.contents) )
            ls.append( self.contents[idx] )
            del self.contents[idx]
        
        return ls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = 0
    
    for k in range(num_experiments) :
        ls = copy.deepcopy(hat).draw(num_balls_drawn)
        verdict = True
        for ball in expected_balls :
            ball_num = len( re.findall(ball , ' '.join(ls)) )
            if ball_num < expected_balls[ball] :
                verdict = False
                break
        if verdict : N += 1
                
    return N / num_experiments
            
        


# hat = Hat(green=3, blue=2)
# hat.draw(3)
# print(hat.contents)

# hat = Hat(black=6, red=4, green=3, test = 2)
# probability = experiment(hat=hat,
#                   expected_balls={"red":2,"green":1},
#                   num_balls_drawn=20,
#                   num_experiments=2000)

# print(probability)
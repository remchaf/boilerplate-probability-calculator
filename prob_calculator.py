import copy
import random
import re
# Consider using the modules imported above.


class Hat:
    contents = None
    colors = ['green', 'blue', 'yellow', 'red',
              'orange', 'black', 'pink', 'striped']
    variables = None

    def __init__(self, green=0, blue=0, red=0, orange=0, black=0, yellow=0, pink=0, striped=0):
        self.variables = (green, blue, yellow, red, orange, black, pink, striped)
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
            return_contents = self.contents.copy()
            self.contens = []
            return self.contents
        
        contents = copy.copy(self.contents)
        ls = list()
        for i in range(n) :
            idx = random.randrange( len(contents) )
            ls.append( contents[idx] )
            del contents[idx]
        
        return ls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N, M = 0, num_experiments
    
    for k in range(num_experiments) :
        ls = hat.draw(num_balls_drawn)
        verdict = True
        for ball in expected_balls :
            ball_num = len( re.findall(ball , ' '.join(ls)) )
            if ball_num < expected_balls[ball] :
                verdict = False
                break
        if verdict : N += 1
                
    return N / M
            
        


# hat = Hat(green=3, blue=2)
# hat.draw(3)
# print(hat.contents)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
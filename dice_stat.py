from random import randint
from plotly import offline
from plotly.graph_objs import Bar, Layout

class Die:
    """A class representing a single die"""

    def __init__(self, sides: int =6) -> None:
        self.sides = sides

    def roll(self, times=1) -> list[int]:
        n = times

        if n <= 0:
            return []

        result = []
        while (n > 0):
            result.append(randint(1, self.sides))
            n -= 1
        
        return result

def create_graph(x_val: list[int], y_val: list[int], x_config: dict[str], y_config: dict[str], filename: str ='bar_graph.html') -> None:
    """creates a bar graph with the specified name"""

    data = [Bar(x=x_val, y=y_val)]
    my_layout = Layout(title='Results of rolling dice 10000 times',
                    xaxis=x_config, yaxis=y_config)

    offline.plot({'data': data, 'layout': my_layout}, filename=filename)

def main():
    """Entry point"""

    while True:
        roll_count = input("Roll the die how many times? > ")
        try:
            roll_count = int(roll_count)
            if roll_count <= 0 :
                print("numbers greater than zero only please")
                continue
            else:
                break
        except:
            print("please enter a number")
            continue
    

    die = Die()
    results = die.roll(roll_count)

    freqs: list[int] = []
    for value in range(1, die.sides+1):
        freq = results.count(value)
        freqs.append(freq)

    x_values = list(range(1, die.sides+1))
    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of result'}

    create_graph(x_values, freqs, x_axis_config, y_axis_config)

if __name__ == '__main__':
    main()
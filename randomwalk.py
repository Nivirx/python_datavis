import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=10000) -> None:
        self.num_points = num_points

        # start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """perform calculation of the random walk"""

        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

def main():
    """Entry point"""

    while True:
        rw = RandomWalk(50_000)
        rw.fill_walk()

        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(11,9), dpi=100)

        point_numbers = range(rw.num_points)

        ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=2)

        # clearly mark first and last points
        ax.scatter(0,0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        # clean up axes
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Generate another walk? (y/n)")
        if keep_running == 'n':
            break

    
if __name__ == '__main__':
    main()
        
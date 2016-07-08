

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = [(0, 0)]
        self.width, self.height = width, height
        self.food = food
        self.count = 0
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        cur_x, cur_y = self.snake[-1][0], self.snake[-1][1]
        if direction == 'U':
            cur_x -= 1
        elif direction == 'L':
            cur_y -= 1
        elif direction == 'R':
            cur_y += 1
        else:
            cur_x += 1
        
        if 0 <= cur_x < self.height and 0 <= cur_y < self.width:
            
            if self.food and cur_x == self.food[0][0] and cur_y == self.food[0][1]:   # eat the food
                self.food.pop(0)    # remove the current food and not increase the length of snake
                self.count += 1
            else:
                self.snake.pop(0)
            
            # eat itself
            if  (cur_x, cur_y) not in self.snake:
                self.snake.append((cur_x, cur_y))
            else:
                return -1
            
            return self.count
                
        else:       # touch the Wall
            return -1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
class GalacticSpaceCraft:
    def _init_(self, initial_position, initial_direction):
        self.position = list(initial_position)
        self.direction = initial_direction
        
    def move_forward(self):
        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'W':
            self.position[0] -= 1
        elif self.direction == 'Up':
            self.position[2] += 1
        elif self.direction == 'Down':
            self.position[2] -= 1
        
    def move_backward(self):
        if self.direction == 'N':
            self.position[1] -= 1
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'E':
            self.position[0] -= 1
        elif self.direction == 'W':
            self.position[0] += 1
        elif self.direction == 'Up':
            self.position[2] -= 1
        elif self.direction == 'Down':
            self.position[2] += 1
        
    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'
        
    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'
        
    def turn_up(self):
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'Up':
            pass  # Already facing Up
        elif self.direction == 'Down':
            pass  # Already facing Down
        
    def turn_down(self):
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'Up':
            pass  # Already facing Up
        elif self.direction == 'Down':
            pass  # Already facing Down
        
    def execute_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'l':
                self.turn_left()
            elif command == 'r':
                self.turn_right()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

# Take user inputs
initial_position = tuple(map(int, input("Enter initial position (x y z): ").split()))
initial_direction = input("Enter initial direction (N, S, E, W, Up, Down): ")
commands = list(input("Enter commands: "))

craft = GalacticSpaceCraft(initial_position, initial_direction)
craft.execute_commands(commands)

print("Final Position:", tuple(craft.position))
print("Final Direction:", craft.direction)
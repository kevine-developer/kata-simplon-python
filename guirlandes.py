import re

class LightGridPart1:

    def __init__(self):
        self.grid_size = 1000
        self.lights = [[False for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def turn_on(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = True

    def turn_off(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = False

    def toggle(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.lights[x][y] = not self.lights[x][y]

    def count_light_on(self):
        total = 0
        for row in self.lights:
            for lamp in row:
                if lamp:
                    total += 1
        return total


class LightGridPart2:

    def __init__(self):
        self.grid_size = 1000
        self.brightness = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def increase(self, x1, y1, x2, y2, value):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.brightness[x][y] += value

    def decrease(self, x1, y1, x2, y2, value):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.brightness[x][y] = max(0, self.brightness[x][y] - value)

    def total_brightness(self):
        total = 0
        for row in self.brightness:
            for lamp_value in row:
                total += lamp_value
        return total


class InstructionProcessor:

    def __init__(self, instructions):
        self.instructions = instructions
        self.grid_part1 = LightGridPart1()
        self.grid_part2 = LightGridPart2()

    def parse_instruction(self, instruction_text):
        instruction = instruction_text.lower()

        numbers = re.findall(r'\d+', instruction)
        x1, y1, x2, y2 = map(int, numbers)

        if "turn on" in instruction:
            action = "on"
        elif "turn off" in instruction:
            action = "off"
        else:
            action = "toggle"

        return action, x1, y1, x2, y2

    def apply_all(self):
        for text in self.instructions:
            action, x1, y1, x2, y2 = self.parse_instruction(text)

            # Partie 1
            if action == "on":
                self.grid_part1.turn_on(x1, y1, x2, y2)
            elif action == "off":
                self.grid_part1.turn_off(x1, y1, x2, y2)
            elif action == "toggle":
                self.grid_part1.toggle(x1, y1, x2, y2)

            # Partie 2
            if action == "on":
                self.grid_part2.increase(x1, y1, x2, y2, 1)
            elif action == "off":
                self.grid_part2.decrease(x1, y1, x2, y2, 1)
            elif action == "toggle":
                self.grid_part2.increase(x1, y1, x2, y2, 2)

    def results(self):
        return (
            self.grid_part1.count_light_on(),
            self.grid_part2.total_brightness()
        )


# Utilisation
instructions = [
    "turn on 887,9 through 959,629",
    "turn on 454,398 through 844,448",
    "turn off 539,243 through 559,965",
    "turn off 370,819 through 676,868",
    "turn off 145,40 through 370,997",
    "turn off 301,3 through 808,453",
    "turn on 351,678 through 951,908",
    "toggle 720,196 through 897,994",
    "toggle 831,394 through 904,860"
]

processor = InstructionProcessor(instructions)
processor.apply_all()

total_lights_on, brightness_total = processor.results()

print("Nombre total de lumières allumées :", total_lights_on)
print("Luminosité totale :", brightness_total)

from utils.files import read_data_into_list


class Game:
    def __init__(self, data):
        self.instructions = self._process_into_dict(data)
        self.no_instructions = len(self.instructions)
        self.processed_instructions = []

        self.accumulator = 0
        self.index = 0

    def run(self) -> int:
        while self.index <= self.no_instructions:
            if self.index in self.processed_instructions:
                print("Already processed instruction")
                print("REACHED END")
                break
            else:
                self.processed_instructions.append(self.index)
                self._process_instruction()
        return self.accumulator

    def _process_instruction(self):
        instruction_dict = self.instructions[self.index]
        for operation, amount in instruction_dict.items():
            if operation == "nop":
                self.index += 1
            if operation == "acc":
                self.accumulator += amount
                self.index += 1
            if operation == "jmp":
                self.index += amount

    @staticmethod
    def _process_into_dict(data):
        instructions = []
        for d in data:
            operation, amount = d.split(" ")
            amount = int(amount.replace("+", ""))
            instructions.append({operation: amount})
        print(instructions)
        return instructions


if __name__ == "__main__":
    data = read_data_into_list("input.txt")

    print("Solution 1", Game(data).run())

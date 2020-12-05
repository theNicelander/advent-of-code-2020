import math
import numpy as np
from utils.files import read_data_into_list


class Ticket:
    def __init__(self, ticket):
        self.rows = ticket[:7]
        self.seats = ticket[7:]
        self.last_row = self.rows[-1]
        self.last_seat = self.seats[-1]

        self.row_number = self._find_seat(127, self.rows, "B")
        self.seat_number = self._find_seat(7, self.seats, "R")
        self.seat_id = (self.row_number * 8) + self.seat_number

    def _find_seat(self, upper, characters, upper_char):
        lower = 0
        for char in characters:
            mid = np.mean([lower, upper])
            if char == upper_char:
                lower = math.ceil(mid)
            else:
                upper = math.floor(mid)
        final = upper if characters[-1] == upper_char else lower
        return final

    def get_seat_id(self):
        return self.seat_id


def test_tickets():
    assert Ticket("FBFBBFFRLR").get_seat_id() == 357
    assert Ticket("BFFFBBFRRR").get_seat_id() == 567
    assert Ticket("FFFBBBFRRR").get_seat_id() == 119
    assert Ticket("BBFFBBFRLL").get_seat_id() == 820
    print("ALL TESTS PASSED")


def find_missing(ticket_id_list):
    range_list = range(ticket_id_list[0], ticket_id_list[-1])
    return set(range_list).difference(ticket_id_list)


if __name__ == "__main__":
    test_tickets()

    data: list = read_data_into_list("input.txt")

    all_ticket_ids = [Ticket(ticket).get_seat_id() for ticket in data]
    print("Part 1: ", max(all_ticket_ids))

    missing = find_missing(all_ticket_ids)
    print("Part 2:", missing)

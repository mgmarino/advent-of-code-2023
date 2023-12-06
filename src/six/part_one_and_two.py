import math
from dataclasses import dataclass
from functools import cached_property, reduce
from operator import attrgetter, mul
from typing import Iterator


@dataclass
class RangeOfTimes:
    min_time: int
    max_time: int

    @property
    def numbers_of_integers(self) -> int:
        return self.max_time - self.min_time + 1


@dataclass
class Race:
    time_of_race: int
    record_distance: int

    @cached_property
    def possible_times_to_beat_distance(self) -> RangeOfTimes:
        """
        The characteristic function for this is following quadratic eqn:

        t**2 - T*t + D < 0


        Where

        T = time_or_race
        D = record_distance

        When this equation is true, than we have succeeded in beating the record
        distance.

        We can solve for the roots of this function quite simply, and we know:

        - the second derivative wrt t (= 2) is always positive (the function is concave up)
        - the first derivative wrt t (2*t - T) has a minumum at T/2

        so the two roots provide us a range where the function above is below

        """

        discriminant = math.sqrt(self.time_of_race**2 - 4 * self.record_distance)

        lower_bound = math.ceil((self.time_of_race - discriminant) / 2)
        upper_bound = math.floor((self.time_of_race + discriminant) / 2)

        if discriminant.is_integer():
            # These are the *exact* roots, which would mean we get *exactly* the
            # record, not greater than it, which is what we need
            lower_bound += 1
            upper_bound -= 1

        return RangeOfTimes(min_time=lower_bound, max_time=upper_bound)

    @property
    def possible_ways_to_beat_distance(self) -> int:
        return self.possible_times_to_beat_distance.numbers_of_integers


def multiply_ways_to_beat_distance(races: Iterator[Race]) -> int:
    return reduce(mul, map(attrgetter("possible_ways_to_beat_distance"), races), 1)


def part_one_and_two(races: Iterator[Race]) -> int:
    return multiply_ways_to_beat_distance(races)

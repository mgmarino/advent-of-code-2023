from contextlib import suppress
from dataclasses import dataclass
from operator import attrgetter
from typing import Iterator


@dataclass
class Card:
    identifier: int
    winning_numbers: set[int]
    numbers: set[int]

    @property
    def number_of_winning_numbers(self) -> int:
        return len(self.winning_numbers & self.numbers)

    @property
    def score(self) -> int:
        if self.number_of_winning_numbers == 0:
            return 0
        return 2 ** (self.number_of_winning_numbers - 1)


@dataclass
class LinkedCard:
    original_card: int
    linked_cards: set[int]


LinkedCardSet = list[LinkedCard]


def parse_card_in_line(line: str) -> Card:
    card_identifier, all_numbers = line.split(": ")

    winning_numbers, numbers = all_numbers.split(" | ")

    def _parse_numbers(number_str: str) -> Iterator[int]:
        for n in number_str.split(" "):
            with suppress(ValueError):
                yield int(n.strip())

    return Card(
        identifier=int(card_identifier.split(" ")[-1]),
        winning_numbers=set(_parse_numbers(winning_numbers)),
        numbers=set(_parse_numbers(numbers)),
    )


def parse_cards(all_lines: Iterator[str]) -> Iterator[Card]:
    yield from map(parse_card_in_line, all_lines)


def link_cards(cards: Iterator[Card]) -> LinkedCardSet:
    """
    Returns cards in reverse order
    """
    return [
        LinkedCard(
            original_card=c.identifier,
            linked_cards=set(
                range(
                    c.identifier + 1,
                    c.identifier + 1 + c.number_of_winning_numbers,
                )
            ),
        )
        for c in reversed(list(cards))
    ]


def count_cards(linked_cards: LinkedCardSet) -> int:
    score_total = {}

    for card in linked_cards:
        score_total[card.original_card] = (
            sum(score_total[c] for c in card.linked_cards) + 1
        )

    return sum(score_total.values())


def part_one(all_lines: Iterator[str]) -> int:
    cards = parse_cards(all_lines)
    return sum(map(attrgetter("score"), cards))


def part_two(all_lines: Iterator[str]) -> int:
    cards = parse_cards(all_lines)
    linked_cards = link_cards(cards)
    return count_cards(linked_cards)

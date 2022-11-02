# Definition of Interval holding two integers


from __future__ import annotations
from typing import List, Annotated


class Interval:

	def __init__(self, interval: Annotated[List[int], 2]) -> bool:
		self.start, self.end = interval

	def __gt__(self, other: Interval) -> bool:
		return self.start > other.end

	def __lt__(self, other: Interval) -> bool:
		return self.end < other.start

	def __ge__(self, other: Interval) -> bool:
		return self.start >= other.end

	def __le__(self, other: Interval) -> bool:
		return self.end <= other.start

	def _overlaps(self, other: Interval) -> bool:
		return not (self > other or self < other)

	def merge(self, other: Interval) -> List[Interval]:
		if self._overlaps(other):
			return [Interval(min(self.start, other.start), max(self.end, other.end))]
		return [self, other] if other > self else [other, self]

	def to_list(self) -> Annotated[List[int], 2]:
		return [self.start, self.end]

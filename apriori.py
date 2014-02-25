import re
import unittest
from collections import defaultdict


class TestApriori(unittest.TestCase):
	"""Tests for Apriori()"""

	def test_apriori(self):
		data = [ 'ABC', 'ABAB', 'BCAA' ]
		expectedResult = { "AB": 2, "BC": 2 } # if 33 < support < 66
		expectedPrimitives = set(['A', 'B', 'C'])
		testedResult = Apriori(data, 34)
		self.assertEqual(expectedResult, testedResult)
		self.assertEqual(expectedPrimitives, testedResult.primitives)


class Apriori(dict):
	"""A simple implementation of the Apriori algorithm.

	It takes only sequences of 1-item events.

	"""

	def __init__(self, listOfSequences, support):
		"""Performs apriori algorithm on `listOfSequences` with `support` as a threshold.

		Args:
			listOfSequences (list): A list of strings, each letter representing a specific event.
			support (int): The minimum percentage of sequences a pattern must match.

		"""

		super(Apriori, self).__init__()
		self.data = listOfSequences
		self.thres = (support * len(self.data)) / 100.0
		self.primitives = self.getPrimitives()
		self.apriori()
		del self.data

	def apriori(self):
		candidates = self.getNewCandidates(self.primitives)
		while len(candidates) > 0:
			res = self.getPatternsCount(candidates)
			self.update(res)
			candidates = self.getNewCandidates(res.keys())
		
	def getPrimitives(self):
		primitives = set()
		for seq in self.data:
			for event in seq:
				primitives.add(event)
		return primitives

	def getNewCandidates(self, candidates):
		newCandidates = set()
		for seq in self.data:
			for can in candidates:
				for subs in re.findall(can+".", seq):
					newCandidates.add(subs)
		return newCandidates

	def getPatternsCount(self, candidates):
		patternsCount = defaultdict(int)
		for seq in self.data:
			for can in candidates:
				if can in seq:
					patternsCount[can] += 1
		return {k:v for k, v in patternsCount.iteritems() if v > self.thres}


if __name__ == '__main__':
	pass
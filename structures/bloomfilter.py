# Python 3 program to build Bloom Filter
# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import math
import mmh3
# we are using the bitarray module (written in C) to efficiently implement bit-arrays
from bitarray import bitarray


# Bloom filter, using the murmur3 hash function
class BloomFilter(object):

	# @params: items_count - Number of items expected to be stored in bloom filter
	# @params: fp_prob - False Positive probability in decimal
	def __init__(self, items_count, fp_prob):

		# False possible probability in decimal
		self.fp_prob = fp_prob

		# Size of bit array to use
		self.size = self.get_size(items_count, fp_prob)

		# number of hash functions to use
		self.hash_count = self.get_hash_count(self.size, items_count)

		# Bit array of given size
		self.bit_array = bitarray(self.size)

		# initialize all bits as 0
		self.bit_array.setall(0)


	# Adds an item to the filter
	# @params: item - item to be added to the filter
	def add(self, item):
		digests = []
		for i in range(self.hash_count):

			# create digest for given item.
			# i work as seed to mmh3.hash() function
			# With different seed, digest created is different
			digest = mmh3.hash(item, i) % self.size
			digests.append(digest)

			# set the bit True in bit_array
			self.bit_array[digest] = True

	
	# Checks for existence of an item in filter
	# @params: item - item to be searched in the filter
	def check(self, item):
		for i in range(self.hash_count):
			digest = mmh3.hash(item, i) % self.size
			if self.bit_array[digest] == False:

				# if any of bit is False then,its not present
				# in filter
				# else there is probability that it exist
				return False
		return True
	

	# Returns the size of bit array(m) to used using the formula: m = -(n * lg(p)) / (lg(2)^2)
	# @params: n - number of items expected to be stored in filter
	# @params: p - False Positive probability in decimal
	@classmethod
	def get_size(self, n, p):

		m = -(n * math.log(p))/(math.log(2)**2)
		return int(m)
	

	# Returns the hash function(k) to be used using the formula k = (m/n) * lg(2)
	# @params: m - size of the bit array
	# @params: n - number of items expected to be stored in the filter
	@classmethod
	def get_hash_count(self, m, n):

		k = (m/n) * math.log(2)
		return int(k)
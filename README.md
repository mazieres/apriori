# Apriori

## About

A simple implementation of the [apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm). A method for extracting frequent substructures in a set of sequences of ordered events.

## How To

`Apriori` takes a list of strings, representing sequences, and an integer, representing the percentage of sequences the pattern must match for being considered.

```python
In [1]: from apriori import *

In [2]: data = ["ABCDEFGHIJKL","ZOPQABCDLMNOP","REWQZOPQAB"]

In [3]: patterns = Apriori(data, 34)

In [4]: patterns
Out[4]:
{'AB': 3,
 'ABC': 2,
 'ABCD': 2,
 'BC': 2,
 'BCD': 2,
 'CD': 2,
 'OP': 2,
 'OPQ': 2,
 'OPQA': 2,
 'OPQAB': 2,
 'PQ': 2,
 'PQA': 2,
 'PQAB': 2,
 'QA': 2,
 'QAB': 2,
 'ZO': 2,
 'ZOP': 2,
 'ZOPQ': 2,
 'ZOPQA': 2,
 'ZOPQAB': 2}
 ```

## References

+ "Mining Frequent Patterns, Associations, and Correlations" (Chap. 5) *in* Han, J., Kamber, M., & Pei, J. (2006). **Data mining: concepts and techniques.** Morgan kaufmann.

+ Mooney, C. H., & Roddick, J. F. (2013). **Sequential pattern mining--approaches and algorithms.** ACM Computing Surveys (CSUR), 45(2), 19.
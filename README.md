[![](https://img.shields.io/pypi/pyversions/columnate.svg?longCache=True)](https://pypi.org/pypi/columnate/)
[![](https://img.shields.io/pypi/v/columnate.svg?maxAge=3600)](https://pypi.org/pypi/columnate/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/columnate.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/columnate.py/)

#### Install
```bash
$ [sudo] pip install columnate
```

#### Functions
function|description
-|-
`columnate.lists(matrix)`|columnate lists

#### Examples
```python
>>> import columnate
>>> matrix = [[308, 0, "com.apple.Finder"],[84509, 0, "com.apple.metadata.mdwrite"]]
>>> columnate.lists(matrix)
308    0  com.apple.Finder
84509  0  com.apple.metadata.mdwrite
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>
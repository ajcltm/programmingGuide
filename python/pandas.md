## **Pandas**
---
### **Object creation**
---
- pd.Series()
~~~python
[in]
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

[out]
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
~~~
- pd.DataFrame()
~~~python
[in]
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

df2

[out]
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
~~~

- pd.DataFrame()에서 row의 length가 하나일때 발생하는 error  
  ! 주의 : 아래 예시는 np.random.randint(0,10,size=(1,5))의 return값이 array([[3, 9, 6, 5, 9]])으로 2차원 배열이기 때문에 배열의 각 원소를 value로 인식하지 않고 array([[3, 9, 6, 5, 9]]) 전체를 하나의 원소(scalar)로 취급하기 때문에 index에러가 발생함. 1차원 배열을 입력해야 의도한 대로 5행 2열의 DataFrame을 얻을 수 있음
  
~~~python
[in]
data = {
    'col1' : np.random.randint(0,10,size=(1,5)),
    'col2' : np.random.randint(0,10,size=(1,5))
}

df = pd.DataFrame(data)
df

[out]
[...]
ValueError: If using all scalar values, you must pass an index
~~~
~~~python
[in]
data = {
    'col1' : np.random.randint(0,10,size=(5)),
    'col2' : np.random.randint(0,10,size=(5))
}

df = pd.DataFrame(data)
df

[out]
	col1	col2
0	1      	1
1	5      	2
2	7      	3
3	6      	6
4	3      	9
~~~

- df.dtypes
~~~python
# df2

     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
---------------------------------------------------------------
[in]
df2.dtypes

[out]
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
~~~

- df.describe()
~~~python 
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
---------------------------------------------------------------
[in]
df.describe()

[out]

              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
~~~

### **Viewing data**
---
- Viewing the top and bottom rows of the frame
~~~python
[in]
df.head()

[Out] 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
~~~
~~~python
[in]
df.tail(3)

[Out]
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~

- Display the index, columns
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df.index

[Out] 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
~~~
~~~python
[in]
df.columns

[Out]
Index(['A', 'B', 'C', 'D'], dtype='object')
~~~

- Transposing data
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
---------------------------------------------------------------
[in]
df.T

[Out]
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
~~~

- Sorting data
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Sorting by an axis
[in]
df.sort_index(axis=1, ascending=False)

[Out]
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
~~~
~~~python
# Sorting by values
[in]
df.sort_values(by="B")

[Out]
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
~~~

### **Data Selection**
---
- Getting
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Selecting a single column, which yields a Series, equivalent to df.A
[in]
df["A"]

[out]
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.67369
~~~

~~~python
# Selecting via [], which slices the rows:
[in]
df[0:3]

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
~~~

~~~python
[in]
df["20130102":"20130104"]

[out]
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
~~~

- Selection by label
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# For getting a cross section using a label
[in]
df.loc[dates[0]]

[out]
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
~~~
~~~python
# Selecting on a multi-axis by label
[in]
df.loc[:, ["A", "B"]]

[out] 
                   A         B
2013-01-01  0.469112 -0.282863
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
2013-01-06 -0.673690  0.113648
~~~

~~~python
# Showing label slicing, both endpoints are included
[in]
df.loc["20130102":"20130104", ["A", "B"]]

[out] 
                   A         B
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
~~~

~~~python
# Reduction in the dimensions of the returned object
[in]
df.loc["20130102", ["A", "B"]

[out] 
A    1.212112
B   -0.173215
Name: 2013-01-02 00:00:00, dtype: float64
~~~

~~~python
# For getting a scalar value
[in]
df.loc[dates[0], "A"]

[out] 
0.4691122999071863
~~~

~~~python
# For getting fast access to a scalar (equivalent to the prior method)
[in]
df.at[dates[0], "A"]

[out] 
0.4691122999071863
~~~

- Selection by position
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# By integer slices, acting similar to NumPy/Python
[in]
df.iloc[3:5, 0:2]

[out] 
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
~~~
~~~python
# By lists of integer position locations, similar to the NumPy/Python style
[in]
df.iloc[[1, 2, 4], [0, 2]]

[out] 
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
~~~

~~~python
# For getting a value explicitly
[in]
df.iloc[1, 1]

[out] 
-0.17321464905330858
~~~

~~~python
# For getting fast access to a scalar (equivalent to the prior method)
[in]
df.iat[1, 1]

[out] 
-0.17321464905330858
~~~

- loc와 iloc의 차이
~~~python
# df
	col1	col2
0	1      	1
1	5      	2
2	7      	3
3	6      	6
4	3      	9
~~~

~~~python
[in]
df.iloc[2:3]

[out]
	col1	col2
2	7      	3
~~~
~~~python
[in]
df.loc[2:3]

[out]
	col1	col2
2	7      	3
3	6      	6
~~~

- Boolean indexing
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Using a single column’s values to select data
[in]
df[df["A"] > 0]

[out]
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
~~~
~~~python
# Selecting values from a DataFrame where a boolean condition is met
[in]
df[df > 0]

[out]
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
~~~
~~~python
# Using the isin() method for filtering
[in]
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2

[out]
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three
---------------------------------------------------------------
[in]
df2[df2["E"].isin(["two", "four"])]

[out]
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
~~~

- Setting
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1

[out]
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
~~~
~~~python
[in]
df["F"] = s1  # Setting a new column automatically aligns the data by the indexes
df.at[dates[0], "A"] = 0  # Setting values by label
df.iat[0, 1] = 0  # Setting values by position
df.loc[:, "D"] = np.array([5] * len(df))  # Setting by assigning with a NumPy array
df

[out]
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059  5  NaN
2013-01-02  1.212112 -0.173215  0.119209  5  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0
2013-01-05 -0.424972  0.567020  0.276232  5  4.0
2013-01-06 -0.673690  0.113648 -1.478427  5  5.0
~~~
~~~python
# A where operation with setting
[in]
df2 = df.copy()
df2[df2 > 0] = -df2
df2

[out]
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -1.509059 -5  NaN
2013-01-02 -1.212112 -0.173215 -0.119209 -5 -1.0
2013-01-03 -0.861849 -2.104569 -0.494929 -5 -2.0
2013-01-04 -0.721555 -0.706771 -1.039575 -5 -3.0
2013-01-05 -0.424972 -0.567020 -0.276232 -5 -4.0
2013-01-06 -0.673690 -0.113648 -1.478427 -5 -5.0
~~~

### **MultiIndex**
---
~~~python
                     A         B         C
first second                              
bar   one     0.895717  0.410835 -1.413681
      two     0.805244  0.813850  1.607920
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
      two    -0.226169 -1.436737 -2.006747
~~~
~~~python
[in]
df.loc[("bar", "two")]

[out] 
A    0.805244
B    0.813850
C    1.607920
Name: (bar, two), dtype: float64
~~~
~~~python
[in]
df.loc[("bar", "two"), "A"]

[out] 
0.8052440253863785
~~~
~~~python
[in]
df.loc["bar"]

[out]
               A         B         C
second                              
one     0.895717  0.410835 -1.413681
two     0.805244  0.813850  1.607920
~~~
~~~python
[in]
df.loc["baz":"foo"]

[out]
                     A         B         C
first second                              
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
~~~
~~~python
[in]
df.loc[("baz", "two"):("qux", "one")] 

[out]
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
~~~
~~~python
[in]
df.loc[("baz", "two"):"foo"]

[out]
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
~~~
~~~python
[in]
df.loc[[("bar", "two"), ("qux", "one")]]

[out]
                     A         B         C
first second                              
bar   two     0.805244  0.813850  1.607920
qux   one    -1.170299  1.130127  0.974466
~~~

~~~python
# another example : there is a seies...
A  c    1   
   d    2   
   e    3   
B  c    4   
   d    5   
   e    6  

[in]
s.loc[[("A", "c"), ("B", "d")]]  # list of tuples

[out]
A  c    1
B  d    5
dtype: int64

[in]
s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists

[out]
A  c    1
   d    2
B  c    4
   d    5
dtype: int64
~~~

~~~python
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C0 D0    1    0    3    2
         D1    5    4    7    6
      C1 D0    9    8   11   10
         D1   13   12   15   14
      C2 D0   17   16   19   18
...          ...  ...  ...  ...
A3 B1 C1 D1  237  236  239  238
      C2 D0  241  240  243  242
         D1  245  244  247  246
      C3 D0  249  248  251  250
         D1  253  252  255  254
~~~
~~~python

[in]
dfmi.loc[(slice("A1", "A3"), slice(None), ["C1", "C3"]), :]

[out]
lvl0           a         b     
lvl1         bar  foo  bah  foo
A1 B0 C1 D0   73   72   75   74
         D1   77   76   79   78
      C3 D0   89   88   91   90
         D1   93   92   95   94
   B1 C1 D0  105  104  107  106
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254

[24 rows x 4 columns]

[in]
idx = pd.IndexSlice

dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
dfmi.loc["A1", (slice(None), "foo")]

[out]
lvl0        a    b
lvl1      foo  foo
B0 C0 D0   64   66
      D1   68   70
   C1 D0   72   74
      D1   76   78
   C2 D0   80   82
...       ...  ...
B1 C1 D1  108  110
   C2 D0  112  114
      D1  116  118
   C3 D0  120  122
      D1  124  126

[16 rows x 2 columns]

[in]
dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
mask = dfmi[("a", "foo")] > 200
dfmi.loc[idx[mask, :, ["C1", "C3"]], idx[:, "foo"]]

[out]
lvl0           a    b
lvl1         foo  foo
A3 B0 C1 D1  204  206
      C3 D0  216  218
         D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

[in]
dfmi.loc(axis=0)[:, :, ["C1", "C3"]]

[out]
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C1 D0    9    8   11   10
         D1   13   12   15   14
      C3 D0   25   24   27   26
         D1   29   28   31   30
   B1 C1 D0   41   40   43   42
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254
~~~


### **타입 변경**
---
- df.to_numpy()
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
[in]
df.to_numpy()

[out]
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
~~~

- to dictionary
~~~python
# df
   col1  col2
0     1     1
1     5     2
2     7     3
3     6     6
4     3     9
~~~
~~~python
[in]
df.to_dict()

[out]
{'col1': {0: 1, 1: 5, 2: 7, 3: 6, 4: 3}, 'col2': {0: 1, 1: 2, 2: 3, 3: 6, 4: 9}}
~~~
~~~python
[in]
df.to_dict(orient="list")

[out]
{'col1': [1, 5, 7, 6, 3], 'col2': [1, 2, 3, 6, 9]}
~~~

~~~python
[in]
df.to_dict(orient='series')

[out]
{'col1': 0    1
1    5
2    7
3    6
4    3
Name: col1, dtype: int64, 'col2': 0    1
1    2
2    3
3    6
4    9
Name: col2, dtype: int64}
~~~

~~~python
[in]
df.to_dict(orient="split")

[out]
{'index': [0, 1, 2, 3, 4], 'columns': ['col1', 'col2'], 'data': [[1, 1], [5, 2], [7, 3], [6, 6], [3, 9]]}
~~~

~~~python
[in]
df.to_dict(orient="index")

[out]
{0: {'col1': 1, 'col2': 1}, 1: {'col1': 5, 'col2': 2}, 2: {'col1': 7, 'col2': 3}, 3: {'col1': 6, 'col2': 6}, 4: {'col1': 3, 'col2': 9}}
~~~

~~~python
[in]
df.to_dict(orient="records")

[out]
[{'col1': 1, 'col2': 1}, {'col1': 5, 'col2': 2}, {'col1': 7, 'col2': 3}, {'col1': 6, 'col2': 6}, {'col1': 3, 'col2': 9}]
~~~

### **column, row, index 변경, 추가, 삭제**
---
- df.set_index()
~~~python
# df
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
---------------------------------
[in]
df = df.set_index('A')
print(df)

[out]
   B  C
A      
1  2  3
4  5  6
7  8  9
~~~
- df.columns or df.rename
~~~python

[in]
# 전체 열 이름 입력하기
df.columns = ['name1', 'name2', 'name3']

# 선택하여 열 이름 변경하기
df.rename(columns={'Beforename':'Aftername'}, inplace=True)
~~~
- df.append()
~~~python
# df
    48  49  50
0   1   2   3
1   4   5   6
2   7   8   9

# a 
   48  49  50
0   1   2   3
---------------------------
[in]
df = df.append(a)
df = df.reset_index(drop=True)

[out]
   48  49  50
0   1   2   3
1   4   5   6
2   7   8   9
3   1   2   3
~~~
- df.drop()
~~~python
# df
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9

[in]
df.drop('A', axis=1, inplace=True)
print(df)

[out]
   B  C
0  2  3
1  5  6
2  8  9
---------------------------
[in]
print(df.drop(df.index[1]))

[out]
   A  B  C
0  1  2  3
2  7  8  9
---------------------------
[in]
print(df.drop(0))

[out]
   A  B  C
1  4  5  6
2  7  8  9
~~~

### **데이터 수정하기**
---
- selecting 후 수정
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df가 원본이면 아래와 같이 작동함
[in]
df.loc[0, 'col1'] = 100

[out]
   col1  col2 col3
0   100     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df를 selectig하면 얕은 복사가된 사본이 되어 원본데이터는 바뀌어 있지 않음
[in]
con = df.loc[:, 'col1']==1
df.loc[con][0] = 100

print(df)

[out]
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
-------------------------
# df를 index로 직접 selectig하면 원본데이터가 변경됨
[in]
con = df.loc[:, 'col1']==1
df.loc[df.loc[con].index, 'col1'] = 100

print(df)

[out]
   col1  col2 col3
0   100     1    a
1   100     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
- df.replace or series.replace로 데이터 수정
~~~python
# df
   A  B  C
0  0  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e

[in]
df.replace(0, 5)

[out]
    A  B  C
0  5  5  a
1  1  6  b
2  2  7  c
3  3  8  d
4  4  9  e
--------------------------
# List-like `to_replace`
[in]
df.replace([0, 1, 2, 3], 4)

[out]
    A  B  C
0  4  5  a
1  4  6  b
2  4  7  c
3  4  8  d
4  4  9  e
--------------------------
# List-like `to_replace`
[in]
df.replace([0, 1, 2, 3], [4, 3, 2, 1])

[out]
    A  B  C
0  4  5  a
1  3  6  b
2  2  7  c
3  1  8  d
4  4  9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({0: 10, 1: 100})

[out]
    A  B  C
0   10  5  a
1  100  6  b
2    2  7  c
3    3  8  d
4    4  9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({'A': 0, 'B': 5}, 100)

[out]
    A    B  C
0  100  100  a
1    1    6  b
2    2    7  c
3    3    8  d
4    4    9  e
--------------------------
# dict-like `to_replace`
[in]
df.replace({'A': {0: 100, 4: 400}})

[out]
    A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
~~~
~~~python
# df
      A    B
0   bat  abc
1   foo  bar
2  bait  xyz
--------------------------
# Regular expression `to_replace`
[in]
df.replace(to_replace=r'^ba.$', value='new', regex=True)

[out]
        A    B
0   new  abc
1   foo  new
2  bait  xyz
--------------------------
[in]
df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)

[out]
        A    B
0   new  abc
1   foo  bar
2  bait  xyz
~~~

- where 또는 mask함수로 수정
~~~python
s = pd.Series(range(5))
--------------------------
[in]
s.where(s > 0)

[out]
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
--------------------------
[in]
s.mask(s > 0)

[out]
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64
--------------------------
[in]
s.where(s > 1, 10)

[out]
0    10
1    10
2    2
3    3
4    4
dtype: int64
--------------------------
[in]
s.mask(s > 1, 10)

[out]
0     0
1     1
2    10
3    10
4    10
dtype: int64
~~~

~~~python
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
--------------------------
[in]
m = df % 3 == 0
df.where(m, -df)

[out]
   A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
~~~

### **Missing data 처리**
---
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data
[in]
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1
[out]
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  NaN
~~~
~~~python
# To drop any rows that have missing data
[in]
df1.dropna(how="any")
[out]
                   A         B         C  D    F    E
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
~~~
~~~python
# Filling missing data
[in]
df1.fillna(value=5)
[out]
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5  5.0  1.0
2013-01-02  1.212112 -0.173215  0.119209  5  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5  2.0  5.0
2013-01-04  0.721555 -0.706771 -1.039575  5  3.0  5.0
~~~
~~~python
# To get the boolean mask where values are nan
[in]
pd.isna(df1)
[out]
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
~~~

### **중복값 또는 고유값 처리**
---
- series.unique()
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
[in]
unique = df.col1.unique()
print(unique)
print(type(unique))

[out]
[1 2 3]
<class 'numpy.ndarray'>
~~~

- df.duplicated() ; row 기준으로 중복 검사하여 bool 값이 있는 series로 반환함
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# row 전체가 같을 경우 뒤에 나오는 row를 중복된 row로 인식
[in]
print(df.duplicated())

[out]
0    False
1     True
2    False
3    False
4    False
dtype: bool
~~~

~~~python
# subset을 인자로 넣을 경우 해당 컬럼들만을 기준으로 중복 검사함
[in]
print(df.duplicated(['col1']))

[out]
0    False
1     True
2    False
3     True
4    False
dtype: bool
~~~

~~~python
# keep='last'로 하면 중복된 마지막 row을 살리고, 앞에 있는 row들을 중복으로 인식
[in]
print(df.duplicated(['col1'], keep='last'))

[out]
0     True
1    False
2     True
3    False
4    False
dtype: bool
~~~

- df.drop_duplicates() ; 중복된 row를 제거
~~~python
# df
   col1  col2 col3
0     1     1    a
1     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# row 전체가 동일한 값을 갖는 뒤에 나오는 row들을 제거
[in]
print(df.drop_duplicates())

[out]
   col1  col2 col3
0     1     1    a
2     2     2    b
3     2     4    c
4     3     7    d
~~~
~~~python
# subset을 인자로 넣을 경우 해당 컬럼들만을 기준으로 중복 제거함
[in]
print(df.drop_duplicates(['col1']))

[out]
   col1  col2 col3
0     1     1    a
2     2     2    b
4     3     7    d
~~~
~~~python
# keep='last'로 하면 중복된 마지막 row을 살리고, 앞에 있는 row들을 중복 제거
[in]
print(df.drop_duplicates(['col1'], keep='last'))

[out]
   col1  col2 col3
1     1     1    a
3     2     4    c
4     3     7    d
~~~


### **데이터 타입 변경** 
---
- to_numeric()  
 : DataFrame 이나 Series 내 문자열 칼럼을 숫자형으로 변환  
 ! 수치형으로 변환이 불가능한 값이 있을 경우, 인자 옵션은 errors = 'raise'(에러메시지 띄움), 'coerce'(nan 반환), 'ignore'(무시하고 원래값 반환)
 ~~~python
# df
   col_1  col_2
0      1    4.0
1      2    bbb
2      3    6.0
~~~
~~~python
[in]
df = df.apply(pd.to_numeric, errors = 'coerce')
print(df)

[out]
   col_1  col_2
0      1    4.0
1      2    NaN
2      3    6.0
~~~

- nan 값을 None 값으로 변환   
 ! Pandas DataFrame에 None 데이터를 넣으면 NaN 객체로 자동 변환이 된다. None은 다른 프로그래밍 언어에서의 NULL이다. NaN은 Not a Number의 약자로 정의되거나, 표현되지 않는 부동소수점 값으로 Python에서는 float 타입이 된다.  math 모듈에서는 isnan(), pandas 모듈에서는 isnull() 함수로 nan인지 확인하는 함수를 제공한다.
~~~python
df = df.where(pd.notnull(df), None)
~~~

### **Operations**
---
- Stats
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Performing a descriptive statistic
[in]
df.mean()

[out]
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
~~~
~~~python
# Same operation on the other axis
[in]
df.mean(1)

[out]
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
~~~
- df.sub()
~~~python
# df
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
~~~
~~~python
# Same operation on the other axis
[in]
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
[out]
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64
~~~
~~~python
# Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension
[in]
df.sub(s, axis="index")

[out]
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
~~~

- Histogramming
~~~python
[in]
s = pd.Series(np.random.randint(0, 7, size=10))
s

[out]
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int64
~~~
~~~python
[in]
s.value_counts()

[out]
4    5
2    2
6    2
1    1
dtype: int64
~~~

### **Merge**
---
- concat
~~~python
[in]
df = pd.DataFrame(np.random.randn(10, 4))
df

[out]
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
~~~
~~~python
[in]
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

[out]
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
~~~

- join  
pd.merge(
    left,
    right,
    how="inner",
    on=None,
    left_on=None,
    right_on=None,
    left_index=False,
    right_index=False,
    sort=True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator=False,
    validate=None,
)

|Merge method| SQL Join Name| Description|
|---|---|---|
|left|LEFT OUTER JOIN|Use keys from left frame only|
|right|RIGHT OUTER JOIN|Use keys from right frame only|
|outer|FULL OUTER JOIN|Use union of keys from both frames|
|inner|INNER JOIN|Use intersection of keys from both frames|
|cross|CROSS JOIN|Create the cartesian product of rows of both frames|


~~~python
# left
   key  lval
0  foo     1
1  foo     2

# right
   key  rval
0  foo     4
1  foo     5
---------------------------------------------------------------
[in]
pd.merge(left, right, on="key")

[out]
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
~~~

~~~python
[in]
# left
   key  lval
0  foo     1
1  bar     2

# right
   key  rval
0  foo     4
1  bar     5
---------------------------------------------------------------
[in]
pd.merge(left, right, on="key")

[out]
   key  lval  rval
0  foo     1     4
1  bar     2     5
~~~

~~~python
# left
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
2  K2  A2  B2
3  K3  A3  B3

# right
  key   C   D
0  K0  C0  D0
1  K1  C1  D1
2  K2  C2  D2
3  K3  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, on="key")

[out]
  key   A   B   C   D
0  K0  A0  B0  C0  D0
1  K1  A1  B1  C1  D1
2  K2  A2  B2  C2  D2
3  K3  A3  B3  C3  D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, on=["key1", "key2"])

[out]
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="left", on=["key1", "key2"])

[out]
  key1 key2   A   B    C    D
0   K0   K0  A0  B0   C0   D0
1   K0   K1  A1  B1  NaN  NaN
2   K1   K0  A2  B2   C1   D1
3   K1   K0  A2  B2   C2   D2
4   K2   K1  A3  B3  NaN  NaN
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="right", on=["key1", "key2"])

[out]
  key1 key2    A    B   C   D
0   K0   K0   A0   B0  C0  D0
1   K1   K0   A2   B2  C1  D1
2   K1   K0   A2   B2  C2  D2
3   K2   K0  NaN  NaN  C3  D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="outer", on=["key1", "key2"])

[out]
  key1 key2    A    B    C    D
0   K0   K0   A0   B0   C0   D0
1   K0   K1   A1   B1  NaN  NaN
2   K1   K0   A2   B2   C1   D1
3   K1   K0   A2   B2   C2   D2
4   K2   K1   A3   B3  NaN  NaN
5   K2   K0  NaN  NaN   C3   D3
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="inner", on=["key1", "key2"])

[out]
  key1 key2   A   B   C   D
0   K0   K0  A0  B0  C0  D0
1   K1   K0  A2  B2  C1  D1
2   K1   K0  A2  B2  C2  D2
~~~

~~~python
# left
  key1 key2   A   B
0   K0   K0  A0  B0
1   K0   K1  A1  B1
2   K1   K0  A2  B2
3   K2   K1  A3  B3

# right
  key1 key2   C   D
0   K0   K0  C0  D0
1   K1   K0  C1  D1
2   K1   K0  C2  D2
3   K2   K0  C3  D3
---------------------------------------------------------------
[in]
result = pd.merge(left, right, how="cross")

[out]
   key1_x key2_x   A   B key1_y key2_y   C   D
0      K0     K0  A0  B0     K0     K0  C0  D0
1      K0     K0  A0  B0     K1     K0  C1  D1
2      K0     K0  A0  B0     K1     K0  C2  D2
3      K0     K0  A0  B0     K2     K0  C3  D3
4      K0     K1  A1  B1     K0     K0  C0  D0
5      K0     K1  A1  B1     K1     K0  C1  D1
6      K0     K1  A1  B1     K1     K0  C2  D2
7      K0     K1  A1  B1     K2     K0  C3  D3
8      K1     K0  A2  B2     K0     K0  C0  D0
9      K1     K0  A2  B2     K1     K0  C1  D1
10     K1     K0  A2  B2     K1     K0  C2  D2
11     K1     K0  A2  B2     K2     K0  C3  D3
12     K2     K1  A3  B3     K0     K0  C0  D0
13     K2     K1  A3  B3     K1     K0  C1  D1
14     K2     K1  A3  B3     K1     K0  C2  D2
15     K2     K1  A3  B3     K2     K0  C3  D3
~~~
### **apply**
---
~~~python
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
df
   A  B
0  4  9
1  4  9
2  4  9
~~~
~~~python
[in]
df.apply(np.sqrt)

[out]
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0
~~~
~~~python
[in]
df.apply(np.sum, axis=0)

[out]
A    12
B    27
dtype: int64
~~~
~~~python
[in]
df.apply(np.sum, axis=1)

[out]
0    13
1    13
2    13
dtype: int64
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1)

[out]
0    [1, 2]
1    [1, 2]
2    [1, 2]
dtype: object
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1, result_type='expand')

[out]
   0  1
0  1  2
1  1  2
2  1  2
~~~
~~~python
[in]
df.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)

[out]
   foo  bar
0    1    2
1    1    2
2    1    2
~~~
~~~python
[in]
df.apply(lambda x: [1, 2], axis=1, result_type='broadcast')

[out]
   A  B
0  1  2
1  1  2
2  1  2
~~~



### **Series.str**
---
- Series.str.strip()
  : 맨 왼쪽과 오른쪽의 공백문자 제거(가운데 공백문자는 제거 하지 않음)
~~~python
df = pd.DataFrame(
    np.random.randn(3, 2), columns=[" Column A ", " Column B "], index=range(3)
)
df
    Column A    Column B
0   -0.020580    0.461255
1   -1.251339   -1.173025
2   -0.445028   -0.658810
~~~

~~~python
[in]
df.columns.str.strip()

[out]
Index(['Column A', 'Column B'], dtype='object')
~~~

- Series.str.replace()
  : 특정 문자를 다른 문자로 대체함(공백문자 제거에 활용할 수 있음)
~~~python
s = pd.Series(["ab c", "c de ", np.nan, " f g h "], dtype="string")
s
0       ab c
1      c de
2       <NA>
3     f g h
~~~

~~~python
[in]
s.str.replace(' ','')

[out]
0     abc
1     cde
2    <NA>
3     fgh
~~~

- Series.str.cat()
  : series의 각 원소를 하나의 str로 합침
~~~python
df = pd.DataFrame({'ticker':['005930', '000829'],
                    'name':['samsung', 'dongsan']})
df
   ticker     name
0  005930  samsung
1  000829  dongsan
~~~

~~~python
[in]
df.apply(lambda row: row.str.cat(sep='&'), axis=1)

[out]
0    005930&samsung
1    000829&dongsan
~~~

- Series.str.contains(string/pattern, case=True/False, regex=True/False)  
  : case는 대소문자 구별여부, regex는 정규식 표현 여부임
~~~python
df
  col1 col2
0  1   apple
1  2   abcde
2  3   lelele
3  4   Ppa
4  5   xyzab
5  6   123
~~~

~~~python
[in]
con = df.col2.str.contains('pp', case=False, regex=False)
df.loc[con]

[out]
	col1	col2
0	1      	apple
3	4      	Ppa
~~~
~~~python
[in]
con = df.col2.str.contains('a+', case=False, regex=True)
df.loc[con]

[out]
	col1	col2
0	1      	apple
1	2      	abcde
3	4      	Ppa
4	5      	xyzab
~~~

- Series.str.extract() : 정규식으로 표현된 그룹을 추출하여 새로운 열로 반환
~~~python
[in]
df.col2.str.extract(r"(a+)")

[out]
	0
0	a
1	a
2	NaN
3	a
4	a
5	NaN
~~~

### **groupby**
---
- groupby + transform()
~~~python
[in]
df = DataFrame({'group_1': ['a', 'a', 'a', 'a', 'b'], 
                       'group_2': ['c', 'c', 'd', 'd','e'], 
                       'col': [1, np.NaN, 4, 5, 6]})
                    
df['count_col'] = df.groupby(['group_1', 'group_2']).col.transform('count')
df

[out]
	group_1	group_2	col	count_col
0	a	       c	1.0	       1
1	a	       c	NaN	       1
2	a	       d	4.0	       2
3	a	       d	5.0	       2
4	b	       e	6.0	       1
~~~
~~~python
[in]
df['sum_col'] = df.groupby(['group_1', 'group_2']).col.transform('sum')
df

[out]
	group_1	group_2	col	sum_col
0	a	       c	1.0    1.0
1	a	       c	NaN    1.0
2	a	       d	4.0    9.0
3	a	       d	5.0    9.0
4	b	       e	6.0    6.0
~~~
~~~python
[in]
df['max_col'] = df.groupby(['group_1', 'group_2']).col.transform('max')
df

[out]
	group_1	group_2	col	max_col
0	a	       c	1.0    1.0
1	a	       c	NaN    1.0
2	a	       d	4.0    5.0
3	a	       d	5.0    5.0
4	b	       e	6.0    6.0
~~~

- groupby + pct_change()
~~~python
[in]
df = pd.DataFrame({'country' : ['kor']*3 + ['jap']*3,
                    'value' : [100,105,109,100,101,100]})
                    
df['pct_change'] = df.groupby(['country']).value.pct_change()
df

[out]
  country value pct_change
0 kor     100   NaN
1 kor     105   0.050000
2 kor     109   0.038095
3 jap     100   NaN
4 jap     101   0.010000
5 jap     100  -0.009901
~~~

- groupby + pct_change() + transform() + cumprod()
~~~python
[in]
df = pd.DataFrame({'country' : ['kor']*3 + ['jap']*3,
                    'value' : [100,105,109,100,101,100]})
df['pct_change']=df.groupby(['country']).value.pct_change()
df['cumulativeReturn']=df.groupby(['country'])['pct_change'].transform(lambda x : x+1)
df['cumulativeReturn']=df.groupby(['country'])['cumulativeReturn'].cumprod()
df

# df.groupby(['country']).value.pct_change().transform(lambda x : x+1).cumprod()  -> 이렇게 하지 않도록 주의!

[out]
       country	value	cumulativeReturn
0	kor	       100	       NaN
1	kor	       105	       1.05
2	kor	       109	       1.09
3	jap	       100	       NaN
4	jap	       101	       1.01
5	jap	       100	       1.00
~~~
### **Reshaping**
- Melt
~~~python
# cheese
  first last  height  weight
0  John  Doe     5.5     130
1  Mary   Bo     6.0     15
~~~
~~~python
[in]
cheese.melt(id_vars=["first", "last"])

[out]
  first last variable  value
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
-------------------------------------------
[in]
cheese.melt(id_vars=["first", "last"], var_name="quantity")

[out]
  first last quantity  value
0  John  Doe   height    5.5
1  Mary   Bo   height    6.0
2  John  Doe   weight  130.0
3  Mary   Bo   weight  150.0
~~~

- Stack
~~~python
[in]
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df2 = df[:4]
df2

[out]
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
~~~
~~~python
[in]
stacked = df2.stack()
stacked

[out]
first  second   
bar    one     A   -0.727965
               B   -0.589346
       two     A    0.339969
               B   -0.693205
baz    one     A   -0.339355
               B    0.593616
       two     A    0.884345
               B    1.591431
dtype: float64
~~~
- unstack
~~~python
[in]
stacked.unstack()

[out]
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
~~~
~~~python
[in]
stacked.unstack(1)

[out]
second        one       two
first                      
bar   A -0.727965  0.339969
      B -0.589346 -0.693205
baz   A -0.339355  0.884345
      B  0.593616  1.591431
~~~
~~~python
[in]
stacked.unstack(0)

[out]
first          bar       baz
second                      
one    A -0.727965 -0.339355
       B -0.589346  0.593616
two    A  0.339969  0.884345
       B -0.693205  1.591431
~~~

### **Pivot Tables**
---

- df.pivot()
~~~python
# df
         date variable     value
0  2000-01-03        A  0.469112
1  2000-01-04        A -0.282863
2  2000-01-05        A -1.509059
3  2000-01-03        B -1.135632
4  2000-01-04        B  1.212112
5  2000-01-05        B -0.173215
6  2000-01-03        C  0.119209
7  2000-01-04        C -1.044236
8  2000-01-05        C -0.861849
9  2000-01-03        D -2.104569
10 2000-01-04        D -0.494929
11 2000-01-05        D  1.071804
----------------------------------------------
[in]
filtered = df[df["variable"] == "A"]
filtered

[out]
        date variable     value
0 2000-01-03        A  0.469112
1 2000-01-04        A -0.282863
2 2000-01-05        A -1.509059
----------------------------------------------
# much better way to represent the column "value"
[in]
pivoted = df.pivot(index="date", columns="variable", values="value")
pivoted

[out]
variable           A         B         C         D
date                                              
2000-01-03  0.469112 -1.135632  0.119209 -2.104569
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804
----------------------------------------------
[in]
df["value2"] = df["value"] * 2
pivoted = df.pivot(index="date", columns="variable")
pivoted

[out]
               value                                  value2                              
variable           A         B         C         D         A         B         C         D
date                                                                                      
2000-01-03  0.469112 -1.135632  0.119209 -2.104569  0.938225 -2.271265  0.238417 -4.209138
2000-01-04 -0.282863  1.212112 -1.044236 -0.494929 -0.565727  2.424224 -2.088472 -0.989859
2000-01-05 -1.509059 -0.173215 -0.861849  1.071804 -3.018117 -0.346429 -1.723698  2.143608
----------------------------------------------
[in]
pivoted["value2"]

[out]
variable           A         B         C         D
date                                              
2000-01-03  0.938225 -2.271265  0.238417 -4.209138
2000-01-04 -0.565727  2.424224 -2.088472 -0.989859
2000-01-05 -3.018117 -0.346429 -1.723698  2.143608
~~~


- pd.pivot_table()  
; While pivot() provides general purpose pivoting with various data types (strings, numerics, etc.), pandas also provides pivot_table() for pivoting with aggregation of numeric data.

~~~
- data: a DataFrame object.

- values: a column or a list of columns to aggregate.

- index: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table index. If an array is passed, it is being used as the same manner as column values.

- columns: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the pivot table column. If an array is passed, it is being used as the same manner as column values.

- aggfunc: function to use for aggregation, defaulting to numpy.mean.
~~~

~~~python
[in]
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
    }
)

[out]
        A  B    C         D         E          F
0     one  A  foo  0.341734 -0.317441 2013-01-01
1     one  B  foo  0.959726 -1.236269 2013-02-01
2     two  C  foo -1.110336  0.896171 2013-03-01
3   three  A  bar -0.619976 -0.487602 2013-04-01
4     one  B  bar  0.149748 -0.082240 2013-05-01
..    ... ..  ...       ...       ...        ...
19  three  B  foo  0.690579 -2.213588 2013-08-15
20    one  C  foo  0.995761  1.063327 2013-09-15
21    one  A  bar  2.396780  1.266143 2013-10-15
22    two  B  bar  0.014871  0.299368 2013-11-15
23  three  C  bar  3.357427 -0.863838 2013-12-15
----------------------------------------------
[in]
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])

[out]
C             bar       foo
A     B                    
one   A  1.120915 -0.514058
      B -0.338421  0.002759
      C -0.538846  0.699535
three A -1.181568       NaN
      B       NaN  0.433512
      C  0.588783       NaN
two   A       NaN  1.000985
      B  0.158248       NaN
      C       NaN  0.176180
----------------------------------------------
[in]
pd.pivot_table(df, values="D", index=["B"], columns=["A", "C"], aggfunc=np.sum)

[out]
A       one               three                 two          
C       bar       foo       bar       foo       bar       foo
B                                                            
A  2.241830 -1.028115 -2.363137       NaN       NaN  2.001971
B -0.676843  0.005518       NaN  0.867024  0.316495       NaN
C -1.077692  1.399070  1.177566       NaN       NaN  0.352360
----------------------------------------------
[in]
pd.pivot_table(
    df, values=["D", "E"],
    index=["B"],
    columns=["A", "C"],
    aggfunc=np.sum,
)

[out]
          D                                                           E                                                  
A       one               three                 two                 one               three                 two          
C       bar       foo       bar       foo       bar       foo       bar       foo       bar       foo       bar       foo
B                                                                                                                        
A  2.241830 -1.028115 -2.363137       NaN       NaN  2.001971  2.786113 -0.043211  1.922577       NaN       NaN  0.128491
B -0.676843  0.005518       NaN  0.867024  0.316495       NaN  1.368280 -1.103384       NaN -2.128743 -0.194294       NaN
C -1.077692  1.399070  1.177566       NaN       NaN  0.352360 -1.976883  1.495717 -0.263660       NaN       NaN  0.872482
~~~

### **Pandas Options**
---
- 출력포맷 변경하기
~~~python

import pandas as pd
pd.options.display.float_format = '{:.02f}'.format

#            date  funding  openCashValue
# 0    1995-05-02     0.00           0.00
# 1    1995-05-03     0.00           0.00
~~~
<br><br><br>


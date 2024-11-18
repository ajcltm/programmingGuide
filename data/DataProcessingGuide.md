#### 데이터 살펴보기
---
~~~python
import pandas as pd
from pathlib import Path

dir = Path.home().joinpath('Desktop', 'train.csv')
origin_data = pd.read_csv(dir)
data = origin_data[['Survived','Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
data
~~~

| |Age|Embarked|Fare|Parch|PassengerId|Pclass|Sex|SibSp|Survived|
|---|---|---|---|---|---|---|---|---|---|
|0|22.0|S|7.2500|0|1|3|male|1|0|
|1|38.0|C|71.2833|0|2|1|female|1|1|
|2|26.0|S|7.9250|0|3|3|female|0|1|
|3|35.0|S|53.1000|0|4|1|female|1|1|
|4|35.0|S|8.0500|0|5|3|male|0|0|
|...|...|...|...|...|...|...|...|...|...|

- 데이터 타입 확인하기
~~~python
data.info()
~~~

~~~
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 9 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Age          714 non-null    float64
 1   Embarked     889 non-null    object 
 2   Fare         891 non-null    float64
 3   Parch        891 non-null    int64  
 4   PassengerId  891 non-null    int64  
 5   Pclass       891 non-null    int64  
 6   Sex          891 non-null    object 
 7   SibSp        891 non-null    int64  
 8   Survived     891 non-null    int64  
dtypes: float64(2), int64(5), object(2)
memory usage: 62.8+
~~~

- 범주형 데이터 빈도 수 확인하기
~~~python
data['Survived'].value_counts()
~~~

~~~
0    549
1    342
Name: Survived, dtype: int64
~~~

- 그룹화해서 빈도 확인하기
~~~python
dead = data[data.loc[:, 'Survived']==0]['Pclass'].value_counts()
survived = data[data.loc[:, 'Survived']==1]['Pclass'].value_counts()
df = pd.DataFrame(data=[dead, survived], index = ['dead', 'survived'])
cols = df.columns
sorted_cols = list(cols)
sorted_cols.sort()
df[sorted_cols]
~~~

| |1|2|3|
|---|---|---|---|
|dead|80|97|372|
|survived|136|87|119|

~~~python
pd.crosstab(data.Survived, data.Pclass)
~~~

|Pclass|1|2|3|
|---|---|---|---|
|Survived||||
|0|80|97|372|
|1|136|87|119|


- 수치형 데이터 기초 통계 확인하기
~~~python
data.describe()
~~~

| |Survived|Pclass|Age|SibSp|Parch|Fare|
|---|---|---|---|---|---|---|
|count|891.000000|891.000000|714.000000|891.000000|891.000000|891.000000|
|mean|0.383838|2.308642|29.699118|0.523008|0.381594|32.204208|
|std|0.486592|0.836071|14.526497|1.102743|0.806057|49.693429|
|min|0.000000|1.000000|0.420000|0.000000|0.000000|0.000000|
|25%|0.000000|2.000000|20.125000|0.000000|0.000000|7.910400|
|50%|0.000000|3.000000|28.000000|0.000000|0.000000|14.454200|
|75%|1.000000|3.000000|38.000000|1.000000|0.000000|31.000000|
|max|1.000000|3.000000|80.000000|8.000000|6.000000|512.329200|

~~~python
data.loc[:, ['Age', 'Fare']].quantile([.1, .25, .5, .75, .9])
~~~

| |Age|Fare|
|---|---|---|
|0.10|14.000|7.5500|
|0.25|20.125|7.9104|
|0.50|28.000|14.4542|
|0.75|38.000|31.0000|
|0.90|50.000|77.9583|

- 범주형 데이터를 기준으로 그룹화해서 통계 확인하기
~~~python
data.groupby(['Survived', 'Pclass']).mean()
# count, sum, mean, median, var, std, min, max, prod, quantile
~~~

| ||Age|SibSp|Parch|Fare|
|---|---|---|---|---|---|
|Survived|Pclass|||||
|0|1|43.695312|0.287500|0.300000|64.684007|
| |2|33.544444|0.319588|0.144330|19.412328|
| |3|26.555556|0.672043|0.384409|13.669364|
|1|1|35.368197|0.492647|0.389706|95.608029|
| |2|25.901566|0.494253|0.643678|22.055700|
| |3|20.646118|0.436975|0.420168|13.694887|

~~~python
data.groupby(['Survived', 'Pclass']).agg(['mean', 'std', 'min', 'max'])
# count, sum, mean, median, var, std, min, max, prod, quantile, unique
~~~

| ||Age|   |   |   |SibSp|   |   |   |Parch|   |   |   |Fare|   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||mean|std|min|max|mean|std|min|max|mean|std|min|max|mean|std|min|max|
|Survived|Pclass|||||||||||||||||
|0|1|43.695312|15.284243|2.00|71.0|0.287500|0.555610|0|3|0.300000|0.700813|0|4|64.684007|60.662089|0.0000|263.0000|
||2|33.544444|12.151581|16.00|70.0|0.319588|0.550500|0|2|0.144330|0.432765|0|2|19.412328|15.307175|0.0000|73.5000|
||3|26.555556|12.334882|1.00|74.0|0.672043|1.504700|0|8|0.384409|0.914144|0|6|13.669364|12.118338|0.0000|69.5500|
|1|1|35.368197|13.760017|0.92|80.0|0.492647|0.632412|0|3|0.389706|0.690387|0|2|95.608029|85.286820|25.9292|512.3292|
||2|25.901566|14.837787|0.67|62.0|0.494253|0.644720|0|3|0.643678|0.820904|0|3|22.055700|10.853502|10.5000|65.0000|
||3|20.646118|11.995047|0.42|63.0|0.436975|0.829934|0|4|0.420168|0.807757|0|5|13.694887|10.692993|0.0000|56.4958

- 범주형 데이터 고유값 확인
~~~python
pd.DataFrame(data = data.apply(lambda col: col.unique().tolist(), axis=0), columns=['unique value'])
~~~

~~~
PassengerId    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14...
Survived                                                  [0, 1]
Pclass                                                 [3, 1, 2]
Name           [Braund, Mr. Owen Harris, Cumings, Mrs. John B...
Sex                                               [male, female]
Age            [22.0, 38.0, 26.0, 35.0, nan, 54.0, 2.0, 27.0,...
SibSp                                      [1, 0, 3, 4, 2, 5, 8]
Parch                                      [0, 1, 2, 5, 3, 4, 6]
Ticket         [A/5 21171, PC 17599, STON/O2. 3101282, 113803...
Fare           [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51....
Cabin          [nan, C85, C123, E46, G6, C103, D56, A6, C23 C...
Embarked                                          [S, C, Q, nan]
dtype: object
~~~

#### 데이터 필터
---

- 수치형 데이터 필터하기
~~~python
data[(data.loc[:, 'Age']>=70) | (data.loc[:, 'Age']<1)]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|78|1|2|male|0.83|0|2|29.0000|S|
|96|0|1|male|71.00|0|0|34.6542|C|
|116|0|3|male|70.50|0|0|7.7500|Q|
|305|1|1|male|0.92|1|2|151.5500|S|
|469|1|3|female|0.75|2|1|19.2583|C|
|493|0|1|male|71.00|0|0|49.5042|C|
|630|1|1|male|80.00|0|0|30.0000|S|
|644|1|3|female|0.75|2|1|19.2583|C|
|672|0|2|male|70.00|0|0|10.5000|S|
|745|0|1|male|70.00|1|1|71.0000|S|
|755|1|2|male|0.67|1|1|14.5000|S|
|803|1|3|male|0.42|0|1|8.5167|C|
|831|1|2|male|0.83|1|1|18.7500|S|
|851|0|3|male|74.00|0|0|7.7750|S|

- 범주형 데이터 필터하기
~~~python
data[(data.loc[:, 'Sex'] == 'male') & (data.loc[:, 'Pclass']==2) & (data.loc[:, 'Embarked'] == 'Q')]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|626|0|2|male|57.0|0|0|12.35|Q|

~~~python
origin_data.loc[origin_data['Name'].str.contains(r'(Mrs.)')].head()
~~~

| |Name|Age|
|---|---|---|
|1|Cumings, Mrs. John Bradley (Florence Briggs Th...|38.0|
|3|Futrelle, Mrs. Jacques Heath (Lily May Peel)|35.0|
|8|Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)|27.0|
|9|Nasser, Mrs. Nicholas (Adele Achem)|14.0|
|15|Hewlett, Mrs. (Mary D Kingcome)|55.0|

- 여러값 동시에 필터하기
~~~python
data[data.loc[:, 'Age'].isin([60, 70, 80])]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|366|1|1|female|60.0|1|0|75.25|C|
|587|1|1|male|60.0|1|1|79.20|C|
|630|1|1|male|80.0|0|0|30.00|S|
|672|0|2|male|70.0|0|0|10.50|S|
|684|0|2|male|60.0|1|1|39.00|S|
|694|0|1|male|60.0|0|0|26.55|S|
|745|0|1|male|70.0|1|1|71.00|S|

#### 데이터 정상화
---
- 데이터 타입 변경
~~~python
data = data.astype({'Survived':'str', 'SibSp':'float'})
data.info()
~~~

~~~
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 8 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Survived  891 non-null    object 
 1   Pclass    891 non-null    int64  
 2   Sex       891 non-null    object 
 3   Age       714 non-null    float64
 4   SibSp     891 non-null    float64
 5   Parch     891 non-null    int64  
 6   Fare      891 non-null    float64
 7   Embarked  889 non-null    object 
dtypes: float64(3), int64(2), object(3)
memory usage: 55.8+ KB
~~~

- 범주형 데이터로 변환
~~~python
train_data.loc[:, 'Survived'] = train_data.Survived.astype('category')
train_data.loc[:, 'Pclass'] = train_data.Pclass.astype('category')
train_data.loc[:, 'Sex'] = train_data.Sex.astype('category')
train_data.loc[:, 'Embarked'] = train_data.Embarked.astype('category')
train_data.info()

# 요인 순서 변경
# train_data.Embarked.cat.set_categories(['S', 'Q', 'C'])
~~~

~~~
<class 'pandas.core.frame.DataFrame'>
Int64Index: 891 entries, 1 to 891
Data columns (total 11 columns):
 #   Column    Non-Null Count  Dtype   
---  ------    --------------  -----   
 0   Survived  891 non-null    category
 1   Pclass    891 non-null    category
 2   Name      891 non-null    object  
 3   Sex       891 non-null    category
 4   Age       714 non-null    float64 
 5   SibSp     891 non-null    int64   
 6   Parch     891 non-null    int64   
 7   Ticket    891 non-null    object  
 8   Fare      891 non-null    float64 
 9   Cabin     204 non-null    object  
 10  Embarked  889 non-null    category
dtypes: category(4), float64(2), int64(2), object(3)
memory usage: 59.7+ KB
~~~

- 수치형 데이터를 범주형 데이터로 분할
~~~python
import numpy as np
age_cat = pd.cut(data['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, np.inf] , labels=[0, 1, 2, 3, 4, 5, 6, 7])
temp_df = data.assign(Age_cat = age_cat)
temp_df[temp_df.loc[:, 'Age'].isin([10,55,74])].loc[:, ['Age', 'Age_cat']].sort_values('Age_cat')
~~~

| |Age|Age_cat|
|---|---|---|
|419|10.0|0|
|819|10.0|0|
|15|55.0|5|
|492|55.0|5|
|851|74.0|7|

- 범주형 데이터를 수치형 데이터로 변환
~~~python
data = data.replace({'Sex': {'male':0, 'female':1}})
data
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|
|0|0|3|0|22.0|1|0|7.2500|S|
|1|1|1|1|38.0|1|0|71.2833|C|
|2|1|3|1|26.0|0|0|7.9250|S|
|3|1|1|1|35.0|1|0|53.1000|S|
|4|0|3|0|35.0|0|0|8.0500|S|

~~~python
one_hot_df = pd.get_dummies(data['Embarked'])
pd.concat([data, one_hot_df], axis=1)[['Embarked','S', 'C', 'Q']]
~~~

| |Embarked|S|C|Q|
|---|---|---|---|---|
|0|S|1|0|0|
|1|C|0|1|0|
|2|S|1|0|0|
|3|S|1|0|0|
|4|S|1|0|0|
|...|...|...|...|...|
|886|S|1|0|0|
|887|S|1|0|0|
|888|S|1|0|0|
|889|C|0|1|0|
|890|Q|0|0|1|


- 결측치 처리
- 결측치 확인
~~~python
data.isna().head(6)  # data.isnull()과 동일함 
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|0|False|False|False|False|False|False|False|False|
|1|False|False|False|False|False|False|False|False|
|2|False|False|False|False|False|False|False|False|
|3|False|False|False|False|False|False|False|False|
|4|False|False|False|False|False|False|False|False|
|5|False|False|False|True|False|False|False|False|

~~~python
data.isna().sum()
~~~

~~~
Survived      0
Pclass        0
Sex           0
Age         177
SibSp         0
Parch         0
Fare          0
Embarked      2
dtype: int64
~~~

~~~python
data[data.loc[:, 'Age'].isna()]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|5|0|3|0|NaN|0|0|8.4583|Q|
|17|1|2|0|NaN|0|0|13.0000|S|
|19|1|3|1|NaN|0|0|7.2250|C|
|26|0|3|0|NaN|0|0|7.2250|C|
|28|1|3|1|NaN|0|0|7.8792|Q|
|...|...|...|...|...|...|...|...|...|
|859|0|3|0|NaN|0|0|7.2292|C|
|863|0|3|1|NaN|8|2|69.5500|S|
|868|0|3|0|NaN|0|0|9.5000|S|
|878|0|3|0|NaN|0|0|7.8958|S|
|888|0|3|1|NaN|1|2|23.4500|S|

- 결측치 삭제

~~~python
data_droped = data.dropna() # 컬럼 중에 결측값이 있으면 해당행 제거
# data.dropna(how='all') 모든 컬럼의 값이 결측값인 경우에만 해당행 제거 (default: how='any')
# data.dropna(subset=['Age']) 특정 컬럼 중에 결측값이 있으면 해당행 제거
data_droped.isna().sum()
~~~

~~~
Survived    0
Pclass      0
Sex         0
Age         0
SibSp       0
Parch       0
Fare        0
Embarked    0
dtype: int64
~~~

- 결측치 대체
~~~python
na_index = data[data.loc[:, 'Embarked'].isna()].index
na_filled_df = data.fillna({'Embarked':'S'})
na_filled_df.iloc[na_index]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|61|1|1|1|38.0|0|0|80.0|NaN|
|829|1|1|1|62.0|0|0|80.0|NaN|

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|61|1|1|1|38.0|0|0|80.0|S|
|829|1|1|1|62.0|0|0|80.0|S|

~~~python
na_index = data[data.loc[:, 'Age'].isna()].index
data_age_filled = data.assign(age_mean = data.groupby(['Pclass', 'Sex'])['Age'].transform('mean')) # mean, median, min, max 등 상황에 따라서 적절한 통계치 사용
data_age_filled = data_age_filled.fillna({'Age':data_age_filled['age_mean']})
data_age_filled.loc[na_index, ['Pclass', 'Sex', 'Age', 'age_mean']]
~~~

| |Pclass|Sex|Age|age_mean|
|---|---|---|---|---|
|5|3|0|26.507589|26.507589|
|17|2|0|30.740707|30.740707|
|19|3|1|21.750000|21.750000|
|26|3|0|26.507589|26.507589|
|28|3|1|21.750000|21.750000|
|...|...|...|...|...|
|859|3|0|26.507589|26.507589|
|863|3|1|21.750000|21.750000|
|868|3|0|26.507589|26.507589|
|878|3|0|26.507589|26.507589|
|888|3|1|21.750000|21.750000|

- 중복값 처리
- 중복값 확인
~~~python
data[~data.duplicated(['SibSp'])].sort_values('SibSp')
# data.duplicated(['SibSp'], keep='last') 
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|2|1|3|1|26.0|0|0|7.925|S|
|0|0|3|0|22.0|1|0|7.250|S|
|38|0|3|1|18.0|2|0|18.000|S|
|7|0|3|0|2.0|3|1|21.075|S|
|16|0|3|0|2.0|4|1|29.125|Q|
|59|0|3|0|11.0|5|2|46.900|S|
|159|0|3|0|NaN|8|2|69.550|S|

- 중복값 제거
~~~python
data.drop_duplicates(['SibSp']) # option : keep= 'first' or 'last' or 'false'
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|
|---|---|---|---|---|---|---|---|---|
|0|0|3|0|22.0|1|0|7.250|S|
|2|1|3|1|26.0|0|0|7.925|S|
|7|0|3|0|2.0|3|1|21.075|S|
|16|0|3|0|2.0|4|1|29.125|Q|
|38|0|3|1|18.0|2|0|18.000|S|
|59|0|3|0|11.0|5|2|46.900|S|
|159|0|3|0|NaN|8|2|69.550|S|

- 이상치 등 특정 조건의 여러 데이터 변경
~~~python
temp_data = data.copy(deep=True) # 원본을 참조하지 않는 새로운 객체 생성
ix_more_than_70 = temp_data[temp_data.loc[:, 'Age']>70][['Age']].index
temp_data.loc[temp_data['Age']>70, 'Age'] = 70
temp_data.iloc[ix_more_than_70][['Age']]
~~~

| |Age|
|---|---|
|96|71.0|
|116|70.5|
|493|71.0|
|630|80.0|
|851|74.0|

| |Age|
|---|---|
|96|70.0|
|116|70.0|
|493|70.0|
|630|70.0|
|851|70.0|

- 범주형 데이터 공백 제거
~~~python
origin_data['Name'].str.strip() # 양쪽 공백 제거
# origin_data['Name'].str.lstrip() # 왼쪽 앞 공백 제거
# origin_data['Name'].str.rstrip() # 오른쪽 뒤 공백 제거
~~~

~~~
0                                Braund, Mr. Owen Harris
1      Cumings, Mrs. John Bradley (Florence Briggs Th...
2                                 Heikkinen, Miss. Laina
3           Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                               Allen, Mr. William Henry
   ...                        
886                                Montvila, Rev. Juozas
887                         Graham, Miss. Margaret Edith
888             Johnston, Miss. Catherine Helen "Carrie"
889                                Behr, Mr. Karl Howell
890                                  Dooley, Mr. Patrick
Name: Name, Length: 891, dtype: object
~~~

#### 데이터 구조변경
---
- stack
~~~python
unstacked_table = pd.crosstab(data['Survived'], data['SibSp'])
unstacked_table.stack().reset_index().rename(columns={0:'values'})
~~~

|SibSp|0|1|2|3|4|5|8|
|---|---|---|---|---|---|---|---|---|
|Survived||||||||
|0|398|97|15|12|15|5|7|
|1|210|112|13|4|3|0|0|

| |Survived|SibSp|values|
|---|---|---|---|
|0|0|0|398|
|1|0|1|97|
|2|0|2|15|
|3|0|3|12|
|4|0|4|15|
|5|0|5|5|
|6|0|8|7|
|7|1|0|210|
|8|1|1|112|
|9|1|2|13|
|10|1|3|4|
|11|1|4|3|
|12|1|5|0|
|13|1|8|0|

- melt
~~~python
unmelted = pd.crosstab(data['Survived'], data['Embarked']).reset_index()
unmelted.columns.name=None
unmelted
pd.melt(unmelted, id_vars=['Survived'])
~~~

|Survived|C|Q|S|
|---|---|---|---|
|0|0|75|47|427|
|1|1|93|30|217|

| |Survived|variable|value|
|---|---|---|---|
|0|0|C|75|
|1|1|C|93|
|2|0|Q|47|
|3|1|Q|30|
|4|0|S|427|
|5|1|S|217|

#### 개별 데이터 생성
---
- 표준화
~~~python
temp_df = data.assign(Age_zscore = (data['Age'] - data['Age'].mean()) / data['Age'].std())
temp_df.loc[:, ['Age', 'Age_zscore']].head()
~~~

| |Age|Age_zscore|
|---|---|---|
|0|22.0|-0.530005|
|1|38.0|0.571430|
|2|26.0|-0.254646|
|3|35.0|0.364911|
|4|35.0|0.364911|

- 정규화
~~~python
temp_df = data.assign(Age_norm = (data['Age'] - data['Age'].min()) / (data['Age'].max() - data['Age'].min()))
temp_df.loc[:, ['Age', 'Age_norm']].head()
~~~

| |Age|Age_norm|
|---|---|---|
|0|22.0|0.271174|
|1|38.0|0.472229|
|2|26.0|0.321438|
|3|35.0|0.434531|
|4|35.0|0.434531|

- 그룹화된 값 생성
~~~python
temp_df = data.assign(Age_median = data.groupby(['Survived', 'Sex'])['Age'].transform('median'))
temp_df.loc[:, ['Survived', 'Sex', 'Age', 'Age_median']].head()
~~~

| |Survived|Sex|Age|Age_median|
|---|---|---|---|---|
|0|0|0|22.0|29.0|
|1|1|1|38.0|28.0|
|2|1|1|26.0|28.0|
|3|1|1|35.0|28.0|
|4|0|0|35.0|29.0|

- 순위 데이터 생성
~~~python
temp_df = data.assign(Age_rank = data.loc[:, 'Age'].rank(ascending=False, method='min'))
temp_df.loc[:, ['Age', 'Age_rank']].sort_values('Age_rank').head(7)

# - 평균(method='average') : 동점 관측치 간의 그룹 내 평균 순위 부여 (default 설정)
# - 최소값(method='min') : 동점 관측치 그룹 내 최소 순위 부여
# - 최대값(method='max') : 동점 관측치 그룹 내 최대 순위 부여
# - 첫번째 값 (method='first') : 동점 관측치 중에서 데이터 상에서 먼저 나타나는 관측치부터 순위 부여
# - 조밀하게 (method='dense') : 최소값('min')과 같은 방법으로 순위부여하나, 'min'과는 다르게 그룹 간 순위가 '1'씩 증가함 (like ‘min’, but rank always increases by 1 between groups) 
~~~

| |Age|Age_rank|
|---|---|---|
|630|80.0|1.0|
|851|74.0|2.0|
|96|71.0|3.0|
|493|71.0|3.0|
|116|70.5|5.0|
|672|70.0|6.0|
|745|70.0|6.0|

- 이상치 여부 확인 데이터 생성
~~~python
ix_70 = data.loc[data.Age > 50, 'Age'].index
q1 = data.loc[:, 'Age'].quantile(.25)
q3 = data.loc[:, 'Age'].quantile(.75)
IQR = q3 - q1
print(q3, q1)
print(q3 + IQR*3)
print(q1 - IQR*3)

def check_outlier(x) :
    if (x > q3 + 1.5 * IQR) or (x < q1 - 1.5 * IQR):
        return True
    else:
        return False

temp_df = data.assign(Outlier= data.Age.apply(lambda x : check_outlier(x)))
temp_df.loc[temp_df['Outlier']]
~~~

| |Survived|Pclass|Sex|Age|SibSp|Parch|Fare|Embarked|Outlier|
|---|---|---|---|---|---|---|---|---|---|
|33|0|2|0|66.0|0|0|10.5000|S|True|
|54|0|1|0|65.0|0|1|61.9792|C|True|
|96|0|1|0|71.0|0|0|34.6542|C|True|
|116|0|3|0|70.5|0|0|7.7500|Q|True|
|280|0|3|0|65.0|0|0|7.7500|Q|True|
|456|0|1|0|65.0|0|0|26.5500|S|True|
|493|0|1|0|71.0|0|0|49.5042|C|True|
|630|1|1|0|80.0|0|0|30.0000|S|True|
|672|0|2|0|70.0|0|0|10.5000|S|True|
|745|0|1|0|70.0|1|1|71.0000|S|True|
|851|0|3|0|74.0|0|0|7.7750|S|True|

- 데이터 간 조합

~~~python
temp_df = data.assign(Family = data.loc[:, ['SibSp', 'Parch']].apply(lambda row : row[0] + row[1], axis=1))
temp_df.loc[:, ['SibSp', 'Parch', 'Family']].iloc[12:20]
~~~

| |SibSp|Parch|Family|
|---|---|---|---|
|12|0|0|0|
|13|1|5|6|
|14|0|0|0|
|15|0|0|0|
|16|4|1|5|
|17|0|0|0|
|18|1|0|1|
|19|0|0|0|

- 범주형 데이터 추출하기
~~~python
origin_data_temp = origin_data.assign(Part_of_name = origin_data['Name'].str[2:5])
origin_data_temp.loc[:, ['Name', 'Part_of_name']].head()
~~~

| |Name|Part_of_name|
|---|---|---|
|0|Braund, Mr. Owen Harris|aun|
|1|Cumings, Mrs. John Bradley (Florence Briggs Th...|min|
|2|Heikkinen, Miss. Laina|ikk|
|3|Futrelle, Mrs. Jacques Heath (Lily May Peel)|tre|
|4|Allen, Mr. William Henry|len|

- 범주형 데이터 분할
~~~python
origin_data['Name'].str.split(', ', expand=True).head()
~~~

| |0|1|
|---|---|---|
|0|Braund|Mr. Owen Harris|
|1|Cumings|Mrs. John Bradley (Florence Briggs Thayer)|
|2|Heikkinen|Miss. Laina|
|3|Futrelle|Mrs. Jacques Heath (Lily May Peel)|
|4|Allen|Mr. William Henry|

- 정규식을 활요한 범주형 데이터 추출 
~~~python
temp_df = origin_data.assign(Name_char = origin_data['Name'].str.extract('([a-zA-Z]+)\.'))
temp_df.loc[:, ['Name', 'Name_char']].head()
~~~

| |Name|Name_char|
|---|---|---|
|0|Braund, Mr. Owen Harris|Mr|
|1|Cumings, Mrs. John Bradley (Florence Briggs Th...|Mrs|
|2|Heikkinen, Miss. Laina|Miss|
|3|Futrelle, Mrs. Jacques Heath (Lily May Peel)|Mrs|
|4|Allen, Mr. William Henry|Mr|
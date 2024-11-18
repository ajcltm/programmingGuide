- Scatter plots (x: Numerical #1, y: Numerical #2)
~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker', style='smoker', ax=ax)
plt.show()
~~~

- Line plots (x: Categorical - ordinal#1, y: Numerical #1)
~~~python
tips_by_day = tips.groupby('day').mean().reset_index()
f, ax = plt.subplots(figsize=(4,4))
sns.lineplot(data=tips_by_day, x='day', y='total_bill', ax=ax)
plt.show()
~~~

- Bar plots (x: Categorical #1, y: Numerical #1)
	- Numerical #1 is often the count of Categorical #1.
~~~python
f, ax = plt.subplots(figsize=(3,3))
sns.countplot(data=tips, x='day', hue='sex', ax=ax)
plt.show()
~~~

~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.barplot(data=tips, x='day', y='tip', estimator='count', hue='sex', errorbar=None ,ax=ax)
plt.show()
~~~

~~~python
tips_by_day = tips.groupby('day').count().reset_index()
tips_by_male = tips.loc[tips.sex=='Male'].groupby('day').count().reset_index()

f, ax = plt.subplots(figsize=(3,3))
sns.barplot(data=tips_by_day, x='day', y='sex', color='darkblue', ax=ax)
sns.barplot(data=tips_by_male, x='day', y='sex', color='lightblue', ax=ax)
plt.show()
~~~

~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.barplot(data=tips, x='day', y='tip', estimator='mean', hue='sex', errorbar=None ,ax=ax)
plt.show()
~~~

- Histogram (x: Numerical #1, y: Numerical #2) 
	- Numerical #1 is combined into groups (converted to a categorical variable), and Numerical #2 is usually the count of this categorical variable.
~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.histplot(data=tips, x='total_bill', hue='sex', multiple='stack', ax=ax)
plt.show()
~~~

- Kernel density plot (x: Numerical #1, y: Numerical #2)
	- Numerical #2 is the frequency of Numerical #1.
~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.kdeplot(data=tips, x='total_bill', hue='sex', multiple='stack', ax=ax)
plt.show()
~~~

- 2-D kernel density plot (x: Numerical #1, y: Numerical #2, color: Numerical #3)
	- Numerical #3 is the joint frequency of Numerical #1 and Numerical #2.
~~~python

~~~

- Box plot (x: Categorical #1, y: Numerical #1, marks: Numerical #2)
	-  Box plot shows the statistics of each value in Categorical #1 so we’ll get an idea of the distribution in the other variable. y-value: the value for the other variable; marks: showing how these values are distributed (range, Q1, median, Q3).
~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.boxplot(data=tips, x='day' , y='tip', hue='sex' , ax=ax)
plt.show()
~~~

- Violin plot (x: Categorical #1, y: Numerical #1, Width/Mark: Numerical #2)
	- Violin plot is sort of similar to box plot but it shows the distribution better.
~~~python
f, ax = plt.subplots(figsize=(4,4))
sns.violinplot(data=tips, x='day' , y='total_bill', hue='sex', split=True , ax=ax)
plt.show()
~~~

- Heat map (x: Categorical #1, y: Categorical #2, Color: Numerical #1)
		- Numerical #1 could be the count for Categorical #1 and Categorical #2 jointly, or it could be other numerical attributes for each value in the pair (Categorical #1, Categorical #2).
~~~python
day_time_table = pd.crosstab(tips.day, tips.time)

f, ax = plt.subplots(figsize=(4,4))
sns.heatmap(day_time_table, annot=True, linewidth=.5, cmap='crest', ax=ax)
plt.show()
~~~

- null check with Heat map
~~~python
f, ax = plt.subplots(figsize=(4, 8))
sns.heatmap(data.isna(), ax=ax)
~~~

- Subplots
~~~python
f, ax = plt.subplots(1, 2,figsize=(8, 4))
sns.barplot(data=tips, x='day', y='tip', estimator='count', hue='sex', errorbar=None ,ax=ax[0])
sns.heatmap(day_time_table, annot=True, linewidth=.5, cmap='crest', ax=ax[1])
plt.show()
~~~

- Overlay plots
~~~python
tips_male = tips.loc[tips.sex=='Male'].groupby('day').mean()
tips_female = tips.loc[tips.sex=='Female'].groupby('day').mean()
f, ax = plt.subplots(figsize=(4, 4))
sns.lineplot(data=tips_male, x='day', y='total_bill', ax=ax)
sns.lineplot(data=tips_female, x='day', y='total_bill', ax=ax)
plt.show()
~~~

~~~python
f, ax1 = plt.subplots(figsize=(4, 4))
ax2 = ax1.twinx()
sns.barplot(data=tips, x='day', y='tip', estimator='mean', errorbar=None, color='lightblue', ax=ax1)
sns.lineplot(data=tips, x='day', y='total_bill', err_style=None, color='darkblue', linewidth=3, ax=ax2)
ax2.grid(None)
plt.show()
~~~
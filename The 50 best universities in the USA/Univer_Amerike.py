import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import redirect_stdout

# THESE DATA ARE MAINLY SUITABLE FOR GRAPHIC CREATION, NOT FOR MACHINE LEARNING!!!!
# there is not enough data for machine learning
df = pd.read_csv('50_Universities_in_America.csv')
# primary analysis
he_text = df.head(10)
des_text = df.describe()
ln_text = len(df)
colu_text = df.columns.tolist()
# Data validation
dt_text = df.dtypes
dup_text = df.duplicated().sum()
isn_text = df.isna().sum()
# Visualization
plt.figure(figsize=(8, 5))
plt.xticks(fontsize=8, rotation=90)
sns.barplot(data=df.sort_values('Employment_Rate'), x='University_Name', y='Employment_Rate', hue='University_Name',
            palette='coolwarm', legend=False)# bar chart
plt.title('University rankings')
plt.xlabel('The names of universities')
plt.ylabel('University ranking')
plt.savefig('Graphs/1_gist_University_Ranking.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5)) # scatter plot
plt.xticks(fontsize=8, rotation=90)
sns.scatterplot(data=df.sort_values('Employment_Rate'), x='University_Name', y='Employment_Rate',
                c=df['Employment_Rate'], cmap='viridis')
plt.title('University ranking')
plt.xlabel('The names of universities')
plt.ylabel('University ranking')
plt.savefig('Graphs/2_University_rating.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5))
plt.xticks(fontsize=8, rotation=90)
sns.barplot(data=df.sort_values('Founded_Year'), x='University_Name', y='Founded_Year', hue='University_Name',
            palette='coolwarm', legend=False)
plt.title('The years when the universities were founded.')
plt.xlabel('The names of universities')
plt.ylabel('Year of establishment')
plt.savefig('Graphs/3_Year_of_founding_of_universities.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5)) # research impact index
plt.xticks(fontsize=8, rotation=90)
sns.scatterplot(data=df.sort_values('Research_Impact_Score'), x='University_Name',
                y='Research_Impact_Score', c=df['Research_Impact_Score'], cmap='viridis')
plt.title('The impact of research')
plt.xlabel('The names of the universities')
plt.ylabel('research index')
plt.savefig('Graphs/4_the_impact_of_research.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5)) # employment in unique
plt.xticks(fontsize=8, rotation=90)
sns.barplot(data=df.sort_values('Employment_Rate'), x='University_Name', y='Employment_Rate',
            hue='University_Name', palette='coolwarm', legend=False)
plt.title('Employment')
plt.xlabel('The names of universities')
plt.ylabel('Employment')
plt.savefig('Graphs/5_employment.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5))# Comparison of employment by type of institution
plt.xticks(fontsize=8, rotation=90)
sns.barplot(data=df.sort_values('Employment_Rate'), x='Institution_Type', y='Employment_Rate',
            hue='Employment_Rate', palette='coolwarm', legend=False)
plt.title('Comparison of employment by type of institution')
plt.xlabel('Type of institute')
plt.ylabel('Employment')
plt.savefig('Graphs/6_employment_by_type_of_institution.png', dpi=300, bbox_inches='tight')
plt.close()

# We are setting the Seaborn style.
sns.set_theme(style="whitegrid")
# Aggregating the data: summing or averaging Employment_Rate by Institution_Type
# Option 1: sum (if Employment_Rate is the number of employed individuals)
employment_summary = df.groupby('Institution_Type')['Employment_Rate'].sum()
# We obtain the data for construction
labels = employment_summary.index.tolist()  # ['Private', 'Public']
sizes = employment_summary.values.tolist() # [meaning for Private, meaning for Public]
colors = sns.color_palette("coolwarm", 2)
plt.figure(figsize=(8, 5))
plt.pie(x=sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors, explode=[0.05, 0.03],
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title('Employment comparison: private vs public institutions', fontsize=14, pad=20)
plt.axis('equal')
plt.savefig('Graphs/7_Employment_comparison_private_vs_public_institutions.png', dpi=300, bbox_inches='tight')
plt.close()

with open('Report/Report_university', 'w', encoding='UTF-8') as f:
    with redirect_stdout(f):
        print('<<< Primary data analysis >>>')
        print('\n Output of the first 10 lines:')
        print(he_text)
        print('\nSummary of data types:')
        print(df.info())
        print('\nStatistical summary of numerical columns:')
        print(des_text)
        print('\nList of column names:')
        print(colu_text)
        print('\n<<< Data validation >>>')
        print('\nData types:')
        print(dt_text)
        print('\nData duplicates:')
        print(dup_text)
        print('\nThe number of missing values')
        print(isn_text)

# df.to_csv('50_Universities_in_America.csv', index=False)
print('All reports are saved in the “Reports” folder..\nAll graphics are saved in the “Graphs” folder...')

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    mark1=(df['education']=='Bachelors')
    percentage_bachelors = round(((len(df[mark1])/len(df['education']))*100),1)
   
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    mark2=(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    #mark3=(df['education']!='Bachelors') | (df['education']!='Masters') | (df['education']!='Doctorate')
    higher_education = df[mark2]
    #print(higher_education['education'].head())
    lower_education = df.loc[(df['education']!='Bachelors')]
    lower_education=lower_education.loc[(lower_education['education']!='Masters')]
    lower_education=lower_education.loc[(lower_education['education']!='Doctorate')]
    #print(lower_education['education'].value_counts())

    # percentage with salary >50K
    mark4=higher_education['salary']=='>50K'
    mark5=lower_education['salary']=='>50K'
    higher_education_rich = round(((len(higher_education[mark4])/len(higher_education['salary']))*100),1)
    lower_education_rich = round(((len(lower_education[mark5])/len(lower_education['salary']))*100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
  

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mark6=(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')
    num_min_workers = len(df[(df['hours-per-week']==min_work_hours)])

    rich_percentage = ((len(df[mark6]))/(num_min_workers)*100)
  

    # What country has the highest percentage of people that earn >50K?
    df_country1=df.loc[(df['salary']=='<=50K')]
    df_country2=df.loc[(df['salary']=='>50K')]
    less_than_50k=df_country1['native-country'].value_counts()
    
    more_than_50k=df_country2['native-country'].value_counts()
    
    country_earn={}

   
    for key, value in  more_than_50k.items():
      for k,v in less_than_50k.items():
        if key==k:
          earn=round(value/(value+v)*100,1)
          country_earn[key]=earn
          
      
    
    highest_earning_country =max(country_earn, key=country_earn.get)
    
    
    highest_earning_country_percentage = max(country_earn.values())

    # Identify the most popular occupation for those who earn >50K in India.
    df_India=df[((df['native-country']=='India') & (df['salary']=='>50K'))]
    top_IN_occupation = df_India['occupation'].value_counts().index[0]
    print(top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df = df.dropna()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    men = df[df["sex"] == "Male"]
    average_age_men = men["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df["education"] == "Bachelors"]) / len(df) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # making new array for true series of higher education for clarity
    highEd = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lowerEd = ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = highEd.sum()
    lower_education = lowerEd.sum()

    # percentage with salary >50K
    higher_education_rich = round(((df[highEd]["salary"] == '>50K').sum() / higher_education * 100),1)
    lower_education_rich = round(((df[~highEd]["salary"] == '>50K').sum() / lower_education * 100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min().round(1)



    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    #making a dataframe of those who work the min work hours:
    minHoursPeople = df[df["hours-per-week"] == df["hours-per-week"].min()]

    rich_percentage = ((minHoursPeople["salary"] == '>50K').sum() / len(minHoursPeople) * 100).round(1)

    # What country has the highest percentage of people that earn >50K?

        #making a new series of countries with highest percentage of high earners
    percentageHighEarningCountries = df[df["salary"] == '>50K']["native-country"].value_counts() / df["native-country"].value_counts() * 100
    percentageHighEarningCountries.sort_values(ascending=False, inplace=True)
    
    
    highest_earning_country = percentageHighEarningCountries.index[0]

    highest_earning_country_percentage = percentageHighEarningCountries.iloc[0].round(1)

    # Identify the most popular occupation for those who earn >50K in India.

    #dataframe for those in india and earn more than 50k
    richIndians = df[(df["native-country"] == 'India') & (df["salary"] == '>50K')]

    top_IN_occupation = richIndians['occupation'].value_counts().sort_values().index[-1]

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


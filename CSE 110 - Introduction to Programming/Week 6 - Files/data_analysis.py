"""
Load the dataset in your Python program
Iterate through the data line by line
Split each line into parts
Find the lowest value for life expectancy and the highest value for life expectancy in the dataset, 
and display both values. 
(Note that at this point, you just need the value for this, 
not the year and the country for that value.)
User can type in a country, then show the minimum, maximum, 
and average life expectancy for that country including the year.
"""
with open("life-expectancy.csv") as file:
    # move to the next line of the file
    next(file)
    # declaring the variable to use 
    max = 0
    min = 99999999
    max_interest = 0
    min_interest = 99999999
    sum = 0
    count = 0
    user_max_country = 0
    user_min_country = 999999
    user_sum_country = 0
    user_count_country = 0
    
    interest = int(input("Enter the year of interest: "))
    user_country = input("\nWhat country did you want to check the life expectancy: ")
    for line in file:
        clean_line = line.strip()
        data = clean_line.split(",")
        country = data[0]
        year = int(data[2])
        life_expectancy = float(data[3])
        # calculating the maximum life expectancy in the dataset
        if max < life_expectancy:
            max = life_expectancy
            max_country = country
            max_year = year
        # calculating the minimum life expectancy in the dataset
        if min > life_expectancy:
            min = life_expectancy
            min_country = country
            min_year = year
        
        # calculating the maximum and minimum life expectancy in the year the user choose
        if interest == year:
            if max_interest < life_expectancy:
                max_interest = life_expectancy
                country_interest_max = country
            if min_interest > life_expectancy:
                min_interest = life_expectancy
                country_interest_min = country
            sum += life_expectancy
            count += 1
        # calculating the maximum and minimum life expectancy for the user chosen country
        if user_country.lower() == country.lower():
            if user_max_country < life_expectancy:
                user_max_country = life_expectancy
                user_max_year_country = year
            if user_min_country > life_expectancy:
                user_min_country = life_expectancy
                user_min_year_country = year
            user_sum_country += life_expectancy
            user_count_country += 1
        
    average = sum /count
    print(f"\nThe overall max life expectancy is: {max} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min} from {min_country} in {min_year}")

    print(f"\nFor the year {interest}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {country_interest_max} with {max_interest}")
    print(f"The min life expectancy was in {country_interest_min} with {min_interest}")

        
    user_average_country = user_sum_country / user_count_country
    print(f"\nFor the country '{user_country.capitalize()}:'")
    print(f"The average life expectancy {user_average_country:.2f}")
    print(f"The max life expectancy was {user_max_country} with {user_max_year_country}")
    print(f"The min life expectancy was in {user_min_country} with {user_min_year_country}")


#TASK7: Run Query on the database and show output on streamlit
    
import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# MySQL Connection Details
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='guvi',
    )

cursor = connection.cursor()

#sample query to get a count of records in the table
query = "Select count(1) from guvi.census"

cursor.execute(query)

records = cursor.fetchall()

for record in records:
    print(record)


df = pd.DataFrame(records, columns=["Count"])
st.subheader("count of records")
st.dataframe(records)

#Query1:  Total population of each district
query1 = "SELECT District, sum(Population) FROM guvi.census group by district"

cursor.execute(query1)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["District", "Total Population"])
st.subheader("1.Total population of each district")
st.dataframe(df)

#Query2:  Literate males and females in each district
query2 = """SELECT district, SUM(Literate_Male) AS Literate_Male, SUM(Literate_Female) AS Literate_Female  
            FROM guvi.census GROUP BY district"""

cursor.execute(query2)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["District", "Literate_Male", "Literate_Female"])
st.subheader("2.Literate males and females in each district")
st.dataframe(df)

#Query3:  Percentage of male and female workers in each district
query3 = """SELECT 
    district,
    round((SUM(Male_Workers) / SUM(Population)) * 100,2) AS Male_Worker_Percentage,
    round((SUM(Female_Workers) / SUM(Population)) * 100,2) AS Female_Worker_Percentage
    FROM guvi.census
    GROUP BY district"""
cursor.execute(query3)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["District", "Male_Worker_Percentage", "Female_Worker_Percentage"])
st.subheader("3.Percentage of male and female workers in each district")
st.dataframe(df)

#query4: Households having access to LPG or PNG as a cooking fuel in each district
query4 = """SELECT 
    district, sum(LPG_or_PNG_Households) AS Households_with_LPG_PNG_Access
    FROM guvi.census
    group by district"""

cursor.execute(query4)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Households_with_LPG_PNG_Access" ])
st.subheader("4.Households having access to LPG or PNG as a cooking fuel in each district")
st.dataframe(df)

#query5: Religious composition (Hindus, Muslims, Christians, etc.) of each district
query5 = """SELECT district, sum(Hindus) as Hindus,
    sum(Muslims) as Muslims,
    sum(Christians) as Christians,
    sum(Sikhs) as Sikhs,
    sum(Buddhists) as Buddhists,
    sum(Jains) as Jains,
    sum(Others_Religions) as Other_Religions,
    sum(Religion_Not_Stated) as Religion_Not_Stated
   FROM guvi.census
   group by district"""

cursor.execute(query5)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains", "Other Religions", "Religions not stated" ])
st.subheader("5.Religious composition in each district")
st.dataframe(df)

#query6: Households having internet access in each district
query6 = """SELECT 
    district, SUM(Households_with_Internet) AS Households_with_Internet_Access
FROM guvi.census
group by district"""

cursor.execute(query6)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Households with internet Access" ])
st.subheader("6.Households having internet access in each district")
st.dataframe(df)

#query7: Educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district
query7 = """SELECT District, 
            SUM(Below_Primary_Education) AS Below_Primary_Education,
            SUM(Primary_Education) AS Primary_Education,
            SUM(Middle_Education) AS Middle_Education,
            SUM(Secondary_Education) AS Secondary_Education,
            SUM(Higher_Education) AS Higher_Education,
            SUM(Graduate_Education) AS Graduate_Education,
            SUM(Other_Education) AS Other_Education,
            SUM(Literate_Education) AS Literate_Education,
            SUM(Illiterate_Education) AS Illiterate_Education
            FROM guvi.census
            group by district"""

cursor.execute(query7)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Below primary education", "Primary Education", "Middle_Education", "Secondary_Education", "Higher_Education",
                                  "Graduate_Education", "Other_Education", "Literate_Education", "Illiterate_Education"])
st.subheader("7.Educational attainment distribution in each district")
st.dataframe(df)

#query8: Households having access to various modes of transportation (bicycle, car, radio, television, etc.) in each district
query8 = """Select District, 
sum(Households_with_Bicycle) as Households_with_Bicycle,
sum(Households_with_Car_Jeep_Van) as Households_with_Car_Jeep_Van, 
sum(Households_with_Radio_Transistor) as Households_with_Radio_Transistor,
sum(Households_with_Scooter_Motorcycle_Moped) as Households_with_Scooter_Motorcycle_Moped, 
sum(Households_with_Telephone_Mobile_Phone_Landline_only) as Households_with_Telephone_Mobile_Phone_Landline_only,
sum(Households_with_Telephone_Mobile_Phone_Mobile_only) as Households_with_Telephone_Mobile_Phone_Mobile_only, 
sum(HHs_TV_Computer_Laptop_Tele_mobile_Scooter_Car) as HHs_TV_Computer_Laptop_Tele_mobile_Scooter_Car,
sum(Households_with_Television) as HHs_with_Television, 
sum(Households_with_Telephone_Mobile_Phone) as Households_with_Telephone_Mobile_Phone, 
sum(Households_with_Telephone_Mobile_Phone_Both) as Households_with_Telephone_Mobile_Phone_Both
FROM guvi.census
group by district"""

cursor.execute(query8)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Households_with_Bicycle", "Households_with_Car_Jeep_Van", "Households_with_Radio_Transistor", "Households_with_Scooter_Motorcycle_Moped", "Households_with_Telephone_Mobile_Phone_Landline_only", "Households_with_Telephone_Mobile_Phone_Mobile_only", "HHs_TV_Computer_Laptop_Tele_mobile_Scooter_Car", "HHs_with_Television", "Households_with_Telephone_Mobile_Phone", "Households_with_Telephone_Mobile_Phone_Both"])
st.subheader("8.Households having access to various modes of transportation in each district")
st.dataframe(df)

#query9: Condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district
query9 = """Select District, 
sum(Condition_of_occupied_census_houses_Dilapidated_Households) as Condition_of_occupied_census_houses_Dilapidated_Households,
sum(Households_with_separate_kitchen_Cooking_inside_house) as Households_with_separate_kitchen_Cooking_inside_house,
sum(Having_bathing_facility_Total_Households) as Having_bathing_facility_Total_Households,
sum(Having_latrine_facility_within_the_premises_Total_Households) as Having_latrine_facility_within_the_premises_Total_Households
from guvi.census
group by district"""

cursor.execute(query9)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Condition_of_occupied_census_houses_Dilapidated_Households", "Households_with_separate_kitchen_Cooking_inside_house", "Having_bathing_facility_Total_Households", "Having_latrine_facility_within_the_premises_Total_Households"])
st.subheader("9.Condition of occupied census houses in each district")
st.dataframe(df)

#query10: Household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district
query10 = """SELECT District, 
sum(Household_size_1_person_Households) as Household_size_1_person_Households,
sum(Household_size_2_persons_Households) as Household_size_2_persons_Households,
sum(Household_size_1_to_2_persons) as Household_size_1_to_2_persons,
sum(Household_size_3_persons_Households) as Household_size_3_persons_Households,
sum(Household_size_3_to_5_persons_Households) as Household_size_3_to_5_persons_Households,
sum(Household_size_4_persons_Households) as Household_size_4_persons_Households,
sum(Household_size_5_persons_Households) as Household_size_5_persons_Households,
sum(Household_size_6_8_persons_Households) as Household_size_6_8_persons_Households,
sum(Household_size_9_persons_and_above_Households) as Household_size_9_persons_and_above_Households
from guvi.census
group by district"""

cursor.execute(query10)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Household_size_1_person_Households", "Household_size_2_persons_Households", "Household_size_1_to_2_persons", "Household_size_3_persons_Households", "Household_size_3_to_5_persons_Households", "Household_size_4_persons_Households", "Household_size_5_persons_Households", "Household_size_6_8_persons_Households", "Household_size_9_persons_and_above_Households"])
st.subheader("10.Household size distribution in each district")
st.dataframe(df)

#query11: Total households in each state
query11 = """SELECT State_UT,
            sum(COALESCE(Households, 0))  AS Total_Households
        FROM guvi.census
        GROUP BY State_UT
        ORDER BY State_UT"""

cursor.execute(query11)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["District", "Total_Households"])
st.subheader("11.Total households in each state")
st.dataframe(df)

#query12: Households having a latrine facility within the premises in each state
query12 = """ SELECT State_UT,
            sum(Having_latrine_facility_within_the_premises_Total_Households)  AS Households_having_latrine_facility
        FROM guvi.census
        GROUP BY State_UT
        ORDER BY State_UT"""

cursor.execute(query12)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "Households_having_latrine_facility"])
st.subheader("12.Households having a latrine facility within the premises in each state")
st.dataframe(df)

#query13: Average household size in each state
query13 = """SELECT State_UT, District, 
        (SUM(Household_size_1_person_Households * 1) + 
         SUM(Household_size_2_persons_Households * 2) + 
         SUM(Household_size_3_persons_Households * 3) + 
         SUM(Household_size_4_persons_Households * 4) + 
         SUM(Household_size_5_persons_Households * 5) + 
         SUM(Household_size_6_8_persons_Households * 7) + 
         SUM(Household_size_9_persons_and_above_Households * 9)) / 
        (SUM(Household_size_1_person_Households + 
             Household_size_2_persons_Households + 
             Household_size_3_persons_Households + 
             Household_size_4_persons_Households + 
             Household_size_5_persons_Households + 
             Household_size_6_8_persons_Households + 
             Household_size_9_persons_and_above_Households)) AS Average_Household_Size
        FROM guvi.census
        GROUP BY State_UT, District"""

cursor.execute(query13)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "District", "Average_Household_Size"])
st.subheader("13.Average household size in each state")
st.dataframe(df)

#query14: Owned versus rented households in each state
query14 = """SELECT State_UT,
            sum(Ownership_Owned_Households) AS Owned_Households,
            sum(Ownership_Rented_Households) AS Rented_Households
        FROM guvi.census
        GROUP BY State_UT"""

cursor.execute(query14)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "Owned_Households", "Rented_Households"])
st.subheader("14.Owned versus rented households in each state")
st.dataframe(df)

#query15: Distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state
query15 = """SELECT State_UT, District,
sum(Type_of_latrine_facility_Pit_latrine_Households) AS Pit_latrine_Households,
sum(Type_of_latrine_facility_Other_latrine_Households) AS Other_latrine_Households,
sum(Type_of_latrine_facility_Night_soil) AS Night_soil_latrine,
sum(Type_of_latrine_facility_Flush_pour) AS Flush_pour_latrine
from guvi.census
group by State_UT, district"""

cursor.execute(query15)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "District", "Pit_latrine_Households", "Other_latrine_Households", "Night_soil_latrine", "Flush_pour_latrine"])
st.subheader("15.Distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state")
st.dataframe(df)

#query16: Households having access to drinking water sources near the premises in each state
query16 = """SELECT State_UT, District, 
        sum(Location_of_drinking_water_source_Near_the_premises_Households) as Location_of_drinking_water_source_Near_the_premises_Households
        FROM guvi.census
        GROUP BY State_UT, District"""

cursor.execute(query16)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "District", "Location_of_drinking_water_source_Near_the_premises_Households"])
st.subheader("16.Households having access to drinking water sources near the premises in each state")
st.dataframe(df)

#query17: Average household income distribution in each state based on the power parity categories
query17 = """SELECT State_UT,
        AVG(Power_Parity_Less_than_Rs_45000) AS Avg_Less_than_Rs_45000,
        AVG(Power_Parity_Rs_45000_90000) AS Avg_Rs_45000_90000,
        AVG(Power_Parity_Rs_90000_150000) AS Avg_Rs_90000_150000,
        AVG(Power_Parity_Rs_150000_240000) AS Avg_Rs_150000_240000,
        AVG(Power_Parity_Rs_240000_330000) AS Avg_Rs_240000_330000,
        AVG(Power_Parity_Rs_330000_425000) AS Avg_Rs_330000_425000,
        AVG(Power_Parity_Rs_425000_545000) AS Avg_Rs_425000_545000,
        AVG(Power_Parity_Above_Rs_545000) AS Avg_Above_Rs_545000
        FROM guvi.census
        GROUP BY State_UT"""

cursor.execute(query17)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records,columns=["State_UT", "Avg_Less_than_Rs_45000", "Avg_Rs_45000_90000", "Avg_Rs_90000_150000", "Avg_Rs_150000_240000", "Avg_Rs_240000_330000", "Avg_Rs_330000_425000", "Avg_Rs_425000_545000", "Avg_Above_Rs_545000"])
st.subheader("17.Average household income distribution in each state based on the power parity categories")
st.dataframe(df)

#query18: Percentage of married couples with different household sizes in each state
query18 = """SELECT State_UT,
        round((SUM(Married_couples_1_Households) / SUM(Households)) * 100,2) AS Married_couples_1_Percentage,
        round((SUM(Married_couples_2_Households) / SUM(Households)) * 100,2) AS Married_couples_2_Percentage,
        round((SUM(Married_couples_3_Households) / SUM(Households)) * 100,2) AS Married_couples_3_Percentage,
        round((SUM(Married_couples_4_Households) / SUM(Households)) * 100,2) AS Married_couples_4_Percentage,
        round((SUM(Married_couples_5__Households) / SUM(Households)) * 100,2) AS Married_couples_5_Percentage
        FROM guvi.census
        GROUP BY State_UT"""

cursor.execute(query18)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["State_UT", "Married_couples_1_Percentage", "Married_couples_2_Percentage", "Married_couples_3_Percentage", "Married_couples_4_Percentage", "Married_couples_5_Percentage"])
st.subheader("18.Percentage of married couples with different household sizes in each state")
st.dataframe(df)

#query19: Households falling below the poverty line in each state based on the power parity categories
query19 = """SELECT State_UT,
        SUM(Power_Parity_Less_than_Rs_45000) AS Households_Below_Poverty_Line
        FROM guvi.census
        GROUP BY State_UT"""

cursor.execute(query19)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["State_UT", "Households_Below_Poverty_Line"])
st.subheader("19.Households falling below the poverty line in each state based on the power parity categories")
st.dataframe(df)

#query20: Overall literacy rate (percentage of literate population) in each state
query20 = """SELECT State_UT, District,
           (SUM(Literate) / SUM(Population)) * 100 AS Literacy_Rate_Percentage
           from guvi.census
           group by State_UT, district"""

cursor.execute(query20)
records = cursor.fetchall()
for record in records:
    print(record)

df = pd.DataFrame(records, columns=["State_UT", "District", "Literacy_Rate_Percentage"])
st.subheader("20.Overall literacy rate (percentage of literate population) in each state")
st.dataframe(df)

# Run this file using 'Streamlit run Task7.py' - command
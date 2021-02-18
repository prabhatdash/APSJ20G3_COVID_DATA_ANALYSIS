import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("covid_19_india.csv")
df=pd.DataFrame(data)
col=df.columns
grouped_data=df.groupby('State/UnionTerritory')
max_cnf = grouped_data['Confirmed'].sum().max()
min_cnf = grouped_data['Confirmed'].sum().min()
max_cured = grouped_data['Cured'].sum().max()
min_cured = grouped_data['Cured'].sum().min()
max_death = grouped_data['Deaths'].sum().max()
min_death = grouped_data['Deaths'].sum().min()
name_sum_cnf = dict(zip(list(grouped_data.groups.keys()),list(grouped_data['Confirmed'].sum())))
name_sum_cured = dict(zip(list(grouped_data.groups.keys()),list(grouped_data['Cured'].sum())))
name_sum_death = dict(zip(list(grouped_data.groups.keys()),list(grouped_data['Deaths'].sum())))
def state_wise():
    print("#"*100)
    print("1->" + "TO GET TOTAL NO OF CURED-DEATH-CONFIRMED CASES SATE/UT WISE")
    print("2->" + "TO GET DETAILS OF STATE/UT WITH MAX CONFIRMED CASES")
    print("3->" + "TO GET DETAILS OF STATE/UT WITH MIN CONFIRMED CASES")
    print("4->" + "TO GET DETAILS OF STATE/UT WITH MAX CURED CASES")
    print("5->" + "TO GET DETAILS OF STATE/UT WITH MIN CURED CASES")
    print("6->" + "TO GET DETAILS OF STATE/UT WITH MAX DEATH CASES")
    print("7->" + "TO GET DETAILS OF STATE/UT WITH MIN DEATH CASES")
    print("8->" + "TO GET MAX AND MIN CONFIRMED CASES IN A DAY")
    print("9->" + "TO GET AVERAGE CONFIRMED | DEATH | CURED CASES PER DAY")
    print("#" * 100)
    input_1 = int(input())
    if input_1 == 1:
        print("TOTAL NO OF CURED-DEATH-CONFIRMED CASES SATE WISE")
        print(grouped_data.sum())
        state_wise()
    if input_1 == 2:
        print("GET DETAILS OF STATE/UT WITH MAXIMUM CONFIRMED CASES")
        for i in name_sum_cnf:
            if name_sum_cnf[i] == max_cnf:
                print("The State/UT with maximum no of cases is:")
                print(i, ": ", name_sum_cnf[i])
                state_wise()
    if input_1 == 3:
        print("GET DETAILS OF STATE/UT WITH MINIMUM CONFIRMED CASES")
        for i in name_sum_cnf:
            if name_sum_cnf[i] == min_cnf:
                print("The State/UT with minimum no of cases is:")
                print(i, ": ", name_sum_cnf[i])
                state_wise()
    if input_1 == 4:
        print("GET DETAILS OF STATE/UT WITH MAX CURED CASES")
        for i in name_sum_cured:
            if name_sum_cured[i] == max_cured:
                print("The State/UT with maximum no of cured cases is:")
                print(i, ": ", name_sum_cured[i])
                state_wise()
    if input_1 == 5:
        print("GET DETAILS OF STATE/UT WITH MIN CURED CASES")
        for i in name_sum_cured:
            if name_sum_cured[i] == min_cured:
                print("The State/UT with maximum no of cases is:")
                print(i, ": ", name_sum_cured[i])
                state_wise()

    if input_1 == 6:
        print("GET DETAILS OF STATE/UT WITH MIN DEATH CASES")
        for i in name_sum_death:
            if name_sum_death[i] == max_death:
                print("The State/UT with maximum no of death is:")
                print(i, ": ", name_sum_death[i])
                state_wise()
    if input_1 == 7:
        print("GET DETAILS OF STATE/UT WITH MIN DEATH CASES")
        for i in name_sum_death:
            if name_sum_death[i] == min_death:
                print("The State/UT with minimum no of death is:")
                print(i, ": ", name_sum_death[i])
                state_wise()
    if input_1 == 8:
        print("GET MAX CONFIRMED CASES IN A DAY:")
        print(df[df.Confirmed==df.Confirmed.max()])
        print("-"*100)
        print("GET MIN CONFIRMED CASES IN A DAY")
        print(df[df.Confirmed == df.Confirmed.min()])
        state_wise()
    if input_1 == 9:
        print("AVERAGE CONFIRMED CASES PER DAY:")
        print(df['Confirmed'].mean())
        print("-"*100)
        print("AVERAGE DEATH CASES PER DAY:")
        print(df['Deaths'].mean())
        print("-" * 100)
        print("AVERAGE CURED CASES PER DAY:")
        print(df['Cured'].mean())
        state_wise()

def state_wise_graph():
    print("#" * 100)
    print("1->" + "TO GET STATES VS CURED GRAPH")
    print("2->" + "TO GET STATES VS DEATH GRAPH")
    print("3->" + "TO GET CURED-DEATH TREND GRAPH")
    print("#" * 100)
    input_2 = int(input())
    if input_2==1:
        x=list(grouped_data['Cured'].sum())
        y = np.arange(30,1080,30)
        plt.barh(y,x,height=20)
        state_list=list(grouped_data.groups.keys())
        plt.yticks(y,state_list)
        plt.tick_params(axis='y',labelsize=7)
        plt.xlabel("CURED")
        plt.ylabel("STATES")
        for i in range(len(x)):
            plt.annotate(str(x[i]), xy=(x[i], y[i]), ha='left', va='center',fontsize=7)
        plt.show()
        state_wise_graph()
    if input_2==2:
        x=list(grouped_data['Deaths'].sum())
        y = np.arange(30,1080,30)
        plt.barh(y,x,height=20)
        state_list=list(grouped_data.groups.keys())
        plt.yticks(y,state_list)
        plt.tick_params(axis='y',labelsize=7)
        plt.xlabel("DEATHS")
        plt.ylabel("STATES")
        for i in range(len(x)):
            plt.annotate(str(x[i]), xy=(x[i], y[i]), ha='left', va='center',fontsize=7)
        plt.show()
        state_wise_graph()
    if input_2==3:
        death_list=list(grouped_data['Deaths'].sum())
        cured_list=list(grouped_data['Cured'].sum())
        cnf_list = list(grouped_data['Confirmed'].sum())
        x1 = np.arange(30,1080,30)
        plt.scatter(x1,death_list,color='r',label="Deaths")
        plt.scatter(x1,cured_list,color='g',label="Cured")
        plt.scatter(x1, cnf_list, color='b',label="Confirmed")
        plt.legend(loc="upper right")
        plt.show()
        state_wise_graph()


print("#"*100)
print()
print("--THE COLUMNS IN THE DATA SET ARE--")
for i in col:
    print(i,end=" ")
print()
print()
print("#" * 100)
print("#"*45+"--OPTIONS--"+"#"*44)
print()
print("PRESS 1 TO ANALYZE STATE/UT WISE")
print("PRESS 2 FOR GRAPHICAL REPRESENTATION")
print()
print("#"*100)
option_input=int(input())
if option_input==1:
    state_wise()
if option_input==2:
    state_wise_graph()
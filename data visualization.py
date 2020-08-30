import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

monster_data = pd.read_csv('C:/Users/Phillip/Desktop/projects/maplestory monster data/Consolidated Data.csv')

#creates a scatterplot that shows relationship between EXP and HP
def EXP_HP():
    plt.figure(figsize=(10,5))
    plt.title('Monster EXP vs HP')
    sns.scatterplot(x='HP', y='EXP', data=monster_data)
    plt.show()

#creates a scatterplot that shows relationship between EXP and levels
def EXP_level():
    plt.figure(figsize=(10,5))
    plt.title('Monster Level vs HP')
    sns.scatterplot(x='Level', y='EXP', data=monster_data)
    plt.show()

#creates a swarmplot that shows EXP of monsters in each area
def EXP_area():
    plt.figure(figsize=(20,5))
    plt.title('Monster EXP by Area')
    sns.swarmplot(x='Area', y='EXP', data=monster_data)
    plt.show()

#function that allows you to choose which areas to show
def sort_by_area():
    areas = input('Enter an area here (multiple areas can be separated with a comma): ')
    selected_area_list = areas.split(',')
    area_df = monster_data[monster_data['Area'].isin(selected_area_list)]
    plt.figure(figsize=(10,5))
    plt.title('EXP of Selected Areas')
    sns.scatterplot(x='HP', y='EXP', data=area_df)
    plt.show()


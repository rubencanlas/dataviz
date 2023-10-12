# SPARTA Data Visualisation Live Course (SP 502) - DAY ONE
# The following is the code used for the Live Course


# Tips dataset is available in this link: https://github.com/rubencanlas/dataviz/blob/fa80c8d8372b3efd93e43857c86b1bd7fad37e58/tips.csv  

# -------------------------------
# 1.1 Exploring the Tips Dataset
import pandas as pd
tips = pd.read_csv("tips.csv")
display(tips)

# -------------------------------
# 1.2 Visualizing the tips dataset 

# Use the Seaborn graphing library 
import seaborn as sns

# Hide depcrecated warning
import warnings
warnings.filterwarnings('ignore')

# Create the x-y plot
sns.set()
sns.relplot(x='total_bill', y='tip', hue='smoker', style='sex', size='size', data=tips);

# -------------------------------
# 1.3 Exploratory Data Analysis (EDA) 
tips.describe()

# -------------------------------
# 1.4 Visualize the IQR through boxplots

# Use the Seaborn graphing library 
import seaborn as sns

# Create the visualization
sns.boxplot(x="day", y="tip", data=tips);

# -------------------------------
# 1.5 Violin plots and more shapely datasets

# Set up the graph in Seaborn
sns.set_style("whitegrid")
# Graph the violin plot with the specs in the paranthesis
sns.catplot(x="day", y="tip", hue="sex", kind="violin", split=True, height=10, aspect=11.7/8.27, data=tips);

# -------------------------------

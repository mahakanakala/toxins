# Regressor Models

endocrine disruptors, carcinogens, mutagens (causing genetic mutations), estrogen mimickers, and /or allergens are harmful to the environment and aquatic life.

## Sources

- Chart Visualization of ML Applications/

[Online Graph Maker · Plotly Chart Studio](https://chart-studio.plotly.com/create/?fid=SolClover:200#/)

# K-Nearest Neighbor

- **feature similarity**
    - new point is assigned a value based on how closely it resembles the points in the training set
1. First, the distance between the new point and each training point is calculated.
2. The closest k data points are selected (based on the distance). In this example, points 1, 5, 6 will be selected if the value of k is 3.
3. The average of these data points is the final prediction for the new point.
4. 

# Support Vector Regression (SVR)

<aside>
💡 SVR is a powerful algorithm that allows us to choose how tolerant we are of errors, both through an acceptable error margin(ϵ) and through tuning our tolerance of falling outside that acceptable error rate. Hopefully, this tutorial has shown you the ins-and-outs of SVR and has left you confident enough to add it to your modeling arsenal.

</aside>

- Hard margin:
    - classes are fully linearly separable
- Soft margin
    - some points are allowed to be misclassified or to fall inside the margin (yellow shaded area).
    - This is where the “slack” value comes in, denoted by a greek letter ξ (xi).

### Radial Basis Function (RBF) Kernel

<aside>
💡 8 ingredients

</aside>

- 

### Sigmond Kernel

<aside>
💡 5 ingredients

</aside>

- 

### High: carcinogens & mutagens

<aside>
💡 4 ingredients

</aside>

- Talc
    - Talc is considered safe for use on the skin though it has been associated with ovarian cancer when used on or near the genitals.
- Parabens
    - The concern with these chemicals is that scientific studies suggest that parabens can disrupt hormones in the body, harm fertility and reproductive organs, affect birth outcomes, and increase cancer risk.
- BHA & BHT
    - BHA and BHT have been linked to quite a few health concerns, including cancer [1], disruption to the hormone system [2], liver damage [3], kidney issues [4], thyroid problems [5], and autoimmunity [6]
    . They can also contribute to changes in fatigue [7], headaches [8], hives [9], and rashes [10].
- Polyethylene glycols
    - various types of cancer

### Sources

- [Byrdie](https://www.byrdie.com/toxic-beauty-ingredients-4782646)
    
    "One idea is key: Kandinsky’s proposition that a line is a point set in motion. Analogies between drawing and movement play tag throughout a show of wildly multifarious works."
    
- [WebMD](https://www.webmd.com/beauty/features/harmful-chemicals-in-your-cosmetics)
    
    "Though Kandinsky is widely credited with inventing abstract painting, art history has generally sided with Malevich, whose “Black Square” threw down the gauntlet for nonobjective painting in 1915. That work (which is not on view) provoked Kandinsky to produce the flip response “In the Black Square,” which he painted in 1923."
    
- [EWG](https://www.ewg.org/the-toxic-twelve-chemicals-and-contaminants-in-cosmetics)
    
    Kandinsky believed that "total abstraction" allowed "complete expression" to occur. 
    

# Factors to keep track of

- Loreal

Price vs. toxins. is there a relationship between the expensive products and the number of toxins used?

1. sort by increasing price
2. create new df from that sorted price
3. scatter plot the number of toxins vs. price
4. find linear regression by using [https://www.statsmodels.org/dev/regression.html](https://www.statsmodels.org/dev/regression.html) ✔️
5. 

# Best Regressor Model

Price vs. toxins. is there a relationship between the expensive products and the number of toxins used?

1. create list of all listed toxins
2. create a loop that searches the ingredients column for the toxins in the list; increment a counter everytime it is found
3. reporting the number of toxins in each product; excluding the ones with 0 toxins
4. create a df with the product price & number of toxins in each product
5. plotting that relationship using [sns.scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html)
6. find linear regression by using [https://www.statsmodels.org/dev/regression.html](https://www.statsmodels.org/dev/regression.html)

# Testing the model with current data

# Testing the model with my own money

how to find the most reputed brands?

- Appendix
    - dataset
        - [https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets](https://www.kaggle.com/datasets/kingabzpro/cosmetics-datasets)
    - fonts
        - [https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/](https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/)
        
    - libraries
        - seaborn
        - pandas
        - numpy
        - 
- this is part of the skincare vault or (cabinet)
- other skincare scraping projects include gathering data from The Ordinary

# Further Steps

1. Type of Skincare
    1. moisturizer
    2. cleanser
    3. treatment
    4. face mask
    5. eye cream
    6. sun protectant
2. Type of Skin
    1. Dry
    2. Normal
    3. Oily
    4. Combination
    5. Sensitive
3. Price Point (range: 3-370)
    1. $3-$20 I am cheap
    2. $20-$50 I can spend a little
    3. $50-$100 I can splurge a little
    4. $100-$200 I can splurge a lot
    5. $200-$370 I wanna break my bank
4. Default the rank is greater than 4 stars

```python
import pandas as pd

# Define the word to search for
word = "example"

# Read the input data from a CSV file and create a dataframe
df = pd.read_csv("input.csv")

# Find the columns that contain the word
columns = df.columns[df.columns.str.contains(word)]

# Create a new dataframe with the columns that contain the word
deleted_df = df[columns]

# Remove the columns that contain the word from the original dataframe
df = df.drop(columns, axis=1)

# Write the original dataframe and the deleted dataframe to CSV files
df.to_csv("output.csv", index=False)
deleted_df.to_csv("deleted.csv", index=False)
```
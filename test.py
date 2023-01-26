from sklearn.feature_selection import chi2
from scipy.stats import chi2_contingency
import pandas as pd
def execute():
    df = pd.read_excel('/Users/salene/Documents/GitHub/SaleneTools/Age_Range_Distribution.xlsx', sheet_name='Original Data by Segment')
    df.dropna(inplace=True)
    crosstabs = pd.crosstab([df['Segment Name'], df['year'], df['month'], df['business_customer'], df['no. predict_audience'], df['no. label_audience']], df['age_range'])
    #crosstabs = pd.crosstab(df['no. predict_audience'], df['no. label_audience'])
    stat, p, dof, expectec = chi2_contingency(crosstabs)
    print(stat, p, dof)
    #print(expectec)
    new_df = pd.DataFrame(expectec, columns=['Segment Name', 'year', 'month', 'business_customer', 'no. predict_audience', 'no. label_audience'])
    new_df.to_excel('expected_values.xlsx')
    print(new_df.shape, df.shape)
if __name__ == '__main__':
    execute()
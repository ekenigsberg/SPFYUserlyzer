# import dependencies
import pandas as pd

# define single-user table-creating function
def MakeUserTable(html, strUserId):
    # grab second datatable on page and clean up
    df = pd.read_html(html)[1]
    # drop unneeded first 2 rows
    df = df.drop(df.index[0])
    df = df.drop(df.index[0])
    # set third row as header
    rowHead = df.iloc[0] 
    df = df[1:] 
    # set the header row as the df header
    df.columns = rowHead
    # drop unneeded columns
    df = df.drop('Storage', axis = 1)
    df = df.drop('Percent', axis = 1)
    # drop unneeded rows
    df = df.drop(df[df['Record Type'] == 'Current File Storage Usage'].index)
    df = df.drop(df[df['Record Type'] == 'Record Type'].index)
    df = df.drop(df[df['Record Count'] == '0'].index)
    df['User Id'] = strUserId
    return df
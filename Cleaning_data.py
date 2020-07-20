#My Little Toolbox for Data Cleaning:
#In the following code snippets, the codes are written in functions for self-explanatory purposes. You can always use the codes directly without putting them into functions with a small change of parameters.
#1. Drop multiple columns::
def drop_multiple_col(col_names_list, df): 
    '''
    AIM    -> Drop multiple columns based on their column names 
    
    INPUT  -> List of column names, df
    
    OUTPUT -> updated df with dropped columns 
    ------
    '''
    df.drop(col_names_list, axis=1, inplace=True)
    return df

#Sometimes, not all columns are useful in our analysis. Therefore, the df.drop comes in handy to drop the selected columns as specified by you.
#2. Change dtypes

def change_dtypes(col_int, col_float, df): 
    '''
    AIM    -> Changing dtypes to save memory
     
    INPUT  -> List of column names (int, float), df
    
    OUTPUT -> updated df with smaller memory  
    ------
    '''
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')

#3. Convert categorical variable to numerical variable::
def convert_cat2num(df):
    # Convert categorical variable to numerical variable
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True) 
#Some machine learning models require variables to be in numerical format. This is when we need to convert categorical variables to numerical variables 
#before feeding them to the models. In terms of data visualization, I’d suggest to retain the categorical variables to have a more explicit interpretation and understanding.

#4. Check missing data::
def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)
#If you want to check the number of missing data for each column, this is the fastest way to go with. This gives you a better understanding of which columns have higher number of missing data that determine your next action of data cleaning and analysis.

#5. Remove strings in columns::
def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True)
    
    # remove all the characters after &# (including &#) for column - col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)

#There might be some time when you’d face the new line character or other weird symbols that appear in your columns of strings. This could easily be dealt with using df['col_1'].replace where col_1 is one of the columns in the dataframe df.
#6. Remove white space in columns::

def remove_col_white_space(df,col):
    # remove white space at the beginning of string 
    df[col] = df[col].str.lstrip()

#Anything is possible when data is messy. It is not uncommon to see there are some white spaces at the beginning of the strings. Thus this approach is useful when you want to remove white spaces at the beginning of the strings in a column.
#7. Concatenate two columns with strings (with condition)::
def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space
#This is helpful when you want to combine two columns with strings conditionally. For instance, you want to concatenate the 1st column with the 2nd column if the strings in the 1st column end with certain letters. 
#The ending letters can also be removed after the concatenation, depending on your needs.
#8. Convert timestamp(from string to datetime format)::
def convert_str_datetime(df): 
    '''
    AIM    -> Convert datetime(String) to datetime(format we want)
     
    INPUT  -> df
    
    OUTPUT -> updated df with new datetime format 
    ------
    '''
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f')) 
#When dealing with time series data, chances are we’ll encounter timestamp column in string format. This means we may have to convert the string format to datetime format — format to be specified based on our
#requirement — in order to give meaningful analysis and presentation using the data.

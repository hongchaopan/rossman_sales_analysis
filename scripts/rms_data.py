# %%file data.py
"""
Example of a python module. Contains a variable called my_variable,
a function called my_function, and a class called MyClass.
"""
import time
import numpy as np

my_variable = 8

def data_prep_v1(data, ifTrain=True):

    # Extract date from Date
    # -----------------------
    tmpDate = [time.strptime(x, '%Y-%m-%d') for x in data.Date]
    data['mday'] = [x.tm_mday for x in tmpDate]
    data['mon'] = [x.tm_mon for x in tmpDate]
    data['year'] = [x.tm_year for x in tmpDate]

    # Mapping of all categorial variables to to integers
    # ---------------------------------------------------
    data['DayOfWeek1'] = 0
    data.loc[data.DayOfWeek == 1, 'DayOfWeek1'] = 1
    data['DayOfWeek2'] = 0
    data.loc[data.DayOfWeek == 2, 'DayOfWeek2'] = 1
    data['DayOfWeek3'] = 0
    data.loc[data.DayOfWeek == 3, 'DayOfWeek3'] = 1
    data['DayOfWeek4'] = 0
    data.loc[data.DayOfWeek == 4, 'DayOfWeek4'] = 1
    data['DayOfWeek5'] = 0
    data.loc[data.DayOfWeek == 5, 'DayOfWeek5'] = 1
    data['DayOfWeek6'] = 0
    data.loc[data.DayOfWeek == 6, 'DayOfWeek6'] = 1
    # dayOfWeek_map = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
    # data.DayOfWeek = data.DayOfWeek.map(dayOfWeek_map)

    data['StateHoliday'] = data['StateHoliday'].astype('str')
    data['StateHolidayA'] = 0
    data.loc[data.StateHoliday.str.contains('a'), 'StateHolidayA'] = 1
    data['StateHolidayB'] = 0
    data.loc[data.StateHoliday.str.contains('b'), 'StateHolidayB'] = 1
    data['StateHolidayC'] = 0
    data.loc[data.StateHoliday.str.contains('c'), 'StateHolidayC'] = 1
    # stateHoliday_map = {'0':1, 'a':2, 'b':3, 'c':4}
    # data.StateHoliday = data.StateHoliday.map(stateHoliday_map)

    data['StoreTypeA'] = 0
    data.loc[data.StoreType.str.contains('a'), 'StoreTypeA'] = 1
    data['StoreTypeB'] = 0
    data.loc[data.StoreType.str.contains('b'), 'StoreTypeB'] = 1
    data['StoreTypeC'] = 0
    data.loc[data.StoreType.str.contains('c'), 'StoreTypeC'] = 1
    # storeType_map = {'a':1, 'b':2, 'c':3, 'd':4}
    # data.StoreType = data.StoreType.map(storeType_map)

    data['AssortmentA'] = 0
    data.loc[data.Assortment.str.contains('a'), 'AssortmentA'] = 1
    data['AssortmentB'] = 0
    data.loc[data.Assortment.str.contains('b'), 'AssortmentB'] = 1
    # assortment_map = {'a':1, 'b':2, 'c':3}
    # data.Assortment = data.Assortment.map(assortment_map)

    data.loc[data.PromoInterval.isnull(), 'PromoInterval'] = 'M'
    data['PromoInterval'] = data['PromoInterval'].astype('str')
    data['PromoInterval1'] = 0
    data.loc[data.PromoInterval.str.contains('Jan,Apr,Jul,Oct'), 'PromoInterval1'] = 1
    data['PromoInterval2'] = 0
    data.loc[data.PromoInterval.str.contains('Feb,May,Aug,Nov'), 'PromoInterval2'] = 1
    data['PromoIntervalMissing'] = 0
    data.loc[data.PromoInterval.str.contains('M'), 'PromoIntervalMissing'] = 1
    # data.loc[data.PromoInterval.isnull(), 'PromoIntervalMissing'] = 1
    # promoInterval_map = {'Jan,Apr,Jul,Oct':1, 'Feb,May,Aug,Nov':2, 'Mar,Jun,Sept,Dec':3}
    # data.PromoInterval = data.PromoInterval.map(promoInterval_map, na_action='ignore')
    # data.PromoInterval = data.PromoInterval.map(promoInterval_map, na_action=None)

    # Convert categorial variables DayOfWeek, StateHoliday, StoreType,
    # Assortment, PromoInterval, ?StoreID to one-hot-encoding
    # data = pd.get_dummies(data=data, columns=['DayOfWeek',
    #                                          'StateHoliday',
    #                                          'StoreType',
    #                                          'Assortment'])
    # data = pd.get_dummies(data=data, columns=['PromoInterval'], dummy_na=True)

    # Square root or Log Sales, Customers, ?CompetitionDistance
    # col = ['Sales', 'Customers']
    # data.loc[:,col]=data.loc[:,col].apply(np.sqrt,axis=0)

    # Drop the original columns after processing them
    # ------------------------------------------------
    data.drop('Date', axis=1, inplace=True)
    data.drop('DayOfWeek', axis=1, inplace=True)
    data.drop('StateHoliday', axis=1, inplace=True)
    data.drop('StoreType', axis=1, inplace=True)
    data.drop('Assortment', axis=1, inplace=True)
    data.drop('PromoInterval', axis=1, inplace=True)

    # Processing specific to training or test data
    # ------------------------------------------------
    if ifTrain:
        data.Sales = data.Sales.apply(lambda x: np.sqrt(x))
        data.drop('Customers', axis=1, inplace=True)
        #data_y = data.Sales
        #data.drop('Sales', axis=1, inplace=True)
        #tmp_Y = train_proc.Sales
        #train_proc.drop('Sales', axis=1, inplace=True)
        #data.Sales = data.Sales.apply(lambda x: np.sqrt(x))
        #data.drop('Customers', axis=1, inplace=True)


    # Rename columns to drop underscores and dots
    # data.rename(columns={col: col.replace("_", "")
    #                            for col in data.columns}, inplace=True)

    # data.rename(columns={col: col.replace(".", "")
    #    for col in data.columns}, inplace=True)

    # stateHoliday_map = {label:float(idx) for idx, label in enumerate(udata.StateHoliday.unique())}
    # udata.StateHoliday = udata.StateHoliday.map(stateHoliday_map)

    return data

def data_prep_v2(data, ifTrain=True):

    # Extract date from Date
    # -----------------------
    tmpDate = [time.strptime(x, '%Y-%m-%d') for x in data.Date]
    data['mday'] = [x.tm_mday for x in tmpDate]
    data['mon'] = [x.tm_mon for x in tmpDate]
    data['year'] = [x.tm_year for x in tmpDate]

    # Mapping of all categorial variables to to integers
    # ---------------------------------------------------
    data['DayOfWeek1'] = 0
    data.loc[data.DayOfWeek == 1, 'DayOfWeek1'] = 1
    data['DayOfWeek2'] = 0
    data.loc[data.DayOfWeek == 2, 'DayOfWeek2'] = 1
    data['DayOfWeek3'] = 0
    data.loc[data.DayOfWeek == 3, 'DayOfWeek3'] = 1
    data['DayOfWeek4'] = 0
    data.loc[data.DayOfWeek == 4, 'DayOfWeek4'] = 1
    data['DayOfWeek5'] = 0
    data.loc[data.DayOfWeek == 5, 'DayOfWeek5'] = 1
    data['DayOfWeek6'] = 0
    data.loc[data.DayOfWeek == 6, 'DayOfWeek6'] = 1
    # dayOfWeek_map = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
    # data.DayOfWeek = data.DayOfWeek.map(dayOfWeek_map)

    data['StateHoliday'] = data['StateHoliday'].astype('str')
    data['StateHolidayA'] = 0
    data.loc[data.StateHoliday.str.contains('a'), 'StateHolidayA'] = 1
    data['StateHolidayB'] = 0
    data.loc[data.StateHoliday.str.contains('b'), 'StateHolidayB'] = 1
    data['StateHolidayC'] = 0
    data.loc[data.StateHoliday.str.contains('c'), 'StateHolidayC'] = 1
    # stateHoliday_map = {'0':1, 'a':2, 'b':3, 'c':4}
    # data.StateHoliday = data.StateHoliday.map(stateHoliday_map)

    data['StoreTypeA'] = 0
    data.loc[data.StoreType.str.contains('a'), 'StoreTypeA'] = 1
    data['StoreTypeB'] = 0
    data.loc[data.StoreType.str.contains('b'), 'StoreTypeB'] = 1
    data['StoreTypeC'] = 0
    data.loc[data.StoreType.str.contains('c'), 'StoreTypeC'] = 1
    # storeType_map = {'a':1, 'b':2, 'c':3, 'd':4}
    # data.StoreType = data.StoreType.map(storeType_map)

    data['AssortmentA'] = 0
    data.loc[data.Assortment.str.contains('a'), 'AssortmentA'] = 1
    data['AssortmentB'] = 0
    data.loc[data.Assortment.str.contains('b'), 'AssortmentB'] = 1
    # assortment_map = {'a':1, 'b':2, 'c':3}
    # data.Assortment = data.Assortment.map(assortment_map)

    data.loc[data.PromoInterval.isnull(), 'PromoInterval'] = 'M'
    data['PromoInterval'] = data['PromoInterval'].astype('str')
    data['PromoInterval1'] = 0
    data.loc[data.PromoInterval.str.contains('Jan,Apr,Jul,Oct'), 'PromoInterval1'] = 1
    data['PromoInterval2'] = 0
    data.loc[data.PromoInterval.str.contains('Feb,May,Aug,Nov'), 'PromoInterval2'] = 1
    data['PromoIntervalMissing'] = 0
    data.loc[data.PromoInterval.str.contains('M'), 'PromoIntervalMissing'] = 1
    # data.loc[data.PromoInterval.isnull(), 'PromoIntervalMissing'] = 1
    # promoInterval_map = {'Jan,Apr,Jul,Oct':1, 'Feb,May,Aug,Nov':2, 'Mar,Jun,Sept,Dec':3}
    # data.PromoInterval = data.PromoInterval.map(promoInterval_map, na_action='ignore')
    # data.PromoInterval = data.PromoInterval.map(promoInterval_map, na_action=None)

    # Convert categorial variables DayOfWeek, StateHoliday, StoreType,
    # Assortment, PromoInterval, ?StoreID to one-hot-encoding
    # data = pd.get_dummies(data=data, columns=['DayOfWeek',
    #                                          'StateHoliday',
    #                                          'StoreType',
    #                                          'Assortment'])
    # data = pd.get_dummies(data=data, columns=['PromoInterval'], dummy_na=True)

    # Square root or Log Sales, Customers, ?CompetitionDistance
    # col = ['Sales', 'Customers']
    # data.loc[:,col]=data.loc[:,col].apply(np.sqrt,axis=0)

    # Drop the original columns after processing them
    # ------------------------------------------------
    data.drop('Date', axis=1, inplace=True)
    data.drop('DayOfWeek', axis=1, inplace=True)
    data.drop('StateHoliday', axis=1, inplace=True)
    data.drop('StoreType', axis=1, inplace=True)
    data.drop('Assortment', axis=1, inplace=True)
    data.drop('PromoInterval', axis=1, inplace=True)

    # Processing specific to training or test data
    # ------------------------------------------------
    if ifTrain:
        data.Sales = data.Sales.apply(lambda x: np.log(x))
        data.drop('Customers', axis=1, inplace=True)
        #data_y = data.Sales
        #data.drop('Sales', axis=1, inplace=True)
        #tmp_Y = train_proc.Sales
        #train_proc.drop('Sales', axis=1, inplace=True)
        #data.Sales = data.Sales.apply(lambda x: np.sqrt(x))
        #data.drop('Customers', axis=1, inplace=True)


    # Rename columns to drop underscores and dots
    # data.rename(columns={col: col.replace("_", "")
    #                            for col in data.columns}, inplace=True)

    # data.rename(columns={col: col.replace(".", "")
    #    for col in data.columns}, inplace=True)

    # stateHoliday_map = {label:float(idx) for idx, label in enumerate(udata.StateHoliday.unique())}
    # udata.StateHoliday = udata.StateHoliday.map(stateHoliday_map)

    return data




def my_function():
    """
    Example function
    """
    return my_variable + 1


class MyClass:
    """
    Example class.
    """

    def __init__(self):
        self.variable = my_variable

    def set_variable(self, new_value):
        """
        Set self.variable to a new value
        """
        self.variable = new_value

    def get_variable(self):
        return self.variable

'''
数据的预处理：
1. Items which have been observed by less than 20 users during this period are removed.
2. After that, user records in one day are treated as a session (i.e., a transac- tion) to represent
   the short-term preference, and all singleton sessions (i.e., contain only one item) are removed.
3. Similar to [Hu et al., 2017], we randomly select 20% of sessions in the last month for testing, and
   the rest are used for training. We also randomly hold out one item in each session as the next item to be predicted.

'''
import pandas as pd

def tmall_dataset():
    user_info_format1 = pd.read_csv('../data/tmall/data_format1/user_info_format1.csv', sep=',', header=None,
                                    skiprows=1)
    user_info_format1.columns = ["user_id", "age_range", "gender"]

    user_log_format1 = pd.read_csv('../data/tmall/data_format1/user_log_format1.csv', sep=',', header=None, skiprows=1)
    user_log_format1.columns = ["user_id", "item_id", "cat_id", "seller_id", "brand_id", "time_stamp", "action_type"]





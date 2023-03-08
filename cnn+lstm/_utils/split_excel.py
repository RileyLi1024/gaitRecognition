import pandas as pd


def process_data1():
    data_df = pd.read_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\数据1_new_y.csv')
    # print(data_df.iloc[0:51,:])

    data_df = data_df.astype(str)
    y = data_df[~data_df["seq"].str.contains('500')]
    a = y.size
    # print(y)

    for i_num, i in enumerate(range(242300, 346150, 50)):
        i_num += 4846
        a = y.iloc[i:i + 50, :]
        a.to_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data/data1_after60/data1_{}.csv'.format(i_num),
                 header=1,
                 index=0)


def process_data2():
    data_df = pd.read_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\数据2_new_y.csv')
    # print(data_df.iloc[0:51,:])

    data_df = data_df.astype(str)
    y = data_df[~data_df["framed"].str.contains('500')]
    # print(y)

    for i_num, i in enumerate(range(242300, 346150, 50)):
        i_num += 4846
        a = y.iloc[i:i + 50, :]
        a.to_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data/data2_after60/data2_{}.csv'.format(i_num),
                 header=1,
                 index=0)


def a():
    data_df = pd.read_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\数据1.csv')
    # print(data_df.iloc[0:51,:])

    data_df = data_df.astype(str)
    y = data_df[~data_df["seq"].str.contains('50')]
    y.to_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data/数据1_no50.csv')


def b():
    data_df = pd.read_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\数据2-new.csv')
    # print(data_df.iloc[0:51,:])

    data_df = data_df.astype(str)
    y = data_df[~data_df["framed"].str.contains('49')]
    y.to_csv(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data/数据2_no49.csv')


if __name__ == '__main__':
    process_data1()
    process_data2()
    # b()

import pandas as pd



def read_csv():
    InputFile = "C:/Users/Jmyanez-TEB/Desktop/payflex.csv"
    # OutputFile= "C:/Users/Jmyanez-TEB/Desktop/AflacSocProc.csv"
    users = pd.read_csv(InputFile)


    count_rows = users.shape[0]
    count_coulumns = users.shape[1]

    for x in range(count_coulumns):
        # for y in range(count_coulumns):
            print(users.values[0][x])



read_csv()

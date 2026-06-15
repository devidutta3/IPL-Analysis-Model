import pandas as pd
def explore_data_set(matches,deliveries):
    
    print(matches.head())
    print("-----"*30)
    print(deliveries.head())
    print("-----"*30)

    print(f"It Tells The Shape Of Matches Data Set {matches.shape}" )
    print(f"It Tells The Shape Of Deliveries Data Set {deliveries.shape}" )
    print("\n"+"==="*50)
    print(f"It Tells The Columns Of Matches Data Set {matches.columns}" )
    print("\n"+"==="*50)
    print(f"It Tells The Columns Of Deliveries Data Set {deliveries.columns}" )

    print("\n"+"~~~"*60)
    print(f"The Matches Info {matches.info()}")
    print("\n"+"~~~"*60)
    print(f"The Deliveries Info {deliveries.info()}")

    print(f"The statistical Description(Matches) {matches.describe()}")
    print(f"The statistical Description {deliveries.describe()}")

matches=pd.read_csv(r"data\matches.csv")
deliveries=pd.read_csv(r"data\deliveries.csv")

explore_data_set(matches,deliveries)
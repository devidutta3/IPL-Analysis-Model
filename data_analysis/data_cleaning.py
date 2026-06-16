from load_dataset import explore_data_set

def cleaning_data(matches,deliveries):
    print("Matches Missing Values \n")
    print(matches.isnull())
    print("\n" + "==="*50)
    print("The Sum Of Null Values Of Matches \n")
    print("\n" + "==="*50) 
    print(matches.isnull().sum())

    print("\n" + "==="*50) 
    print("Deliveries Missing Values \n")
    print(deliveries.isnull())

    print("\n" + "==="*50)
    print("The Sum Of Null Values Of Deliveries \n")
    print("\n" + "==="*50) 
    print(deliveries.isnull().sum())

    print("\n"+ "----"*50)
    print("\n The Duplicate Values Of Matches \n")
    print(matches.duplicate())  
    print("\n" + "==="*50) 
    print("\n The Sum Of The Duplicate Values Of Matches \n") 
    print(matches.duplicate().sum())
    print("\n" + "==="*50)

    print("\n"+ "----"*50)
    print("\n The Duplicate Values Of Deliveries \n")
    print(deliveries.duplicate())  
    print("\n" + "==="*50) 
    print("\n The Sum Of The Duplicate Values Of Deliveries \n") 
    print(deliveries.duplicate().sum())
    print("\n" + "==="*50) 

matches=pd.read_csv(r"data\matches.csv") 
matches=pd.read_csv(r"data\matches.csv") 
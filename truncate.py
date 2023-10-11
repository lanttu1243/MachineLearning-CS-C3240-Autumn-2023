import pandas as pd
data = pd.read_csv("creditcard_2023.csv")
creditData = pd.DataFrame(data)
creditData = creditData.iloc[::5000, :].reset_index(drop=True)
creditData[['id']] /= 5000
creditData[['id']] = creditData[['id']].astype(int)
creditData.to_csv("creditcard_truncated.csv", index=False)

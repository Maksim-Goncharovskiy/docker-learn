import pandas as pd


async def add_user(name, age, sex):
    df = pd.read_csv("/app/data/users.csv", index_col=0)

    df.loc[len(df.index)] = [name, age, sex]

    df.to_csv("/app/data/users.csv")

    return 0



if __name__ == "__main__":
    df = pd.DataFrame(
        columns=["name", "age", "sex"]
    )
    df.to_csv("/app/data/users.csv")
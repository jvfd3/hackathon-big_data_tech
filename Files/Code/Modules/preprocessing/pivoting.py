""" FUNC: Pivoting the dataframe """

def pivoting_df(df):
    pivoted_df = (
        df.pivot_table(
        index="transaction_date", # agora usa transaction_date
        columns=["internal_product_id", "internal_store_id"],  
        values="quantity", # mantenha 'quantity' se esse for o nome certo
        aggfunc="sum",
        fill_value=0
        )
    )
    return pivoted_df
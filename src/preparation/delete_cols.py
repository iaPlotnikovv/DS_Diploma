def del_consts(df):
    """Удаляет const столбцы из DF"""
    describe = df.describe().T
    const_vals_cols= describe.loc[describe["std"]==0].index
    return df.drop(columns=const_vals_cols)
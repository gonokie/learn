import marimo

__generated_with = "0.14.16"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    car_brands = pd.Series(["Toyota", "Audi", "Honda"])  # series
    return (car_brands,)


@app.cell
def _(car_brands):
    car_brands
    return


@app.cell
def _(pd):
    colors = pd.Series(["Red", "Blue", "Green"])
    return (colors,)


@app.cell
def _(colors):
    colors
    return


@app.cell
def _(car_brands, colors, pd):
    car_data = pd.DataFrame({"car make": car_brands, "color": colors})  # dataframe
    return (car_data,)


@app.cell
def _(car_data):
    car_data
    return


@app.cell
def _(pd):
    sales = pd.read_csv("01_pandas/car-sales.csv")
    return (sales,)


@app.cell
def _(sales):
    sales
    return


@app.cell
def _(sales):
    # describe data
    sales.head()
    return


@app.cell
def _(sales):
    sales.dtypes
    return


@app.cell
def _(sales):
    sales.columns
    return


@app.cell
def _(sales):
    sales.index
    return


@app.cell
def _(sales):
    sales.describe()
    return


@app.cell
def _(sales):
    sales.info()
    return


@app.cell
def _(sales):
    sales.mean(numeric_only=True)
    return


@app.cell
def _(pd):
    prices = pd.Series([4000, 56000, 13400, 2900])
    prices.mean(numeric_only=True)
    return


@app.cell
def _(sales):
    sales.sum()
    return


@app.cell
def _(sales):
    sales["Doors"].sum()
    return


@app.cell
def _(sales):
    len(sales)
    return


@app.cell
def _(sales):
    sales.tail()
    return


@app.cell
def _(pd):
    birds = pd.Series(
        ["Pegion", "Hawk", "Sparrow", "Crow", "Eagle", "Kite", "Peacock"],
        index=[0, 3, 5, 2, 6, 8, 1],
    )
    return (birds,)


@app.cell
def _(birds):
    birds
    return


@app.cell
def _(birds):
    birds.loc[3]
    return


@app.cell
def _(birds):
    birds.iloc[3]
    return


@app.cell
def _(sales):
    sales.loc[4]
    return


@app.cell
def _(sales):
    sales
    return


@app.cell
def _(birds):
    birds.iloc[:3]
    return


@app.cell
def _(birds):
    birds.loc[:6]
    return


@app.cell
def _(sales):
    sales["Make"]
    return


@app.cell
def _(sales):
    sales.Colour
    return


@app.cell
def _(sales):
    sales[sales["Make"] == "Toyota"]
    return


@app.cell
def _(sales):
    sales[sales["Odometer (KM)"] > 100000]
    return


@app.cell
def _(pd, sales):
    pd.crosstab(sales["Make"], sales["Doors"])
    return


@app.cell
def _(sales):
    sales.groupby(["Make"]).mean(numeric_only=True)
    return


@app.cell
def _(sales):
    sales["Odometer (KM)"].plot()
    return


@app.cell
def _(sales):
    sales["Odometer (KM)"].hist()
    return


@app.cell
def _(sales):
    sales["Price"] = sales["Price"].replace('[\$\,\.]', '', regex=True).astype(float)
    return


@app.cell
def _(sales):
    sales["Price"].plot()
    return


@app.cell
def _(sales):
    sales["Price"].head()
    return


@app.cell
def _(sales):
    sales["Make"] = sales["Make"].str.lower()
    return


@app.cell
def _(sales):
    sales.head()
    return


@app.cell
def _(pd):
    sales_missing = pd.read_csv("01_pandas/car-sales-missing-data.csv")
    return (sales_missing,)


@app.cell
def _(sales_missing):
    sales_missing.head()
    return


@app.cell
def _(sales_missing):
    # sales_missing["Odometer"].fillna(sales_missing["Odometer"].mean(), inplace=True) # will deprecate
    sales_missing.fillna({"Odometer": sales_missing["Odometer"].mean()}, inplace=True)
    return


@app.cell
def _(sales_missing):
    sales_missing
    return


@app.cell
def _(sales_missing):
    sales_missing["Odometer"].mean().astype(int)
    return


@app.cell
def _(sales_missing):
    sales_missing_nadropped = sales_missing.dropna()
    return (sales_missing_nadropped,)


@app.cell
def _(sales_missing):
    sales_missing
    return


@app.cell
def _(sales_missing_nadropped):
    sales_missing_nadropped
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

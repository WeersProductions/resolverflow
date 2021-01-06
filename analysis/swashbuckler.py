from pyspark.sql.dataframe import DataFrameWriter
# Ja deze import klopt ook niet helemaal, maar ik weet niet wat ik moet hebben voor bucketBy()


def mass_apply(dataframe, *functions):
    """
    Takes a dataframe of a single column, and creates a new column for every function given

    Args:
        dataframe: single-column dataframe to be processed
        *functions: all functions that are to be applied

    Returns:
        dataframe with one extra column for every function that was given as input with its results
    """

    result = dataframe

    for func in functions:
        result.flatMap(func) # no way dat dit werkt, maar ik bedoel het goed

    return result


def bucketize(dataframe, bucket_size=100):
    # Weet niet zeker of deze functie veel toe gaat voegen aangezien het een enkele function call zou moeten zijn

    return dataframe.bucketBy(bucket_size, dataframe.columns[0])

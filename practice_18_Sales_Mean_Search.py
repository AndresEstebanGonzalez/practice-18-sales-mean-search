import pandas as pd

#Read dataset
sales_df = pd.read_csv("sales_data.csv")
sales_list = sales_df["sales"].tolist()

def find_mean_sales_position(sales):
    """Find the mean of the sales list and search for it with binary search.

    :param sales: list[int] - a sorted list of daily sales totals
    :return: int - the index of the mean if found
    :raises ValueError: if the mean is not found in the list
    """

    #Calculate mean
    mean = sum(sales) / len(sales)
    
    # Check if mean is a whole number
    if not mean.is_integer():
        raise ValueError(f"Mean {mean} is not an integer, so it can't be in the list")

    mean = int(mean)  # safe to convert
    
    #Define low & high
    low, high = 0, len(sales) - 1
    
    #Binary search for mean
    while low <= high:
        #Define mid
        mid = (high + low) // 2
        
        #Loop searching mean in list
        if sales[mid] == mean:
            return mid
        elif sales[mid] < mean:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError(f"Mean daily ({mean}) sales not recorded")
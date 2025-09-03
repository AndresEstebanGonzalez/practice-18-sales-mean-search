from  practice_18_Sales_Mean_Search import find_mean_sales_position

def test_mean_found():
    result = find_mean_sales_position([100,200,300,400,500])
    assert result == 2
    
    
def test_mean_not_found():
    try:
        find_mean_sales_position([120, 150, 200, 250])
    except ValueError as e:
        assert "not recorded" in str(e)
    else:
        assert False, "expected ValueError but none was raised"
        
def test_mean_not_integer():
    try:
        find_mean_sales_position([100,200,250])
    except ValueError as e:
        assert "not an integer" in str(e)
    else:
        assert False, "Expecte ValueError but non was raised"
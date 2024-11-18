def test_function(x):
    return x**2 - 2  # Example function: Find square root of 2

def GetArg(F, minArg, maxArg, Value, eps):
    minVal= F(minArg)
    maxVal= F(maxArg)

    while abs((maxArg - minArg)/maxArg) > eps:
        midArg = (minArg + maxArg)/2
        midVal = F(midArg)

        if midVal > Value:
            maxArg = midArg
            maxVal = midVal
        else:
            minArg = midArg
            minVal = midVal
            
    return (minArg + maxArg)/2


root = GetArg(test_function, 0, 2, 0, 1e-9)  # Find root within precision
print("Root:", root)

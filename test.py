import math
import matplotlib.pyplot as plt

# Define standard deviations and expectations
exp_values = [10, 10, 10, 12]
std_values = [2, 1, 0.5, 1]


def normal_dis_function(std, expectation, x):
    part_1 = 1 / (std * (math.sqrt(2 * math.pi)))  # standard deviation
    part_2 = math.exp((-1 / 2) * (((x - expectation) / std) ** 2))  # expectation
    result = part_1 * part_2
    return result


def cdf_function(x, std=2, expectation=10):
    # Extend the x range to better capture the full area
    left_boundary = 0
    right_boundary = 20
    x_values = [left_boundary + i * (right_boundary - left_boundary) / 100 for i in range(100)]  # List of x values

    # Calculate PDF values for the x_values range
    pdf_values = [normal_dis_function(std, expectation, x_val) for x_val in x_values]

    # Calculate CDF value for the input 'x'
    cumulative_sum = 0
    dx = x_values[1] - x_values[0]  # Step size

    if x <= left_boundary:
        return 0.0  # CDF is 0 below the range
    if x >= right_boundary:
        return 1.0  # CDF is 1 above the range
    
    # Loop through the PDF values and compute the cumulative sum until we reach the desired 'x'
    for i, pdf in enumerate(pdf_values):
        cumulative_sum += pdf * dx
        if x_values[i] >= x:
            break

    # Normalize the CDF to go from 0 to 1
    total_area = sum(pdf_values) * dx  # Total area under the curve (approximation)
    normalized_cdf = cumulative_sum / total_area  # Normalize to the total area under the curve

    return normalized_cdf



def draw_pdf(left_boundary, right_boundary):
    # Create the histogram plot
    plt.figure(figsize=(8, 6))

    x_values = [left_boundary + i * (right_boundary - left_boundary) / 100 for i in range(100)]

    # Loop over each pair of std and expectation values
    for std, expectation in zip(std_values, exp_values):
        y_values = [normal_dis_function(std, expectation, x) for x in x_values]
        plt.plot(x_values, y_values, label=f"PDF with mean={expectation}, std={std}")

    # Labeling the axes
    plt.title("Normal distribution law")
    plt.xlabel("Random Number")
    plt.ylabel("Probability Density")
    plt.legend()

    # Show the plot
    plt.show()

# Define boundaries and number of plots
left_boundary = 0  # Minimum boundary of the range
right_boundary = 20  # Maximum boundary of the range

draw_pdf(left_boundary, right_boundary)



def draw_cdf(left_boundary, right_boundary):

    x_values = [left_boundary + i * (right_boundary - left_boundary) / 100 for i in range(100)]

    cdf_values = [cdf_function(x) for x in x_values]  # Use cdf_function to get a single CDF value for each x

    # Plot the CDF
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, cdf_values, color='blue', label=f"CDF with mean={exp_values[0]}, std={std_values[0]}")
    plt.title("Cumulative Distribution Function (CDF) of Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.grid(True)
    plt.show()



draw_cdf(left_boundary, right_boundary)
#cdf_function(10) #for testing if cdf function is giving expected results


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



def GetTabF(F, minArg, maxArg, PointsCount):
    # Calculate the range of the function
    minVal = F(minArg)
    maxVal = F(maxArg)

    # Calculate the step size for dividing the CDF range
    dVal = (maxVal - minVal) / (PointsCount - 1)

    # Initialize lists to store XTab and YTab
    YTab = [minVal]
    XTab = [minArg]
    
    # Loop to populate intermediate points
    for i in range(1, PointsCount - 2):
        YTab_i = minVal + dVal * i  # Calculate the YTab value
        XTab_i = GetArg(F, minArg, maxArg, YTab_i, 10**-15)  # Find the corresponding XTab value

        YTab.append(YTab_i)
        XTab.append(XTab_i)
    
    YTab.append(maxVal) # YTab[PointsCount-1]= maxVal
    XTab.append(maxArg) # XTab[PointsCount-1]= maxArg

    print(f"YTab={YTab}")
    print(f"XTab={XTab}")

    
    return XTab, YTab


expectation= 10
std=2


# Get the tabulated data
minArg = expectation - 10
maxArg = expectation + 10
TabSize = 101

 # Get the XTab and YTab values
XTab, YTab = GetTabF(cdf_function, minArg, maxArg, TabSize)

def plot_xtab_ytab(XTab, YTab):
   
    plt.figure(figsize=(8, 6))
    plt.plot(XTab, YTab, label="Tabulated values")
    
    plt.title("Plot of XTab against YTab")
    plt.xlabel("XTab")
    plt.ylabel("YTab (Function values)")
    plt.legend()
    plt.grid(True)
    
    # Show the plot
    plt.show()

plot_xtab_ytab(XTab, YTab)


def Model_N(XTab, YTab, p):
    for i in range(1, len(XTab)):
        if YTab[i-1] <= p <= YTab[i]:
            # Linear interpolation formula
            y = (
                XTab[i-1] * (p - YTab[i]) / (YTab[i-1] - YTab[i]) +
                XTab[i] * (p - YTab[i-1]) / (YTab[i] - YTab[i-1])
            )
            return y
    return None  # Return None if p is out of bounds

def plot_model_N(XTab, YTab):
    left_boundary = 0
    right_boundary = 1
    p_values = [left_boundary + i * (right_boundary - left_boundary) / 100 for i in range(101)]

    # Compute Model_N for each p
    model_N_values = [Model_N(XTab, YTab, p) for p in p_values]

    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.plot(p_values, model_N_values, label="Model_N(XTab, YTab, p)")

    plt.title("Plot of Model_N(XTab, YTab, p) against p")
    plt.xlabel("p")
    plt.ylabel("Model_N(XTab, YTab, p)")

     # Adjust the legend location to the right of the plot
    #plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.legend()
    plt.grid(True)
    plt.show()


plot_model_N(XTab, YTab)


import random

# Define the different n values
n_values = [10**3, 10**4, 10**5, 10**6]

# Dictionary to store results for each n
ParArr_results = {}

for n in n_values:
    p_values = [random.uniform(0, 1) for _ in range(n)]  # Generate random p values

    # Compute Model_N for each p and store in the dictionary
    ParArr_results[n] = [Model_N(XTab, YTab, p) for p in p_values]

    # Output statistics
    print(f"Results for n = {n}:")
    print(f"Series: {len(ParArr_results[n])}")
    print(f"Max: {max(ParArr_results[n])}")
    print(f"Min: {min(ParArr_results[n])}")
    print()


def GetFreqDistr(RParamsArr, A, B, IntervalsCount):
    dY = (B-A)/IntervalsCount

    Freq = [0] * IntervalsCount

    for j in range(len(RParamsArr)-1):
        Yc= RParamsArr[j]
        fN = math.floor(Yc/dY)

        Freq[fN]+=1
        
    #Normalizing the frequency values
    for i in range(IntervalsCount): #normalizing all bins including the last one
        Freq[i] = Freq[i]/(len(RParamsArr)*dY)

    return Freq


A= 0
B= 20
K= 100

resX_values=[]

for k in range(K):
    resX= ((B-A)/K)*(0.5 + k)
    resX_values.append(resX)

resY_e3= GetFreqDistr(ParArr_results[10**3], A, B, K)
resY_e4= GetFreqDistr(ParArr_results[10**4], A, B, K)
resY_e5= GetFreqDistr(ParArr_results[10**5], A, B, K)
resY_e6= GetFreqDistr(ParArr_results[10**6], A, B, K)

resY_list= [resY_e3, resY_e4, resY_e5, resY_e6]

#print(resY_e4)
#print(ParArr_results[10**6])
#print(resX_values)


def draw_pdf_and_hist(left_boundary, right_boundary, num_plots, relative_frequencies, std=2, expectation=10):
    # Create the histogram plot
    plt.figure(figsize=(8, 6))

    bar_width = (right_boundary - left_boundary) / num_plots

    x_values = [left_boundary + i * (right_boundary - left_boundary) / 100 for i in range(100)] 
    y_values = [normal_dis_function(std, expectation, x) for x in x_values]
    plt.plot(x_values, y_values, label=f"PDF with mean={expectation}, std={std}", color='red')


    
     # Calculate the bin edges
    bins = [left_boundary + (i * (right_boundary - left_boundary) / num_plots) for i in range(num_plots + 1)]
    
    # Adjust the x positions to match the bins
    x_positions = [bins[i] for i in range(num_plots)]



    # Plot the bars with uniform width across the boundary range
    plt.bar(x_positions, relative_frequencies, width=bar_width, align='edge', edgecolor='black', 
            tick_label=[f'{bins[i]:.1f}' for i in range(len(bins)-1)], label="Histogram")
    
    
     # Set x-ticks every 5 units
    xticks = range(0, right_boundary, 5)  # Labels every 5 units
    plt.xticks(xticks)  # Set the x-ticks
        
    # Labeling the axes
    plt.title("Histogram and PDF")
    plt.xlabel("resXk")
    plt.ylabel("resY_e3k & N(resXk, m, std)")
    plt.legend()

    # Show the plot
    plt.show()


left_boundary = 0  
right_boundary = 20  


for n, resY in enumerate(resY_list, start=0):  # Enumerate starting from 3 for proper labeling
    print(f" Histogram and pdf for resY_e {n}")
    print(resY)
    draw_pdf_and_hist(left_boundary, right_boundary, K, resY)

def rod_cutting(n, prices):
    # Initialize arrays to store maximum revenues and cuts
    max_revenue = [0] * (n + 1)  # max_revenue[i] will store the max revenue for length i
    cuts = [0] * (n + 1)         # cuts[i] will store the optimal cut length for length i

    # Fill the tables by calculating the maximum revenue for each length
    for length in range(1, n + 1):
        max_value = 0
        for cut in range(1, length + 1):
            # Compute revenue if we make a cut of 'cut' length
            revenue = prices[cut - 1] + max_revenue[length - cut]
            if revenue > max_value:
                max_value = revenue
                cuts[length] = cut
        max_revenue[length] = max_value

    # Reconstruct the list of cuts from the 'cuts' array
    result = []
    while n > 0:
        result.append(cuts[n])
        n -= cuts[n]

    return result, max_revenue[-1]  # list of cuts and the maximum obtainable revenue
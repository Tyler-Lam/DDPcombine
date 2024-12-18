# template to add to categories:

# {'year': '', 'V': '', 'l': '', 'm': 0, 'ct': 0, 'quant': {0.025: [], 0.16: [], 0.5: [], 0.84: [], 0.975: [], -1: []}}

#  year = data taking era ('2016', '2017', '2018', 'Run2')
#  V = 'W', 'Z' (or 'V' for combined)
#  'l' = 'ELE', 'MU', (delete this key or put None for combined categories)
#  m, ct = mass, lifetime of Phi
#  quant = grid intervals and step size for each quantile (any number of quantiles > 0 is permitted)


# Current categories for old binning, need to update with old binning
categories = [
    
    #2018 Z->ee, m = 15 GeV
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 15, 'ct': 0, 'quant': {0.025: [1, 1.5, 0.0125], 0.16: [1, 1.5, 0.0125], 0.5: [1, 1.5, 0.0125], 0.84: [1, 1.5, 0.0125], 0.975: [1, 1.5, 0.0125], -1: [1, 1.5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 15, 'ct': 10, 'quant': {0.025: [1.2, 1.7, 0.0125], 0.16: [1.2, 1.7, 0.0125], 0.5: [1.2, 1.7, 0.0125], 0.84: [1.2, 1.7, 0.0125], 0.975: [1.2, 1.7, 0.0125], -1: [1.2, 1.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 15, 'ct': 20, 'quant': {0.025: [1.2, 1.7, 0.0125], 0.16: [1.2, 1.7, 0.0125], 0.5: [1.2, 1.7, 0.0125], 0.84: [1.2, 1.7, 0.0125], 0.975: [1.2, 1.7, 0.0125], -1: [1.2, 1.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 15, 'ct': 50, 'quant': {0.025: [2.2, 2.7, 0.0125], 0.16: [2.2, 2.7, 0.0125], 0.5: [2.2, 2.7, 0.0125], 0.84: [2.2, 2.7, 0.0125], 0.975: [2.2, 2.7, 0.0125], -1: [2.2, 2.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 15, 'ct': 100, 'quant': {0.025: [2.5, 4, 0.0125], 0.16: [2.5, 4, 0.0125], 0.5: [2.5, 4, 0.0125], 0.84: [2.5, 4, 0.0125], 0.975: [2.5, 4, 0.0125], -1: [2.5, 4, 0.0125]}},

    # Remaining limits don't have -1 quantile (for unblinded, observed limits), add or implement later
    
    #2018 Z->ee, m = 20 GeV
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 20, 'ct': 10, 'quant': {0.84: [0.6, 0.9, 0.0125]}},   # Check this one by hand, limit scans look weird. Possibly issue with my fix? UPDATE: limit scan looks ok with fixed grid

    # 2018 Z->ee, m = 30 GeV
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 30, 'ct': 0, 'quant': {0.025: [0.45, 0.7, 0.0125], 0.16: [0.45, 0.7, 0.0125], 0.5: [0.45, 0.7, 0.0125], 0.84: [0.45, 0.7, 0.0125], 0.975: [0.45, 0.7, 0.0125], -1: [0.45, 0.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 30, 'ct': 10, 'quant': {0.025: [0.45, 0.7, 0.0125], 0.16: [0.45, 0.7, 0.0125], 0.5: [0.45, 0.7, 0.0125], 0.84: [0.45, 0.7, 0.0125], 0.975: [0.45, 0.7, 0.0125], -1: [0.45, 0.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 30, 'ct': 20, 'quant': {0.025: [0.45, 0.7, 0.0125], 0.16: [0.45, 0.7, 0.0125], 0.5: [0.45, 0.8, 0.0125], 0.84: [0.45, 0.8, 0.0125], 0.975: [0.45, 1, 0.0125], -1: [0.45, 1, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 30, 'ct': 100, 'quant': {0.025: [0.55, 0.8, 0.0125], 0.16: [0.55, 0.8, 0.0125], 0.5: [0.55, 0.85, 0.0125], 0.84: [0.6, 1.6, 0.0125], 0.975: [0.6, 1.6, 0.0125], -1: [0.6, 1.6, 0.0125]}},

    #2018 Z->ee, m = 40 GeV
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 0, 'quant': {0.025: [0.6, 0.7, 0.0125], 0.16: [0.6, 0.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 10, 'quant': {0.025: [0.5, 0.65, 0.0125], 0.5: [0.5, 0.65, 0.0125], 0.84: [0.5, 0.65, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 20, 'quant': {0.025: [0.5, 0.7, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 50, 'quant': {0.16: [0.5, 0.7, 0.0125], 0.5: [0.5, 0.7, 0.0125], 0.84: [0.75, 0.95, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 100, 'quant': {0.84: [0.9, 1.15, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 40, 'ct': 1000, 'quant': {0.84: [3, 4, 0.025]}},

    #2018 Z->ee, m = 50 GeV #MISSING ctau 50 quant 0.16?
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 0, 'quant': {0.025: [.6, .75, 0.0125], 0.16: [.65, .8, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 10, 'quant': {0.025: [.5, .75, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 20, 'quant': {0.5: [.55, .8, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 50, 'quant': {0.5: [.55, .75, 0.0125], 0.975: [1.3, 1.5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 100, 'quant': {0.16: [.5, .7, 0.0125], 0.84: [1.1, 1.3, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 50, 'ct': 1000, 'quant': {0.025: [1.4, 1.65, 0.0125], 0.975: [4.5, 5.5, 0.05]}},

    #2018 Z->ee, m = 55 GeV
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 0, 'quant': {0.025: [.55, .7, 0.0125], 0.16: [.625, .75, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 10, 'quant': {0.025: [0.4, 0.5, 0.0125], 0.84: [0.85, 1.05, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 20, 'quant': {0.975: [1.3, 1.5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 50, 'quant': {0.5: [0.6, 0.8, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 100, 'quant': {0.5: [0.7, 1.2, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'ELE', 'm': 55, 'ct': 1000, 'quant': {0.975: [3.5, 4.5, 0.05]}},

    #2018 Z->mumu, m = 15 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 15, 'ct': 0, 'quant': {0.025: [0.65, 0.85, 0.0125], 0.16: [0.65, 0.85, 0.0125], 0.5: [0.65, 0.85, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 15, 'ct': 50, 'quant': {0.16: [1.0, 1.3, 0.025], 0.5: [1.0, 1.3, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 15, 'ct': 100, 'quant': {0.84: [2.40, 3.0, 0.05]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 15, 'ct': 1000, 'quant': {0.16: [12, 16.5, 0.25], 0.5: [12, 16.5, 0.25], 0.975: [24, 30, 0.25]}},

    #2018 Z->mumu, m = 20 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 0, 'quant': {0.025: [0.42, 0.5, 0.0125], 0.84: [0.5, 0.65, 0.0125], 0.975: [0.75, 0.95, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 10, 'quant': {0.025: [0.4, 0.45, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 20, 'quant': {0.025: [0.4, 0.5, 0.025], 0.975: [1, 1.1, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 50, 'quant': {0.025: [0.5, 0.65, 0.0125], 0.5: [0.6, 0.7, 0.0125], 0.975: [1.2, 1.6, .025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 100, 'quant': {0.16: [.6, .9, 0.0125], 0.975: [1.6, 1.9, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 20, 'ct': 1000, 'quant': {0.025: [3.5, 4.5, 0.05], 0.16: [3.5, 4.5, 0.05], 0.84: [6, 8, 0.125]}},

    #2018: Z->mumu, m = 30 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 0, 'quant': {0.16: [.3, .375, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 10, 'quant': {0.025: [0.3, 0.4, 0.0125], 0.16: [0.325, 0.4, 0.0125], 0.5: [.325, .425, 0.0125], 0.975: [0.65, 0.8, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 20, 'quant': {0.16: [.275, .35, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 50, 'quant': {0.025: [0.25, 0.5, 0.025], 0.16: [.3, .45, 0.0125], 0.5: [.4, .5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 100, 'quant': {0.975: [1.2, 1.5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 30, 'ct': 1000, 'quant': {0.025: [1.2, 1.8, 0.025], 0.5: [2.5, 3, 0.025]}},

    #2018: Z->mumu, m = 40 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 0, 'quant': {0.025: [0.3, 0.4, 0.0125], 0.16: [.3, .4, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 10, 'quant': {0.84: [0.5, 0.7, 0.0125], 0.975: [0.7, 0.95, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 20, 'quant': {0.025: [0.25, 0.45, 0.0125], 0.84: [0.6, 0.7, 0.0125], 0.975: [0.8, 1.0, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 50, 'quant': {0.16: [0.35, 0.45, 0.0125], 0.975: [1, 1.3, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 100, 'quant': {0.025: [0.3, 0.55, 0.0125], 0.16: [0.4, 0.55, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 40, 'ct': 1000, 'quant': {0.025: [1.3, 1.65, 0.0125], 0.975: [4.5, 5.5, 0.05]}},

    #2018: Z->mumu, m = 50 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 0, 'quant': {0.025: [0.3, 0.55, 0.0125], 0.84: [0.8, 1.0, 0.025], 0.975: [1.1, 1.4, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 10, 'quant': {0.025: [0.3, 0.4, 0.0125], 0.16: [0.35, 0.5, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 20, 'quant': {0.16: [0.39, 0.46, 0.01]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 50, 'quant': {0.025: [0.3, 0.4, 0.0125], 0.16: [0.4, 0.5, 0.0125], 0.5: [0.55, 0.65, 0.0125], 0.84: [0.85, 1.0, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 100, 'quant': {0.025: [0.35, 0.5, 0.0125], 0.5: [0.6, 0.8, 0.0125], 0.975: [1.3, 1.6, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 50, 'ct': 1000, 'quant': {0.025: [0.8, 1.3, 0.025], 0.5: [2.0, 2.4, 0.025]}},

    #2018: Z->mumu, m = 50 GeV
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 0, 'quant': {.025: [.35, .5, 0.0125], 0.16: [0.4, 0.6, 0.025]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 10, 'quant': {.025: [.35, .45, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 20, 'quant': {.025: [.5, .65, 0.0125], 0.16: [0.4, 0.5, 0.0125], 0.84: [0.8, 1.2, 0.025], 0.975: [1.2, 1.4, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 50, 'quant': {.025: [0.3, 0.45, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 100, 'quant': {.025: [0.35, 0.45, 0.0125], 0.84: [1.0, 1.2, 0.0125]}},
    {'year': '2018', 'V': 'Z', 'l': 'MU', 'm': 55, 'ct': 1000, 'quant': {0.025: [1, 1.3, 0.0125], 0.16: [1.2, 1.5, 0.025], 0.5: [1.8, 2.0, 0.0125]}},

    #2018: VH, m = 15 GeV
    {'year': '2018', 'V': 'V', 'm': 15, 'ct': 0, 'quant': {0.025: [0.046, 0.066, 0.001], 0.16: [0.05, 0.065, 0.00125]}},
    {'year': '2018', 'V': 'V', 'm': 15, 'ct': 10, 'quant': {0.025: [0.05, 0.07, 0.002]}},
    {'year': '2018', 'V': 'V', 'm': 15, 'ct': 20, 'quant': {0.025: [0.04, 0.06, 0.002], 0.84: [0.14, 0.18, 0.005]}},
    {'year': '2018', 'V': 'V', 'm': 15, 'ct': 1000, 'quant': {0.025: [1, 1.25, 0.025], 0.016: [1.0, 1.4, 0.05]}},

    #2018: VH, m = 20 GeV
    {'year': '2018', 'V': 'V', 'm': 20, 'ct': 0, 'quant': {0.025: [0.025, 0.04, 0.001], 0.84: [0.065, 0.085, 0.0025]}},
    {'year': '2018', 'V': 'V', 'm': 20, 'ct': 10, 'quant': {0.025: [0.025, 0.04, 0.001]}},
    {'year': '2018', 'V': 'V', 'm': 20, 'ct': 100, 'quant': {0.025: [0.07, 0.14, 0.005]}},
    {'year': '2018', 'V': 'V', 'm': 20, 'ct': 1000, 'quant': {0.025: [0.45, 0.55, 0.01]}},

    #2018: VH, m = 30 GeV
    {'year': '2018', 'V': 'V', 'm': 30, 'ct': 10, 'quant': {0.025: [0.024, 0.04, 0.002], 0.5: [0.05, 0.06, 0.002]}},
    {'year': '2018', 'V': 'V', 'm': 30, 'ct': 1000, 'quant': {0.16: [0.35, 0.45, 0.01], 0.5: [0.5, 0.7, 0.025]}},

    #2018: VH, m = 40 GeV
    {'year': '2018', 'V': 'V', 'm': 40, 'ct': 0, 'quant': {0.025: [0.03, 0.04, 0.001]}},
    {'year': '2018', 'V': 'V', 'm': 40, 'ct': 10, 'quant': {0.16: [0.045, 0.06, 0.001]}},
    {'year': '2018', 'V': 'V', 'm': 40, 'ct': 50, 'quant': {0.16: [0.065, 0.076, 0.001]}},
    {'year': '2018', 'V': 'V', 'm': 40, 'ct': 100, 'quant': {0.5: [0.1, 0.14, 0.0025]}},

    #2018: VH, m = 50 GeV
    {'year': '2018', 'V': 'V', 'm': 50, 'ct': 0, 'quant': {0.5: [0.1, 0.12, 0.0025]}},
    {'year': '2018', 'V': 'V', 'm': 50, 'ct': 100, 'quant': {0.025: [0.065, 0.08, 0.0025]}},
    {'year': '2018', 'V': 'V', 'm': 50, 'ct': 1000, 'quant': {0.025: [0.022, 0.028, 0.001]}},

    #2018 VH, m = 55 GeV
    {'year': '2018', 'V': 'V', 'm': 55, 'ct': 10, 'quant': {0.025: [0.045, 0.06, 0.0025], 0.16: [0.08, 0.09, 0.002], 0.5: [0.1, 0.13, 0.0025]}},
    {'year': '2018', 'V': 'V', 'm': 55, 'ct': 50, 'quant': {0.16: [0.08, 0.1, 0.00125]}}, #Check limit scan for this one too
    {'year': '2018', 'V': 'V', 'm': 55, 'ct': 100, 'quant': {0.025: [0.074, 0.084, 0.00125]}},
    {'year': '2018', 'V': 'V', 'm': 55, 'ct': 1000, 'quant': {0.025: [0.2, 0.27, 0.005], 0.975: [0.8, 0.95, 0.01]}},
]

gridPoints = {}
for cat in categories:
    year = cat['year']
    v = cat['V']
    l = cat['l'] if 'l' in cat else None
    m = cat['m']
    ct = cat['ct']
    quants = cat['quant']

    if l is not None:
        continue
        if (year, v, l, m, ct) not in gridPoints:
            gridPoints[year, v, l, m, ct] = quants
    else:
        if (year, v, m, ct) not in gridPoints:
            gridPoints[year, v, m, ct] = quants

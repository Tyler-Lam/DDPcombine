Code to run datacards and make limit plots for the VH DDP analysis

Requires a CMSSW area with both [combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combine-v10-recommended-version) and [combineHarvester](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combineharvestercombinetools) installed

* Install using  
```git clone https://github.com/Tyler-Lam/DDPcombine.git python```

* Once you have the datacards, run combine to produce the limits using  
```python3 python/VHTools/runCombine.py -d {date} -y {year} {-b}```  
  * `{date}`: datacards should be saved in directory named `datacards_{date}`  
  * `{year}`: which year of data taking (2016, 2017, 2018 or Run2 for all years)  
  * `{-b}`: Add to run blind (ignore observed data and just produce expected limits)

* After producing the limits, plot them using  
```python3 python/VHTools/plotLimits.py -d {date} -y {year} {-b}```

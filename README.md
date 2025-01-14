Code to run datacards and make limit plots for the VH DDP analysis using toys

Requires a CMSSW area with both [combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combine-v10-recommended-version) and [combineHarvester](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combineharvestercombinetools) installed

For HybridNew, there are possible issues with how combine handles duplicate test statistics. See [slides](https://cernbox.cern.ch/s/OM3M8g4WZCdoLyt) for details.

* Install using  
```git clone https://github.com/Tyler-Lam/DDPcombine.git python```

* Checkout the branch for HybridNew
* ```cd python```
* ```git checkout HybridNew```
* ```cd $CMSSW_BASE/src```

* Once you have the datacards, run combine to produce the limits using  
```python3 python/VHTools/runCombine_toys.py -d {date} -y {year} {-b} {-g} {-m}```  
  * `{date}`: datacards should be saved in directory named `datacards_{date}`  
  * `{year}`: which year of data taking (2016, 2017, 2018 or Run2 for all years)  
  * `{-b}`: Add to run blind (ignore observed data and just produce expected limits)
  * Running with a fixed grid:
    * For specific categories/masses/lifetimes/quantiles, combine sometimes doesn't do a good job scanning for the upper limit. For these, it can help to generate a fixed grid in signal strength
    * The specific points are saved in `VHTools/gridPoints.py` (currently configured for previous datacard binning, will likely have to be redone). You have to run all points and manually check the limit scan outputs to determine which points need to be added, as well as the range/increments for the limit point scan
    * `{-g}`: This tells the script to only run the points found in `VHTools/gridPoints.py` and skip all others
    * `{-m}`: Merge gridpoints. Once the individual gridpoints are run, you have to use this option to merge them into one file
  * Other Useful arguments:
    * `-l {limit}`: Changes behavior of test statistic and toy generation. limit = LHC (default LHC style) or CH (Cousins-Hihgland, recommended for low background)
    * `{-p}`: Save plot of the limit scan as a png
    * `-v {verbose}`: Verbosity of the combine output log

* After producing the limits, plot them using  
```python3 python/VHTools/plotLimits_toys.py -d {date} -y {year} {-b}```

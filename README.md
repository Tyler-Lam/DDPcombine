Code to run datacards and make limit plots for the VH DDP analysis

Requires a CMSSW area with both [combine](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combine-v10-recommended-version) and [combineHarvester](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#combineharvestercombinetools) installed

* Install using  
```git clone https://github.com/Tyler-Lam/DDPcombine.git python```

* Once you have the datacards, run combine to produce the limits using  
```python3 python/VHTools/runCombine.py -d {date} -y {year} {-b}```  
  * `{date}`: datacards should be saved in directory named `datacards_{date}`  
  * `{year}`: which year of data taking (2016, 2017, 2018 or Run2 for all years)  
  * `{-b}`: Add to run blind (ignore observed data and just produce expected limits)
* Additional Options for combine using toys:
  * `{-g/--grid}`: Run only categories/quantiles using fixed point grid generation
  * `{-m/--merge}`: Merge fixed point grids and run limits on merged categories
  * `-v {v}`: Verbosity for combine output
* Using toys produces a huge number of log/output files from condor. If running on lxplus, you may run into issues with the AFS file threshold. One minor fix is to add the following line into the CONDOR_TEMPLATE in the CombineToolBase.py script `output_destination = root://eosuser.cern.ch//eos/user/{u}/{user}/{output_dir}/` to transfer the output logs to your eos area.

* After producing the limits, plot them using  
```python3 python/VHTools/plotLimits.py -d {date} -y {year} {-b}```

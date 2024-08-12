import os, math, glob
import ROOT

import optparse
parser = optparse.OptionParser()
parser.add_option("-d", "--date", dest="date", default="08_12_24",help="date for plot directory")
parser.add_option("-y","--year",dest="year",default="2018",help="2016 or 2017 or 2018 (or Run2)")
parser.add_option("-b", "--blind", dest = "blind", action="store_true", default = False, help="Use option --run blind for combine")
(options,args) = parser.parse_args()

dir_out = "" # Change this to wherever you keep your datacards
#dir_out = "/home/tyler/DDP/rdf_simple/"
if not os.path.isdir(dir_out+"datacards_{}".format(options.date)):
    os.mkdir(dir_out+"datacards_{}".format(options.date))
os.chdir(dir_out+"datacards_{}".format(options.date))

masses = [15, 20, 30, 40, 50, 55]
ctaus = [0, 3, 10, 14, 20, 32, 50, 70, 100, 316, 1000]

years = []
if options.year == "Run2":
    years = ['2016', '2017', '2018']
else:
    years.append(options.year)

rMax = 5

# First combine bins for the individual categories
for year in years:
    for m in masses:
        for ct in ctaus:
            #for v in ['Z', 'W']:
            for v in ['Z']:
                for l in ['ELE', 'MU']:
                    name = "{}H_{}_m{}_ctau{}_{}".format(v,l,m,ct,year)
                    cmd = "combineCards.py "
                    files = glob.glob("datacard_{}_bin*.txt".format(name))
                    for f in files:
                        cmd += "{} ".format(f)
                    cmd += " > datacard_{}.txt".format(name)
                    os.system(cmd)

# If full run2, then combine all years
if options.year == "Run2": 
    rMax = 2.0
    for m in masses:
        for ct in ctaus:
            #for v in ['Z', 'W']:
            for v in ['Z']:
                for l in ['ELE', 'MU']:
                    name = "{}H_{}_m{}_ctau{}".format(v,l,m,ct)
                    cmd = "combineCards.py "
                    for y in years:
                        cmd += "datacard_{}_{}.txt ".format(name,y)
                    cmd += " > datacard_{}_Run2.txt".format(name)
                    os.system(cmd)

for m in masses:
    for ct in ctaus:
        #for v in ['Z', 'W']:
        for v in ['Z']:
            cmd_v = "combineCards.py "
            for l in ['ELE', 'MU']:
                print ("{}->{} m{} ctau{}".format(v,l,m,ct))
                # Run combine to get limits for each individual category
                name = "{}H_{}_m{}_ctau{}_{}".format(v,l,m,ct,options.year)
                cmd = "combine -M AsymptoticLimits datacard_{}.txt -m 125 -n .{} --rMax {}".format(name, name, rMax)
                if options.blind:
                    cmd += " --run blind"
                os.system(cmd)
                cmd_v += "datacard_{}.txt ".format(name)
            name = "{}H_m{}_ctau{}_{}".format(v,m,ct,options.year)
            cmd_v += "> datacard_{}.txt".format(name)
            os.system(cmd_v)

            print ("{}H m{} ctau{}".format(v, m, ct))
            cmd = "combine -M AsymptoticLimits datacard_{}.txt -m 125 -n .{} --rMax {}".format(name,name,rMax)
            if options.blind:
                cmd += " --run blind"
            os.system(cmd)

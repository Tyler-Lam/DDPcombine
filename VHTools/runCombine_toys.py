import os, math, glob
import ROOT
from gridPoints import *
import optparse
parser = optparse.OptionParser()
parser.add_option("-d", "--date",
                  dest="date",
                  default="08_12_24",
                  help="date for plot directory")
parser.add_option("-y","--year",
                  dest="year",
                  default="2018",
                  help="2016 or 2017 or 2018 (or Run2)")
parser.add_option("-b", "--blind",
                  dest = "blind",
                  action="store_true",
                  default = False,
                  help="Run blind expected limits (no prefit for nuisance parameters)")
parser.add_option("-l","--limits",
                  dest="limits",
                  default="CH",
                  help="Parameters for toy generation and limits, LHC or CH (cousins-highland)")
parser.add_option("", "--signif",
                  dest = "signif",
                  action="store_true",
                  default = False,
                  help="Use the --significance option in combine to get signif instead of CLs")
parser.add_option("", "--pval",
                  dest = "pval",
                  action="store_true",
                  default = False,
                  help = "Return significance as a p-value (must run with --signif)")
parser.add_option("-p", "--plot",
                  dest = "plot",
                  action = "store_true",
                  default = False,
                  help = "Return plot of the limit scan as a png")
parser.add_option("-v", "--verbose",
                  dest = "verbose",
                  default = "0",
                  help = "Verbose output level of combine: (-1 = very quiet; 0 = quiet, 1 = verbose, 2+ = debug)")
parser.add_option("-m", "--merge",
                  dest = "merge",
                  action = "store_true",
                  default = False,
                  help = "Merge single point limits into grid to calculate limits")
parser.add_option("-g", "--grid",
                  dest = "grid",
                  action = "store_true",
                  default = False,
                  help = "Run only points that require fixed grid generation")
(options,args) = parser.parse_args()

dir_out = "" # Change this to wherever you keep your datacards
#dir_out = "/home/tyler/DDP/rdf_simple/"
if not os.path.isdir(dir_out+"datacards_{}".format(options.date)):
    os.mkdir(dir_out+"datacards_{}".format(options.date))
os.chdir(dir_out+"datacards_{}".format(options.date))

masses = [15, 20, 30, 40, 50, 55]
#masses = [30]
#ctaus = [0, 3, 10, 14, 20, 32, 50, 70, 100, 316, 1000]
ctaus = [0, 10, 20, 50, 100, 1000]
#ctaus = [0, 20, 50, 100, 1000]

#Vs = ['Z']
Vs = ['Z', 'W']
years = []
if options.year == "Run2":
    years = ['2016', '2017', '2018']
else:
    years.append(options.year)

rMax = 5

combineArgs = "-H AsymptoticLimits --saveHybridResult --saveToys --rAbsAcc 0.0001 -m 125 -T 1000 --fullBToys"
mergeArgs = "--saveHybridResult --saveToys --rAbsAcc 0.0001 -m 125"
# Cousins-Highland (CH) recommended options for low background categories:
# https://indico.cern.ch/event/1284926/contributions/5416351/attachments/2650985/4589955/nobackground.pdf
if options.limits == "CH":
    if not options.blind:
        combineArgs += " --generateNuisances=1 --generateExternalMeasurements=0 --fitNuisances=1 --testStat LHC"
        mergeArgs += " --generateNuisances=1 --generateExternalMeasurements=0 --fitNuisances=1 --testStat LHC"
    else:
        combineArgs += " --generateNuisances=1 --generateExternalMeasurements=0 --fitNuisances=0 --testStat LHC"
        mergeArgs += " --generateNuisances=1 --generateExternalMeasurements=0 --fitNuisances=0 --testStat LHC"
elif options.limits == "LHC":
    if not options.blind:
        combineArgs += " --LHCmode LHC-limits"
        mergeArgs += " --LHCmode LHC-limits"
    else:
        combineArgs += " --generateNuisances=0 --generateExternalMeasurements=1 --fitNuisances=0 --testStat LHC"
        mergeArgs += " --generateNuisances=0 --generateExternalMeasurements=1 --fitNuisances=0 --testStat LHC"
else:
    print("Unrecognized argument for treatment of nuisances, defaulting to LHC limits")
    if not options.blind:
        combineArgs += " --LHCmode LHC-limits"
        mergeArgs += " --LHCmode LHC-limits"
    else:
        combineArgs += " --generateNuisances=0 --generateExternalMeasurements=1 --fitNuisances=0 --testStat LHC"
        mergeArgs += " --generateNuisances=0 --generateExternalMeasurements=1 --fitNuisances=0 --testStat LHC"

# Options to return significances/pvalue instead of limits
if options.signif:
    combineArgs += " --significance"
    mergeArgs += " --significance"
    if options.pval:
        combineArgs += " --pval"
        mergeArgs += " --pval"

# Return plots of limit scans
if options.plot:
    combineArgs += " --plot=limit_scan.{name}.png"
    mergeArgs += " --plot=limit_scan.{name}.png"

# if blind, generate pre-fit asimov and use as toy data
if options.blind:
    combineArgs += " -D higgsCombine.{asimov}_asimov.GenerateOnly.mH125.123456.root:toys/toy_asimov"

if options.verbose != "0":
    combineArgs += " -v {}".format(options.verbose)
    mergeArgs += " -v {}".format(options.verbose)
    
condorArgs = """--job-mode condor --sub-opts='+JobFlavour="testmatch"'"""
    
# First combine bins for the individual categories
for year in years:
    for m in masses:
        for ct in ctaus:
            for v in Vs:
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
    rMax = 2.0 # Need lower rMax due to higher sensitivity
    for m in masses:
        for ct in ctaus:
            for v in Vs:
                for l in ['ELE', 'MU']:
                    name = "{}H_{}_m{}_ctau{}".format(v,l,m,ct)
                    cmd = "combineCards.py "
                    for y in years:
                        cmd += "datacard_{}_{}.txt ".format(name,y)
                    cmd += " > datacard_{}_Run2.txt".format(name)
                    os.system(cmd)

for m in masses:
    for ct in ctaus:
        cmd_combine = "combineCards.py " # Command to combine all categories into 1 card
        for v in Vs:
            cmd_v = "combineCards.py " # Command to combine e+mu categories for a given V type
            for l in ['ELE', 'MU']:
                # Run combine to get limits for each individual category
                print ("Running combine for {}->{} m{} ctau{}".format(v,l,m,ct))
                name = "{}H_{}_m{}_ctau{}_{}".format(v,l,m,ct,options.year)

                if options.grid or options.merge:
                    if (options.year, v, l, m, ct) not in gridPoints:
                        print("   Category does not require fixed grid. skipping point")
                        continue
                    elif options.merge:
                        points = gridPoints[options.year, v, l, m, ct]
                        for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
                            if q not in points:
                                continue
                            # Merge the grid points:
                            cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.quant{:.3f}.root higgsCombine.{}.POINT*HybridNew.mH125*quant{}*.root".format(name, q, name, q)
                            os.system(cmd)

                            # Run combine on merged grid
                            cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.quant{q:0.3f}.root --expectedFromGrid {q} -n .{name}".format(name=name, q=q, args = mergeArgs.format(name = name + ".quant{}".format(q)))
                            os.system(cmd)
                        if not options.blind and -1 in points:
                            cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.root higgsCombine.{}.POINT*HybridNew.mH125.root".format(name, name)
                            os.system(cmd)

                            cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.root -n .{name}".format(name = name, args = mergeArgs.format(name=name))
                            os.system(cmd)
                        continue
                
                if options.blind:
                    asimov = "combine -d datacard_{name}.txt -M GenerateOnly -t -1 --saveToys -m 125 --bypassFrequentistFit -n .{name}_asimov".format(name=name)
                    os.system(asimov)

                points = gridPoints[options.year, v, l, m, ct] if (options.year, v, l, m, ct) in gridPoints else []
                
                for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
                    cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} --expectedFromGrid={q} -n .{name} --rMax {rMax} {cond} --task-name {name}.quant{q}'''.format(a=combineArgs.format(name=name+".quant{}".format(q), asimov=name), q=q, name=name, rMax=rMax, cond=condorArgs)
                    if q == 0.025:
                        cmd = cmd.replace("testmatch", "nextweek")
                    if q in points:
                        cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[q][0], r1 = points[q][1], deltaR = points[q][2])
                        cmd = cmd.replace("-H AsymptoticLimits", "")
                    elif options.grid:
                        continue
                    
                    os.system(cmd)
                    log = open("condor_{}.quant{}.txt".format(name,q), 'w')
                    log.write(cmd+"\n")
                    log.close()

                if not options.blind:
                    cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} -n .{name} --rMax {rMax} {cond} --task-name {name}'''.format(a=combineArgs.format(name=name), name=name, rMax=rMax, cond=condorArgs)
                    if -1 in points:
                        points = gridPoints[options.year, v, l, m, ct]
                        cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[-1][0], r1 = points[-1][1], deltaR = points[-1][2])
                    elif options.grid:
                        continue
                    os.system(cmd)
                    log = open("condor_{}.txt".format(name), 'w')
                    log.write(cmd+"\n")
                    log.close()

                cmd_v += "datacard_{}.txt ".format(name)

            # Run combine on combined e+mu datacard
            name = "{}H_m{}_ctau{}_{}".format(v,m,ct,options.year)
            cmd_v += "> datacard_{}.txt".format(name)
            os.system(cmd_v)

            print ("Running combine for all {}H m{} ctau{}".format(v, m, ct))

            if options.grid or options.merge:
                if (options.year, v, m, ct) not in gridPoints:
                    print ("   category does not require fixed grid. skipping point")
                    continue
                elif options.merge:
                    points = gridPoints[options.year, v, m, ct]
                    for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
                        if q not in points:
                            continue
                        cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.quant{:.3f}.root higgsCombine.{}.POINT*HybridNew.mH125*quant{}*.root".format(name, q, name, q)
                        os.system(cmd)

                        cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.quant{q:.3f}.root --expectedFromGrid={q} -n .{name}".format(name=name, q = q, args = mergeArgs.format(name=name))
                        os.system(cmd)
                    if not options.blind and -1 in points:
                        cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.root higgsCombine.{}.POINT*HybridNew.mH125.root".format(name, name)
                        os.system(cmd)

                        cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.root -n .{name}".format(name=name, args = mergeArgs.format(name=name))
                        os.system(cmd)
                    continue
                
            if options.blind:
                asimov = "combine -d datacard_{name}.txt -M GenerateOnly -t -1 --saveToys -m 125 --bypassFrequentistFit -n .{name}_asimov".format(name=name)
                os.system(asimov)

            points = gridPoints[options.year, v, m, ct] if (options.year, v, m, ct) in gridPoints else []
            for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
                cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} --expectedFromGrid={q} -n .{name} --rMax {rMax} {cond} --task-name {name}quant{q}'''.format(a=combineArgs.format(name=name+".quant{}".format(q), asimov=name), q=q, name=name, rMax=rMax, cond=condorArgs)
                if q in points:
                    cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[q][0], r1 = points[q][1], deltaR = points[q][2])
                    cmd = cmd.replace("-H AsymptoticLimits", "")
                elif options.grid:
                    continue
                if q == 0.025:
                    cmd = cmd.replace("testmatch", "nextweek")
                    if ct == 1000:
                        cmd += ' --memory 4000'
                os.system(cmd)
                log = open("condor_{}.quant{}.txt".format(name,q), 'w')
                log.write(cmd+"\n")
                log.close()

            if not options.blind:
                cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} --LHCmode LHC-limits --saveHybridResult -n .{name} --rMax {rMax} {cond} --task-name {name}'''.format(a = combineArgs.format(name=name), name=name, rMax=rMax, cond=condorArgs)
                if -1 in points:
                    cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[-1][0], r1 = points[-1][1], deltaR = points[-1][2])
                elif options.grid:
                    continue
                os.system(cmd)
                log = open("condor_{}.txt".format(name), 'w')
                log.write(cmd+"\n")
                log.close()

            cmd_combine += "datacard_{}.txt ".format(name)

        # combineCards all V types and run combine
        name = "VH_m{}_ctau{}_{}".format(m,ct,options.year)
        cmd_combine += "> datacard_{}.txt".format(name)
        os.system(cmd_combine)

        print ("Running combine for all VH m{} ctau{}".format(m,ct))
        if options.grid or options.merge:
            if (options.year, 'V', m, ct) not in gridPoints:
                print ("   category does not require fixed grid. skipping point")
                continue
            elif options.merge:
                points = gridPoints[options.year, 'V', m, ct]
                for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
                    if q not in points:
                        continue
                    cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.quant{:.3f}.root higgsCombine.{}.POINT*HybridNew.mH125*quant{}*.root".format(name, q, name, q)
                    os.system(cmd)

                    cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.quant{q:.3f}.root -n .{name}".format(name=name, args = mergeArgs.format(name = name + ".quant{}".format(q)), q = q)
                    os.system(cmd)
                if not options.blind and -1 in points:
                    cmd = "hadd -f higgsCombine.{}_grid.HybridNew.mH125.root higgsCombine.{}.POINT*HybridNew.mH125.root".format(name, name)
                    os.system(cmd)

                    cmd = "combine -M HybridNew -d datacard_{name}.txt {args} --grid=higgsCombine.{name}_grid.HybridNew.mH125.root -n .{name}".format(name=name, args = mergeArgs.format(name=name))
                    os.system(cmd)
                continue

        if options.blind:
            asimov = "combine -d datacard_{name}.txt -M GenerateOnly -t -1 --saveToys -m 125 --bypassFrequentistFit -n .{name}_asimov".format(name=name)
            os.system(asimov)

        points = gridPoints[options.year, 'V', m, ct] if (options.year, 'V', m, ct) in gridPoints else []
        for q in [0.025, 0.16, 0.5, 0.84, 0.975]:
            cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} --expectedFromGrid={q} -n .{name} --rMax {rMax} {cond} --task-name {name}.quant{q}'''.format(a=combineArgs.format(name=name+".quant{}".format(q),asimov=name), q=q, name=name, rMax=rMax, cond=condorArgs)
            if q == 0.025:
                cmd = cmd.replace("testmatch", "nextweek")
            if q in points:
                cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[q][0], r1 = points[q][1], deltaR = points[q][2])
            elif options.grid:
                continue
            os.system(cmd)
            log = open("condor_{}.quant{}.txt".format(name,q), 'w')
            log.write(cmd+"\n")
            log.close()

        if not options.blind:
            cmd = '''combineTool.py -M HybridNew -d datacard_{name}.txt {a} -n .{name} --rMax {rMax} {cond} --task-name {name}'''.format(a=combineArgs.format(name=name), name=name, rMax=rMax, cond=condorArgs)
            if -1 in points:
                cmd += " --singlePoint {r0}:{r1}:{deltaR}".format(r0 = points[-1][0], r1 = points[-1][1], deltaR = points[-1][2])
            elif options.grid:
                continue
            os.system(cmd)
            log = open("condor_{}.txt".format(name), 'w')
            log.write(cmd+"\n")
            log.close()

import ROOT
import os, math
import sys
sys.path.append("../../")
from CombineHarvester.CombineTools.plotting import *
sys.path.append("../../python/VHTools/")
import CMS_lumi as CMS_lumi
#sty = tdrstyle.setTDRStyle()

ROOT.gROOT.SetBatch(True)
import optparse
parser = optparse.OptionParser()
parser.add_option("-y","--year",dest="year",default="2018",help="2016 or 2017 or 2018 or Run2")
parser.add_option("-d", "--date", dest="date", default="01_06_23",help="date for plot directory")
parser.add_option("-b", "--blind", dest = "blind", action="store_true", default = False, help="Use option --run blind for combine")
(options,args) = parser.parse_args()

dir_out = ""
year = options.year
if not os.path.isdir(dir_out+"datacards_{}".format(options.date)):
    os.mkdir(dir_out+"datacards_{}".format(options.date))
os.chdir(dir_out+"datacards_{}".format(options.date))

#ctaus = [0, 3, 10, 20, 32, 50, 70, 100, 316, 1000]
ctaus = [0, 10, 20, 50, 100, 1000]
#masses = [15, 20, 30, 40, 50, 55]
masses = [15, 20, 50]
Vs = ['W', 'Z']
#Vs = ['Z']
intLumi = 0
if options.year == "2018":
    intLumi = 59.83
elif options.year == "2017":
    intLumi = 41.48
elif options.year == "2016":
    intLumi = 19.52 + 16.81
elif options.year == "Run2":
    intLumi = 137.62

def convertToJSON(limits, name, scale):
    quant = {25: "exp-2", 160: "exp-1", 500: "exp0", 840: "exp+1", 975: "exp+2", -1000: "obs"}
    f = open(name+".json", "w")
    f.write("{\n")
    text = []
    for i in range(len(limits)):
        x = limits[i][0]
        limit = limits[i][1]
        tree = limit.Get("limit")
        #Check if point should be added:
        tree.GetEntry(2)
        if tree.GetEntries() < 5:
            continue
        #if tree.limit > 1:
        #    continue

        text.append("")
        #f.write('  "{}"'.format(x))
        #f.write(': {\n')
        text[-1] = '  "{}"'.format(x)+': {\n'
        

        for j in range(tree.GetEntries()):
            tree.GetEntry(j)
            q = round(tree.quantileExpected*1000)
            if j != tree.GetEntries()-1:
                #f.write('    "{}": {},\n'.format(quant[q], tree.limit))
                text[-1] += '    "{}": {},\n'.format(quant[q], tree.limit*scale)
            else:
                #f.write('    "{}": {}\n'.format(quant[q], tree.limit))
                text[-1] += '    "{}": {}\n'.format(quant[q], tree.limit*scale)
        text[-1] += '  }'
        #if i != len(limits)-1:
        #    f.write('  },\n')
        #else:
        #    f.write('  }\n')
    
    for i in range(len(text)):
        f.write(text[i])
        if i != len(text) - 1:
            f.write(',\n')
        else:
            f.write('\n')
    f.write("}\n")
    f.close()

def drawLimitPlot(json, lumi, blind = False, logx = False, logy = True, extraJSON = None):
    ModTDRStyle()
    canv = ROOT.TCanvas("limit", "limit")
    #canv.SetLogX()
    #canv.SetLogy()
    pads = OnePad()

    graphs = None
    if blind:
        graphs = StandardLimitsFromJSONFile(json, draw=['exp0', 'exp1', 'exp2'])
    else:
        graphs = StandardLimitsFromJSONFile(json, draw=['obs', 'exp0', 'exp1', 'exp2'])

    axis = CreateAxisHist(list(graphs.values())[0])
    axis.GetXaxis().SetTitle("c#tau [mm]")
    axis.GetYaxis().SetTitle("BR(H#rightarrow#Phi#Phi)#timesBR(#Phi#rightarrow#gamma#gamma)")
    pads[0].cd()
    axis.Draw("axis")

    legend = PositionedLegend(0.3, .2, 1, .015)

    StyleLimitBand(graphs)
    DrawLimitBand(pads[0], graphs, legend=legend)
    legend.Draw()

    if logx:
        ROOT.gPad.SetLogx()
    if logy:
        ROOT.gPad.SetLogy()

    pads[0].RedrawAxis()
    pads[0].GetFrame().Draw()

    FixBothRanges(pads[0], graphs['exp2'].GetHistogram().GetMinimum(), 0, 1, 0)

    CMS_lumi.CMS_lumi(canv, 4, 0, relPosX = 0.077, lumi_13TeV = str(intLumi), extraText = "Work in progress")

    return {'canv': canv, 'graphs': graphs, 'legend': legend, 'pad': pads[0], 'axis': axis}

# Make json files:
br = 0.5 # Fixed BR(phi->gamma+gamma) from sample
scale = 0.1 # Scale used for signal yield in datacards

# Combined Limit vs ctau:
for m in masses:

    limits = []
    for ct in ctaus:
        # hadd quantiles together:
        os.system("hadd -f higgsCombine.VH_m{m}_ctau{ct}_{year}.HybridNew.mH125.root higgsCombine.VH_m{m}_ctau{ct}_{year}.HybridNew.mH125.123456.*root".format(m=m, ct=ct, year=year))
        
        f = ROOT.TFile("higgsCombine.VH_m{}_ctau{}_{}.HybridNew.mH125.root".format(m, ct, year))
        limits.append([max(0.0,ct), f])
    name = "limitsVsCtau_VH_m{}_{}".format(m,year)
    convertToJSON(limits, name, br*scale)
    
    
    limits = {}
    #for v in ['W', 'Z']:
    for v in Vs:
        limits[v] = {}
        for l in ['ELE','MU']:
        #for l in ['ELE']:
            limits[v][l] = []
            for ct in ctaus:
                os.system("hadd -f higgsCombine.{v}H_{l}_m{m}_ctau{ct}_{yr}.HybridNew.mH125.root higgsCombine.{v}H_{l}_m{m}_ctau{ct}_{yr}.HybridNew.mH125.123456*.root".format(v=v,l=l,m=m,ct=ct,yr=year))
                f = ROOT.TFile("higgsCombine.{}H_{}_m{}_ctau{}_{}.HybridNew.mH125.root".format(v,l,m,ct,year))
                limits[v][l].append([max(0.0, ct), f])
            name = "limitsVsCtau_{}H_{}_m{}_{}".format(v,l,m,year)
            convertToJSON(limits[v][l], name, br*scale)

f = ROOT.TFile("limits_{}.root".format(year), "RECREATE")
styleDict = {'MU': 1, 'ELE': 2}
colorDict = {'W': ROOT.kRed, 'Z': ROOT.kBlue}
legendDict = {('W', 'MU'): "W#rightarrow#mu#nu", ('W', 'ELE'): "W#rightarrow"+"e#nu",
              ('Z', 'MU'): "Z#rightarrow#mu#mu", ('Z', 'ELE'): "Z#rightarrow"+"ee"}

for m in masses:

    
    # Central combined limits
    json = "limitsVsCtau_VH_m{}_{}.json".format(m,year)
    
    c = drawLimitPlot(json, intLumi, options.blind, logx = True, logy = True)
    tex = ROOT.TLatex()
    tex.SetTextSize(0.04)
    tex.SetTextFont(42)
    tex.DrawLatexNDC(0.20 ,0.67, "m_{#Phi} = " + "{} GeV".format(m))
    tex.Draw("same")
    tex2 = ROOT.TLatex()
    tex2.SetTextSize(0.04)
    tex2.SetTextFont(42)
    tex2.DrawLatexNDC(0.20, .61, "BR(#Phi#rightarrow#gamma#gamma)=0.5")
    tex2.Draw("same")
    c['canv'].Write("limitVsCtau_m{}_{}".format(m,year))
    c['canv'].SaveAs("limitVsCtau_m{}_{}.png".format(m,year))
    
    # Limits for each category
    graphs = {}
    for v in Vs:
        graphs[v] = {}
        for l in ['ELE','MU']:
        #for l in ['ELE']:
            jsonfile = "limitsVsCtau_{}H_{}_m{}_{}.json".format(v,l,m,year)
            graphs[v][l] = LimitTGraphFromJSONFile(jsonfile, "exp0")
            graphs[v][l].SetLineColor(colorDict[v])
            graphs[v][l].SetLineStyle(styleDict[l])
            graphs[v][l].SetLineWidth(3)
    
    central = LimitTGraphFromJSONFile(json, "exp0")
    central.SetLineColor(ROOT.kBlack)
    central.SetLineWidth(3)
    central.SetMarkerSize(0)
    central.Write("central_m{}_{}".format(m,year))

    c = ROOT.TCanvas("c")
    
    minY = central.GetHistogram().GetMinimum()
    maxY = central.GetHistogram().GetMaximum()

    central.Draw()
    central.SetTitle("")
    c.SetGrid()
    
    legend = ROOT.TLegend(.2, .68, .68, .88)
    legend.SetHeader("m_{#Phi} = "+"{} GeV, BR(#Phi#rightarrow#gamma#gamma) = 0.5".format(m))
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.AddEntry(central, "Combined expected limit")
    for v in graphs:
        for l in graphs[v]:
            graphs[v][l].Write("{}_{}_m{}_{}".format(v,l,m,year))
            graphs[v][l].Draw("same")
            if graphs[v][l].GetHistogram().GetMaximum() > maxY:
                maxY = graphs[v][l].GetHistogram().GetMaximum()
            if graphs[v][l].GetHistogram().GetMinimum() < minY:
                minY = graphs[v][l].GetHistogram().GetMinimum()
            legend.AddEntry(graphs[v][l], legendDict[(v,l)], "l")
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.Draw("same")
    c.SetLogy()
    c.SetLogx()
    central.GetYaxis().SetRangeUser(0.001, 1)
    central.GetYaxis().SetNdivisions(10)
    central.GetXaxis().SetTitle("c#tau [mm]")
    central.GetXaxis().SetLimits(0.1, 1000)
    central.GetYaxis().SetTitle("BR(H#rightarrow#Phi#Phi)#timesBR(#Phi#Phi#rightarrow#gamma#gamma)")
    c.cd()
    tex.Draw("same")
    c.Write("limitVsCtau_m{}_{}_cats".format(m,year))
    
    for v in Vs:
        for l in ['ELE', 'MU']:
        #for l in ['ELE']:
            jsonfile = "limitsVsCtau_{}H_{}_m{}_{}.json".format(v,l,m,year)
            c = drawLimitPlot(jsonfile, intLumi, options.blind, logx=True, logy=True)
            tex = ROOT.TLatex()
            tex.SetTextSize(0.04)
            tex.SetTextFont(42)
            tex.DrawLatexNDC(0.20 ,0.67, "m_{#Phi} = " + "{} GeV".format(m))
            tex.Draw("same")
            tex2 = ROOT.TLatex()
            tex2.SetTextSize(0.04)
            tex2.SetTextFont(42)
            tex2.DrawLatexNDC(0.20, .61, "BR(#Phi#rightarrow#gamma#gamma)=0.5")
            tex2.Draw("same")
            c['canv'].Write("limitVsCtau_{}_{}_m{}_{}".format(v,l,m,year))
            c['canv'].SaveAs("limitVsCtau_{}_{}_m{}_{}.png".format(v,l,m,year))


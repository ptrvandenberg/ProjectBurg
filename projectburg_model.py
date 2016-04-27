# Project Burg [working title] model: field force rostering.

# Copyright 2016, Peter van den Berg

# This file implements a function [solve] that formulates and solves the model.

from gurobipy import *
from ticdat import TicDatFactory, freeze_me

# Define the input schema - 7 tables.

dataFactory = TicDatFactory (
    days = [["dayseq"], []],
    shifts = [["shiftid"], ["type", "shift", "starttime", "crew", "description"]],
    members = [["memid"], ["ranknum", "lastname", "firstname"]],
    carryover = [["memid"], ["lastWEoff", "day0shift"]],
    leave = [["memid", "dayseq"], ["value"]],
    commitment = [["memid", "dayseq"], ["value"]],
    fieldout = [["memid", "dayseq"], ["value"]])

# Add foreign keys

dataFactory.add_foreign_key("carryover", "members", ['memid', 'memid'])
dataFactory.add_foreign_key("leave", "members", ['memid', 'memid'])
dataFactory.add_foreign_key("commitment", "members", ['memid', 'memid'])
dataFactory.add_foreign_key("fieldout", "members", ['memid', 'memid'])

dataFactory.add_foreign_key("leave", "days", ['dayseq', 'dayseq'])
dataFactory.add_foreign_key("commitment", "days", ['dayseq', 'dayseq'])
dataFactory.add_foreign_key("fieldout", "days", ['dayseq', 'dayseq'])
                
# Define the solution schema - 1 table.

solutionFactory = TicDatFactory(
    utilisation = [[],["VanCrew"]],
    roster = [["memid", "dayseq"], ["value"]])

def solve(dat, week_res, shiftweek_res, shift_res):

    assert dataFactory.good_tic_dat_object(dat)
    assert not dataFactory.find_foreign_key_failures(dat)
    
    # Model
    m = Model("roster")

    # Create the decision variables - reformulate with shiftid as 3rd index, better sparsity?

    # AMPL: var x{d in DAY, m in MEMBER} binary;
    x = {}
    
    # AMPL: var x_d{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_s{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_o{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_x{d in DAY, m in MEMBER} binary;
    x_d = {}
    x_s = {}
    x_o = {}
    x_x = {}
    
    # AMPL: var x_dv{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dv1{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dv2{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dv3{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_dv = {}
    x_dv1 = {}
    x_dv2 = {}
    x_dv3 = {}
    
    # AMPL: var x_dr{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dr1{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dr2{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_dr3{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_dr = {}
    x_dr1 = {}
    x_dr2 = {}
    x_dr3 = {}

    # AMPL: var x_ds{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_ds1{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_ds2{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_ds3{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_ds = {}
    x_ds1 = {}
    x_ds2 = {}
    x_ds3 = {}

    # AMPL: var x_sg{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_sg1{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_sg2{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_sg3{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_sg4{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_sg = {}
    x_sg1 = {}
    x_sg2 = {}
    x_sg3 = {}
    x_sg4 = {}

    # AMPL: var x_sf{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_sf = {}

    # AMPL: var x_os{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    # AMPL: var x_or{d in DAY, m in MEMBER} binary <= 1 - leave[d,m];
    x_os = {}
    x_or = {}
    
    for m in dat.members:
        for d in dat.days:
            x[m,d] = m.addvar(vtype=GRB.BINARY)
            x_d[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_s[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_o[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_x[m,d] = m.addvar(vtype=GRB.BINARY)
            x_dv[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"], obj = 1)
            x_dv1[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dv2[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dv3[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dr[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dr1[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dr2[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_dr3[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_ds[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_ds1[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_ds2[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_ds3[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sg[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sg1[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sg2[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sg3[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sg4[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_sf[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_os[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])
            x_or[m,d] = m.addvar(vtype=GRB.BINARY, ub=1-dat.leave[m,d]["value"])

    # AMPL: var y{d in DAY, s in 1..3} binary;
    y = {}
    for d in dat.days:
        for s in range(1,3):
            y[d,s] = m.addvar(vtype=GRB.BINARY)
            
    # AMPL: var wo{w in WEEK0, m in MEMBER} binary;
    wo = {}
    for m in dat.members:
        for w in range(-4,week_res):
            wo[m,w] = m.addvar(vtype=GRB.BINARY)
                
    # The objective is to maximize the in-field utilisation
    m.modelSense = GRB.MAXIMIZE

    # Update model to integrate new variables
    m.update()

    # Add the basic constraints

    # AMPL: s.t. Allocated {d in DAY, m in MEMBER}: x[d,m] = 1;
    # AMPL: s.t. Rostered {d in DAY, m in MEMBER}: x[d,m] = x_d[d,m] + x_s[d,m] + x_o[d,m] + x_x[d,m];
    # AMPL: s.t. Daily {d in DAY, m in MEMBER}: x_d[d,m] = x_dv[d,m] + x_dr[d,m] + x_ds[d,m];
    # AMPL: s.t. Station {d in DAY, m in MEMBER}: x_s[d,m] = x_sg[d,m] + x_sf[d,m];
    # AMPL: s.t. Other {d in DAY, m in MEMBER}: x_o[d,m] = x_os[d,m] + x_or[d,m];

    # AMPL: s.t. Van {d in DAY, m in MEMBER}: x_dv[d,m] = x_dv1[d,m] + x_dv2[d,m] + x_dv3[d,m];
    # AMPL: s.t. Reception {d in DAY, m in MEMBER}: x_dr[d,m] = x_dr1[d,m] + x_dr2[d,m] + x_dr3[d,m];
    # AMPL: s.t. Sergeant {d in DAY, m in MEMBER}: x_ds[d,m] = x_ds1[d,m] + x_ds2[d,m] + x_ds3[d,m];
    # AMPL: s.t. General {d in DAY, m in MEMBER}: x_sg[d,m] = x_sg1[d,m] + x_sg2[d,m] + x_sg3[d,m] + x_sg4[d,m];

    for m in dat.members:
        for d in dat.days:
            m.addConstr(x[m,d] == 1, "Allocated")
            m.addConstr(x[m,d] == x_d[m,d] + x_s[m,d] + x_o[m,d] + x_x[m,d], "Rostered")
            m.addConstr(x_d[m,d] == x_dv[m,d] + x_dr[m,d] + x_ds[m,d], "Daily")
            m.addConstr(x_s[m,d] == x_sg[m,d] + x_sf[m,d], "Station")
            m.addConstr(x_o[m,d] == x_os[m,d] + x_or[m,d], "Other")
            m.addConstr(x_dv[m,d] == x_dv1[m,d] + x_dv2[m,d] + x_dv3[m,d], "Van")
            m.addConstr(x_dr[m,d] == x_dr1[m,d] + x_dr2[m,d] + x_dr3[m,d], "Reception")
            m.addConstr(x_ds[m,d] == x_ds1[m,d] + x_ds2[m,d] + x_ds3[m,d], "Sergeant")
            m.addConstr(x_sg[m,d] == x_sg1[m,d] + x_sg2[m,d] + x_sg3[m,d] + x_sg4[m,d], "General")
        
    # AMPL: s.t. Shifts {m in MEMBER}: sum {d in DAY} (x_d[d,m] + x_s[d,m] + x_o[d,m] + leave[d,m]) = week_res * shiftweek_res;

    for m in dat.members:
        m.addConstr(quicksum(x_d[m,d] + x_s[m,d] + x_o[m,d] + leave[m,d]  for d in dat.days) == week_res * shiftweek_res, "Shifts")

    # AMPL: s.t. Van_1_Crew {d in DAY}: sum {m in MEMBER} x_dv1[d,m] = crew[1] * (1 + y[d,1]);
    # AMPL: s.t. Van_2_Crew {d in DAY}: sum {m in MEMBER} x_dv2[d,m] = crew[2] * (1 + y[d,2]);
    # AMPL: s.t. Van_3_Crew {d in DAY}: sum {m in MEMBER} x_dv3[d,m] = crew[3] * (1 + y[d,3]);
    # AMPL: s.t. Van_1_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dv1[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dv1[d,m];
    # AMPL: s.t. Van_2_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dv2[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dv2[d,m];
    # AMPL: s.t. Van_3_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dv3[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dv3[d,m];

    # AMPL: s.t. Recep_1_Crew {d in DAY}: sum {m in MEMBER} x_dr1[d,m] = crew[4];
    # AMPL: s.t. Recep_2_Crew {d in DAY}: sum {m in MEMBER} x_dr2[d,m] = crew[5];
    # AMPL: s.t. Recep_3_Crew {d in DAY}: sum {m in MEMBER} x_dr3[d,m] = crew[6];
    # AMPL: s.t. Recep_1_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dr1[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dr1[d,m];
    # AMPL: s.t. Recep_2_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dr2[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dr2[d,m];
    # AMPL: s.t. Recep_3_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_dr3[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_dr3[d,m];

    # AMPL: s.t. Sgt_1_Crew {d in DAY}: sum {m in MEMBER} x_ds1[d,m] = crew[7];
    # AMPL: s.t. Sgt_2_Crew {d in DAY}: sum {m in MEMBER} x_ds2[d,m] = crew[8];
    # AMPL: s.t. Sgt_3_Crew {d in DAY}: sum {m in MEMBER} x_ds3[d,m] <= crew[9];

    for d in dat.days:
        m.addConstr(quicksum(x_dv1[m,d] for m in dat.members) == dat.shifts[1]["crew"] * (1 + y[d,1]), "Van_1_Crew")
        m.addConstr(quicksum(x_dv2[m,d] for m in dat.members) == dat.shifts[2]["crew"] * (1 + y[d,2]), "Van_2_Crew")
        m.addConstr(quicksum(x_dv3[m,d] for m in dat.members) == dat.shifts[3]["crew"] * (1 + y[d,3]), "Van_3_Crew")
        m.addConstr(quicksum(x_dv1[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dv1[m,d] for m in dat.members), "Van_1_Con")
        m.addConstr(quicksum(x_dv2[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dv2[m,d] for m in dat.members), "Van_2_Con")
        m.addConstr(quicksum(x_dv3[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dv3[m,d] for m in dat.members), "Van_3_Con")
        m.addConstr(quicksum(x_dr1[m,d] for m in dat.members) == dat.shifts[4]["crew"], "Recep_1_Crew")
        m.addConstr(quicksum(x_dr2[m,d] for m in dat.members) == dat.shifts[5]["crew"], "Recep_2_Crew")
        m.addConstr(quicksum(x_dr3[m,d] for m in dat.members) == dat.shifts[6]["crew"], "Recep_3_Crew")
        m.addConstr(quicksum(x_dr1[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dr1[m,d] for m in dat.members), "Recep_1_Con")
        m.addConstr(quicksum(x_dr2[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dr2[m,d] for m in dat.members), "Recep_2_Con")
        m.addConstr(quicksum(x_dr3[m,d] for m in dat.members if dat.members[m]["ranknum"] == 1) <= 0.5 * quicksum(x_dr3[m,d] for m in dat.members), "Recep_3_Con")
        m.addConstr(quicksum(x_ds1[m,d] for m in dat.members) == dat.shifts[7]["crew"], "Sgt_1_Crew")
        m.addConstr(quicksum(x_ds2[m,d] for m in dat.members) == dat.shifts[8]["crew"], "Sgt_2_Crew")
        m.addConstr(quicksum(x_ds3[m,d] for m in dat.members) <= dat.shifts[9]["crew"], "Sgt_3_Crew")

    # Add the complex constraints
        
    # AMPL: s.t. Sequential_Shifts {d in DAY0, m in MEMBER}: (if d = 0 then shifttime[day0shift[m]] else x_dv1[d,m] * shifttime[1] + x_dv2[d,m] * shifttime[2] + x_dv3[d,m] * shifttime[3] + x_dr1[d,m] * shifttime[4] + x_dr2[d,m] * shifttime[5] + x_dr3[d,m] * shifttime[6] + x_ds1[d,m] * shifttime[7] + x_ds2[d,m] * shifttime[8] + x_ds3[d,m] * shifttime[9] + x_sg1[d,m] * shifttime[10] + x_sg2[d,m] * shifttime[11] + x_sg3[d,m] * shifttime[12] + x_sg4[d,m] * shifttime[13] + x_sf[d,m] * shifttime[14] + x_os[d,m] * shifttime[15] + x_or[d,m] * shifttime[16] + x_x[d,m] * shifttime[17]) + 8 + 10 - 24 <= (if d = week_res * weekday_res then 24 else x_dv1[d+1,m] * shifttime[1] + x_dv2[d+1,m] * shifttime[2] + x_dv3[d+1,m] * shifttime[3] + x_dr1[d+1,m] * shifttime[4] + x_dr2[d+1,m] * shifttime[5] + x_dr3[d+1,m] * shifttime[6] + x_ds1[d+1,m] * shifttime[7] + x_ds2[d+1,m] * shifttime[8] + x_ds3[d+1,m] * shifttime[9] + x_sg1[d+1,m] * shifttime[10] + x_sg2[d+1,m] * shifttime[11] + x_sg3[d+1,m] * shifttime[12] + x_sg4[d+1,m] * shifttime[13] + x_sf[d+1,m] * shifttime[14] + x_os[d+1,m] * shifttime[15]  + x_or[d+1,m] * shifttime[16]+ x_x[d+1,m] * 24);

    for m in dat.members:
        for d in range(0,week_res * 7):
            if d == 0:
                m.addConstr(dat.shifts[dat.carryover[m]["day0shift"]]["starttime"] + 8 + 10 - 24 <= x_dv1[m,d+1] * dat.shifts[1]["starttime"] + x_dv2[m,d+1] * dat.shifts[2]["starttime"] + x_dv3[m,d+1] * dat.shifts[3]["starttime"] + x_dr1[m,d+1] * dat.shifts[4]["starttime"] + x_dr2[m,d+1] * dat.shifts[5]["starttime"] + x_dr3[m,d+1] * dat.shifts[6]["starttime"] + x_ds1[m,d+1] * dat.shifts[7]["starttime"] + x_ds2[m,d+1] * dat.shifts[8]["starttime"] + x_ds3[m,d+1] * dat.shifts[9]["starttime"] + x_sg1[m,d+1] * dat.shifts[10]["starttime"] + x_sg2[m,d+1] * dat.shifts[11]["starttime"] + x_sg3[m,d+1] * dat.shifts[12]["starttime"] + x_sg4[m,d+1] * dat.shifts[13]["starttime"] + x_sf[m,d+1] * dat.shifts[14]["starttime"] + x_os[m,d+1] * dat.shifts[15]["starttime"] + x_or[m,d+1] * dat.shifts[16]["starttime"] + x_x[m,d+1] * 24, "Sequential_Shifts")
            elif d == week_res * 7:
                m.addConstr(x_dv1[m,d] * dat.shifts[1]["starttime"] + x_dv2[m,d] * dat.shifts[2]["starttime"] + x_dv3[m,d] * dat.shifts[3]["starttime"] + x_dr1[m,d] * dat.shifts[4]["starttime"] + x_dr2[m,d] * dat.shifts[5]["starttime"] + x_dr3[m,d] * dat.shifts[6]["starttime"] + x_ds1[m,d] * dat.shifts[7]["starttime"] + x_ds2[m,d] * dat.shifts[8]["starttime"] + x_ds3[m,d] * dat.shifts[9]["starttime"] + x_sg1[m,d] * dat.shifts[10]["starttime"] + x_sg2[m,d] * dat.shifts[11]["starttime"] + x_sg3[m,d] * dat.shifts[12]["starttime"] + x_sg4[m,d] * dat.shifts[13]["starttime"] + x_sf[m,d] * dat.shifts[14]["starttime"] + x_os[m,d] * dat.shifts[15]["starttime"] + x_or[m,d] * dat.shifts[16]["starttime"] + x_x[m,d] * dat.shifts[17]["starttime"] + 8 + 10 - 24 <= 24, "Sequential_Shifts")
            else:
                m.addConstr(x_dv1[m,d] * dat.shifts[1]["starttime"] + x_dv2[m,d] * dat.shifts[2]["starttime"] + x_dv3[m,d] * dat.shifts[3]["starttime"] + x_dr1[m,d] * dat.shifts[4]["starttime"] + x_dr2[m,d] * dat.shifts[5]["starttime"] + x_dr3[m,d] * dat.shifts[6]["starttime"] + x_ds1[m,d] * dat.shifts[7]["starttime"] + x_ds2[m,d] * dat.shifts[8]["starttime"] + x_ds3[m,d] * dat.shifts[9]["starttime"] + x_sg1[m,d] * dat.shifts[10]["starttime"] + x_sg2[m,d] * dat.shifts[11]["starttime"] + x_sg3[m,d] * dat.shifts[12]["starttime"] + x_sg4[m,d] * dat.shifts[13]["starttime"] + x_sf[m,d] * dat.shifts[14]["starttime"] + x_os[m,d] * dat.shifts[15]["starttime"] + x_or[m,d] * dat.shifts[16]["starttime"] + x_x[m,d] * dat.shifts[17]["starttime"] + 8 + 10 - 24 <= x_dv1[m,d+1] * dat.shifts[1]["starttime"] + x_dv2[m,d+1] * dat.shifts[2]["starttime"] + x_dv3[m,d+1] * dat.shifts[3]["starttime"] + x_dr1[m,d+1] * dat.shifts[4]["starttime"] + x_dr2[m,d+1] * dat.shifts[5]["starttime"] + x_dr3[m,d+1] * dat.shifts[6]["starttime"] + x_ds1[m,d+1] * dat.shifts[7]["starttime"] + x_ds2[m,d+1] * dat.shifts[8]["starttime"] + x_ds3[m,d+1] * dat.shifts[9]["starttime"] + x_sg1[m,d+1] * dat.shifts[10]["starttime"] + x_sg2[m,d+1] * dat.shifts[11]["starttime"] + x_sg3[m,d+1] * dat.shifts[12]["starttime"] + x_sg4[m,d+1] * dat.shifts[13]["starttime"] + x_sf[m,d+1] * dat.shifts[14]["starttime"] + x_os[m,d+1] * dat.shifts[15]["starttime"] + x_or[m,d+1] * dat.shifts[16]["starttime"] + x_x[m,d+1] * 24, "Sequential_Shifts")

    # AMPL: s.t. Sgt_Rank {d in DAY, m in MEMBER}: x_ds[d,m] = (if memrank[m] <> 5 then 0 else x_ds[d,m]);
    # AMPL: s.t. Sgt_Stat {d in DAY, m in MEMBER}: x_sg[d,m] = (if memrank[m] = 5 then 1 - x_ds[d,m] - x_or[d,m] - x_x[d,m] else x_sg[d,m]);

    for m in dat.members:
        for d in dat.days:
            if dat.members[m]["ranknum"] != 5:
                m.addConstr(x_ds[m,d] == 0, "Sgt_Rank")
            else:
                m.addConstr(x_sg[m,d] == 1 - x_ds[m,d] - x_or[m,d] - x_x[m,d], "Sgt_Stat")

    # AMPL: s.t. SenSgt_Stat {d in DAY, m in MEMBER}: x_sg[d,m] = (if memrank[m] = 6 then 1 - x_x[d,m] else x_sg[d,m]);

    for m in dat.members:
        for d in dat.days:
            if dat.members[m]["ranknum"] == 6:
                m.addConstr(x_sg[m,d] == 1 - x_x[m,d], "SenSgr_Stat")

    # AMPL: s.t. Sgt_WE {we in 0..1, w in WEEK, m in MEMBER}: x_x[1+6*we+7*(w-1),m] = (if memrank[m] = 5 then 1 - x_ds[1+6*we+7*(w-1),m] - x_or[1+6*we+7*(w-1),m] else x_x[1+6*we+7*(w-1),m]);

    for m in dat.members:
        for w in range(1,week_res):
            for we in range(0,1):
                if dat.members[m]["ranknum"] == 5:
                    m.addConstr(x_x[m,1+6*we+7*(w-1)] == 1 - x_ds[m,1+6*we+7*(w-1)] - x_or[m,1+6*we+7*(w-1)], "Sgt_WE")
                else:
                    m.addConstr(x_x[m,1+6*we+7*(w-1)] == x_x[m,1+6*we+7*(w-1)], "Sgt_WE")


    # AMPL: s.t. SenSgt_WE {we in 0..1, w in WEEK, m in MEMBER}: x_x[1+6*we+7*(w-1),m] = (if memrank[m] = 6 then 1 else x_x[1+6*we+7*(w-1),m]);

    for m in dat.members:
        for w in range(1,week_res):
            for we in range(0,1):
                if dat.members[m]["ranknum"] == 6:
                    m.addConstr(x_x[m,1+6*we+7*(w-1)] == 1, "SenSgt_WE")
                else:
                    m.addConstr(x_x[m,1+6*we+7*(w-1)] == x_x[m,1+6*we+7*(w-1)], "SenSgt_WE")

    # AMPL: s.t. Files {d in DAY}: sum {m in MEMBER} x_sf[d,m] = crew[14];
    # AMPL: s.t. Files_Con {d in DAY}: sum {m in MEMBER} (if memrank[m]=1 then x_sf[d,m] else 0) <= 0.5 * sum {m in MEMBER} x_sf[d,m];

    for d in dat.days:
        m.addConstr(x_sf[m,d] == dat.shift[14]["crew"], "Files")
        if dat.members[m]["ranknum"] == 1:
            m.addConstr(x_sf[m,d] <= 0.5 * quicksum(x_sf[m,d] for m in dat.members), "Files_Con")

    # AMPL: s.t. SafStr_Non {nss in 1..5, w in WEEK, m in MEMBER}: x_os[nss+7*(w-1),m] = 0;
    # AMPL: s.t. SafStr_Crew {ssd in 6..7, w in WEEK}: sum {m in MEMBER} x_os[ssd+7*(w-1),m] = crew[15];
    # AMPL: s.t. SafStr_Con {d in DAY}: sum{m in MEMBER} (if memrank[m]=1 then x_os[d,m] else 0) <= 0.75 * sum{m in MEMBER} x_os[d,m];
    # AMPL: s.t. SafStr_Night {w in WEEK, m in MEMBER}: x_os[6+7*(w-1),m] = x_os[7+7*(w-1),m];

    for m in dat.members:
        for w in range(1,week_res):
            for nss in range(1,5):
                m.addConstr(x_os[m,nss+7*(w-1)] == 0, "SafStr_Non")

    for m in dat.members:
        for ssd in range(6,7):
            m.addConstr(quicksum(x_os[m,ssd+7*(w-1)] for m in dat.members) == dat.shifts[15]["crew"], "SafStr_Crew")

    for d in dat.days:
        m.addConstr(quicksum(x_os[m,d] for m in dat.members if dat.members[m]["ranknum"]==1) <= 0.75 * quicksum(x_os[m,d] for m in dat.members), "SafStr_Con")

    for m in dat.members:
        for w in range(1,week_res):
            m.addConstr(x_os[m,6+7*(w-1)] == x_os[m,7+7*(w-1)], "SafStr_Night")

    # AMPL: s.t. Van_Night {w in WEEK, m in MEMBER}: sum {d in 1+7*(w-1)..7*w} x_dv3[d,m] = x_dv3[1+7*(w-1),m] * 7;
    # AMPL: s.t. Rec_Night {w in WEEK, m in MEMBER}: sum {d in 1+7*(w-1)..7*w} x_dr3[d,m] = x_dr3[1+7*(w-1),m] * 7;
    # AMPL: s.t. Sgt_Night {w in WEEK, m in MEMBER}: sum {d in 1+7*(w-1)..7*w} x_ds3[d,m] = x_ds3[1+7*(w-1),m] * 7;

    for m in dat.members:
        for w in range(1,week_res):
            m.addConstr(quicksum(x_dv3[m,d] for d in range(1+7*(w-1),7*w)) == x_dv3[m,1+7*(w-1)] * 7, "Van_Night")
            m.addConstr(quicksum(x_dr3[m,d] for d in range(1+7*(w-1),7*w)) == x_dr3[m,1+7*(w-1)] * 7, "Rec_Night")
            m.addConstr(quicksum(x_ds3[m,d] for d in range(1+7*(w-1),7*w)) == x_ds3[m,1+7*(w-1)] * 7, "Sgt_Night")

    # AMPL: s.t. Reco_Night {w in WEEK, m in MEMBER}: x_or[7+7*(w-2)+1,m] = (if leave[7+7*(w-2)+1,m] = 1 then 0 else (if w = 1 then (if shifttime[day0shift[m]] = 23 then 1 else 0) else x_dv3[7+7*(w-2),m] + x_dr3[7+7*(w-2),m] + x_ds3[7+7*(w-2),m]));
    # AMPL: s.t. Reco_Non {nrc in 2..7, w in WEEK, m in MEMBER}: x_or[nrc+7*(w-1),m] = 0;

    for m in dat.members:
        for w in range(1,week_res):
            if dat.leave[m,7+7*(w-2)+1]["value"] == 1:
                m.addConstr(x_or[m,7+7*(w-2)+1] == 0, "Reco_Night")
            elif w == 1:
                if dat.shifts[dat.carryover[m]["day0shift"]]["starttime"] == 23:
                    m.addConstr(x_or[m,7+7*(w-2)+1] == 1, "Reco_Night")
                else:
                    m.addConstr(x_or[m,7+7*(w-2)+1] == 0, "Reco_Night")
            else:
                m.addConstr(x_or[m,7+7*(w-2)+1] == x_dv3[m,7+7*(w-2)] + x_dr3[m,7+7*(w-2)] + x_ds3[m,7+7*(w-2)], "Reco_Night")

    for m in dat.members:
        for w in range(1,week_res):
            for nrc in range(2,7):
                m.addConstr(x_or[m,nrc+7*(w-1)] == 0, "Reco_Non")

    # AMPL: s.t. Weekend_Off_7 {w in 1..week_res-1, m in MEMBER}: wo[w,m] <= x_x[7+7*(w-1),m];
    # AMPL: s.t. Weekend_Off_1 {w in 1..week_res-1, m in MEMBER}: wo[w,m] <= x_x[1+7*w,m];
    # AMPL: s.t. Weekend_Off_71 {w in 1..week_res-1, m in MEMBER}: wo[w,m] >= x_x[7+7*(w-1),m] + x_x[1+7*w,m] - 1;
    # AMPL: s.t. Weekend_Off_7lw {w in week_res..week_res, m in MEMBER}: wo[w,m] = x_x[7+7*(w-1),m];
    # AMPL: s.t. Weekend_Off_1fw { w in 0..0, m in MEMBER}: wo[w,m] = (if day0shift[m] >= shift_res - 1 then 1 else 0) * x_x[1,m];
    # AMPL: s.t. Weekend_Off_pre {w in -4..-1, m in MEMBER}: wo[w,m] = (if lastweoff[m] = w then 1 else 0);
    # AMPL: s.t. WO_Periods {per in 0..week_res, m in MEMBER}: sum {w in per-3..per} wo[w,m] >= 1;

    for m in dat.members:
        for w in range(1,week_res-1):
            m.addConstr(wo[m,w] <= x_x[m,7+7*(w-1)], "Weekend_Off_7")
            m.addConstr(wo[m,w] <= x_x[m,1+7*w], "Weekend_Off_1")
            m.addConstr(wo[m,w] >= x_x[m,7+7*(w-1)] + x_x[m,1+7*w] - 1, "Weekend_Off_71")

    for m in dat.members:
        for w in range(week_res,week_res):
            m.addConstr(wo[m,w] == x_x[m,7+7*(w-1)], "Weekend_Off_71w")

    for m in dat.members:
        for w in range(0,0):
            if dat.carryover[m]["day0shift"] >= shift_res - 1:
                m.addConstr(wo[m,w] == x_x[m,1], "Weekend_Off_1fw")
            else:
                m.addConstr(wo[m,w] == 0, "Weekend_Off_1fw")

    for m in dat.members:
        for w in range(-4,-1):
            if dat.carryover[m]["lastWEoff"] == w:
                m.addConstr(wo[m,w] == 1, "Weekend_Off_pre")
            else:
                m.addConstr(wo[m,w] == 0, "Weekend_Off_pre")

    for m in dat.members:
        for per in range(0,week_res):
            m.addConstr(quicksum(wo[w,m] for w in range(per-3,per)) >= 1, "WO_Periods")

    # AMPL: s.t. Commit_1 {d in DAY, m in MEMBER}: x_sg1[d,m] = (if leave[d,m] = 1 then 0 else (if commit[d,m] = 1 then 1 else x_sg1[d,m]));
    # AMPL: s.t. Commit_2 {d in DAY, m in MEMBER}: x_sg2[d,m] = (if leave[d,m] = 1 then 0 else (if commit[d,m] = 2 then 1 else x_sg2[d,m]));
    # AMPL: s.t. Commit_3 {d in DAY, m in MEMBER}: x_sg3[d,m] = (if leave[d,m] = 1 then 0 else (if commit[d,m] = 3 then 1 else x_sg3[d,m]));
    # AMPL: s.t. Commit_4 {d in DAY, m in MEMBER}: x_sg4[d,m] = (if leave[d,m] = 1 then 0 else (if commit[d,m] = 4 then 1 else x_sg4[d,m]));

    for m in dat.members:
        for d in dat.days:
            if dat.leave[m,d]["value"] == 1:
                m.addConstr(x_sg1[m,d] == 0, "Commit_1")
                m.addConstr(x_sg2[m,d] == 0, "Commit_2")
                m.addConstr(x_sg3[m,d] == 0, "Commit_3")
                m.addConstr(x_sg4[m,d] == 0, "Commit_4")
            elif dat.commitment[m,d]["value"] == 1:
                m.addConstr(x_sg1[m,d] == 1, "Commit_1")
            elif dat.commitment[m,d]["value"] == 2:
                m.addConstr(x_sg2[m,d] == 1, "Commit_2")
            elif dat.commitment[m,d]["value"] == 3:
                m.addConstr(x_sg3[m,d] == 1, "Commit_3")
            elif dat.commitment[m,d]["value"] == 4:
                m.addConstr(x_sg4[m,d] == 1, "Commit_4")

    # AMPL: s.t. FieldOut_Van {d in DAY, m in MEMBER}: x_dv[d,m] <= 1 - fieldout[d,m];
    # AMPL: s.t. FieldOut_SafStr {d in DAY, m in MEMBER}: x_os[d,m] <= 1 - fieldout[d,m];
  
    for m in dat.members:
        for d in dat.days:
            m.addConstr(x_dv[m,d] <= 1 - dat.fieldout[m,d]["value"], "FieldOut_Van")
            m.addConstr(x_os[m,d] <= 1 - dat.fieldout[m,d]["value"], "FieldOut_SafStr")

    # Solve
    m.optimize()

    if m.status == GRB.status.OPTIMAL:
        sln = solutionFactory.TicDat()
        sln.utilisation.append(m.objVal)
        for d in range(-1,week_res*7):
            for m in dat.members:
                if d == -1:
                    sln.roster[m,d] = dat.carryover[m]["lastWEoff"]
                elif d == 0:
                    if dat.carryover[m]["day0shift"] >= shift_res-2:
                        sln.roster[m,d] = dat.carryover[m]["day0shift"] + 81
                    else:
                        sln.roster[m,d] = dat.carryover[m]["day0shift"]
                else:
                    sln.roster[m,d] = x_dv1[m,d] * 1 + x_dv2[m,d] * 2 + x_dv3[m,d] * 3 + x_dr1[m,d] * 4 + x_dr2[m,d] * 5 + x_dr3[m,d] * 6 + x_ds1[m,d] * 7 + x_ds2[m,d] * 8 + x_ds3[m,d] * 9 + x_sg1[m,d] * 10 + x_sg2[m,d] * 11 + x_sg3[m,d] * 12 + x_sg4[m,d] * 13 + x_sf[m,d] * 14 + x_os[m,d] * 15 + x_or[m,d] * 16 + dat.leave[m,d]["value"] * 98 + (x_x[m,d] - dat.leave[m,d]["value"]) * 99
        return freeze_me(sln)

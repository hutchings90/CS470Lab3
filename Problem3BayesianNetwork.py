class BayesianNetwork:
    af = [
        [True, True, .1],
        [False, True, .9],
        [True, False, .9],
        [False, False, .1]
    ]
    dvfrs = [
        [True, True, .1],
        [False, True, .9],
        [True, False, .9],
        [False, False, .1]
    ]
    ppshg = [
        [True, True, .7],
        [False, True, .3],
        [True, False, .6],
        [False, False, .4],
    ]
    frsm = [
        [True, True, .9],
        [False, True, .1],
        [True, False, .2],
        [False, False, .8]
    ]
    fm = [
        [True, True, .49],
        [False, True, .51],
        [True, False, .7],
        [False, False, .3]
    ]
    kppm = [
        [True, True, True, .9],
        [False, True, True, .1],
        [True, False, True, .6],
        [False, False, True, .4],
        [True, True, False, .3],
        [False, True, False, .7],
        [True, False, False, .6],
        [False, False, False, .4],
    ]
    oshgf = [
        [True, True, True, .25],
        [False, True, True, .75],
        [True, False, True, .1],
        [False, False, True, .9],
        [True, True, False, .95],
        [False, True, False, .05],
        [True, False, False, 0],
        [False, False, False, 1],
    ]

    def prob(self):
        retVal = []
        total = 0
        for pdvfrs in BayesianNetwork.dvfrs:
            if pdvfrs[0]:
                pfrs = pdvfrs[1]
                for pfrsm in BayesianNetwork.frsm:
                    if pfrs == pfrsm[0] and pfrsm[1]:
                        partial = pdvfrs[2] * pfrsm[2]
                        total += partial
                        # print(total, partial, pfrs, pfrsm)
        retVal.append({
            'prob': 'P[DV|M](True|True): ',
            'val': round(total * 100)
        })
        total = 0
        for pdvfrs in BayesianNetwork.dvfrs:
            if pdvfrs[0] == False:
                pfrs = pdvfrs[1]
                for pfrsm in BayesianNetwork.frsm:
                    if pfrs == pfrsm[0] and pfrsm[1]:
                        partial = pdvfrs[2] * pfrsm[2]
                        total += partial
                        # print(total, partial, pfrs, pfrsm)
        retVal.append({
            'prob': 'P[DV|M](False|True)]: ',
            'val': round(total * 100)
        })
        total = 0
        for paf in BayesianNetwork.af:
            if paf[0]:
                pf = paf[1]
                for pfm in BayesianNetwork.fm:
                    if pfm[0] == pf and pfm[1]:
                        partial = paf[2] * pfm[2]
                        total += partial
                        # print(total, partial, paf, pfm)
        retVal.append({
            'prob': 'P[A|M](True|True): ',
            'val': round(total * 100)
        })
        total = 0
        for paf in BayesianNetwork.af:
            if paf[0] == False:
                pf = paf[1]
                for pfm in BayesianNetwork.fm:
                    if pfm[0] == pf and pfm[1]:
                        partial = paf[2] * pfm[2]
                        total += partial
                        # print(total, partial, paf, pfm)
        retVal.append({
            'prob': 'P[A|M](False|True): ',
            'val': round(total * 100)
        })
        total = 0
        for pkppm in BayesianNetwork.kppm:
            if pkppm[0] and pkppm[2]:
                ppp = pkppm[1]
                for pppshg in BayesianNetwork.ppshg:
                    if ppp == pppshg[0] and pppshg[1]:
                        partial = pkppm[3] * pppshg[2]
                        total += partial
                        # print(total, partial, kppm, ppshg)
        retVal.append({
            'prob': 'P[K|M,SHG](True|True,True): ',
            'val': round(total * 100)
        })
        total = 0
        for pkppm in BayesianNetwork.kppm:
            if pkppm[0] == False and pkppm[2]:
                ppp = pkppm[1]
                for pppshg in BayesianNetwork.ppshg:
                    if ppp == pppshg[0] and pppshg[1]:
                        partial = pkppm[3] * pppshg[2]
                        total += partial
                        # print(total, partial, kppm, ppshg)
        retVal.append({
            'prob': 'P[K|M,SHG](False|True,True): ',
            'val': round(total * 100)
        })
        total = 0
        for poshgf in BayesianNetwork.oshgf:
            if poshgf[0] and poshgf[1]:
                pf = poshgf[2]
                for pfm in BayesianNetwork.fm:
                    if pfm[0] == pf and pfm[1]:
                        partial = poshgf[3] * pfm[2]
                        total += partial
                        # print(total, partial, kppm, ppshg)
        retVal.append({
            'prob': 'P[O|SHG,M](True|True,True): ',
            'val': round(total * 100)
        })
        total = 0
        for poshgf in BayesianNetwork.oshgf:
            if poshgf[0] == False and poshgf[1]:
                pf = poshgf[2]
                for pfm in BayesianNetwork.fm:
                    if pfm[0] == pf and pfm[1]:
                        partial = poshgf[3] * pfm[2]
                        total += partial
                        # print(total, partial, kppm, ppshg)
        retVal.append({
            'prob': 'P[O|SHG,M](False|True,True): ',
            'val': round(total * 100)
        })
        return retVal

b = BayesianNetwork()
print('****************************************************************')
results = b.prob()
total = 0
i = 1
for result in results:
    print(result['prob'], result['val'])
    total += result['val']
    if i % 2 == 0:
        print(total)
        total = 0
    i += 1
print('****************************************************************\n')

class BayesianNetwork:
    af = [
        [True, True, .1],
        [False, True, .9],
        [True, False, .9],
        [False, False, .1]
    ]
    dvfrs = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .9],
        [False, False, .1]
    ]
    ppshg = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .6],
        [False, False, .4],
    ]
    frsm = [
        [True, True, .7],
        [False, True, .3],
        [True, False, .2],
        [False, False, .8]
    ]
    fm = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .6],
        [False, False, .4]
    ]

    kppm = [
        [True, True, True, .3],
        [False, True, True, .7],
        [True, False, True, .6],
        [False, False, True, .4],
        [True, True, False, .3],
        [False, True, False, .7],
        [True, False, False, .6],
        [False, False, False, .4],
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
            'val': total
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
            'val': total
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
            'val': total
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
            'val': total
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
            'val': total
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
            'val': total
        })
        return retVal

b = BayesianNetwork()
print('****************************************************************')
results = b.prob()
total = 0
i = 1
for result in results:
    print(result['prob'] + ':', result['val'])
    total += result['val']
    if i % 2 == 0:
        print(total)
        total = 0
    i += 1
print('****************************************************************\n')

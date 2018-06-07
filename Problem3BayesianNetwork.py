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
        for dvfrs in BayesianNetwork.dvfrs:
            if dvfrs[0]:
                frs = dvfrs[1]
                for frsm in BayesianNetwork.frsm:
                    if frs == frsm[0] and frsm[1]:
                        partial = dvfrs[2] * frsm[2]
                        total += partial
                        # print(total, partial, frs, frsm)
        retVal.append({
            'prob': 'P[DV|M](True|True): ',
            'val': total
        })
        total = 0
        for dvfrs in BayesianNetwork.dvfrs:
            if dvfrs[0] == False:
                frs = dvfrs[1]
                for frsm in BayesianNetwork.frsm:
                    if frs == frsm[0] and frsm[1]:
                        partial = dvfrs[2] * frsm[2]
                        total += partial
                        # print(total, partial, frs, frsm)
        retVal.append({
            'prob': 'P[DV|M](False|True)]: ',
            'val': total
        })
        total = 0
        for af in BayesianNetwork.af:
            if af[0]:
                f = af[1]
                for fm in BayesianNetwork.fm:
                    if fm[0] == f and fm[1]:
                        partial = af[2] * fm[2]
                        total += partial
                        # print(total, partial, af, fm)
        retVal.append({
            'prob': 'P[A|M](True|True): ',
            'val': total
        })
        total = 0
        for af in BayesianNetwork.af:
            if af[0] == False:
                f = af[1]
                for fm in BayesianNetwork.fm:
                    if fm[0] == f and fm[1]:
                        partial = af[2] * fm[2]
                        total += partial
                        # print(total, partial, af, fm)
        retVal.append({
            'prob': 'P[A|M](False|True): ',
            'val': total
        })
        total = 0
        for kppm in BayesianNetwork.kppm:
            if kppm[0] and kppm[2]:
                pp = kppm[1]
                for ppshg in BayesianNetwork.ppshg:
                    if pp == ppshg[0] and ppshg[1]:
                        partial = kppm[3] * ppshg[2]
                        total += partial
                        # print(total, partial, kppm, ppshg)
        retVal.append({
            'prob': 'P[K|M,SHG](True|True,True): ',
            'val': total
        })
        total = 0
        for kppm in BayesianNetwork.kppm:
            if kppm[0] == False and kppm[2]:
                pp = kppm[1]
                for ppshg in BayesianNetwork.ppshg:
                    if pp == ppshg[0] and ppshg[1]:
                        partial = kppm[3] * ppshg[2]
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

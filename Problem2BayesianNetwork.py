class BayesianNetwork:
    bm = [
        [True, True, .9],
        [False, True, .1],
        [True, False, .01],
        [False, False, .99]
    ]
    dm = [
        [True, True, .5],
        [False, True, .5],
        [True, False, 0],
        [False, False, 1]
    ]
    jb = [
        [True, True, .01],
        [False, True, .99],
        [True, False, .95],
        [False, False, .05]
    ]
    wjbd = [
        [True, True, True, True, .1],
        [False, True, True, True, .9],
        [True, False, True, True, .6],
        [False, False, True, True, .4],
        [True, True, False, True, .7],
        [False, True, False, True, .3],
        [True, False, False, True, 1],
        [False, False, False, True, 0],
        [True, True, True, False, 0],
        [False, True, True, False, 1],
        [True, False, True, False, .4],
        [False, False, True, False, .6],
        [True, True, False, False, .5],
        [False, True, False, False, .5],
        [True, False, False, False, 1],
        [False, False, False, False, 0]
    ]

    def prob(self):
        retVal = []
        total = 0
        for pwjbd in BayesianNetwork.wjbd:
            if pwjbd[0] == False:
                pd = pwjbd[3]
                pb = pwjbd[2]
                pj = pwjbd[1]
                for pdm in BayesianNetwork.dm:
                    if pdm[0] == pd and pdm[1]:
                        for pbm in BayesianNetwork.bm:
                            if pbm[0] == pb and pbm[1]:
                                for pjb in BayesianNetwork.jb:
                                    if pjb[0] == pj and pjb[1] == pb:
                                        partial = pwjbd[4] * pdm[2] * pbm[2] * pjb[2]
                                        total += partial
                                        # print(pwjbd, pdm, pbm, pjb)
        retVal.append({
            'prob': 'P[W|M](False|True): ',
            'val': round(total * 100)
        })
        total = 0
        for pwjbd in BayesianNetwork.wjbd:
            if pwjbd[0] == False:
                pd = pwjbd[3]
                pb = pwjbd[2]
                pj = pwjbd[1]
                for pdm in BayesianNetwork.dm:
                    if pdm[0] == pd and pdm[1] == False:
                        for pbm in BayesianNetwork.bm:
                            if pbm[0] == pb and pbm[1] == False:
                                for pjb in BayesianNetwork.jb:
                                    if pjb[0] == pj and pjb[1] == pb:
                                        partial = pwjbd[4] * pdm[2] * pbm[2] * pjb[2]
                                        total += partial
                                        # print(total, partial, pdm, pbm, pjb)
        retVal.append({
            'prob': 'P[W|M](False|False): ',
            'val': round(total * 100)
        })
        return retVal

b = BayesianNetwork()
print('****************************************************************')
results = b.prob()
for result in results:
    print(result['prob'], result['val'])
print('****************************************************************\n')

class BayesianNetwork:
    bm = [
        [True, True, .42],
        [False, True, .58],
        [True, False, .3],
        [False, False, .7]
    ]
    dm = [
        [True, True, .5],
        [False, True, .5],
        [True, False, 0],
        [False, False, 1]
    ]
    jb = [
        [True, True, .05],
        [False, True, .95],
        [True, False, .4],
        [False, False, .6]
    ]
    wjbd = [
        [True, True, True, True, .3],
        [False, True, True, True, .7],
        [True, False, True, True, .65],
        [False, False, True, True, .35],
        [True, True, False, True, .65],
        [False, True, False, True, .35],
        [True, False, False, True, 1],
        [False, False, False, True, 0],
        [True, True, True, False, .1],
        [False, True, True, False, .9],
        [True, False, True, False, .6],
        [False, False, True, False, .4],
        [True, True, False, False, .6],
        [False, True, False, False, .4],
        [True, False, False, False, .9],
        [False, False, False, False, .1]
    ]

    def prob(self, w, m):
        print('w:', w, '\nm:', m)
        total = 0
        for pwjbd in BayesianNetwork.wjbd:
            if pwjbd[0] == w:
                j = pwjbd[1]
                b = pwjbd[2]
                d = pwjbd[3]
                for pbm in BayesianNetwork.bm:
                    if pbm[0] == b and pbm[1] == m:
                        for pdm in BayesianNetwork.dm:
                            if pdm[0] == d and pdm[1] == m:
                                for pjb in BayesianNetwork.jb:
                                    if pjb[0] == j:
                                        partial = pbm[2] * pwjbd[4] * pdm[2] * pjb[2]
                                        total += partial
                                        # print(partial, pbm, pwjbd, pdm, pjb)
        return round(total * 100)

b = BayesianNetwork()
print('****************************************************************\n', b.prob(False, True), '\n****************************************************************\n')
print('****************************************************************\n', b.prob(False, False), '\n****************************************************************\n')

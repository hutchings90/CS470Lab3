from RandomVariable import RandomVariable

class BayesianNetwork:
    af = [
        [True, True, .1],
        [False, True, .9],
        [True, False, .9],
        [False, False, .1]
    ]
    dvm = [
        [True, True, .5],
        [False, True, .5],
        [True, False, .5],
        [False, False, .5]
    ]
    rsdshg = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .6],
        [False, False, .4],
        [True, True, .03],
    ]
    mpp = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .6],
        [False, False, .4]
    ]
    mf = [
        [True, True, .3],
        [False, True, .7],
        [True, False, .6],
        [False, False, .4]
    ]

    krsdm = [
        [True, True, True, .3],
        [False, True, True, .7],
        [True, False, True, .6],
        [False, False, True, .4],
        [True, True, False, .3],
        [False, True, False, .7],
        [True, False, False, .6],
        [False, False, False, .4],
    ]

    def prob(self, w, m):
        print('w:', w, '\nm:', m)
        retVal = {}
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
        retVal['A'] = total
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
        retVal['DV'] = total
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
        retVal['K'] = total
        return retVal

    def __str__(self):
        string = '** Bayesian Network ***************************************************************'
        for randomVariable in self.randomVariables:
            string += '\n' + str(randomVariable)
        return string + '\n***********************************************************************************'

b = BayesianNetwork()
print('****************************************************************\n', b.prob(False, True), '\n****************************************************************\n')
print('****************************************************************\n', b.prob(False, False), '\n****************************************************************\n')

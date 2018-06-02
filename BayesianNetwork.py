from RandomVariable import RandomVariable

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
        [True, True, .05],
        [False, True, .95],
        [True, False, .4],
        [False, False, .6]
    ]
    wjbd = [
        [True, True, True, True, .3],
        [False, True, True, True, .7],
        [True, False, True, True, .6],
        [False, False, True, True, .4],
        [True, True, False, True, .65],
        [False, True, False, True, .35],
        [True, False, False, True, 1],
        [False, False, False, True, 0],
        [True, True, True, False, .1],
        [False, True, True, False, .9],
        [True, False, True, False, .6],
        [False, False, True, False, .4],
        [True, True, False, False, .7],
        [False, True, False, False, .3],
        [True, False, False, False, .9],
        [False, False, False, False, .1]
    ]

    def __init__(self):
        self.b = [
            RandomVariable('w', 'Microloan'),
            RandomVariable('b', 'Start Business'),
        ]
        self.d = [
            RandomVariable('d', 'Debt'),
            RandomVariable('m', 'Microloan'),
        ]
        self.j = [
            RandomVariable('j', 'Wage-Paying Job'),
            RandomVariable('b', 'Start Business'),
        ]
        self.w = [
            RandomVariable('w', 'Woman in Poverty'),
            RandomVariable('j', 'Wage-Paying Job'),
            RandomVariable('b', 'Start Business'),
            RandomVariable('d', 'Debt')
        ]

    def prob(self, w, m):
        total = 0
        for pbm in BayesianNetwork.bm:
            if pbm[1] == m:
                for pwjbd in BayesianNetwork.wjbd:
                    if pwjbd[0] == w:
                        j = pwjbd[1]
                        for pdm in BayesianNetwork.dm:
                            if pdm[1] == m:
                                for pjb in BayesianNetwork.jb:
                                    if pjb[0] == j
                                    partial = pbm[2] * pwjbd[4] * pdm[2] * pjb[2]
                                    total += partial
                                    print(partial, pbm, pwjbd, pdm, pjb)
        return total

    def __str__(self):
        string = '** Bayesian Network ***************************************************************'
        for randomVariable in self.randomVariables:
            string += '\n' + str(randomVariable)
        return string + '\n***********************************************************************************'

b = BayesianNetwork()
print('****************************************************************\n', b.prob(False, True), '\n****************************************************************\n')
print('****************************************************************\n', b.prob(False, False), '\n****************************************************************\n')

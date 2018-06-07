from RandomVariable import RandomVariable

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
        retVal = {}

        total = 0
        for fm in BayesianNetwork.fm:
            if fm[1]:
                for af in BayesianNetwork.af:
                    if af[0]:
                        partial = fm[2] * af[2]
                        total += partial
                        print(partial, fm, af)
        retVal['P(True|True)'] = total
        print()
        total = 0
        for fm in BayesianNetwork.fm:
            if fm[1]:
                for af in BayesianNetwork.af:
                    if af[0] == False:
                        partial = fm[2] * af[2]
                        total += partial
                        print(partial, fm, af)
        retVal['P[A|M](False|True)'] = total
        print()

        total = 0
        for dvfrs in BayesianNetwork.dvfrs:
            if dvfrs[0]:
                partial = 0
                for frsm in BayesianNetwork.frsm:
                    if frsm[0] and frsm[1]:
                        partial += frsm[2] * dvfrs[2]
                        print(partial, frsm, dvfrs)
                total = partial
                for frsm in BayesianNetwork.frsm:
                    if frsm[0] == False and frsm[1]:
                        partial = frsm[2] * dvfrs[2]
                        print(partial, frsm, dvfrs)
                total += partial
        print()
        retVal['P[DV|M](True|True)'] = total
        total = 0
        for dvfrs in BayesianNetwork.dvfrs:
            if dvfrs[0] == False:
                partial = 0
                for frsm in BayesianNetwork.frsm:
                    if frsm[0] and frsm[1]:
                        partial += frsm[2] * dvfrs[2]
                        print(partial, frsm, dvfrs)
                total = partial
                for frsm in BayesianNetwork.frsm:
                    if frsm[0] == False and frsm[1]:
                        partial = frsm[2] * dvfrs[2]
                        print(partial, frsm, dvfrs)
                total += partial
        print()
        retVal['P[DV|M](False|True)'] = total

        total = 0
        retVal['K'] = total
        return retVal

    def __str__(self):
        string = '** Bayesian Network ***************************************************************'
        for randomVariable in self.randomVariables:
            string += '\n' + str(randomVariable)
        return string + '\n***********************************************************************************'

b = BayesianNetwork()
print('****************************************************************\n', b.prob(), '\n****************************************************************\n')

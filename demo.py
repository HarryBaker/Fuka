__author__ = 'loaner'
from addDoc import trainingCorpus
from keywordLearner import solutionTrainer
from SpellerCorrector import Corrector


if __name__ == '__main__':

    X = Corrector('big.txt')
    print X.correct('quadratic')
    print X.correct('qudratic')
    print X.correct("quadrtic")
    print X.correct("queadrtic")

    print X.correct("equation")
    print X.correct("want")
    print X.correct("method")
    print X.correct("factor")
    print X.correct("formula")
    print X.correct("formula")
    print X.correct("formula")
    print X.correct("formula")


    CS = trainingCorpus()
    FQ = trainingCorpus()
    QF = trainingCorpus()
    SR = trainingCorpus()
    EM = trainingCorpus()
    SM = trainingCorpus()
    BU = trainingCorpus()
    #t.addDoc('WikiQuadraticEquation')
    #t.addDoc('CompleteSquareWiki')
    #t.addDoc('FactorizationWiki')
    #t.addDoc('SquareRootWiki')
    BU.addDoc('backup', ['All'])



    CS.addDoc('completeSquare_clean.txt', ['complete', 'square'])
    EM.addDoc('eliminationMethod_clean.txt', ['elimination', 'method'])
    FQ.addDoc('factorQuadratic_clean.txt', ['factor', 'square'])
    QF.addDoc('quadraticFormula_clean.txt', ['quadratic', 'formula'])
    SM.addDoc('substitutionMethod_clean.txt', ['substitution', 'method'])
    SR.addDoc('takeSquareRoot_clean.txt', ['take', 'square', 'root'])



    sentencesCS = CS.createSentances()
    sentencesFQ = FQ.createSentances()
    sentencesQF = QF.createSentances()
    sentencesSR = SR.createSentances()
    sentencesSM = SM.createSentances()
    sentencesEM = EM.createSentances()
    sentencesBU = BU.createSentances()



    stuff = solutionTrainer(sentencesCS + sentencesFQ + sentencesQF + sentencesSR + sentencesBU + sentencesBU
                            + sentencesBU, .3)

    stuff.createModel(sentencesCS, 'complete square')
    stuff.createModel(sentencesFQ, 'factor quadratic')
    stuff.createModel(sentencesQF, 'quadratic formula')
    stuff.createModel(sentencesSR, 'square root')
    #stuff.createModel(sentencesSM, 'substitution method')
    #stuff.createModel(sentencesEM, 'elimination method')


    #stuff.possibleSolutions.append('quadratic formula')
    ##stuff.possibleSolutions.append('complete the square')
    #stuff.possibleSolutions.append('take square root')
    #stuff.possibleSolutions.append('factor the quadratic')
    #stuff.possibleSolutions.append('elimination method')
    #stuff.possibleSolutions.append('substitution method')


    a = stuff.predictMethod("I want to do the quadratic formula")
    b = stuff.predictMethod("I want to do the qudratic formula")
    c = stuff.predictMethod("I want to do the quadrtic formula")
    d = stuff.predictMethod("I want to do the queadrtic formula")
    e = stuff.predictMethod(("I want to do the quadratic method, not factor the quadratic"))


    #aa = stuff.predictMethod('complete-the-squares method')
    #ab = stuff.predictMethod('complete-the-square method')
    #ac = stuff.predictMethod('complete the squares method')
    #ad = stuff.predictMethod('complete the square method')


    #ae = stuff.predictMethod("i want to replace stuff in the equation")
    #af = stuff.predictMethod("i want to break apart the equation")
    #ag = stuff.predictMethod('lets do the square root')
    #ah = stuff.predictMethod('i want to square it')
    #ai = stuff.predictMethod('use the complete the squares method')
    #aj = stuff.predictMethod('i\'ll use the method of completing the squares')
    #ak = stuff.predictMethod('komplete da skware')
    #al = stuff.predictMethod('i\'m not sure')
    #am = stuff.predictMethod('complete-the-squares method')
    #an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    ##ao = stuff.predictMethod('dunno, maybe quadratic?')
    #ap = stuff.predictMethod('i\'ll factor quadratics')
    #aq = stuff.predictMethod('i plan to complete the squares')
    ##ar = stuff.predictMethod('do a square root')
    #at = stuff.predictMethod('i have no idea')
    #au = stuff.predictMethod('help')
    #av = stuff.predictMethod('Xyzzy')
    #aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    #ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    #ay = stuff.predictMethod('Consult the i ching')
    #z23 = stuff.predictMethod('Read Tea Leaves')

    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')



    print "done"
    #print ae



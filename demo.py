__author__ = 'loaner'
from addDoc import trainingCorpus
from keywordLearner import solutionTrainer
from SpellerCorrector import Corrector
  

if __name__ == '__main__':
   # x = ('dog',3)
   # y = (4,6)
   # z = (7,)

    ##list = []
    #list.append(x)
    #list.append(y)
    #list.append(z)
    z = 'dog and cat'
    g = (z,)
    t = {g : 0}
    t = "a"
#    z = list['dog']
  #  CS = trainingCorpus()
  #  FQ = trainingCorpus()
  ##  QF = trainingCorpus()
   # SR = trainingCorpus()
   # EM = trainingCorpus()
   # SM = trainingCorpus()
   # BU = trainingCorpus()

    TC = trainingCorpus()
    TC.addTopic('complete square')
    TC.addTopic('factor quadratic')
    TC.addTopic('take square root')
    TC.addTopic('quadratic formula')
    TC.addTopic('help')
    TC.addTopic('all')



    TC.addDoc('backup', 'all')
    TC.addDoc('completeSquare_clean.txt', 'complete square')
    TC.addDoc('factorQuadratic_clean.txt', 'factor quadratic')
    TC.addDoc('quadraticFormula_clean.txt', 'quadratic formula')
    TC.addDoc('takeSquareRoot_clean.txt', 'take square root')
    TC.addDoc('Help.txt', 'help')



 #   sentencesCS = CS.createSentances()
 #   sentencesFQ = FQ.createSentances()
 #   sentencesQF = QF.createSentances()
 #   sentencesSR = SR.createSentances()
 #   sentencesSM = SM.createSentances()
 #   sentencesEM = EM.createSentances()
 #   sentencesBU = BU.createSentances()



    #stuff = solutionTrainer(sentencesCS + sentencesFQ + sentencesQF + sentencesSR + sentencesBU + sentencesBU
    #                        + sentencesBU, .3)

    model = solutionTrainer(TC, .3)

    #stuff.createModel(sentencesCS, 'complete square')
    #stuff.createModel(sentencesFQ, 'factor quadratic')
    #stuff.createModel(sentencesQF, 'quadratic formula')
    #stuff.createModel(sentencesSR, 'square root')
    #stuff.createModel(sentencesSM, 'substitution method')
    #stuff.createModel(sentencesEM, 'elimination method')


    #stuff.possibleSolutions.append('quadratic formula')
    ##stuff.possibleSolutions.append('complete the square')
    #stuff.possibleSolutions.append('take square root')
    #stuff.possibleSolutions.append('factor the quadratic')
    #stuff.possibleSolutions.append('elimination method')
    #stuff.possibleSolutions.append('substitution method')


    aa = model.predictMethod("I want to do the quadratic formula")
    ab = model.predictMethod("I want to do the qudratic formula")
    ac = model.predictMethod("I want to do the quadrtic formula")
    ad = model.predictMethod("I want to do the queadrtic formula")
    ae = model.predictMethod(("I want to do the quadratic formula, not factor the quadratic"))
    af = model.predictMethod('lets do the square root')



    ag = model.predictMethod('complete-the-squares method')
    ah = model.predictMethod('complete-the-square method')
    #ac = stuff.predictMethod('complete the squares method')
    #ad = stuff.predictMethod('complete the square method')


    #ae = stuff.predictMethod("i want to replace stuff in the equation")
    bf = model.predictMethod("i want to break apart the equation")
    #ag = stuff.predictMethod('lets do the square root')
    #ah = stuff.predictMethod('i want to square it')
    ai = model.predictMethod('use the complete the squares method')
    #aj = stuff.predictMethod('i\'ll use the method of completing the squares')
    #ak = stuff.predictMethod('komplete da skware')
    #al = stuff.predictMethod('i\'m not sure')
    #am = stuff.predictMethod('complete-the-squares method')
    #an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    ##ao = stuff.predictMethod('dunno, maybe quadratic?')
    ap = model.predictMethod('i\'ll factor quadratics')
    #aq = stuff.predictMethod('i plan to complete the squares')
    ##ar = stuff.predictMethod('do a square root')
    #at = stuff.predictMethod('i have no idea')
    #au = stuff.predictMethod('help')
    #av = stuff.predictMethod('Xyzzy')
    #aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    #ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    ay = model.predictMethod('Consult the i ching')
    #z23 = stuff.predictMethod('Read Tea Leaves')

    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')






    print "done"
    #print ae



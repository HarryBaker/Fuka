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

    # Examples

    # Quadratic formula examples
    str = "I want to do the quadratic formula"
    q = model.predictMethod(str)
    print(str)
    print (q)
    
    str = "I want to do the qudratic formula"
    q = model.predictMethod(str)
    print(str)
    print (q)
    
    str = "I want to do the quadrtic formula"
    q = model.predictMethod(str)
    print(str)
    print (q)
    
    str = "I want to do the queadrtic formula"
    q = model.predictMethod(str)
    print(str)
    print (q)
    
    str = "I want to do the quadratic formula, not factor the quadratic"
    q = model.predictMethod(str)
    print(str)
    print (q)
    
    #an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    
    # Square root method examples
    str = "lets do the square root"
    s = model.predictMethod(str)
    print(str)
    print (s)
    
    str = ""
    s = model.predictMethod(str)
    print(str)
    print (s)

    ag = model.predictMethod('lets do the square root')
    ##ar = stuff.predictMethod('do a square root')
    

    # Complete the square method examples
    str = ""
    c = model.predictMethod(str)
    print(str)
    print (c)

    ag = model.predictMethod('complete-the-squares method')
    ah = model.predictMethod('complete-the-square method')
    ac = model.predictMethod('complete the squares method')
    ad = model.predictMethod('complete the square method')
    ai = model.predictMethod('use the complete the squares method')
    aj = model.predictMethod('i\'ll use the method of completing the squares')
    ak = model.predictMethod('komplete da skware')
    #am = stuff.predictMethod('complete-the-squares method')
    #aq = stuff.predictMethod('i plan to complete the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    

    # Factor quadratic method examples
    bf = model.predictMethod("i want to break apart the equation")
    ap = model.predictMethod('i\'ll factor quadratics')
    
    
    # High confidence in two methods examples
    ah = model.predictMethod('i want to square it')
    ah = model.predictMethod('quadratic')
     ##ao = stuff.predictMethod('dunno, maybe quadratic?')
    
    # Help examples
    #al = stuff.predictMethod('i\'m not sure')
    #at = stuff.predictMethod('i have no idea')
    #au = stuff.predictMethod('help')
    
    # Unknown examples
    #av = stuff.predictMethod('Xyzzy')
    #aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    #ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    ay = model.predictMethod('Consult the i ching')
    #z23 = stuff.predictMethod('Read Tea Leaves')

    
    # User input 




    print "done"
    #print ae



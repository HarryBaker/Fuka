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
    print("Sample input and the method each is most closely associated with. \n")

    # Quadratic formula examples
    print("\n Input indicating quadratic formula \n")
    str = "I want to do the quadratic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q + "\n")
    
    str = "I want to do the qudratic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[0] + "Confidence: " + q[1]  + "\n")
    
    str = "I want to do the quadrtic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[0] + "Confidence: " + q[1]  + "\n")
    
    str = "I want to do the queadrtic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[0] + "Confidence: " + q[1]  + "\n")
    
    str = "I want to do the quadratic formula, not factor the quadratic"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[0] + "Confidence: " + q[1]  + "\n")
    
    str = "i\'d use the quadratic formula cuz itz my fave"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[0] + "Confidence: " + q[1]  + "\n")
    
    
    # Square root method examples
    print("\n Input indicating square root method \n")
    str = "lets do the square root"
    s = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + s[0] + "Confidence: " + s[1]  + "\n")
    
    str = "do a square root"
    s = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + s[0] + "Confidence: " + s[1]  + "\n")


    # Complete the square method examples
    print("\n Input indicating complete the square \n")
    str = "'complete-the-squares method'"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "complete-the-square method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "complete the squares method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "complete the square method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "use the complete the squares method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "komplete da skware"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "i plan to complete the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[0] + "Confidence: " + c[1]  + "\n")
   
    

    # Factor quadratic method examples
    print("\n Input indicating factor the quadratic method \n")
    str = "i want to break apart the equation"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[0] + "Confidence: " + f[1]  + "\n")
    
    str = "i\'ll factor quadratics"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[0] + "Confidence: " + f[1]  + "\n")
    
    str = "i\'ll find what the factors are"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[0] + "Confidence: " + f[1]  + "\n")
    
    # High confidence in two methods examples
    print("\n Input indicating high confidence in two methods \n")
    str = "i want to square it"
    t = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + t[0] + "Confidence: " + t[1]  + "\n")
    
    str = "quadratic"
    t = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + t[0] + "Confidence: " + t[1]  + "\n")
    
    str = "dunno, maybe quadratic?"
    t = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + t[0] + "Confidence: " + t[1]  + "\n")
    
    
    # Help examples
    print("\n Input indicating user is asking for help \n")
    str = "i\'m not sure"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[0] + "Confidence: " + h[1]  + "\n")
    
    str = "i have no idea"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[0] + "Confidence: " + h[1]  + "\n")
    
    str = "help"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[0] + "Confidence: " + h[1]  + "\n")
    
    
    # Unknown examples
    print("\n Unknown input \n")
    str = "Xyzzy"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[0] + "Confidence: " + u[1]  + "\n")
    
    str = "Use Kolmolgorov Turbulence"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[0] + "Confidence: " + u[1]  + "\n")
    
    str = "Factor Third-order Partial Differential Equations"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[0] + "Confidence: " + u[1]  + "\n")
    
    str = "Consult the i ching"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[0] + "Confidence: " + u[1]  + "\n")
    
    str = "Read Tea Leave"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[0] + "Confidence: " + u[1]  + "\n")

    
    # User input examples
    




    print "done"
    #print ae



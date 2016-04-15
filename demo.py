__author__ = 'loaner'
from addDoc import trainingCorpus
from keywordLearner import solutionTrainer
from SpellerCorrector import Corrector


if __name__ == '__main__':


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


    model = solutionTrainer(TC, .3)

<<<<<<< HEAD

    #aa = model.predictMethod("I want to do the quadratic formula")
    #ab = model.predictMethod("I want to do the qudratic formula")
    ac = model.predictMethod("I want to do the quadrtic formula")
    help = model.predictMethod("help me i don't know what to do")
    ad = model.predictMethod("I want to do the queadrtic formula")
    ae = model.predictMethod(("I want to do the quadratic formula, not factor the quadratic"))
    af = model.predictMethod('lets do the square root')



    ag = model.predictMethod('complete-the-squares method')
    ah = model.predictMethod('complete-the-square method')
    #ac = stuff.predictMethod('complete the squares method')
    #ad = stuff.predictMethod('complete the square method')


    #ae = stuff.predictMethod("i want to replace stuff in the equation")
    #bf = model.predictMethod("i want to break apart the equation")
    #ag = stuff.predictMethod('lets do the square root')
    #ah = stuff.predictMethod('i want to square it')
    #ai = model.predictMethod('use the complete the squares method')
    #aj = model.predictMethod('i\'ll use the method of completing the squares')
    #ak = model.predictMethod('komplete da skware')
    #al = model.predictMethod('i\'m not sure')
    #am = stuff.predictMethod('complete-the-squares method')
    #an = stuff.predictMethod('i\'d use the quadratic formula cuz itz my fave')
    ##ao = stuff.predictMethod('dunno, maybe quadratic?')
    #ap = model.predictMethod('i\'ll factor quadratics')
    #aq = stuff.predictMethod('i plan to complete the squares')
    ##ar = stuff.predictMethod('do a square root')
    #at = model.predictMethod('i have no idea')
    #au = model.predictMethod('help')
    #av = stuff.predictMethod('Xyzzy')
    #aw = stuff.predictMethod('Use Kolmolgorov Turbulence')
    #ax = stuff.predictMethod('Factor Third-order Partial Differential Equations')
    #ay = model.predictMethod('Consult the i ching')
    #z23 = stuff.predictMethod('Read Tea Leaves')

    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    ##z8 = stuff.predictMethod('i\'ll use the method of completing the squares')
    #z8 = stuff.predictMethod('i\'ll use the method of completing the squares')


=======
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
    
>>>>>>> cc1eef74d43f791a705d559abc78f8f077e7b04b




    print "done"
    #print ae



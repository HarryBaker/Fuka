__author__ = 'loaner'
from addDoc import trainingCorpus
from keywordLearner import SolutionTrainer
from SpellerCorrector import Corrector
import string
  

if __name__ == '__main__':
 
 # Compiling training corpus
    print("Compiling training corpus ...")
    TC = trainingCorpus()
    TC.addTopic('complete square')
    TC.addTopic('factor quadratic')
    TC.addTopic('take square root')
    TC.addTopic('quadratic formula')
    TC.addTopic('help')
    TC.addTopic('all')
    TC.addTopic('elimination method')
    TC.addTopic('substitution method')


 # Adding documents for each topic to training corpus
    print("Adding documents for each topic to training corpus ... ")
    TC.addDoc('backup', 'all')
    TC.addDoc('completeSquare_clean.txt', 'complete square')
    TC.addDoc('factorQuadratic_clean.txt', 'factor quadratic')
    TC.addDoc('quadraticFormula_clean.txt', 'quadratic formula')
    TC.addDoc('takeSquareRoot_clean.txt', 'take square root')
    TC.addDoc('Help.txt', 'help')
    TC.addDoc('eliminationMethod_clean.txt', 'elimination method')
    TC.addDoc('substitutionMethod_clean.txt', 'substitution method')
    
    
    # Initializaing neural network model
    print("Initializing neural network model ... ")
    model = SolutionTrainer(TC, .5)


    # Examples
    print("Demonstrating some examples ... ")
    print("\nSample input and the method each is most closely associated with: ")



    str = "I might use the substitutittiion method"
    sub = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + sub[1][1] + "\nConfidence: ")
    print sub[1][0]


    # Elimination Method examples
    print("\nInput indicating the elimination method")
    str = "i\'ll use the elimination method"
    e = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + e[1][1] + "\nConfidence: ")
    print e[1][0]

    # Substitution Method examples
    print("\nInput indicating the substitution method")
    str = "i\'ll use the substitution method"
    sub = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + sub[1][1] + "\nConfidence: ")
    print sub[1][0]

    str = "I might use the substitutittiion method"
    sub = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + sub[1][1] + "\nConfidence: ")
    print sub[1][0]


    # Quadratic formula examples
    print("\nInput indicating quadratic formula:")
    str = "I want to do the quadratic formula"
    q = model.predictMethod(str)
    t = q[1]
    print("\nInput: " + str + "\n-> Method: " + q[1][1] + "\nConfidence ")
    print q[1][0]

    str = "I want to do the qudratic formula"
    q = model.predictMethod(str)
    print("\nInput: " + str + "\n Method: " + q[1][1] + "\nConfidence: ")
    print q[1][0]
    
    str = "I want to do the quadrtic formula"
    q = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + q[1][1] + "\nConfidence: ")
    print q[1][0]
    
    str = "I want to do the queadrtic formula"
    q = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + q[1][1] + "\nConfidence: ")
    print q[1][0]
    
    str = "I want to do the quadratic formula, not factor the quadratic"
    q = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + q[1][1] + "\nConfidence: ")
    print q[1][0]
    
    str = "i\'d use the quadratic formula cuz itz my fave"
    q = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + q[1][1] + "\nConfidence: ")
    print q[1][0]
    
    
    # Square root method examples
    print("\nInput indicating square root method")
    str = "lets do the square root"
    s = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + s[1][1] + "\nConfidence: ")
    print s[1][0]
    
    str = "do a square root"
    s = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + s[1][1] + "\nConfidence: ")
    print s[1][0]


    # Complete the square method examples
    print("\nInput indicating complete the square")
    str = "'complete-the-squares method'"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "complete-the-square method"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "complete the squares method"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "complete the square method"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "use the complete the squares method"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "komplete da skware"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "i plan to complete the squares"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + c[1][1] + "\nConfidence: ")
    print c[1][0]
   
   
    # Factor quadratic method examples
    print("\nInput indicating factor the quadratic method")
    str = "i want to break apart the equation"
    f = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + f[1][1] + "\nConfidence: ")
    print f[1][0]
    
    str = "i\'ll factor quadratics"
    f = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + f[1][1] + "\nConfidence: ")
    print f[1][0]
    
    str = "i\'ll find what the factors are"
    f = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + f[1][1] + "\nConfidence: ")
    print f[1][0]


    
    
    # Help examples
    print("\nInput indicating user is asking for help")
    str = "i\'m not sure"
    h = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + h[1][1] + "\nConfidence: ")
    print h[1][0]
    
    str = "i have no idea"
    h = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + h[1][1] + "\nConfidence: ")
    print h[1][0]
    
    str = "help"
    h = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + h[1][1] + "\nConfidence: ")
    print h[1][0]




    
    
    # Unknown examples
    print("\nUnknown input")
    str = "Xyzzy"
    u = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + u[1][1] + "\nConfidence: ")
    print u[1][0]
    
    str = "Use Kolmolgorov Turbulence"
    u = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + u[1][1] + "\nConfidence: ")
    print u[1][0]
    
    str = "Factor Third-order Partial Differential Equations"
    u = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + u[1][1] + "\nConfidence: ")
    print u[1][0]
    
    str = "Consult the i ching"
    u = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + u[1][1] + "\nConfidence: ")
    print u[1][0]
    
    str = "Read Tea Leave"
    u = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + u[1][1] + "\nConfidence: ")
    print u[1][0]
    
    
    # User input examples
    print("\nTry out 5 inputs of your own")
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + i[1][1] + "\nConfidence: ")
    print i[1][0]
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + i[1][1] + "\nConfidence: ")
    print i[1][0]
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + i[1][1] + "\nConfidence: ")
    print i[1][0]
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + i[1][1] + "\nConfidence: ")
    print i[1][0]
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("\nInput: " + str + "\n-> Method: " + i[1][1] + "\nConfidence: ")
    print i[1][0]
    
    
    print "done"
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


 # Adding documents for each topic to training corpus
 print("Adding documents for each topic to training corpus ... ")
    TC.addDoc('backup', 'all')
    TC.addDoc('completeSquare_clean.txt', 'complete square')
    TC.addDoc('factorQuadratic_clean.txt', 'factor quadratic')
    TC.addDoc('quadraticFormula_clean.txt', 'quadratic formula')
    TC.addDoc('takeSquareRoot_clean.txt', 'take square root')
    TC.addDoc('Help.txt', 'help')
    
    
    # Initializaing neural network model
    print("Initializing neural network model ... ")
    model = SolutionTrainer(TC, .3)


    # Examples
    print("Demonstrating some examples ... ")
    print("\n Sample input and the method each is most closely associated with.")


    # Quadratic formula examples
    print("\n Input indicating quadratic formula")
    str = "I want to do the quadratic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "\n  Method: " + q[1][0][1] + " Confidence ")
    print q[1][0][0]
    print("\n")

    str = "I want to do the qudratic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[1][0][1] + " Confidence: ")
    print q[1][0][0]  
    print("\n")
    
    str = "I want to do the quadrtic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[1][0][1] + " Confidence: ")
    print q[1][0][0]  
    print("\n")
    
    str = "I want to do the queadrtic formula"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[1][0][1] + " Confidence: ")
    print q[1][0][0]  
    print("\n")
    
    str = "I want to do the quadratic formula, not factor the quadratic"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[1][0][1] + " Confidence: ")
    print q[1][0][0]  
    print("\n")
    
    str = "i\'d use the quadratic formula cuz itz my fave"
    q = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + q[1][0][1] + " Confidence: ")
    print q[1][0][0]  
    print("\n")
    
    
    # Square root method examples
    print("\n Input indicating square root method")
    str = "lets do the square root"
    s = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + s[1][0][1] + " Confidence: ")
    print s[1][0][0]  
    print("\n")
    
    str = "do a square root"
    s = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + s[1][0][1] + " Confidence: ")
    print s[1][0][0]  
    print("\n")


    # Complete the square method examples
    print("\n Input indicating complete the square")
    str = "'complete-the-squares method'"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "complete-the-square method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "complete the squares method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "complete the square method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "use the complete the squares method"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "komplete da skware"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "i plan to complete the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
    
    str = "i\'ll use the method of completing the squares"
    c = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + c[1][0][1] + " Confidence: ")
    print c[1][0][0]  
    print("\n")
   
   
    # Factor quadratic method examples
    print("\n Input indicating factor the quadratic method")
    str = "i want to break apart the equation"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[1][0][1] + " Confidence: ")
    print f[1][0][0]  
    print("\n")
    
    str = "i\'ll factor quadratics"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[1][0][1] + " Confidence: ")
    print f[1][0][0]  
    print("\n")
    
    str = "i\'ll find what the factors are"
    f = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + f[1][0][1] + " Confidence: ")
    print f[1][0][0]  
    print("\n")
    
    
    # Help examples
    print("\n Input indicating user is asking for help")
    str = "i\'m not sure"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[1][0][1] + " Confidence: ")
    print h[1][0][0]  
    print("\n")
    
    str = "i have no idea"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[1][0][1] + " Confidence: ")
    print h[1][0][0]  
    print("\n")
    
    str = "help"
    h = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + h[1][0][1] + " Confidence: ")
    print h[1][0][0]  
    print("\n")
    
    
    # Unknown examples
    print("\n Unknown input")
    str = "Xyzzy"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[1][0][1] + " Confidence: ")
    print u[1][0][0]  
    print("\n")
    
    str = "Use Kolmolgorov Turbulence"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[1][0][1] + " Confidence: ")
    print u[1][0][0]  
    print("\n")
    
    str = "Factor Third-order Partial Differential Equations"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[1][0][1] + " Confidence: ")
    print u[1][0][0]  
    print("\n")
    
    str = "Consult the i ching"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[1][0][1] + " Confidence: ")
    print u[1][0][0]  
    print("\n")
    
    str = "Read Tea Leave"
    u = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + u[1][0][1] + " Confidence: ")
    print u[1][0][0]  
    print("\n")
    
    
    # User input examples
    print("\n Try out 5 inputs of your own")
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + i[1][0][1] + " Confidence: ")
    print i[1][0][0]  
    print("\n")
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + i[1][0][1] + " Confidence: ")
    print i[1][0][0]  
    print("\n")
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + i[1][0][1] + " Confidence: ")
    print i[1][0][0]  
    print("\n")
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + i[1][0][1] + " Confidence: ")
    print i[1][0][0]  
    print("\n")
    
    str = input("Enter your own sample input: ")
    i = model.predictMethod(str)
    print("Input: " + str + "-> Method: " + i[1][0][1] + " Confidence: ")
    print i[1][0][0]  
    print("\n")
    
    
    print "done"
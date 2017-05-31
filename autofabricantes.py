import logging
import time

from ioutils import InputOutputOutils
from statemachine import StateMachine

class AutofabricantesExm:
    
    def __init__(self):        
        
        logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
        
        self.counter = 0;
                
        time.sleep(5)
    
        logging.info("\n---> Setup")

        self.inputOutputUtils = InputOutputOutils()
        self.inputOutputUtils.initializeInputElements()
        self.inputOutputUtils.initializeOutputElements()
        
        self.stateMachine = StateMachine(self.inputOutputUtils)
        self.stateMachine.start()
      
  
    def loop(self):

        while(True):
            logging.info("\n---> Loop (%i)", self.counter)
            self.counter = self.counter + 1
            self.stateMachine.executeTransition()
            #time.sleep(5);


    def reset(self): 

        logging.debug("\n---> Reset (%i)", self.counter)
           
        self.inputOutputUtils.initializeInputElements()

        self.inputOutputUtils.initializeOutputElements()

        self.stateMachine.reset();
 


def main():
    
    main = AutofabricantesExm()
    
    main.loop();
    
    
main()

    

import state
import io
import streamreader

class FiniteStateMachine:
    def __init__(self, states, startStateId, classes):
        self.states = states
        self.startStateId = startStateId
        self.classes = classes

        for stateId in self.states:
            self.states[stateId].setClasses(classes)

    def accepts(self, strm):
        c = strm.readChar() 
        stateId = self.startStateId
        states = self.states
        accepted = False
        while not strm.eof():
            
            # process character 
            q = states[stateId]
            stateId = states[stateId].onGoTo(c)     
        
            if stateId == state.NoTransition:
                print("That string is not accepted.")
                return
    
            c = strm.readChar()

        
        if states[stateId].isAccepting():
            print("That string is accepted by this finite state machine.")
        else:
            print("That string is not accepted.")
        
def main():

    s = input("please enter a string of a's and b's: ")
    strm = streamreader.StreamReader(io.StringIO(s))
    
    q0 = state.State(0)
    q1 = state.State(1)
    q2 = state.State(2, True) #can be any value except None
    
    classes = {"a":frozenset("a"), "b":frozenset("b")}
    
    q0.setClasses(classes)
    q1.setClasses(classes)
    q2.setClasses(classes)    
    
    q0.addTransition("a", 2)
    q0.addTransition("b", 1)
    
    q1.addTransition("a", 2)
    q1.addTransition("b", 1)
    
    q2.addTransition("b", 2)
        
    states = {0:q0, 1:q1, 2:q2}    
                 
    dfa = FiniteStateMachine(states, 0, classes)
    
    dfa.accepts(strm)
    
    
     
if __name__ == "__main__":
    main()
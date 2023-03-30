from heapq import *

### SYSTEM STATE ## 

class State:
    def __init__(self):
        self.windowState = "closed" # closed, busy or open
        self.total_wait = 0  # Total Wait time of all customers 
        self.total_customers = 0 #  Total customers served 
        self.waiting_queue =  [] # Waiting Customers 
        # testing 
        self.waitings = []
    
    
    def windowState(self):
        return self.windowState
        
    def add_customer(self):
        self.total_customers +=  1

    def get_customers_count(self):
        return self.total_customers

    def set_total_wait_time(self, time):
        self.total_wait += time
        #testing 
        self.waitings.append(time)

    def get_total_wait_time(self):
        return self.total_wait
   
   
class Event:
    def time(self):
        """
        Returns the time at which the event will be processed
        """
        return self.t
        
    def duration(self):
        """
        Returns the duration of the event  
        """
        return self.duration

    def __str__(self):
        """
        Displays Event
        """
        return self.name + "(" + str( self.t ) + "," + str(self.duration) +  ")"
    def __lt__(self, other):
        """
        Compares the event with another sorted by processing order priority
        """
        return self.t < other.t
        
class WCLOSE(Event):
    def __init__(self, time):
        self.t = time
        self.name = "WCLOSE"

    def __str__(self):
        """
        Displays Event
        """
        return self.name + "(" + str( self.t ) + ")"
    def action(self,queue,state):
        state.windowState = "closed"

class WBUSY(Event):
    def __init__(self, time, duration):
        self.t = time
        self.duration = duration 
        self.name = "WBUSY"

    def action(self,queue,state):
        state.windowState = "busy"
 
class WOPEN(Event):
    def __init__(self, time, duration):
        self.t = time
        self.duration = duration 
        self.name = "WOPEN"

    def action(self,queue,state):
    
        state.windowState = "open" 
        if len(state.waiting_queue):
            # make it busy for a period =  customer service duration 
            customer = state.waiting_queue.pop(0)  # serve a customer 
            queue.insert( WBUSY(self.t , customer[1] ) )
            # process the customer
            state.set_total_wait_time( self.t - customer[0] + customer[1])
            state.add_customer()  
            # schedule an open event again with the new opening time and duration
            # if d <= 0, then schedule a close event  
            if self.duration - customer[1] > 0: 
                queue.insert( WOPEN(self.t + customer[1], self.duration - customer[1] ) )
            else:
                queue.insert( WCLOSE(self.t + customer[1]) )
        else:
            queue.insert( WCLOSE(self.t + self.duration) )
        
class CUSTOMER(Event):
    def __init__(self, time, duration):
        self.t = time
        self.name = "CUSTOMER"
        self.duration = duration
        
    def action(self,queue,state):
        if state.windowState == "open":
            # make it busy for the customer service duration 
            queue.insert( WBUSY(self.t , self.duration ) )
            state.set_total_wait_time( self.duration)

            # process the customer
            state.add_customer() 
            state.windowState = "open"
        else:
            state.waiting_queue.append( (self.t, self.duration) )

### EVENT QUEUE ##############################################

class EventQueue:
    def __init__(self):
        self.q = []
    def notEmpty(self):
        """
        Returns true if the queue is not empty
        """
        return len(self.q) > 0
    def remaining(self):
        """
        Returns the number of events awaiting processing
        """
        return len(self.q)
    def insert(self, event):
        """ 
        Create a new event in the queue
        """
        heappush( self.q, event )
    def next(self):
        """
        Returns and removes from the queue the next event to be processed
        """
        return heappop( self.q )

### MAIN #####################################################
Q = EventQueue()


def QInsert(event):
    Q.insert(event)
    
def CustomerArrivalEvent(arrival, serviceDuration):
    Q.insert( CUSTOMER(arrival,serviceDuration))

def WindowOpenEvent(start, duration):
    Q.insert( WOPEN(start, duration) )

def WindowBusyEvent(start,duration):
    Q.insert( WBUSY(start, duration)) 

def WindowCloseEvent(time):
    Q.insert( WCLOSE(time))
 
    
S = State()

# Processing events until the queue is Q is empty
def processEvents():
    while Q.notEmpty():
        e = Q.next()
        print( e )
        e.action(Q,S)   
    i = S.get_total_wait_time()
    j = S.get_customers_count()
    print(i,j, i/j )
    print(S.waitings)

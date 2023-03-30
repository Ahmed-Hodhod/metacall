const {processEvents, WindowCloseEvent, WindowBusyEvent, WindowOpenEvent, QInsert,CustomerArrivalEvent} = require('./DisreteEventSimulator.py')

CustomerArrivalEvent(1,1)
CustomerArrivalEvent(1.1,3)
WindowOpenEvent(2,5) // the window opens at 2 and closes after 5 t i.e closes at 7 or if it processes a customer then after the customer finishes.
CustomerArrivalEvent(2,1)
CustomerArrivalEvent(3,1)
WindowOpenEvent(10,5)

// the main function to process the added events 
processEvents()

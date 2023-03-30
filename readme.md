# Discrete Event Simulator 
This is a python simulation for a Post Office model with the following characterestics:
- the post office has a window with one worker.
- the window is either open, busy or closed.
- the window opens or closes serveral times through the day with a pre-ahead schdeule  to make the worker work in internal office work. 
- if the worker is serving one customer then the window is busy till he finishes.
- if a customer comes during the window is closed or busy, then he should waits in the queue.
- the goal of this simulator is to optimize the open/close schedule [time and duaration]


# Run the Example:
- `metacall main.js`

# How to use the simulator 
You can use the simulator by inserting your events using the functions imported from the python file and then run the main.js file to see the output and how the simulator schedules the events and some statistics about the waiting time. 

Here is the application output: 
```text
     $ metacall main.js 
        CUSTOMER(1.0,1.0)
        CUSTOMER(1.1,3.0)
        WOPEN(2.0,5.0)
        CUSTOMER(2.0,1.0)
        WBUSY(2.0,1.0)
        WBUSY(2.0,1.0)
        CUSTOMER(3.0,1.0)
        WOPEN(3.0,4.0)
        WBUSY(3.0,3.0)
        WOPEN(6.0,1.0)
        WBUSY(6.0,1.0)
        WCLOSE(7.0)
        WOPEN(10.0,5.0)
        WCLOSE(15.0)
        Total Waiting Time= 11.9  Of  4  Customers. Avg Waiting Time of one Customer =   2.975
        Customers waiting times  [2.0, 1.0, 4.9, 4.0]
        Script (main.js) loaded correctly 
```

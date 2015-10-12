-- Synch vectors for the assembly of <Application_Queue(),Application_Body(), Application_requestKey_Delegate, Application_requestKey_Proxy_Manager(p), Application_requestKey_Proxy[p], Comp1, Comp2, Comp3, Comp4, Scenario>
-- with the following input specification:

Structure
p:0..2 -- IntInterval
f:0..2 -- IntInterval
val:1..4 -- IntInterval

<Application_Queue(),Application_Body(), Application_requestKey_Delegate, Application_requestKey_Proxy_Manager(p), Application_requestKey_Proxy[p], Comp1, Comp2, Comp3, Comp4, Scenario>

Vectors
<  Serve_runPeterson  Serve_runPeterson  _  _  _  _  _  _  _  _  > => Serve_runPeterson

<  _  Call_runPeterson  _  _  _  _  _  _  Queue_runPeterson  _  > => Call_runPeterson

<  Q_requestKey  _  _  _  _  _  _  Q_requestKey  _  _  > => Comp3_Q_requestKey

<  Q_IAmTheLeader  _  _  _  _  _  _  _  Q_IAmTheLeader  _  > => Comp4_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  _  _  _  _  Q_IAmNotTheLeader  _  > => Comp4_Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  _  _  _  Q_IAmTheLeader  _  _  _  _  > => Comp1_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  _  Q_IAmNotTheLeader  _  _  _  _  > => Comp1_Q_IAmNotTheLeader

<  Q_requestKey  _  _  _  _  Q_requestKey  _  _  _  _  > => Comp1_Q_requestKey

<  Q_requestKey  _  _  _  _  _  _  _  Q_requestKey  _  > => Comp4_Q_requestKey

<  Q_requestKey  _  _  _  _  _  Q_requestKey  _  _  _  > => Comp2_Q_requestKey

<  Q_IAmTheLeader  _  _  _  _  _  Q_IAmTheLeader  _  _  _  > => Comp2_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  _  _  Q_IAmNotTheLeader  _  _  _  > => Comp2_Q_IAmNotTheLeader

<  Q_IAmTheLeader  _  _  _  _  _  _  Q_IAmTheLeader  _  _  > => Comp3_Q_IAmTheLeader

<  Q_IAmNotTheLeader  _  _  _  _  _  _  Q_IAmNotTheLeader  _  _  > => Comp3_Q_IAmNotTheLeader

<  Serve_IAmTheLeader  _  _  _  _  _  _  _  _  _  > => Q_IAmTheLeader

<  Serve_IAmNotTheLeader  _  _  _  _  _  _  _  _  _  > => Q_IAmNotTheLeader

<  Serve_requestKey  Serve_requestKey  _  _  _  _  _  _  _  _  > => Serve_requestKey

<  _  Call_requestKey  Call_requestKey  _  _  _  _  _  _  _  > => Call_requestKey

<  _  R_requestKey(f)  Q_requestKey(p)  _  _  _  _  _  _  _  > => Q_requestKey(p)

<  _  _  Get_Proxy_requestKey  Get_Proxy_requestKey  _  _  _  _  _  _  > => Get_Proxy_requestKey

<  _  _  New_requestKey(p)  New_requestKey(p,f)  New_requestKey(f)&p  _  _  _  _  _  > => New_requestKey(p,f)

<  _  _  _  Recycle_requestKey(p)  R_requestKey(f)&p  _  R_requestKey(f,val)  _  _  _  > => R_requestKey(p,val)

<  _  _  _  Recycle_requestKey(p)  R_requestKey(f)&p  _  _  R_requestKey(f,val)  _  _  > => R_requestKey(p,val)

<  _  _  _  Recycle_requestKey(p)  R_requestKey(f)&p  R_requestKey(f,val)  _  _  _  _  > => R_requestKey(p,val)

<  _  _  _  Recycle_requestKey(p)  R_requestKey(f)&p  _  _  _  R_requestKey(f,val)  _  > => R_requestKey(p,val)

<  _  _  _  _  _  _  _  Q_message  Queue_message  _  > => Comp3_Comp4_Q_message

<  _  _  _  _  _  Q_message  Queue_message  _  _  _  > => Comp1_Comp2_Q_message

<  _  _  _  _  _  _  Q_message  Queue_message  _  _  > => Comp2_Comp3_Q_message

<  _  _  _  _  _  Queue_message  _  _  Q_message  _  > => Comp4_Comp1_Q_message

<  Q_runPeterson  _  _  _  _  _  _  _  _  Q_runPeterson  > => Scenario_runPeterson

<  _  _  _  _  _  _  _  _  _  Call_Scenario  > => Call_Scenario

<  _  _  _  _  _  _  _  ErrorQueue  _  _  > => Comp3_ErrorQueue

<  _  _  _  _  _  _  _  _  ErrorQueue  _  > => Comp4_ErrorQueue

<  _  _  _  _  _  ErrorQueue  _  _  _  _  > => Comp1_ErrorQueue

<  _  _  _  _  _  _  ErrorQueue  _  _  _  > => Comp2_ErrorQueue

<  ErrorQueue  _  _  _  _  _  _  _  _  _  > => Application_ErrorQueue


-- Synch vectors for the assembly of <WorkFlow_Queue(),WorkFlow_Body(), WorkFlow_Validate_Delegate, WorkFlow_Validate_Proxy_Manager(p), WorkFlow_Validate_Proxy[p], TaskDistributor, W1, W2, Scenario_WF>
-- with the following input specification:

Structure
p:0..1 -- IntInterval
xInterval:0..1 -- IntInterval
val:0..1 -- BoolType
f:0..1 -- IntInterval
res:0..1 -- IntInterval

<WorkFlow_Queue(),WorkFlow_Body(), WorkFlow_Validate_Delegate, WorkFlow_Validate_Proxy_Manager(p), WorkFlow_Validate_Proxy[p], TaskDistributor, W1, W2, Scenario_WF>

Vectors
<  Serve_runWorkflow  Serve_runWorkflow  _  _  _  _  _  _  _  > => Serve_runWorkflow

<  _  Call_runWorkflow  _  _  _  Queue_runWorkflow  _  _  _  > => Call_runWorkflow

<  Q_Validate  _  _  _  _  Q_Validate  _  _  _  > => TaskDistributor_Q_Validate

<  _  _  Q_Validate(p,xInterval)  _  _  _  _  _  _  > => Q_Validate(p,xInterval)

<  _  _  _  Recycle_Validate(p)  R_Validate(f)&p  R_Validate(f,val)  _  _  _  > => R_Validate(p,val)

<  Serve_Validate  Serve_Validate  _  _  _  _  _  _  _  > => Serve_Validate

<  _  Call_Validate  Call_Validate  _  _  _  _  _  _  > => Call_Validate

<  _  _  Get_Proxy_Validate  Get_Proxy_Validate  _  _  _  _  _  > => Get_Proxy_Validate

<  _  _  New_Validate(p)  New_Validate(p,f)  New_Validate(f)&p  _  _  _  _  > => New_Validate(p,f)

<  _  _  _  _  _  Q_Task2  _  Queue_Task2  _  > => TaskDistributor_W2_Q_Task2

<  _  _  _  _  _  Q_Task1  Queue_Task1  _  _  > => TaskDistributor_W1_Q_Task1

<  _  _  _  _  _  R_Task1(p,res)  R_Task1(p,res)  _  _  > => R_TaskDistributor_W1_Q_Task1(p,res)

<  Q_runWorkflow  _  _  _  _  _  _  _  Q_runWorkflow  > => Scenario_runWorkflow

<  _  _  _  _  _  _  _  _  Call_Scenario_WF  > => Call_Scenario_WF

<  _  _  _  _  _  ErrorQueue  _  _  _  > => TaskDistributor_ErrorQueue

<  _  _  _  _  _  _  _  ErrorQueue  _  > => W2_ErrorQueue

<  _  _  _  _  _  _  ErrorQueue  _  _  > => W1_ErrorQueue

<  ErrorQueue  _  _  _  _  _  _  _  _  > => WorkFlow_ErrorQueue


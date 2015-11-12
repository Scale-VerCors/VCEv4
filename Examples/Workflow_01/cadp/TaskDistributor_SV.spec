-- Synch vectors for the assembly of <TaskDistributor_Queue,TaskDistributor_Body, TaskDistributor_runWorkflow(), TaskDistributor_Task1_Proxy_Manager(p), TaskDistributor_Validate_Proxy_Manager(p), TaskDistributor_Task1_Proxy[p], TaskDistributor_Validate_Proxy[p]>
-- with the following input specification:

Structure
p:0..1 -- IntInterval
cxval0:0..1 -- IntInterval
cxval1:0..1 -- BoolType

<TaskDistributor_Queue,TaskDistributor_Body, TaskDistributor_runWorkflow(), TaskDistributor_Task1_Proxy_Manager(p), TaskDistributor_Validate_Proxy_Manager(p), TaskDistributor_Task1_Proxy[p], TaskDistributor_Validate_Proxy[p]>

Vectors
<  Q_runWorkflow  _  _  _  _  _  _  > => Queue_runWorkflow

<  Serve_runWorkflow  Serve_runWorkflow  _  _  _  _  _  > => Serve_runWorkflow

<  _  Call_runWorkflow  Call_runWorkflow  _  _  _  _  > => Call_runWorkflow

<  _  R_runWorkflow  R_runWorkflow  _  _  _  _  > => R_runWorkflow

<  _  _  Q_Task2  _  _  _  _  > => Q_Task2

<  _  _  Get_Proxy_Task1  Get_Proxy_Task1  _  _  _  > => Get_Proxy_Task1

<  _  _  New_Task1(p)  New_Task1(p)  _  New_Task1&p  _  > => New_Task1(p)

<  _  _  Q_Task1  _  _  _  _  > => Q_Task1

<  _  _  Get_Value_Task1(p)  _  _  Get_Value_Task1&p  _  > => Get_Value_Task1(p)

<  _  _  R_Get_ValueTask1  _  _  R_Get_ValueTask1&p  _  > => R_Get_ValueTask1

<  _  _  Get_Proxy_Validate  _  Get_Proxy_Validate  _  _  > => Get_Proxy_Validate

<  _  _  New_Validate(p)  _  New_Validate(p)  _  New_Validate&p  > => New_Validate(p)

<  _  _  Q_Validate  _  _  _  _  > => Q_Validate

<  _  _  Get_Value_Validate(p)  _  _  _  Get_Value_Validate&p  > => Get_Value_Validate(p)

<  _  _  R_Get_ValueValidate  _  _  _  R_Get_ValueValidate&p  > => R_Get_ValueValidate

<  _  _  _  _  _  R_Task1(cxval0)&p  _  > => R_Task1(p,cxval0)

<  _  _  _  _  _  _  R_Validate(cxval1)&p  > => R_Validate(p,cxval1)

<  ErrorQueue  _  _  _  _  _  _  > => ErrorQueue


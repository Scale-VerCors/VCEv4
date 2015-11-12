-- Synch vectors for the assembly of <W1_Queue,W1_Body, W1_Task1()>
-- with the following input specification:

Structure
fid:0..1 -- IntInterval
rr:0..1 -- IntInterval

<W1_Queue,W1_Body, W1_Task1()>

Vectors
<  Q_Task1  _  _  > => Queue_Task1

<  Serve_Task1  Serve_Task1  _  > => Serve_Task1

<  _  Call_Task1  Call_Task1  > => Call_Task1

<  _  R_Task1(fid)  R_Task1(rr)  > => R_Task1(fid,rr)

<  ErrorQueue  _  _  > => ErrorQueue


-- Synch vectors for the assembly of <Comp2_Queue,Comp2_Body, Comp2_f1(), Comp2_f4(), Comp2_f5_PM(p), Comp2_f5_Proxy[p]>
-- with the following input specification:

Structure
fid:0..1 -- IntInterval
rr:0..1 -- IntInterval
p:0..1 -- IntInterval
cxval0:0..1 -- IntInterval

<Comp2_Queue(), Comp2_Body, Comp2_f1, Comp2_f4, Comp2_f5_PM(p), Comp2_f5_Proxy[p]>

Vectors
<  Serve_f1  Serve_f1  _  _  _  _  > => Serve_f1

<  Q_f4  _  _  _  _  _  > => Queue_f4

<  _  Call_f4  _  Call_f4  _  _  > => Call_f4

<  Serve_f4  Serve_f4  _  _  _  _  > => Serve_f4

<  _  R_f1(fid)  R_f1(rr)  _  _  _  > => R_f1(fid,rr)

<  _  _  _  _  _  R_f5(cxval0)&p  > => R_f5(p,cxval0)

<  _  _  Recycle_f5(p)  _  Recycle_f5(p)  Recycle_f5&p  > => Recycle_f5(p)

<  _  _  Q_f5  _  _  _  > => Q_f5

<  _  _  R_Get_Valuef5  _  _  R_Get_Valuef5&p  > => R_Get_Valuef5

<  _  _  Get_Value_f5(p)  _  _  Get_Value_f5&p  > => Get_Value_f5(p)

<  _  _  _  _  Error_NO_MORE_PROXY  _  > => Error_NO_MORE_PROXY

<  _  Call_f1  Call_f1  _  _  _  > => Call_f1

<  _  _  Get_Proxy_f5  _  Get_Proxy_f5  _  > => Get_Proxy_f5

<  _  _  New_f5(p)  _  New_f5(p)  New_f5&p  > => New_f5(p)

<  ErrorQueue  _  _  _  _  _  > => ErrorQueue

<  _  R_f4(fid)  _  R_f4(rr)  _  _  > => R_f4(fid,rr)

<  Q_f1  _  _  _  _  _  > => Queue_f1


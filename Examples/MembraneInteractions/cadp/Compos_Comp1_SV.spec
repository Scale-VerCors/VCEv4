-- Synch vectors for the assembly of <Comp1_Queue,Comp1_Body, Comp1_f2(), Comp1_f5(), Comp1_f4_PM(p), Comp1_f3_PM(p), Comp1_f4_Proxy[p], Comp1_f3_Proxy[p]>
-- with the following input specification:

Structure
p:0..1 -- IntInterval
cxval1:0..1 -- IntInterval
fid:0..1 -- IntInterval
rr:0..1 -- IntInterval
cxval0:0..1 -- IntInterval

<Comp1_Queue(), Comp1_Body, Comp1_f2, Comp1_f5, Comp1_f4_PM(p), Comp1_f3_PM(p), Comp1_f4_Proxy[p], Comp1_f3_Proxy[p]>

Vectors
<  _  Call_f5  _  Call_f5  _  _  _  _  > => Call_f5

<  _  _  _  Get_Proxy_f4  Get_Proxy_f4  _  _  _  > => Get_Proxy_f4

<  _  _  _  Get_Value_f4(p)  _  _  Get_Value_f4&p  _  > => Get_Value_f4(p)

<  _  _  _  R_Get_Valuef3  _  _  _  R_Get_Valuef3&p  > => R_Get_Valuef3

<  _  _  _  Recycle_f3(p)  _  Recycle_f3(p)  _  Recycle_f3&p  > => Recycle_f3(p)

<  Serve_f2  Serve_f2  _  _  _  _  _  _  > => Serve_f2

<  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  > => Error_NO_MORE_PROXY

<  Q_f2  _  _  _  _  _  _  _  > => Queue_f2

<  Q_f5  _  _  _  _  _  _  _  > => Queue_f5

<  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  > => Error_NO_MORE_PROXY

<  ErrorQueue  _  _  _  _  _  _  _  > => ErrorQueue

<  _  _  _  Q_f4  _  _  _  _  > => Q_f4

<  _  _  _  _  _  _  _  R_f3(cxval1)&p  > => R_f3(p,cxval1)

<  _  R_f5(fid)  _  R_f5(rr)  _  _  _  _  > => R_f5(fid,rr)

<  _  _  _  Recycle_f4(p)  Recycle_f4(p)  _  Recycle_f4&p  _  > => Recycle_f4(p)

<  _  _  _  New_f3(p)  _  New_f3(p)  _  New_f3&p  > => New_f3(p)

<  _  _  _  Q_f3  _  _  _  _  > => Q_f3

<  _  _  _  Get_Value_f3(p)  _  _  _  Get_Value_f3&p  > => Get_Value_f3(p)

<  _  Call_f2  Call_f2  _  _  _  _  _  > => Call_f2

<  _  R_f2(fid)  R_f2(rr)  _  _  _  _  _  > => R_f2(fid,rr)

<  _  _  _  R_Get_Valuef4  _  _  R_Get_Valuef4&p  _  > => R_Get_Valuef4

<  Serve_f5  Serve_f5  _  _  _  _  _  _  > => Serve_f5

<  _  _  _  _  _  _  R_f4(cxval0)&p  _  > => R_f4(p,cxval0)

<  _  _  _  Get_Proxy_f3  _  Get_Proxy_f3  _  _  > => Get_Proxy_f3

<  _  _  _  New_f4(p)  New_f4(p)  _  New_f4&p  _  > => New_f4(p)


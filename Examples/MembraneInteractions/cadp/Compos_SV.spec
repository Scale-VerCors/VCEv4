-- Synch vectors for the assembly of <Compos_Queue(),Compos_Body(), Compos_f3_Delegate, Compos_f1_Delegate, Compos_f2_Delegate, Compos_f3_PM(p), Compos_f1_PM(p), Compos_f2_PM(p), Compos_f3_Proxy[p], Compos_f1_Proxy[p], Compos_f2_Proxy[p], Compos_Comp2>
-- with the following input specification:

Structure
p:0..1 -- IntInterval
f:0..1 -- IntInterval
res1:0..1 -- IntInterval
res00:0..1 -- IntInterval
res2:0..1 -- IntInterval
res0:0..1 -- IntInterval
val:0..1 -- IntInterval

<Compos_Queue(), Compos_Body, Compos_f1_Delegate, Compos_f2_Delegate, Compos_f5_Delegate, Compos_f3_Delegate, Compos_f4_Delegate, Compos_f1_PM(p), Compos_f2_PM(p), Compos_f5_PM(p), Compos_f3_PM(p), Compos_f4_PM(p), Compos_f1_Proxy[p], Compos_f2_Proxy[p], Compos_f5_Proxy[p], Compos_f3_Proxy[p], Compos_f4_Proxy[p], Compos_Comp2, Compos_Comp1>

Vectors
<  _  _  _  _  _  _  Get_Proxy_f4  _  _  _  _  Get_Proxy_f4  _  _  _  _  _  _  _  > => Get_Proxy_f4

<  _  _  _  _  _  New_f3(p)  _  _  _  _  New_f3(p,f)  _  _  _  _  New_f3(f)&p  _  _  _  > => New_f3(p,f)

<  _  _  _  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  _  _  _  _  _  > => Error_NO_MORE_PROXY

<  Q_f3  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  Q_f3  > => Comp1_Q_f3

<  _  Call_f2  _  Call_f2  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Call_f2

<  ErrorQueue  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Compos_ErrorQueue

<  _  Call_f1  Call_f1  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Call_f1

<  _  _  _  _  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  _  _  _  _  > => Error_NO_MORE_PROXY

<  _  _  _  _  _  _  _  _  Recycle_f2(p)  _  _  _  _  R_f2(f)&p  _  _  _  _  R_f2(p,res1)  > => R_f2(f,res1)

<  Serve_f4  Serve_f4  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Serve_f4

<  Q_f2  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Queue_f2

<  _  _  _  _  _  _  _  _  _  _  _  Recycle_f4(p)  _  _  _  _  R_f4(f)&p  R_f4(p,res00)  _  > => R_f4(f,res00)

<  _  _  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  _  _  _  _  _  _  > => Error_NO_MORE_PROXY

<  _  _  _  _  _  _  _  _  _  Recycle_f5(p)  _  _  _  _  R_f5(f)&p  _  _  R_f5(f,res2)  _  > => R_f5(p,res2)

<  _  _  _  _  New_f5(p)  _  _  _  _  New_f5(p,f)  _  _  _  _  New_f5(f)&p  _  _  _  _  > => New_f5(p,f)

<  _  _  _  _  _  Get_Proxy_f3  _  _  _  _  Get_Proxy_f3  _  _  _  _  _  _  _  _  > => Get_Proxy_f3

<  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  ErrorQueue  _  > => Comp2_ErrorQueue

<  _  _  _  Get_Proxy_f2  _  _  _  _  Get_Proxy_f2  _  _  _  _  _  _  _  _  _  _  > => Get_Proxy_f2

<  _  Call_f5  _  _  Call_f5  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Call_f5

<  _  R_f5  _  _  Q_f5(p)  _  _  _  _  _  _  _  _  _  _  _  _  _  Queue_f5(p)  > => QSub_f5(p)

<  _  _  _  _  _  _  New_f4(p)  _  _  _  _  New_f4(p,f)  _  _  _  _  New_f4(f)&p  _  _  > => New_f4(p,f)

<  Serve_f2  Serve_f2  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Serve_f2

<  _  _  New_f1(p)  _  _  _  _  New_f1(p,f)  _  _  _  _  New_f1(f)&p  _  _  _  _  _  _  > => New_f1(p,f)

<  Q_f5  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  Q_f5  _  > => Comp2_Q_f5

<  _  _  _  _  _  _  _  Recycle_f1(p)  _  _  _  _  R_f1(f)&p  _  _  _  _  R_f1(p,res0)  _  > => R_f1(f,res0)

<  _  R_f4  _  _  _  _  Q_f4(p)  _  _  _  _  _  _  _  _  _  _  Queue_f4(p)  _  > => QSub_f4(p)

<  _  R_f3  _  _  _  Q_f3(p)  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Q_f3(p)

<  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  > => Comp2_Error_NO_MORE_PROXY

<  _  _  _  _  Get_Proxy_f5  _  _  _  _  Get_Proxy_f5  _  _  _  _  _  _  _  _  _  > => Get_Proxy_f5

<  _  _  _  New_f2(p)  _  _  _  _  New_f2(p,f)  _  _  _  _  New_f2(f)&p  _  _  _  _  _  > => New_f2(p,f)

<  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  _  _  _  _  _  _  _  _  > => Error_NO_MORE_PROXY

<  Serve_f1  Serve_f1  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Serve_f1

<  Serve_f3  Serve_f3  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Serve_f3

<  _  Call_f4  _  _  _  _  Call_f4  _  _  _  _  _  _  _  _  _  _  _  _  > => Call_f4

<  _  Call_f3  _  _  _  Call_f3  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Call_f3

<  _  R_f1  Q_f1(p)  _  _  _  _  _  _  _  _  _  _  _  _  _  _  Queue_f1(p)  _  > => QSub_f1(p)

<  _  _  _  _  _  _  _  _  _  _  Recycle_f3(p)  _  _  _  _  R_f3(f)&p  _  _  R_f3(f,val)  > => R_f3(p,val)

<  Serve_f5  Serve_f5  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Serve_f5

<  Q_f1  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  > => Queue_f1

<  _  _  Get_Proxy_f1  _  _  _  _  Get_Proxy_f1  _  _  _  _  _  _  _  _  _  _  _  > => Get_Proxy_f1

<  _  R_f2  _  Q_f2(p)  _  _  _  _  _  _  _  _  _  _  _  _  _  _  Queue_f2(p)  > => QSub_f2(p)

<  _  _  _  _  _  _  _  _  Error_NO_MORE_PROXY  _  _  _  _  _  _  _  _  _  _  > => Error_NO_MORE_PROXY


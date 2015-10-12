-- Synch vectors for the assembly of <Comp2_Queue,Comp2_Body, Comp2_message(), Comp2_encrypt(key), Comp2_isActive_ac(), Comp2_left_ac(), Comp2_cnum_ac(), Comp2_max_ac(), Comp2_requestKey_Proxy_Manager(px0), Comp2_requestKey_Proxy[px0]>
-- with the following input specification:

Structure
px0:0..2 -- IntType
cxval0:1..4 -- IntInterval

<Comp2_Queue,Comp2_Body, Comp2_message(), Comp2_encrypt(key), Comp2_isActive_ac(), Comp2_left_ac(), Comp2_cnum_ac(), Comp2_max_ac(), Comp2_requestKey_Proxy_Manager(px0), Comp2_requestKey_Proxy[px0]>

Vectors
<  Q_message  _  _  _  _  _  _  _  _  _  > => Queue_message

<  Serve_message  Serve_message  _  _  _  _  _  _  _  _  > => Serve_message

<  _  Call_message  Call_message  _  _  _  _  _  _  _  > => Call_message

<  _  R_message  R_message  _  _  _  _  _  _  _  > => R_message

<  _  _  Q_IAmTheLeader  _  _  _  _  _  _  _  > => Q_IAmTheLeader

<  _  _  Get_Proxy_requestKey  _  _  _  _  _  Get_Proxy_requestKey  _  > => Get_Proxy_requestKey

<  _  _  New_requestKey(px0)  _  _  _  _  _  New_requestKey(px0)  New_requestKey&px0  > => New_requestKey(px0)

<  _  _  Q_requestKey  _  _  _  _  _  _  _  > => Q_requestKey

<  _  _  Get_Value_requestKey(px0)  _  _  _  _  _  _  Get_Value_requestKey&px0  > => Get_Value_requestKey(px0)

<  _  _  R_Get_ValuerequestKey  _  _  _  _  _  _  R_Get_ValuerequestKey&px0  > => R_Get_ValuerequestKey

<  _  _  Q_IAmNotTheLeader  _  _  _  _  _  _  _  > => Q_IAmNotTheLeader

<  _  _  Q_message  _  _  _  _  _  _  _  > => Q_message

<  _  _  Call_encrypt  Call_encrypt  _  _  _  _  _  _  > => Call_encrypt

<  _  _  R_encrypt  R_encrypt  _  _  _  _  _  _  > => R_encrypt

<  _  _  Call_set_isActive  _  Call_set_isActive  _  _  _  _  _  > => Call_set_isActive

<  _  _  Call_get_isActive  _  Call_get_isActive  _  _  _  _  _  > => Call_get_isActive

<  _  _  R_get_isActive  _  R_get_isActive  _  _  _  _  _  > => R_get_isActive

<  _  _  Call_get_left  _  _  Call_get_left  _  _  _  _  > => Call_get_left

<  _  _  R_get_left  _  _  R_get_left  _  _  _  _  > => R_get_left

<  _  _  Call_set_left  _  _  Call_set_left  _  _  _  _  > => Call_set_left

<  _  _  Call_get_cnum  _  _  _  Call_get_cnum  _  _  _  > => Call_get_cnum

<  _  _  R_get_cnum  _  _  _  R_get_cnum  _  _  _  > => R_get_cnum

<  _  _  Call_get_max  _  _  _  _  Call_get_max  _  _  > => Call_get_max

<  _  _  R_get_max  _  _  _  _  R_get_max  _  _  > => R_get_max

<  _  _  Call_set_max  _  _  _  _  Call_set_max  _  _  > => Call_set_max

<  _  _  _  _  _  _  _  _  _  R_requestKey(cxval0)&px0  > => R_requestKey(px0,cxval0)

<  ErrorQueue  _  _  _  _  _  _  _  _  _  > => ErrorQueue


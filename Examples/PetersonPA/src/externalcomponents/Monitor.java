package externalcomponents;

import le.interfaces.MonitorItf;

public class Monitor implements MonitorItf{

	@Override
	public void IAmTheLeader(int cnum) {
		System.out.println("The leader is: " + cnum);
	}

	@Override
	public void IAmNotTheLeader(int cnum) {
		System.out.println("The leader is not: " + cnum);
	}

}

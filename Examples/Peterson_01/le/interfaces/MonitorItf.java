package le.interfaces;

import le.types.*;

import org.objectweb.proactive.core.util.wrapper.BooleanWrapper;
import org.objectweb.proactive.core.util.wrapper.IntWrapper;


public interface MonitorItf{
	public void IAmTheLeader(int cnum);
	public void IAmNotTheLeader(int cnum);
	}

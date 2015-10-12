package le.classes;

import le.types.*;
import le.interfaces.*;



import java.io.Serializable;
import org.objectweb.proactive.Body;
import org.objectweb.proactive.core.component.body.ComponentRunActive;
import org.objectweb.fractal.api.control.AttributeController;
import org.objectweb.proactive.multiactivity.component.ComponentMultiActiveService;

public class Class1 extends Class0 implements Serializable, ElectionItf, RunElection, Class1AC{




	@Override
	public void runComponentActivity(Body body) {
		ComponentMultiActiveService multiActiveService = new ComponentMultiActiveService(body);
		while (body.isActive()) {
			multiActiveService.multiActiveServing();
		}
	} 

	public  void runPeterson() {
		State curState = State.Initial1;

		while(true) {
		switch (curState) {
		case Initial1:
			C1.message(0, 1);
			curState = State.State1;
			break;
		case State1:
			return ;
		case State2:
			return ;
		default:
			return;
		}
		}

	}
	

}

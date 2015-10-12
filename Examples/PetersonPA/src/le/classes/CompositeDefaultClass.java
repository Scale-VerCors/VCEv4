package le.classes;

import le.types.*;
import le.interfaces.*;



import java.io.Serializable;
import org.objectweb.proactive.Body;
import org.objectweb.proactive.core.component.body.ComponentRunActive;
import org.objectweb.fractal.api.control.AttributeController;
import org.objectweb.proactive.multiactivity.component.ComponentMultiActiveService;

public class CompositeDefaultClass implements Serializable, ComponentRunActive, AttributeController{




	@Override
	public void runComponentActivity(Body body) {
		ComponentMultiActiveService multiActiveService = new ComponentMultiActiveService(body);
		while (body.isActive()) {
			multiActiveService.multiActiveServing();
		}
	} 


}

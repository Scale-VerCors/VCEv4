package wf.classes;

import wf.types.*;
import wf.interfaces.*;

import java.util.HashMap;
import java.util.Map;

import org.objectweb.fractal.api.NoSuchInterfaceException;
import org.objectweb.fractal.api.control.BindingController;
import org.objectweb.fractal.api.control.IllegalBindingException;
import org.objectweb.fractal.api.control.IllegalLifeCycleException;
import org.objectweb.proactive.core.util.wrapper.IntWrapper;
import org.objectweb.proactive.core.util.wrapper.BooleanWrapper;


import java.io.Serializable;
import org.objectweb.proactive.Body;
import org.objectweb.proactive.core.component.body.ComponentRunActive;
import org.objectweb.fractal.api.control.AttributeController;
import org.objectweb.proactive.multiactivity.component.ComponentMultiActiveService;

public class TaskDistributor implements Serializable, BindingController, ComponentRunActive, RunWorkflow{


	protected Interface1 C1;
	protected Interface2 C2;
	protected Interface3 C3;

	@Override
	public void bindFc(String myClientItf, Object serverItf) throws NoSuchInterfaceException, IllegalBindingException, IllegalLifeCycleException {
		switch(myClientItf) {
		case "C1":
			this.C1 =  (Interface1) serverItf;
			break;
		case "C2":
			this.C2 =  (Interface2) serverItf;
			break;
		case "C3":
			this.C3 =  (Interface3) serverItf;
			break;
		default:
			throw new NoSuchInterfaceException(myClientItf);
		}
	}


	@Override
	public String[] listFc() {
		return new String[]{"C1", "C2", "C3"};
	}
	@Override
	public Object lookupFc(String myClientItf) throws NoSuchInterfaceException {
		switch(myClientItf) {
		case "C1":
			return this.C1;
		case "C2":
			return this.C2;
		case "C3":
			return this.C3;
		default:
			throw new NoSuchInterfaceException(myClientItf);
		}
	}


	@Override
	public void unbindFc(String myClientItf) throws NoSuchInterfaceException {
		switch(myClientItf) {
		case "C1":
			this.C1 =  null;
			break;
		case "C2":
			this.C2 =  null;
			break;
		case "C3":
			this.C3 =  null;
			break;
		default:
			throw new NoSuchInterfaceException(myClientItf);
		}
	}



	@Override
	public void runComponentActivity(Body body) {
		ComponentMultiActiveService multiActiveService = new ComponentMultiActiveService(body);
		while (body.isActive()) {
			multiActiveService.multiActiveServing();
		}
	} 

	public  void runWorkflow() {
		State curState = State.Initial1;
		IntWrapper x = null;
		BooleanWrapper b = null;

		while(true) {
		switch (curState) {
		case State1:
			C2.Task2();
			curState = State.State2;
			break;
		case Initial1:
			x=C1.Task1();
			curState = State.State1;
			break;
		case State2:
			b=C3.Validate(x.intValue());
			curState = State.State3;
			break;
		case State3:
			return ;
		case State4:
			return ;
		default:
			return;
		}
		}

	}
	

}

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

public class Class2 implements Serializable, BindingController, ComponentRunActive, Interface2{



	@Override
	public void bindFc(String myClientItf, Object serverItf) throws NoSuchInterfaceException, IllegalBindingException, IllegalLifeCycleException {
		switch(myClientItf) {
		default:
			throw new NoSuchInterfaceException(myClientItf);
		}
	}


	@Override
	public String[] listFc() {
		return new String[0];
	}
	@Override
	public Object lookupFc(String myClientItf) throws NoSuchInterfaceException {
		switch(myClientItf) {
		default:
			throw new NoSuchInterfaceException(myClientItf);
		}
	}


	@Override
	public void unbindFc(String myClientItf) throws NoSuchInterfaceException {
		switch(myClientItf) {
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

	public  void Task2() {
		State curState = State.Initial1;

		while(true) {
		switch (curState) {
		case State1:
			return ;
		case Initial1:
			return ;
		default:
			return;
		}
		}

	}
	

}

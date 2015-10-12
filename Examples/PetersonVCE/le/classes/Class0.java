package le.classes;

import le.types.*;
import le.interfaces.*;

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

public class Class0 implements Serializable, BindingController, ComponentRunActive, ElectionItf, Class0AC{

	public boolean isActive = false;
	public int left = 1;
	public int cnum = 1;
	public int max = 1;

	protected ElectionItf C1;
	protected MonitorItf C2;
	protected KeyStorageItf C3;

	@Override
	public void bindFc(String myClientItf, Object serverItf) throws NoSuchInterfaceException, IllegalBindingException, IllegalLifeCycleException {
		switch(myClientItf) {
		case "C1":
			this.C1 =  (ElectionItf) serverItf;
			break;
		case "C2":
			this.C2 =  (MonitorItf) serverItf;
			break;
		case "C3":
			this.C3 =  (KeyStorageItf) serverItf;
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

	public  void message(int step, int val) {
		State curState = State.Initial;
		Boolean isActive = null;
		Integer left = null;
		Integer max = null;
		Integer cnum = null;
		IntWrapper key = null;

		while(true) {
		switch (curState) {
		case Initial:
			isActive=this.get_isActive();
			curState = State.Choice6;
			break;
		case Choice5:
			if(step == 1) {
				curState = State.Choice3;
				break;
			}
			else if(step == 2) {
				left=this.get_left();
				curState = State.Choice4;
				break;
			}
		case Choice3:
			if(val > max || val < max) {
				C1.message(2, val);
				curState = State.State1;
				break;
			}
			else if(val == max) {
				cnum=this.get_cnum();
				curState = State.State10;
				break;
			}
		case State1:
			this.set_left(val);
			curState = State.State13;
			break;
		case Choice4:
			if(left > val && left > max) {
				this.set_max(left);
				curState = State.State3;
				break;
			}
			else if(left <= val || left <= max) {
				this.set_isActive(false);
				curState = State.State9;
				break;
			}
		case State3:
			C1.message(1, left);
			curState = State.State13;
			break;
		case State13:
			return ;
		case Choice2:
			if(isActive == true) {
				max=this.get_max();
				curState = State.Choice5;
				break;
			}
			else if(isActive == false) {
				C1.message(step, val);
				curState = State.State13;
				break;
			}
		case State4:
			this.set_isActive(false);
			curState = State.State13;
			break;
		case State5:
			C2.IAmNotTheLeader(cnum);
			curState = State.State13;
			break;
		case Choice6:
			if(step == 1 || step == 2) {
				curState = State.Choice2;
				break;
			}
			else if(step == 0) {
				curState = State.Choice7;
				break;
			}
		case Choice7:
			if(isActive == true) {
				curState = State.State13;
				break;
			}
			else if(isActive == false) {
				this.set_isActive(true);
				curState = State.State6;
				break;
			}
		case State6:
			C1.message(0, val);
			curState = State.State7;
			break;
		case State7:
			max=this.get_max();
			curState = State.State8;
			break;
		case State8:
			C1.message(1, max);
			curState = State.State13;
			break;
		case State9:
			cnum=this.get_cnum();
			curState = State.State5;
			break;
		case State10:
			key=C3.requestKey();
			curState = State.State12;
			break;
		case State11:
			this.encrypt(key.intValue());
			curState = State.State4;
			break;
		case State12:
			//System.out.println("I  am the leader!" + cnum);
			curState = State.State14;
			break;
		case Final:
			return ;
		case State14:
			C2.IAmTheLeader(cnum);
			curState = State.State11;
			break;
		default:
			return;
		}
		}

	}
	
	public  void set_max(int value) {
		this.max = value;
	}
	
	public  int get_left() {
		return this.left;
	}
	
	public  void set_left(int value) {
		this.left = value;
	}
	
	public  boolean get_isActive() {
		return this.isActive;
	}
	
	public  void set_isActive(boolean value) {
		this.isActive = value;
	}
	
	public  void set_cnum(int value) {
		this.cnum = value;
	}
	
	public  int get_max() {
		return this.max;
	}
	
	public  int get_cnum() {
		return this.cnum;
	}
	
	public  void encrypt(int key) {
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

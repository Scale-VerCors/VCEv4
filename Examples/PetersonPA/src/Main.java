import java.util.HashMap;
import java.util.Map;

import le.interfaces.RunElection;

import org.objectweb.fractal.adl.Factory;
import org.objectweb.fractal.api.Component;
import org.objectweb.fractal.util.Fractal;

public class Main {
	public static void main (String[] args) {
		try {
			Component component = launchComponent("Application");
			RunElection itf;
		
			itf = (RunElection)(component.getFcInterface("S1"));
			itf.runPeterson();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	//launch a component from ADL, launch Monitor and KeyStorage and bind the component 
	//to the monitor and keyStorage
	private static Component launchComponent (String adl) throws Exception {
		  Factory f = org.objectweb.proactive.core.component.adl.FactoryFactory.getFactory();// getFactory();
		  Map<String, Object> context = new HashMap<String, Object>();
		  
		  //create components from ADL
		  Component mainComponent = (Component) f.newComponent(adl, context);
		  Component monitor = (Component) f.newComponent("Monitor", context);
		  Component keyStorage = (Component) f.newComponent("KeyStorage", context);
		  
		  //bind components
		  Fractal.getBindingController(mainComponent).bindFc("C2",
                  monitor.getFcInterface("S1"));
		  Fractal.getBindingController(mainComponent).bindFc("C3",
                  keyStorage.getFcInterface("S1"));
		  
		  //start components
		  Fractal.getLifeCycleController(mainComponent).startFc();
		  Fractal.getLifeCycleController(monitor).startFc();	
		  Fractal.getLifeCycleController(keyStorage).startFc();	
		  
		  return mainComponent;
	}
	

}

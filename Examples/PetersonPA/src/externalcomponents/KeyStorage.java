package externalcomponents;

import org.objectweb.proactive.core.util.wrapper.IntWrapper;

import le.interfaces.KeyStorageItf;

public class KeyStorage implements KeyStorageItf{

	@Override
	public IntWrapper requestKey() {
		System.out.println("The key was requested");
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("The key will be returned");
		return new IntWrapper(0);
	}

}

package mod.tolly67p.testmod;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import net.minecraftforge.fml.common.Mod;

@Mod(TestMod.MODID)
public final class TestMod {
	public static final String MODID = "testmod";

	private static final Logger LOGGER = LogManager.getLogger();

	// V a constructor I think
	public TestMod() {
		LOGGER.debug("Hello from Test Mod!");
	}

}

import static org.junit.Assert.*;

import org.junit.Test;


public class SpampedeDataTest_CellInDir {

	@Test
	public void test_getNextCellNorth() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		myData.setDirectionNorth();
		MazeCell neighborCell = myData.getNextCellInDir();
		assertEquals("[0, 2, *]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(0, 2));
	}

	@Test
	public void test_getNextCellSouth() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		myData.setDirectionSouth();
		MazeCell neighborCell = myData.getNextCellInDir();
		assertEquals("[2, 2,  ]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(2, 2));
	}
	@Test
	public void test_getNextCellEast() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		myData.setDirectionEast();
		MazeCell neighborCell = myData.getNextCellInDir();
		assertEquals("[1, 3, X]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(1, 3));
	}

	@Test
	public void test_getNextCellWest() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		myData.setDirectionWest();
		MazeCell neighborCell = myData.getNextCellInDir();
		assertEquals("[1, 1, B]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(1, 1));
	}


}

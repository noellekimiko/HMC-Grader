import static org.junit.Assert.*;

import org.junit.Test;


public class SpampedeDataTest_Neighbors {
	// Want pictures of the test boards?
	// http://tinyurl.com/spampedeTestBoards
	@Test
	public void test_NorthNeighborWithArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell focalCell = myData.getCell(2, 3);
		MazeCell neighborCell = myData.getNorthNeighbor(focalCell);
		assertEquals("[1, 3, X]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(1, 3));
	}
	@Test
	public void test_NorthNeighborWithoutArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell neighborCell = myData.getNorthNeighbor();
		assertEquals("[0, 2, *]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(0, 2));

	}
	@Test
	public void test_SouthNeighborWithArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell focalCell = myData.getCell(2, 3);
		MazeCell neighborCell = myData.getSouthNeighbor(focalCell);
		assertEquals("[3, 3,  ]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(3, 3));
	}
	@Test
	public void test_SouthNeighborWithoutArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell neighborCell = myData.getSouthNeighbor();
		assertEquals("[2, 2,  ]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(2, 2));
	}
	@Test
	public void test_EastNeighborWithArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell focalCell = myData.getCell(2, 3);
		MazeCell neighborCell = myData.getEastNeighbor(focalCell);
		assertEquals("[2, 4,  ]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(2, 4));
	}
	@Test
	public void test_EastNeighborWithoutArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell neighborCell = myData.getEastNeighbor();
		assertEquals("[1, 3, X]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(1, 3));
	}

	@Test
	public void test_WestNeighborWithArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell focalCell = myData.getCell(2, 3);
		MazeCell neighborCell = myData.getWestNeighbor(focalCell);
		assertEquals("[2, 2,  ]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(2, 2));
	}
	@Test
	public void test_WestNeighborWithoutArgument() {
		SpampedeData myData = new SpampedeData(TestGame.G1);
		MazeCell neighborCell = myData.getWestNeighbor();
		assertEquals("[1, 1, B]", neighborCell.toString());
		// check they're the same object (Not a new MazeCell!)
		assertTrue(neighborCell == myData.getCell(1, 1));
	}
}

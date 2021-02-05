<h2>573. Squirrel Simulation</h2><h3>Medium</h3><hr><div>There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the <b>minimal</b> distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most <b>one nut</b> at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
<p><b>Example 1:</b></p>

<pre><b>Input:</b> 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
<b>Output:</b> 12
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/22/squirrel_simulation.png" style="width: 40%;">​​​​​
</pre>

<p><b>Note:</b></p>

<ol>
	<li>All given positions won't overlap.</li>
	<li>The squirrel can take at most one nut at one time.</li>
	<li>The given positions of nuts have no order.</li>
	<li>Height and width are positive integers. 3 &lt;= height * width &lt;= 10,000.</li>
	<li>The given positions contain at least one nut, only one tree and one squirrel.</li>
</ol>
</div>
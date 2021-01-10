<h2>307. Range Sum Query - Mutable</h2><h3>Medium</h3><hr><div><p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> ≤ <i>j</i>), inclusive.</p>

<p>The <i>update(i, val)</i> function modifies <i>nums</i> by updating the element at index <i>i</i> to <i>val</i>.</p>

<p><b>Example:</b></p>

<pre>Given nums = [1, 3, 5]

sumRange(0, 2) -&gt; 9
update(1, 2)
sumRange(0, 2) -&gt; 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The array is only modifiable by the <i>update</i> function.</li>
	<li>You may assume the number of calls to <i>update</i> and <i>sumRange</i> function is distributed evenly.</li>
	<li><code>0 &lt;= i &lt;= j &lt;= nums.length - 1</code></li>
</ul>
</div>
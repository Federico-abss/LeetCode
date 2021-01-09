<h2>127. Word Ladder</h2><h3>Hard</h3><hr><div><p>Given two words <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>the length of the shortest transformation sequence from</em> <code>beginWord</code> <em>to</em> <code>endWord</code>, <em>such that</em>:</p>

<ul>
	<li>Only one letter can be changed at a time.</li>
	<li>Each transformed word must exist in the word list.</li>
</ul>

<p>Return <code>0</code> if there is no such transformation sequence.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
<strong>Output:</strong> 5
<strong>Explanation:</strong> As one shortest transformation is "hit" -&gt; "hot" -&gt; "dot" -&gt; "dog" -&gt; "cog", return its length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The endWord "cog" is not in wordList, therefore no possible transformation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;beginWord.length &lt;= 100</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 5000</code></li>
	<li><code>wordList[i].length ==&nbsp;beginWord.length</code></li>
	<li><code>beginWord</code>,&nbsp;<code>endWord</code>, and&nbsp;<code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord !=&nbsp;endWord</code></li>
	<li>All the strings in&nbsp;<code>wordList</code> are <strong>unique</strong>.</li>
</ul>
</div>
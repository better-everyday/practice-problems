<h2><a href="https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150">Title</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<!-- Description -->
<div class="elfjS" data-track-load="description_content"><p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s = "leetcode", wordDict = ["leet","code"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "leetcode" can be segmented as "leet code".
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s = "applepenapple", wordDict = ["apple","pen"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> false
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>
</div>

<!-- <h2>
<a href="https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1368490871?envType=daily-question&envId=2024-08-26">Results</a>
</h2>
<p>Runtime: 48ms, beats 38.87%</p>
<p>Memory: 18.28MB, beats 43.75%</p> -->

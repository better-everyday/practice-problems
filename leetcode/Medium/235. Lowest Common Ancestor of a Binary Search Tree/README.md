<h2><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/">235. Lowest Common Ancestor of a Binary Search Tree</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<!-- Description -->
<div class="elfjS" data-track-load="description_content"><p>Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: “The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <strong>a node to be a descendant of itself</strong>).”</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;">
<pre style="position: relative;"><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> The LCA of nodes 2 and 8 is 6.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;">
<pre style="position: relative;"><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> root = [2,1], p = 2, q = 1
<strong>Output:</strong> 2
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the BST.</li>
</ul>
</div>

<!-- <h2>
<a href="https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1368490871?envType=daily-question&envId=2024-08-26">Results</a>
</h2>
<p>Runtime: 48ms, beats 38.87%</p>
<p>Memory: 18.28MB, beats 43.75%</p> -->

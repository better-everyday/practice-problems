<h2><a href="https://neetcode.io/problems/meeting-schedule-ii">253. Meeting Rooms II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<!-- Description -->
<div class="my-article-component-container ng-star-inserted"><div><p style="font-size: 17px;">Given an array of meeting time interval objects consisting of start and end times <code class="hljs language-scheme" style="font-size: 14.5px;">[[start_1,end_1],[start_2,end_2],...] (start_i &lt; end_i)</code>, find the minimum number of days required to schedule all meetings without any conflicts.</p>
<p style="font-size: 17px;"><strong>Example 1:</strong></p>
<div class="code-toolbar"><pre class="language-java" tabindex="0"><code class="hljs language-java" style="font-size: 14.5px;"><span class="token class-name" style="font-size: 14.5px;">Input</span><span class="token operator" style="font-size: 14.5px;">:</span> intervals <span class="token operator" style="font-size: 14.5px;">=</span> <span class="token punctuation" style="font-size: 14.5px;">[</span><span class="token punctuation" style="font-size: 14.5px;">(</span><span class="token number" style="font-size: 14.5px;">0</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token number" style="font-size: 14.5px;">40</span><span class="token punctuation" style="font-size: 14.5px;">)</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token punctuation" style="font-size: 14.5px;">(</span><span class="token number" style="font-size: 14.5px;">5</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token number" style="font-size: 14.5px;">10</span><span class="token punctuation" style="font-size: 14.5px;">)</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token punctuation" style="font-size: 14.5px;">(</span><span class="token number" style="font-size: 14.5px;">15</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token number" style="font-size: 14.5px;">20</span><span class="token punctuation" style="font-size: 14.5px;">)</span><span class="token punctuation" style="font-size: 14.5px;">]</span>

<span class="token class-name" style="font-size: 14.5px;">Output</span><span class="token operator" style="font-size: 14.5px;">:</span> <span class="token number" style="font-size: 14.5px;">2</span>
</code></pre><div class="toolbar"><div class="toolbar-item"><button class="copy-to-clipboard-button" type="button" data-copy-state="copy"><span>Copy</span></button></div></div></div>
<p style="font-size: 17px;">Explanation:<br>day1: (0,40)<br>day2: (5,10),(15,20)</p>
<p style="font-size: 17px;"><strong>Example 2:</strong></p>
<div class="code-toolbar"><pre class="language-java" tabindex="0"><code class="hljs language-java" style="font-size: 14.5px;"><span class="token class-name" style="font-size: 14.5px;">Input</span><span class="token operator" style="font-size: 14.5px;">:</span> intervals <span class="token operator" style="font-size: 14.5px;">=</span> <span class="token punctuation" style="font-size: 14.5px;">[</span><span class="token punctuation" style="font-size: 14.5px;">(</span><span class="token number" style="font-size: 14.5px;">4</span><span class="token punctuation" style="font-size: 14.5px;">,</span><span class="token number" style="font-size: 14.5px;">9</span><span class="token punctuation" style="font-size: 14.5px;">)</span><span class="token punctuation" style="font-size: 14.5px;">]</span>

<span class="token class-name" style="font-size: 14.5px;">Output</span><span class="token operator" style="font-size: 14.5px;">:</span> <span class="token number" style="font-size: 14.5px;">1</span>
</code></pre><div class="toolbar"><div class="toolbar-item"><button class="copy-to-clipboard-button" type="button" data-copy-state="copy"><span>Copy</span></button></div></div></div>
<p style="font-size: 17px;"><strong>Note:</strong></p>
<ul style="font-size: 17px;">
<li>(0,8),(8,10) is not considered a conflict at 8</li>
</ul>
<p style="font-size: 17px;"><strong>Constraints:</strong></p>
<ul style="font-size: 17px;">
<li><code class="hljs language-basic" style="font-size: 14.5px;">0 &lt;= intervals.length &lt;= 500</code></li>
<li><code class="hljs language-basic" style="font-size: 14.5px;">0 &lt;= intervals[i].start &lt; intervals[i].end &lt;= 1,000,000</code></li>
</ul>
</div></div>

<!-- <h2>
<a href="https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1368490871?envType=daily-question&envId=2024-08-26">Results</a>
</h2>
<p>Runtime: 48ms, beats 38.87%</p>
<p>Memory: 18.28MB, beats 43.75%</p> -->

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="Chayce Ross" />
  <title>MATH318 - HW # 1</title>
  <style type="text/css">
    @media (max-width: 600px) {
      body {
        font-size: 0.9em;
        padding: 12px;
      }
      h1 {
        font-size: 1.8em;
      }
    }
    @media print {
      html {
        background-color: white;
      }
      body {
        background-color: transparent;
        color: black;
        font-size: 12pt;
      }
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      h2, h3, h4 {
        page-break-after: avoid;
      }
    }
    p {
      margin: 1em 0;
    }
    a {
      color: #1a1a1a;
    }
    a:visited {
      color: #1a1a1a;
    }
    img {
      max-width: 100%;
    }
    svg {
      height: auto;
      max-width: 100%;
    }
    h1, h2, h3, h4, h5, h6 {
      margin-top: 1.4em;
    }
    h5, h6 {
      font-size: 1em;
      font-style: italic;
    }
    h6 {
      font-weight: normal;
    }
    ol, ul {
      padding-left: 1.7em;
      margin-top: 1em;
    }
    li > ol, li > ul {
      margin-top: 0;
    }
    blockquote {
      margin: 1em 0 1em 1.7em;
      padding-left: 1em;
      border-left: 2px solid #e6e6e6;
      color: #606060;
    }
    code {
      font-family: Menlo, Monaco, Consolas, 'Lucida Console', monospace;
      font-size: 85%;
      margin: 0;
      hyphens: manual;
    }
    pre {
      margin: 1em 0;
      overflow: auto;
    }
    pre code {
      padding: 0;
      overflow: visible;
      overflow-wrap: normal;
    }
    .sourceCode {
     background-color: transparent;
     overflow: visible;
    }
    hr {
      background-color: #1a1a1a;
      border: none;
      height: 1px;
      margin: 1em 0;
    }
    table {
      margin: 1em 0;
      border-collapse: collapse;
      width: 100%;
      overflow-x: auto;
      display: block;
      font-variant-numeric: lining-nums tabular-nums;
    }
    table caption {
      margin-bottom: 0.75em;
    }
    tbody {
      margin-top: 0.5em;
      border-top: 1px solid #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
    }
    th {
      border-top: 1px solid #1a1a1a;
      padding: 0.25em 0.5em 0.25em 0.5em;
    }
    td {
      padding: 0.125em 0.5em 0.25em 0.5em;
    }
    header {
      margin-bottom: 4em;
      text-align: center;
    }
    #TOC li {
      list-style: none;
    }
    #TOC ul {
      padding-left: 1.3em;
    }
    #TOC > ul {
      padding-left: 0;
    }
    #TOC a:not(:hover) {
      text-decoration: none;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    /* The extra [class] is a hack that increases specificity enough to
       override a similar rule in reveal.js */
    ul.task-list[class]{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      font-size: inherit;
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    /* CSS for citations */
    div.csl-bib-body { }
    div.csl-entry {
      clear: both;
      margin-bottom: 0em;
    }
    .hanging-indent div.csl-entry {
      margin-left:2em;
      text-indent:-2em;
    }
    div.csl-left-margin {
      min-width:2em;
      float:left;
    }
    div.csl-right-inline {
      margin-left:2em;
      padding-left:1em;
    }
    div.csl-indent {
      margin-left: 2em;
    }  </style>
  <script src="https://cdnjs.cloudflare.com/polyfill/v3/polyfill.min.js?features=es6"></script>
  <script
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"
  type="text/javascript"></script>
</head>
<body>
<div id="header">
<h1 class="title">MATH318 - HW # 1</h1>
<h2 class="author">Chayce Ross</h2>
</div>
<h1 class="unnumbered" id="question-1">Question 1</h1>
<table>
<thead>
<tr class="header">
<th colspan="2" style="text-align: center;"><strong>Space</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;">Outcome</td>
<td style="text-align: center;">P(Outcome)</td>
</tr>
<tr class="even">
<td style="text-align: center;">HH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{2} =
0.25\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">THH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{3} =
0.125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">HTHH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{4} =
0.0625\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">TTHH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{4} =
0.0625\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">TTTTT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">HTTTT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">THTTT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">TTHTT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">TTTHT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">TTTTH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">HTHTT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">HTTHT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">HTTTH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">THTHT</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">THTTH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">TTHTH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">TTTHH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">HTHTH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td style="text-align: center;">HTTHH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="odd">
<td style="text-align: center;">THTHH</td>
<td style="text-align: center;"><span class="math inline">\((0.5)^{5} =
0.03125\)</span></td>
</tr>
<tr class="even">
<td colspan="2" style="text-align: center;"><span
class="math inline">\(\sum_{O} P(O) = P(S) = 1  \quad
\checkmark\)</span></td>
</tr>
</tbody>
</table>
<h1 class="unnumbered" id="question-2">Question 2</h1>
<ol>
<li><p><span class="math inline">\(F E^{c} G^{c}\)</span></p></li>
<li><p><span class="math inline">\(EFG^{c}\)</span></p></li>
<li><p><span class="math inline">\(E \cup F \cup G\)</span></p></li>
<li><p><span class="math inline">\(EF \cup EG \cup GF\)</span></p></li>
<li><p><span class="math inline">\(EFG\)</span></p></li>
<li><p><span class="math inline">\(E^{c} F^{c} G^{c}\)</span></p></li>
<li><p><span class="math inline">\(EF^{c} G^{c} \cup E^{c} FG^{c} \cup
E^{c} F^{c} G \cup E^{c} F^{c} G^{c}\)</span></p></li>
<li><p><span class="math inline">\((EFG)^{c}\)</span></p></li>
</ol>
<h1 class="unnumbered" id="question-3">Question 3</h1>
<p>To find the count of the sample space we choose any <span
class="math inline">\(60\)</span> beetles from the pond of <span
class="math inline">\(N\)</span> beetles. <span
class="math display">\[N(S) = \frac{n!}{60!(n-60)!} =
\begin{pmatrix}         n \\         60 \\    \end{pmatrix}\]</span> Let
the event where we have <span class="math inline">\(i\)</span> marked
beetles of the 60 be <span class="math inline">\(E_i\)</span>. We first
choose <span class="math inline">\(i\)</span> beetles from the 40 marked
beetles, then choose <span class="math inline">\(60 - i\)</span> beetles
from the unmarked beetles. <span class="math display">\[N(E_i) =
\begin{pmatrix}         40 \\         i \\    \end{pmatrix}
\cdot  \begin{pmatrix}         n - 40 \\        60 -
i  \\    \end{pmatrix}\]</span> For the case where we choose <span
class="math inline">\(12\)</span> beetles. <span
class="math display">\[N(E_{12} ) = \begin{pmatrix}        40
\\        12 \\   \end{pmatrix} \cdot  \begin{pmatrix}        n - 40
\\       48  \\   \end{pmatrix}\]</span> Therefore the probability <span
class="math inline">\(L(n)\)</span> where we choose <span
class="math inline">\(12\)</span> marked beetles from the pond. <span
class="math display">\[L(n) = \frac{40!}{28!12!}\cdot  \frac{(n -
40)!}{(n - 88)!48!} \cdot  \left( \frac{n!}{60!(n-60)!} \right)
^{-1}\]</span> Finally to find the maximum likelihood we find where
<span class="math inline">\(\frac{L(n)}{L(n - 1)} = 1\)</span>, ignoring
any constants as they will cancel out: <span
class="math display">\[\begin{aligned}    &amp;\frac{L(n)}{L(n - 1)} = 1
= \frac{(n - 40)!}{(n - 41)!} \cdot  \frac{(n  - 60)!}{(n - 61)!}
\cdot  \frac{(n - 1)!}{n!} \cdot  \frac{(n - 89)!}{(n - 88)!}
\\    &amp;\frac{(n - 40 )(n - 60)}{n ( n - 88)} = 1 \\
\\    &amp;\therefore \, n = 200\end{aligned}\]</span></p>
<h1 class="unnumbered" id="question-4">Question 4</h1>
<ol>
<li><p>The total count of the sample space for poker hands is choosing
any <span class="math inline">\(5\)</span> cards from <span
class="math inline">\(52\)</span>. <span class="math display">\[N(S) =
\begin{pmatrix}             52 \\             2 \\        \end{pmatrix}
= 2\,598\,960\]</span> Now let <span class="math inline">\(E_i\)</span>
be the case where we have one pair and <span
class="math inline">\(E_{ii}\)</span> two pairs.</p>
<ol>
<li><p>To find the event with one pair, we choose 1 number from 13, then
we choose 2 suits from that number, next we choose any 3 numbers of the
remaining 12 finally choosing any suit from each of those 3 numbers.
<span class="math display">\[\begin{aligned}            N(E_i) &amp;=
\begin{pmatrix}                 13
\\                1\\            \end{pmatrix}             \begin{pmatrix}                 4
\\                 2
\\            \end{pmatrix}            \begin{pmatrix}                12
\\                 3
\\            \end{pmatrix}            \begin{pmatrix}                 12
\\                 3
\\            \end{pmatrix}             \begin{pmatrix}                 4
\\                 1
\\            \end{pmatrix}            \begin{pmatrix}                4
\\                1
\\           \end{pmatrix}           \begin{pmatrix}            4
\\            1 \\       \end{pmatrix} = 1 \, 098 \, 240 \\       P(E_i)
&amp;= 0.42256    \end{aligned}\]</span></p></li>
<li><p>For two pairs, we must choose 2 numbers from the 13 to be our
pairs, then for each of those numbers choose 2 suits, finally choose one
number from the remaining 11 and a suit. <span
class="math display">\[\begin{aligned}        N(E_{i i}) &amp;=
\begin{pmatrix}            13
\\           2\\       \end{pmatrix}        \begin{pmatrix}            4
\\            2 \\       \end{pmatrix}
^{2}        \begin{pmatrix}           11 \\            1
\\       \end{pmatrix}       \begin{pmatrix}            4
\\            1 \\       \end{pmatrix}  = 123 \, 552 \\       P(E_{i i})
&amp;= 0.04754    \end{aligned}\]</span></p></li>
</ol></li>
<li><p>For poker dice the sample space count is found by choosing one
number from the 6 sides 5 times in a row. <span
class="math display">\[N(S) = 6^{5} = 7\,776\]</span></p>
<ol>
<li><p>To get one pair we choose 2 dice for the pair. We can group the 5
dice into 4 "groups" from the first group we have 6 possible numbers,
the second 5 and so on so forth. <span
class="math display">\[\begin{aligned}            N(E_i) &amp;=
\begin{pmatrix}                 5 \\                 2
\\            \end{pmatrix} \cdot  6 \cdot  5 \cdot  4 \cdot  3 =
3600\\            P(E_{i}) &amp;=
0.463        \end{aligned}\]</span></p></li>
<li><p>For two pairs, I have 3 "groups" for the two pairs we can choose
any two numbers from the 6, then we have 4 numbers left for the
remaining dice. The 5 dice can be arranged in <span
class="math inline">\(5!\)</span> ways, and we must divide by <span
class="math inline">\((2!)^{2}\)</span> to account for the repetitions
in the pairs. <span
class="math display">\[\begin{aligned}            N(E_{ii}) &amp;=
\begin{pmatrix}                 6 \\                 2
\\            \end{pmatrix} \cdot  4 \cdot  \frac{5!}{2!2!} =
1800\\            P(E_{i i}) &amp;=
0.2315        \end{aligned}\]</span></p></li>
</ol></li>
</ol>
<h1 class="unnumbered" id="question-5">Question 5</h1>
<ol>
<li><p>Following the suggestion from the question we can line up <span
class="math inline">\(m - 1\)</span> lines and <span
class="math inline">\(n\)</span> stars. e.g. “ <span
class="math inline">\(| | | | | * * * * * *\, *\)</span> ” would be the
initial arrangement for <span class="math inline">\(6\)</span> urns and
<span class="math inline">\(7\)</span> balls. The total number
arrangements of the elements in this string is, <span
class="math inline">\((m - 1 + n)!\)</span> divided by <span
class="math inline">\((m - 1)!\)</span> and <span
class="math inline">\(n!\)</span> to account for the repetitions: <span
class="math display">\[N(S_{mn}) = \frac{(m - 1 + n)!}{n! (m - 1)!} =
\begin{pmatrix}             m - 1 + n \\             n
\\        \end{pmatrix}\]</span></p></li>
<li><p>For the Fermi Dirac case with <span class="math inline">\(m
\geq  n\)</span> once an urn has a ball it can no longer have another
ball. “ <span class="math inline">\(\bullet \bullet \circ \circ
\circ\)</span> ” is an example of an arrangement with 5 urns and 2
balls. The total arrangements for this case is <span
class="math inline">\(m!\)</span> divided by <span
class="math inline">\(n!\)</span> for the repetitions of full urns and
<span class="math inline">\((m - n)!\)</span> for the repetitions of
empty urns. <span class="math display">\[N(S_{mn} ) = \frac{m!}{n!(m -
n)!} = \begin{pmatrix}             m  \\             n
\\        \end{pmatrix}\]</span></p></li>
</ol>
</body>
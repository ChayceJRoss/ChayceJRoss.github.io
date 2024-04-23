<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="Chayce Ross and Sarah Gauthier" />
  <title>Sigma</title>
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
<h1 class="title">Sigma</h1>
<h2 class="author">Chayce Ross and Sarah Gauthier</h2>
<h3 class="date">6th April 2024</h3>
</div>
<h1 class="unnumbered" id="introduction-and-theory">Introduction and
Theory</h1>
<p>In order to map the coordinate system for the fiducials in the CT
scans <span class="math inline">\(x_l\)</span> (“CT fiducials") to the
fiducials in our game world <span class="math inline">\(x_r\)</span>
(“physical fiducials") we used Horns algorithm <span class="citation"
data-cites="RoboticsRegistration">(Robotics Knowledgebase 11th May
2020)</span>. The goal of Horn’s algorithm is to minimize the error
(<span class="math inline">\(e_i\)</span>) in distance between
corresponding fiducials in two coordinate systems.</p>
<h1 class="unnumbered" id="steps">Steps</h1>
<ol>
<li><p>Find the centroid of each coordinate system where each fiducial
has equal weighting. <span
class="math display">\[\begin{aligned}        \overline{x}  =
\frac{1}{N} \sum_i x_i     \end{aligned}\]</span></p></li>
<li><p>Create new coordinate systems <span
class="math inline">\(x^{\prime}\)</span> that are shifted by the
centroids. <span
class="math display">\[\begin{aligned}        x^{\prime}_i = x_i -
\overline{x}_i     \end{aligned}\]</span></p></li>
<li><p>Find the scale, by the ratio of the norm squared of each shifted
coordinate system. <span class="math display">\[\begin{aligned}        s
= \sqrt{\left( \sum_{i} \vert x^{\prime}_{l,i} \vert ^{2}  \right)
\bigg/ \left( \sum_{i} \vert x^{\prime}_{r,i} \vert
^{2}  \right)}     \end{aligned}\]</span></p></li>
<li><p>Finally we find the rotation matrix, by minimizing the resulting
error function - <span class="math inline">\(F(\theta ,\phi,
\psi)\)</span> (derivation can be found in Appendix 1). <span
class="math display">\[\begin{aligned}        R = \text{argmin} \,2
\left( \sqrt{\left( \sum_{i} \vert x^{\prime}_{l,i} \vert ^{2}  \right)
\left( \sum_{i} \vert x^{\prime}_{r,i} \vert ^{2}  \right)}  -
\sum_{i}  x^{\prime}_{l,i} \cdot \left( R x^{\prime}_{r,i} \right)
\right)     \end{aligned}\]</span></p></li>
</ol>
<h2 class="unnumbered"
id="optimization-of-rotation-function">Optimization of Rotation
Function</h2>
<p>The .NET standard library does not provide a package for scientific
analysis. While there are .NET packages that do provide ways of
optimizing functions, they have proven hard to include in our Unity
projects because many do not target Android. Accordingly, we implemented
our own optimizer <span class="math inline">\(Q\{E(\theta, \phi, \psi)\}
\to (\theta, \phi, \psi)\)</span>. Our algorithm uses a
<span><strong>prune and search</strong></span> method to iteratively
select candidate spaces. This drastically reduces the time complexity in
searching for the minimizing rotation matrix. If we were to test every
possible solution with an precision of <span
class="math inline">\(\Delta t\)</span> degrees of <span
class="math inline">\((\theta , \phi , \psi )\)</span> the search space
<span class="math inline">\(S\)</span> would be <span
class="math inline">\(S_\theta \cdot S_\phi \cdot S_\psi = \left(
\frac{S_0}{\Delta t} \right)^3\)</span> where <span
class="math inline">\(S_0\)</span> is the breadth of the search
space.</p>
<h3 class="unnumbered" id="prune-and-search">Prune and Search</h3>
<p>Our prune and search algorithm breaks the search space (<span
class="math inline">\(S_i\)</span>) into an <span
class="math inline">\(N \times N \times N\)</span> tensor (<span
class="math inline">\({}_i\mathbf{T}\)</span>), where each element is
identified by its centre: <span class="math inline">\({}_i\mathbf{T}
_{(x,y,z)} = {}_i(\Theta_x, \Phi_y, \Psi_z)\)</span> with <span
class="math inline">\((x, y, z) \in [0, 1, \dots, N)\)</span>. We then
create a new tensor <span class="math inline">\(({}_i \mathbf{E}
)\)</span>, representing the corresponding errors by passing this tensor
through our error function: <span class="math inline">\({}_i \mathbf{E}
= F({}_i \mathbf{T} )\)</span>. The algorithm then selects the <span
class="math inline">\(P\)</span> smallest elements <span
class="math inline">\(e_{0}, e_1, \dots, e_{P - 1}\)</span> from <span
class="math inline">\({}_i \mathbf{E}\)</span>, and returns their
corresponding arguments (“candidates”): <span class="math inline">\(G =
\{G_j | j \in [0, 1, \dots, P) \}\)</span>. These define <span
class="math inline">\(P\)</span> new search spaces each with size <span
class="math inline">\(S_i / N\)</span>. Successive iterations of the
algorithm run similarly on each element <span
class="math inline">\(G_j\)</span> of <span class="math inline">\({}_i
G\)</span>; however, the smallest elements <span
class="math inline">\(e_{0}, e_1, \dots, e_{P - 1}\)</span> are selected
from all <span class="math inline">\(\mathbf{E}_j\)</span>. i.e. Each
iteration only produces <span class="math inline">\(P\)</span>
candidates for the next iteration. This is repeated for <span
class="math inline">\(M\)</span> iterations, i.e. <span
class="math inline">\(i \in [0, 1, \dots M)\)</span>, where the
algorithm’s precision is <span class="math inline">\(\Delta t =
\frac{S_0}{N^M}\)</span>. On the last iteration the the candidate that
returns the smallest error is returned as the solution to the
optimization.</p>
<figure id="fig:optimizer_tree">
<img src="./resources/optimizer_tree.png" />
<figcaption>Tree diagram of rotation optimizer (analogy in 1 dimension).
Note that the grey blocks are the minima values of each
sequence.</figcaption>
</figure>
<p>The time complexity of this algorithm is: <span
class="math display">\[\mathcal{O} (N^3 \cdot P \cdot M) = \mathcal{O}
\left( PN^3 \cdot \frac{ \log (S_0 /\Delta t)}{\log N}\right)\]</span>
When we consider for <span class="math inline">\(S_0 = 360^{\circ},\,
\Delta t = 0.1,\, N \sim \mathcal{O} (10),\, P \sim 10\)</span> the time
complexity is about <span class="math inline">\(\mathcal{O}
(10^5)\)</span> rather than the naive solution which was about <span
class="math inline">\(\mathcal{O} (10^9)\)</span>.</p>
<figure id="fig:optimizer">
<img src="./resources/optimizer.png" />
<figcaption>Flowchart of rotation optimizer.</figcaption>
</figure>
<div id="refs" class="references csl-bib-body hanging-indent"
data-entry-spacing="0" role="list">
<div id="ref-RoboticsRegistration" class="csl-entry" role="listitem">
Robotics Knowledgebase. 11th May 2020. <span>“Registration Techniques in
Robotics.”</span> 11th May 2020. <a
href="https://roboticsknowledgebase.com/wiki/math/registration-techniques/">https://roboticsknowledgebase.com/wiki/math/registration-techniques/</a>.
</div>
</div>
</body>
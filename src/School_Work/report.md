<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <meta name="author" content="Sarah Gauthier, Chayce Ross, Henrique Saito, Sumin Olivia Kim" />
  <title>Augmented Reality Guidance for CT Spinal Injections</title>
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
      display: block;
      margin-left: auto;
      margin-right: auto;
      max-width: 100%;
    }
    figcaption {
      text-align: center;
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
<h1 class="title">Augmented Reality Guidance for CT Spinal
Injections</h1>
<h2 class="author">Sarah Gauthier, Chayce Ross, Henrique Saito, Sumin
Olivia Kim</h2>
<h3 class="date">12th April 2024</h3>
</div>
<figure id="fig:controller_header">
<p><img src="./figs/quest_controller.jpg" style="width:70.0%"
alt="image" /> <span id="fig:controller_header"
label="fig:controller_header"></span></p>
</figure>
<div class="center">
<h2 class="unnumbered" id="project-sponsor">Project Sponsor</h2>
<p>Philip Edgcumbe - UBC Radiology<br />
</p>
<h2 class="unnumbered" id="project-2405">Project 2405</h2>
<p>ENPH 459<br />
Engineering Physics Project Lab<br />
University of British Columbia<br />
</p>
</div>
<h1 id="introduction---olivia">Introduction - Olivia</h1>
<h2 id="background">Background</h2>
<p>Spinal injections are a common medical procedure involving the
injection of medication near specific nerves in the spinal area to
relieve pain. These procedures are performed by neuroradiologists who
use CT scans of the patient’s spine to guide the injection needle to the
desired location. To ensure precise needle placement, physicians must
take multiple CT scans of the patient’s spine at different angles to
confirm that the needle is correctly inserted. This is a long process
that exposes patients and physicians to harmful radiation. Additionally,
due to the trial-and-error nature of this procedure, it may require
multiple needle insertion attempts, each involving a series of CT
scans.<br />
To reduce the number of CT scans and needle insertion attempts required,
we propose an Augmented Reality (AR) tool, using the Meta Quest 3
headset, to guide these spinal injection procedures.</p>
<h2 id="team-introduction---sponsors-and-students">Team Introduction -
Sponsors and Students</h2>
<p>This project is sponsored by Dr. Philip Edgcumbe, a resident
physician, entrepreneur, biomedical engineer and clinician-scientist
(MD, PhD) working in Diagnostic Radiology at the University of British
Columbia (UBC). Dr. Edgcumbe also holds a BASc in Engineering Physics
from UBC, obtained in 2011. He has invented, patented and licensed an
augmented reality navigational aid for surgery and co-founded two
biomedical start-up companies. Given his extensive background in both
medicine and engineering, Dr. Philip Edgcumbe was able to provide
excellent guidance and support throughout this project.<br />
In addition to Dr. Edgcumbe, Dr. Will Guest (MD, PhD, BSc), a
neuroradiologist at the Vancouver General Hospital (VGH), provided
supervisory support.<br />
The student team is comprised of four 4th-Year Engineering Physics
students at UBC: Sarah Gauthier, Chayce Ross, Henrique Saito and Sumin
Olivia Kim.</p>
<h2 id="discussion-with-stakeholders">Discussion with Stakeholders</h2>
<p>Prior to developing this AR solution, the team held discussions with
stakeholders to accurately scope project needs. Dr. Will Guest, a staff
physician at the Vancouver General Hospital was a key stakeholder in
this project, with in-depth experience with spinal injections and
radiology.<br />
During an interview conducted at the Vancouver General Hospital, Dr.
Guest described in detail the steps involved in a spinal injection
(which we outline in <a
href="#spine-procedure:Overview of Spinal Injection Procedure"
data-reference-type="ref"
data-reference="spine-procedure:Overview of Spinal Injection Procedure">1.4</a>).
He also explained the limitations of the current procedure. He mentioned
that the procedure can be uncomfortable to perform for physicians as the
patient needs to be lying inside the CT scanning unit at all times. If a
patient has a large torso, they may take up most of this area, making it
difficult to insert the needle at the right angle.<br />
Dr. Guest expressed that having the patient’s bony structures projected
onto their body during this procedure would be a great asset to
neuroradiologists as they would be able to insert the needle using with
less iterative CT scans, and perform the injections more quickly.</p>
<p>This interview allowed the engineering team to assess the key project
objectives.<br />
<a href="https://www.youtube.com/watch?v=NSqduAn1Zb4">This video shows
the steps of a CT-guided spinal procedure, by Dr. Will Guest.</a></p>
<h2 id="spine-procedure:Overview of Spinal Injection Procedure">Overview
of Spinal Injection Procedure</h2>
<p>Spinal injection procedures are used primarily to relieve pain by
delivering medication directly to the spinal nerves’ vicinity, and are
often employed in cases of chronic back pain, sciatica, herniated discs,
and spinal stenosis, among other conditions.<br />
<br />
The procedure involves patient preparation, precise needle insertion
guided by imaging techniques (such as fluoroscopy or CT scans), and
medication delivery directly to the pain site.<br />
</p>
<ol>
<li><p><strong>Patient Preparation:</strong> Before the procedure,
patients receive a comprehensive evaluation where the risks and benefits
are explained. This phase also involves monitoring vital signs and
positioning the patient.</p></li>
<li><p><strong>Initial CT Scan:</strong> A CT scan of the patient’s
spinal region is done to accurately locate the optimal needle insertion
trajectory. This imaging m odality provides real-time visuals of the
spine, enabling precise needle guidance to the affected area.</p></li>
<li><p><strong>Sterilization and Anesthesia:</strong> The skin over the
targeted site is meticulously cleaned and sterilized to minimize
infection risks. A local anaesthetic is then administered to numb the
area, reducing discomfort during needle insertion.</p></li>
<li><p><strong>Initial Needle Insertion:</strong> With the patient still
inside the CT scanning unit, a needle is inserted through the skin,
about 1cm deep, and meticulously directed toward the area adjacent to
the spinal nerves.</p></li>
<li><p><strong>Verification CT Scan:</strong> The physician takes
another CT scan of the patient with the needle inserted. The needle’s
position is checked. If the needle is in the right position, the
physician moves on to the next step. Otherwise, they remove the needle
and return to the initial needle insertion step.</p></li>
<li><p><strong>Deeper Needle Insertion:</strong> The physician pushes
the needle in slightly deeper. The needle’s placement is continuously
adjusted based on imaging feedback until the optimal position is
confirmed. Subsequently, the medication—commonly a steroid or
anesthetic—is injected to diminish inflammation and mitigate
pain.</p></li>
<li><p><strong>Procedure Conclusion:</strong> Upon successful medication
delivery, the needle is carefully withdrawn, and the injection site is
cleaned and bandaged. Post-injection, patients are observed for a brief
period to monitor for adverse reactions.</p></li>
</ol>
<h2 id="previous-work---chayce">Previous Work - Chayce</h2>
<p>This work is inspired by a previous paper (<span class="citation"
data-cites="HoloInjections">(Heinrich et al. 2019)</span>) that tested
and compared different assistance and guidance techniques for needle
insertion procedures using the <a
href="https://www.microsoft.com/en-ca/hololens">Microsoft Hololens</a>,
an AR headset. In this paper, the researchers used the HoloLens to
project a needle trajectory above a foam block. The user would try to
match the trajectory and insert a needle into the foam. The goals of the
paper were to:</p>
<ol>
<li><p>Find out if AR headsets are a viable form of guidance for
surgical settings.</p></li>
<li><p>Compare the effectiveness of different visualization methods for
guidance, including the intersection of two planes, a line, and a cone
(Figure <a href="#fig:cones" data-reference-type="ref"
data-reference="fig:cones">2</a>).</p></li>
</ol>
<figure id="fig:cones">
<img src="figs/cones.jpg" style="width:90.0%" />
<figcaption>Different guidance methods for injections compared in the
HoloInjections paper (<span class="citation"
data-cites="HoloInjections">(Heinrich et al. 2019)</span>).
<strong>(a)</strong> Intersection of planes, <strong>(b)</strong> line,
<strong>(c)</strong> cone.</figcaption>
</figure>
<h4 id="methodologyevaluation">Methodology/Evaluation</h4>
<p>To test these different guidance cues, the authors of this paper
chose a trajectory angle at random and asked the user to follow it.
After the user inserted the needle completely into the block, they
measured the difference between the expected endpoint and the actual
endpoint of the needle. The authors evaluated each injection by two
criteria:</p>
<ol>
<li><p><strong>In-Plane Accuracy:</strong> Remembering that each
injection is conducted in the <strong>transverse plane</strong> of the
patient, this measures the difference in angle between the expected and
actual angles in the transverse plane.</p></li>
<li><p><strong>Out-of-Plane Accuracy:</strong> This measures the
smallest angle between the transverse plane of the patient and the angle
of the needle.</p></li>
</ol>
<p>After testing, the authors found that the <strong>cone</strong> was
the most accurate and intuitive method for guidance. They also concluded
that the HoloLens was not accurate enough to use for AR guidance and
some improvements would need to be made to the tracking sensors in the
headset. Moreover, the Hololens uses a “projection" technique to create
AR environments. To do this, it projects items onto a glass screen in
front of the user’s eyes. This allows for clear vision into the real
world but does not allow the 3D objects to be “embedded” into the user’s
environment. Rather, to the user, everything appears behind the
projections. This makes it hard to sense depth as the user cannot tell
when they have passed the intended point of insertion between the
projection and the real world.<br />
Given these important conclusions and our own research, we have chosen
to pursue the Meta Quest 3 headset given that it has greater depth
perception to allow the user to interact with the projections more
naturally.</p>
<h2 id="problem-statement">Problem Statement</h2>
<p>Spinal injection procedures currently rely on multiple CT scans to
guide needle placement. This traditional method exposes patients and
healthcare providers to significant radiation and often requires
numerous needle adjustments, making the process time-consuming and prone
to errors. There is a critical need for a solution that enhances
precision, reduces radiation exposure, and streamlines the procedure to
improve patient outcomes and safety.</p>
<h2 id="sec:ProposedSolution">Proposed Solution</h2>
<p>Our proposed solution leverages augmented reality (AR) technology to
enhance the accuracy, safety, and speed of spinal injection procedures.
By using an AR headset, we can provide the user with a real-time,
three-dimensional visual guidance system, embedded directly into the
operating environment.<br />
<br />
The core of our solution involves overlaying a virtual image of the
patient’s anatomical structures onto their actual body as viewed through
the AR headset. This “X-ray vision" feature allows the physician to see
the target area for the needle insertion without the need for repeated
CT scans, reducing radiation exposure for both patient and healthcare
providers.<br />
<br />
Additionally, our AR system projects the optimal needle trajectory into
3D space. This pathway guides the physician in real-time, suggesting the
best angle and depth for needle insertion.</p>
<h2 id="project-objectives">Project Objectives</h2>
<p>The project aims to develop a user-friendly augmented reality
solution to expedite spinal injection procedures. The AR solution should
achieve the following, in order of importance:</p>
<ol>
<li><p>Reduce the total operative time of the spinal injection
procedure</p></li>
<li><p>Reduce the average number of CT scans performed on the patient,
thereby reducing their exposure to radiation</p></li>
<li><p>Reduce the average number of needle insertion attempts required
per procedure</p></li>
<li><p>Reduce patient discomfort during the procedure</p></li>
</ol>
<h1 id="discussion">Discussion</h1>
<h2 id="theory">Theory</h2>
<h3 id="computerized-tomography-ct-scans---sarah">Computerized
Tomography (CT) Scans - Sarah</h3>
<p>To perform spinal injections, physicians must find the ideal
injection trajectory; one that avoids bony structures while targeting
the desired nerves. This is done using computerized tomography (CT)
scans of the patient’s spine. A CT scan is a diagnostic tool that uses
X-ray beams to produce images of a patient’s anatomical structures (John
Hopkins <span class="citation" data-cites="HopkinsMed">(Medicine
2023)</span>). X-rays are beams of high-energy electromagnetic radiation
that are “absorbed in different amounts depending on the density of the
material they pass through" (Mayo <span class="citation"
data-cites="MayoClinic">(Clinic 2022)</span>). The denser the material
is, the lighter it will appear in the X-ray or CT scan image. Thus,
bones and metals are easily identifiable on these types of scans since
they appear white.<br />
We can therefore leverage the fact that metal is easily identifiable in
CT scans to link the structures of the CT scans to the patient’s body in
the real world. We will explain this process in greater depth in Section
<a href="#reg:Registration" data-reference-type="ref"
data-reference="reg:Registration">2.1.4</a>.<br />
</p>
<figure id="fig:x_ray">
<img src="figs/x_ray.jpeg" style="width:30.0%" />
<figcaption>X-Ray image of a spine</figcaption>
</figure>
<p>To produce CT scans, a patient is placed inside a CT scanning unit,
which is a large cylindrical tube. They are then slowly pushed through
this tube while an X-ray beam is aimed at the patient and quickly
rotated around their body (Figure <a href="#fig:ct_unit"
data-reference-type="ref" data-reference="fig:ct_unit">4</a>).<br />
</p>
<figure id="fig:ct_unit">
<img src="figs/ct_scanner.png" style="width:50.0%" />
<figcaption>Animation of a patient inside a CT scanning
unit</figcaption>
</figure>
<p>This produces a series of cross-sectional images, or "slices" of the
patient’s body (Figure <a href="#fig:ct_stack" data-reference-type="ref"
data-reference="fig:ct_stack">5</a>). These images can then be stacked
and rendered to form a three-dimensional object of the patient’s
anatomy.</p>
<figure id="fig:ct_stack">
<img src="figs/ct-stack.png" style="width:40.0%" />
<figcaption>A stack of 2D cross-sectional CT scans</figcaption>
</figure>
<h3 id="augmented-reality---henrique">Augmented Reality - Henrique</h3>
<p>Augmented Reality (AR) is a type of immersive technology that allows
the user to see both the virtual rendered world and the real physical
world around them. It provides the user with “visual elements, sound and
other sensory information [...] through a device like a smartphone,
glasses or a headset" (<span class="citation" data-cites="ar">(Gillis
2024)</span>). We can leverage this technology to give doctors all the
necessary information they need for the procedure while simultaneously
allowing them to keep eyes on the operation. In other words, this allows
us to give guidance without interfering with the doctor’s focus or
workflow.<br />
There are various head-mounted displays (HMD) (i.e. headsets) that
support augmented reality, with varying quality. Important factors to
consider include spatial mapping precision and pass-through
resolution.</p>
<h3 id="unity">Unity</h3>
<p>In this project, Unity serves as the core development environment for
creating AR applications designed to run on headsets.<br />
Unity’s platform allows developers to utilize features such as
controller tracking, spatial anchoring, and interactive visual overlays
to create immersive AR experiences that are stable and responsive. It
also allows developers to download software development kits (SDKs) for
different headset types to the platform, which greatly helps the
development process. After development, the Unity application can be
loaded onto the headset and tested.</p>
<h3 id="reg:Registration">Registration</h3>
<p>In order to map the coordinate system for the fiducials in the CT
scans <span class="math inline">\(x_c\)</span> (“CT fiducials") to the
fiducials in our game world <span class="math inline">\(x_p\)</span>
(“physical fiducials"). Where each fiducial <span
class="math inline">\(x_{ci}\)</span> is transformed by <span
class="math inline">\(\underbar{x}_i = \underbar{t} + s \cdot \textbf{R}
\underbar{x}_{ci}\)</span>. Where <span
class="math inline">\(\underbar{t}\)</span> is a translation vector,
<span class="math inline">\(s\)</span> is a scalar scaling factor and
<span class="math inline">\(\textbf{R}\)</span> is a rotation matrix.
This process of mapping the two virtual coordinate systems together is
called “Registration”.</p>
<h2 id="design-approach">Design &amp; Approach</h2>
<h3 id="proposed-user-experience-and-workflow">Proposed User Experience
and Workflow</h3>
<p>To achieve our project objectives, we propose a system that allows
neuroradiologists to visualize both the patient’s internal anatomy and
the optimal needle insertion trajectory during spinal injections.<br />
When utilizing our developed AR solution, the physician would perform
spinal injections following these steps (illustrated in Figure <a
href="#fig:work-flow" data-reference-type="ref"
data-reference="fig:work-flow">6</a>):</p>
<ol>
<li><p>The physician places metal fiducial markers on the patient’s back
near the injection site.</p></li>
<li><p>The physician performs a CT scan of the patient’s torso with the
fiducial markers present.</p></li>
<li><p>The physician puts on the Quest 3 headset. The CT scan data is
loaded into the headset and is projected in front of the user.</p></li>
<li><p>The physician scrolls through all the CT slices using a scroll
bar below the images. When they see a white dot at the top of the CT
scan, they click on it to register it as a CT fiducial marker. When all
the fiducials are identified, the physician selects a desired CT slice
to annotate with the optimal needle trajectory.</p></li>
<li><p>The physician opens the CT scan annotation applet in the headset.
They select two points on the CT slice using the controller. A red line
joining these two points is created on the CT slice.</p></li>
<li><p>The stack of 2D CT slices is <strong>rendered into a 3D
object</strong> (<a href="#mesh:3D Meshing with Marching Cubes"
data-reference-type="ref"
data-reference="mesh:3D Meshing with Marching Cubes">2.2.4</a>)
representing the patient’s spine. The annotation of the needle
trajectory is rendered on the object.</p></li>
<li><p>The physician takes the controller with the pointer tip
attachment and opens the fiducial registration applet in the headset.
They tap each fiducial marker one at a time to <strong>register their
coordinates as spatial anchors</strong> (<a href="#spa:Spatial Anchors"
data-reference-type="ref"
data-reference="spa:Spatial Anchors">2.2.3</a>).</p></li>
<li><p>The fiducial markers on the 3D spinal object are <strong>mapped
to the fiducial markers on the patient’s torso using a coordinate
transformation</strong> (<a
href="#coord:Coordinate Transform using Horn&#39;s Method"
data-reference-type="ref"
data-reference="coord:Coordinate Transform using Horn&#39;s Method">2.2.5</a>).
The physician sees the needle trajectory and the patient’s internal
anatomy projected on their body.</p></li>
<li><p>The physician attaches the needle to one of the controllers using
a custom attachment piece. The controller allows the <strong>needle’s
location to be continuously tracked</strong> (<a
href="#cont:Controller Tracking and Attachments"
data-reference-type="ref"
data-reference="cont:Controller Tracking and Attachments">2.2.2</a>).
Wearing the headset, the physician follows the projected trajectory with
the needle attached to the controller.</p></li>
<li><p>The physician receives feedback on their alignment with the
optimal trajectory.</p></li>
</ol>
<p>The above components that are <strong>bolded</strong> have been
developed by our team. In the following sections, we provide an overview
of the critical design decisions made when developing these
components.</p>
<figure id="fig:work-flow">
<img src="figs/newer-workflow.png" style="width:90.0%" />
<figcaption>Proposed user experience using AR</figcaption>
</figure>
<h3 id="cont:Controller Tracking and Attachments">Controller Tracking
and Attachments</h3>
<p>For both tracking the needle and registering fiducials, we must have
a method of knowing the exact coordinates of real-world tools in the
headset’s frame of reference. We can do this by using the two
controllers that come with the Quest 3 headset. These controllers are
automatically being tracked by the headset using IR beacons, and so we
can attach the needle or a pointer to the controller and by proxy know
its coordinates.</p>
<p>In software, each controller has a set of cartesian coordinates with
respect to the world. These coordinates represent the location of a
specific point on the controller. We can call this point the “tracking
anchor". Unfortunately, the tracking anchor of the Quest 3 controller is
at a seemingly arbitrary location on the face of the controller (Figure
<a href="#fig:controller_anchor" data-reference-type="ref"
data-reference="fig:controller_anchor">7</a>).</p>
<figure id="fig:controller_anchor">
<img src="figs/controller_anchor.png" style="width:30.0%" />
<figcaption>Quest 3 controller tracking anchor point</figcaption>
</figure>
<p>Thus, the core technical problem is to find the offset between the
controller’s tracking anchor and the desired point that needs to be
tracked (needle or pointer end). In other words, we must find the black
vector illustrated in Figure <a href="#fig:controller_pointer_diagram"
data-reference-type="ref"
data-reference="fig:controller_pointer_diagram">8</a>, which shows an
example pointer attachment.</p>
<figure id="fig:controller_pointer_diagram">
<img src="figs/controller_anchor_pointer.png" style="width:30.0%" />
<figcaption>Unknown vector between anchor point and pointer
tip</figcaption>
</figure>
<p>Our initial plan was to lock down the end of the pointer in one spot
with a purpose-built rig (as an example, see Figure <a
href="#fig:controller_calibration_rig" data-reference-type="ref"
data-reference="fig:controller_calibration_rig">9</a>). We then rotate
the controller around and record the Cartesian coordinates and rotation
of the controller at three different spots. We can convert the rotation
to a directional vector, which combines with the Cartesian coordinates
to form a line equation. By finding the intersection of these lines, we
can then find the desired point and thus the unknown vector.</p>
<figure id="fig:controller_calibration_rig">
<img src="figs/calibration_rig.png" style="width:50.0%" />
<figcaption>Example calibration rig to keep end point
static</figcaption>
</figure>
<p>If the three lines were guaranteed to intersect, finding the
intersection would be trivial. Unfortunately, the lines will note
exactly intersect, so a least-squares approximation has to be used to
find the point which minimizes the distance to each of the lines. A
system diagram can be found in figures <a
href="#fig:old_calibration_diagram" data-reference-type="ref"
data-reference="fig:old_calibration_diagram">10</a> and <a
href="#fig:old_calibration_diagram2" data-reference-type="ref"
data-reference="fig:old_calibration_diagram2">11</a>.</p>
<figure id="fig:old_calibration_diagram">
<img src="figs/old_calibration_diagram_1.png" style="width:70.0%" />
<figcaption>System diagram for each recorded controller
location</figcaption>
</figure>
<figure id="fig:old_calibration_diagram2">
<img src="figs/old_calibration_diagram_2.png" style="width:90.0%" />
<figcaption>Finding intersection between lines</figcaption>
</figure>
<p>Unfortunately, this approach has a fatal flaw. The aforementioned
procedure has an inherent assumption that the controller attachment is
pointing in the same direction as the controller’s internal direction.
If the attachment was pointing to the left of the controller’s face, for
example, the lines would never all intersect and the least squares
approximation would not return the correct point (Figure <a
href="#fig:old_calibration_diagram3" data-reference-type="ref"
data-reference="fig:old_calibration_diagram3">12</a>).</p>
<figure id="fig:old_calibration_diagram3">
<img src="figs/old_calibration_diagram_3.png" style="width:50.0%" />
<figcaption>If the pointer attachment pointed left, the lines would
never intersect</figcaption>
</figure>
<p>Instead, we can do a similar procedure, where we still keep the
pointer end static and then rotate the controller about the pointer end.
We can then record four different sets of coordinates as the controller
moves around. Note that because the length of the pointer is constant,
and the location of the endpoint is also constant, the four coordinates
we have collected will define the surface of a sphere. If the
coordinates were all exactly on the surface of the sphere, it is then
trivial to find the centre of the sphere, and thus the coordinates of
the pointer end, but this is not the case. Instead, we have to optimize
the 3 parameters, which correspond with the Cartesian coordinates of the
pointer end, such that the variance in distance between each recorded
set of coordinates and the 3 parameters, is as low as possible. Thus we
have our cost function:</p>
<p><span class="math display">\[\text{Cost} =
\frac{1}{4}\sum^{4}_{i=1}(r_i - \bar{r})^2\]</span></p>
<p>where <span class="math inline">\(r_i\)</span> represents the
distance between the <span class="math inline">\(i\)</span>th recorded
coordinates and the proposed centre and <span
class="math inline">\(\bar{r}\)</span> represents the mean distance
between all of the recorded coordinates and the proposed centre.<br />
Software aside there exist further considerations about the controller
attachments. Taking off and putting back on the attachment may end up
with slightly different positioning, so ideally we keep the attachments
permanently on the controllers. Luckily for us, we have two controllers
and two separate attachments. Another further consideration is the
attachment mechanism to the actual medical needle. We have decided to
delay designing for the needle until the underlying engineering work is
done.<br />
Lastly, there is one final consideration in the medical context. In an
operation, the common rule of thumb is that everything below the
doctor’s neck must be sterilized. This means while we do not have to
worry about the sterilization of the headset, we must sterilize the
controllers. The easiest solution is to place the controllers inside
sterilized plastic bags, which are custom-made for sterilizing
non-medical tools. There is a concern that the plastic bag will
interfere with the IR tracking beacons on the controller, but like the
needle attachment design, we will delay this decision.</p>
<h3 id="spa:Spatial Anchors">Spatial Anchors</h3>
<p>To translate the real world into the AR space, physical objects on
the patient’s body (metal fiducial markers) are registered as spatial
anchors.<br />
Spatial anchors are digital markers that allow AR environments to
accurately anchor virtual objects to specific locations in the real
world. This ensures that virtual content appears stable and remains in
the correct real-world position, even as the user moves and interacts
with the environment.<br />
<br />
<strong>SDKs</strong><br />
<br />
To build spatial anchors within Unity for the Meta Oculus Quest 3
headset, several SDKs and integration packages were used. Specifically,
the Meta Oculus Integration package (deprecated) as well as the Meta
All-In-One SDK provided extensive support for the creation,
customization and data extraction for spatial anchors. Using these two
packages, two sets of preliminary spatial anchor prototypes were
created.<br />
</p>
<figure id="fig:meta-all">
<img src="figs/oculus-int.png" />
<img src="figs/meta-all.png" />
<figcaption>Meta All-In-One SDK</figcaption>
</figure>
<p><br />
<strong>Prototype 1: Oculus Integration (deprecated)</strong><br />
<br />
The Oculus Integration package (release: 07/2017) provides several
Oculus Unity SDK integrations as a single Unity asset, as well as an
extensive range of existing examples, tutorials and documentation. This
abundance of resources made it a straightforward process to develop the
first prototype.<br />
<br />
This prototype, derived from Meta’s Unity StarterSamples, incorporates
XR features such as controller tracking, 3D location markers, anchor
placement, and various tools for interacting with anchors—specifically,
selecting, moving, and deleting them.<br />
<br />
This model features a user menu with two options: "Create Anchor" and
"Select Anchor." In the "Create Anchor" mode, the user sees the
controller, which displays location tracking lines to guide placement of
the anchor in 3D space. Users can then place the anchor, represented by
a small anchor icon—a custom prefab specified within Unity—at the chosen
location. Once placed, the anchor remains fixed in that position,
allowing users to observe that it does not move as they interact with
and move around their environment. In the "Select Anchor" mode, users
can select previously placed anchors, move them, or delete them as
needed.<br />
<br />
Despite these capabilities, the prototype primarily depended on APIs and
packages that Meta has recently deprecated. This raised concerns about
the prototype’s scalability and long-term maintainability, which are
critical considerations given that the project is expected to span
several years. Since precise and reliable spatial anchoring is essential
for accurately displaying AR overlays, the continued use of this
deprecated integration poses significant risks to the project’s future
effectiveness and support. Therefore, evaluating alternatives or updates
becomes a priority to ensure the longevity and robustness of the system
in handling AR elements within a medical setting.</p>
<figure id="fig:spatial_anc">
<img src="figs/spatial_anc.png" style="width:30.0%" />
<figcaption>Spatial anchors in AR</figcaption>
</figure>
<h3 id="mesh:3D Meshing with Marching Cubes">3D Meshing with Marching
Cubes</h3>
<p>An important part of our proposed user experience is the use of a 3D
model in our game engine for the user to see the bone structure in real
time. There are many online applications that can take CT scans and turn
them into surface meshes. However, we cannot use them as we would like
all data to stay on the device. Moreover, we want to ensure that we can
render our surfaces as soon as the CT scan is conducted (i.e. at
runtime). As a result, we have implemented an algorithm for meshing
called “Marching Cubes” (<span class="citation"
data-cites="MarchingCubes">(Wikipedia 2023)</span>), that runs in
parallel on the Graphics Processing Unit (GPU) on the headset. Below, we
will walk through our implementation, describe the algorithm and define
some necessary to understand terms.</p>
<h4 id="dsurface-meshes">3D/Surface Meshes:</h4>
<p>Unity renders 3D objects using a <span><strong>polygon
mesh</strong></span> (Figure <a href="#fig:3d_reps"
data-reference-type="ref" data-reference="fig:3d_reps">15</a>(iii)). A
polygon mesh is a list of triangles situated in 3D space that reflect
light (based on the texture of their assigned material). A smooth 3D
object is created by placing triangles along the surface of the object
to form a 3D shape.</p>
<h4 id="voxels-and-point-clouds">Voxels and Point Clouds:</h4>
<p>Recall that the CT scan returns a stack of CT images. These can be
layered on top of each other into a 3-dimensional tensor, where each
element is a number between 0 and 1 (where the 1s are the brightest
values representing the most dense structures in the anatomy). This 3D
tensor can be envisioned in two ways:</p>
<ol>
<li><p>Voxels: each element in the tensor represents a cube in 3D
space.</p></li>
<li><p>Point Cloud: each element in the tensor represents the corner of
a cube in 3D space.</p></li>
</ol>
<p>These are illustrated in Figure <a href="#fig:3d_reps"
data-reference-type="ref" data-reference="fig:3d_reps">15</a>.</p>
<figure id="fig:3d_reps">
<img src="figs/voxels.png" style="width:90.0%" />
<figcaption>Different methods of representing 3D objects created by CT
scans. <strong>(i)</strong>: Point Cloud Representation.
<strong>(ii)</strong>: Voxel Representation. <strong>(iii)</strong>:
Surface Mesh. (<span class="citation"
data-cites="3DRepresentations">(Gao et al. 2022)</span>)</figcaption>
</figure>
<h4 id="marching-cubes">Marching Cubes:</h4>
<p>To take our voxels and turn them into a surface mesh we implement an
algorithm called <span><strong>marching cubes</strong></span> (<span
class="citation" data-cites="MarchingCubes">(Wikipedia
2023)</span>):</p>
<ol>
<li><p>The stack of CT slices are converted to a <strong>point
cloud</strong> representation.</p></li>
<li><p>A threshold value is set from which to cull elements of the
tensor. If the value is less than the threshold, the element is set to
0.0, otherwise it is set to 1.0. The point cloud is now a binary
representation of the tensor. The threshold value is selected such that
only points remaining represent bones.</p></li>
<li><p>The algorithm selects <strong>eight</strong> adjacent elements of
the tensor. These form a “cube” in 3D space, where each point is a
corner of the cube. There are 256 possible cubes; however, by exploiting
their symmetry they can be reduced to 15 different unique
cubes.</p></li>
<li><p>The cube is compared against a dictionary (Figure <a
href="#fig:marching_cubes" data-reference-type="ref"
data-reference="fig:marching_cubes">16</a>) of the 15 cubes, which
returns a predetermined set of polygons that best describe the surface
created by those points (<span class="citation"
data-cites="MarchingCubes">(Wikipedia 2023)</span>).</p></li>
<li><p>This is repeated for every <strong>cube</strong> in the tensor as
the algorithm <strong>marches</strong> along all the elements in the
tensor.</p></li>
</ol>
<figure id="fig:marching_cubes">
<img src="figs/marching_cubes.png" style="width:80.0%" />
<figcaption>The dictionary that maps the fifteen unique cubes to their
corresponding surface meshes (<span class="citation"
data-cites="MarchingCubes">(Wikipedia 2023)</span>).</figcaption>
</figure>
<h4 id="shaders">Shaders:</h4>
<p>To speed up rendering, game and graphics engines use “shaders”. These
provide an interface for the engines to run rendering processes in
parallel on a Graphics Processing Unit (GPU). Unity provides an API
called “Compute Shaders" which allows the user to define a function,
that is not necessarily used for rendering, to run in parallel on the
GPU, and pass information to and from the CPU by buffers.<br />
Our implementation of the Marching Cubes algorithm works as described
above. We choose our culling threshold so only bones are rendered
(usually <span class="math inline">\(\approx 0.85\)</span>).
Additionally, we run the algorithm on the GPU in parallel with shaders
(inspired by <span class="citation" data-cites="SebLague">(Lague
2019)</span>) – where the mesh for each cube is calculated concurrently
by each GPU thread. Code for this is included in Appendix <a
href="#sec:MarchingCubes" data-reference-type="ref"
data-reference="sec:MarchingCubes">[sec:MarchingCubes]</a> and the
associated GitHub repository.</p>
<h3 id="coord:Coordinate Transform using Horn&#39;s Method">Coordinate
Transform using Horn’s Method</h3>
<p>To project the patient’s anatomy onto their body, we must apply a
coordinate transform to the rendered volume of the spine obtained from
the marching cubes algorithm.<br />
The first step is to find the Cartesian coordinates of the fiducial
markers in the CT scans. We denote this set of points by the vector
<span class="math inline">\(x_c\)</span> (CT Fiducials).<br />
Since the fiducial markers are made of metal and are lying on top of the
patient, they will appear as bright dots on the outer surface of the CT
scan (as shown in Figure <a href="#fig:mannequin"
data-reference-type="ref" data-reference="fig:mannequin">17</a>). While
scrolling through the CT slices, the physician can click on these bright
dots by aiming the controller at them one at a time. This will register
their Cartesian coordinates in the CT frame of reference.<br />
</p>
<figure id="fig:mannequin">
<img src="figs/mannequin.jpg" style="width:80.0%" />
<figcaption>A 2D CT slice of a hollow mannequin with a metal fiducial
marker on its surface.</figcaption>
</figure>
<p>To obtain the coordinates of the physical fiducial markers on the
patient’s body the physician can register them as spatial anchors as
outlined in Section <a href="#spa:Spatial Anchors"
data-reference-type="ref"
data-reference="spa:Spatial Anchors">2.2.3</a>. We denote this set of
points by the vector <span class="math inline">\(x_p\)</span> (Physical
Fiducials).<br />
With these two sets of coordinates, we can apply Horn’s Algorithm. This
mapping algorithm was recommended to us Dr. Robert Rohling, an expert in
medical information systems at UBC. It is used to estimate "the
translational (<strong>t</strong>), rotational (<strong>R</strong>), and
uniform scalar (<strong>s</strong>) correspondence between two different
Cartesian coordinate systems given a set of corresponding point pairs"
(Robotics <span class="citation"
data-cites="RoboticsRegistration">(Knowledgebase 2020)</span>). In our
case, the point pairs are the registered points in <span
class="math inline">\(x_p\)</span> and <span
class="math inline">\(x_c\)</span>.</p>
<p><span class="math display">\[x_p = sRx_c + t\]</span></p>
<p>The goal of Horn’s algorithm is to minimize the error (<span
class="math inline">\(e_i\)</span>) between corresponding fiducials when
the transformation is applied to the CT fiducials (<span
class="math inline">\(x_c\)</span>).<br />
We applied the following steps to find the best possible transformation
between both coordinate frames.</p>
<h4 id="steps">Steps:</h4>
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
= \sqrt{\left( \sum_{i} \vert x^{\prime}_{p,i} \vert ^{2}  \right)
\bigg/ \left( \sum_{i} \vert x^{\prime}_{c,i} \vert
^{2}  \right)}     \end{aligned}\]</span></p></li>
<li><p>Finally we find the rotation matrix, by minimizing the resulting
error function - <span class="math inline">\(F(\theta ,\phi,
\psi)\)</span>. <span class="math display">\[\begin{aligned}        R =
\text{argmin} \,2 \left( \sqrt{\left( \sum_{i} \vert x^{\prime}_{p,i}
\vert ^{2}  \right) \left( \sum_{i} \vert x^{\prime}_{c,i} \vert
^{2}  \right)}  - \sum_{i}  x^{\prime}_{p,i} \cdot \left( R
x^{\prime}_{c,i} \right) \right)     \end{aligned}\]</span></p></li>
<li><p>After which the translation (<span
class="math inline">\(t\)</span>) vector can be found: <span
class="math display">\[\begin{aligned}        t = \bar{x_p} - s R
\bar{x}_c    \end{aligned}\]</span></p></li>
</ol>
<p>To find the rotation matrix <strong>R</strong>, we must perform an
optimization function that minimizes the error between the Physical
Fiducials and the transformed CT Fiducials. This is simple to do in
Python; we can leverage the programming language’s libraries such as
SciPy.optimize.minimize. However, since Horn’s Algorithm must be
performed in real-time in the headset, it must be coded in C#, with the
.NET standard library.</p>
<p>The .NET standard library does not provide a package for scientific
analysis. While there are .NET packages that do provide ways of
optimizing functions, they have proven hard to include in our Unity
projects because many do not target Android. Accordingly, we implemented
our own optimizer <span class="math inline">\(Q\{E(\theta, \phi, \psi)\}
\to (\theta, \phi, \psi)\)</span>. Our algorithm uses a
<span><strong>prune and search</strong></span> method to iteratively
select candidate spaces. This drastically reduces the time complexity in
searching for the minimizing rotation matrix. From a search space of
about <span class="math inline">\(\mathcal{O}(10^9)\)</span> to about
<span class="math inline">\(\mathcal{O}(10^5)\)</span>. A software
diagram of our algorithm is included in Figure <a href="#fig:optimizer"
data-reference-type="ref" data-reference="fig:optimizer">18</a> and a
detailed description attached in Appendix <a href="#sec:Optimizer"
data-reference-type="ref"
data-reference="sec:Optimizer">[sec:Optimizer]</a>.</p>
<figure id="fig:optimizer">
<embed src="./figs/optimizer.pdf" style="width:90.0%" />
<figcaption>Flowchart of rotation optimizer.</figcaption>
</figure>
<h2 id="tests-and-results">Tests and Results</h2>
<p>Our main goal was to design and build an augmented reality system
that has high precision and accuracy while maintaining ease of use for
the user. We aimed to minimize the error between the intended needle
trajectory and the actual needle trajectory. Since our system comprises
numerous registrations and transformations, each with some associated
error, we aimed to minimize the error of each of these components as
much as possible so that the resultant propagated error was also
minimized. Throughout the design of our system, we tried to quantify the
error associated with our various registrations and transformations and
quantify how these errors would affect the final system.</p>
<h3 id="proposed-controller-attachment-tests">Proposed Controller
Attachment Tests</h3>
<p>The crucial thing to test with respect to the controller attachment
is the accuracy of the calibration offset. To test the repeatability of
the calibration procedure, we can perform the calibration multiple times
and examine the variance of our results.<br />
To test the accuracy of the calibration offset, we will add a marker to
a piece of paper on a flat surface. A user will then put on the headset
and draw a dot on the paper where they see the offset point in AR. By
measuring the distance between the drawn dot and the marker, we get a
measure of the accuracy of the calibration offset (Figure <a
href="#fig:controller_pointer_testing" data-reference-type="ref"
data-reference="fig:controller_pointer_testing">19</a>).</p>
<figure id="fig:controller_pointer_testing">
<img src="figs/controller_pointer_testing.png" style="width:60.0%" />
<figcaption>Testing controller calibration offset accuracy</figcaption>
</figure>
<h3 id="horns-algorithm-error-propagation">Horn’s Algorithm Error
Propagation</h3>
<p>To test how errors propagate we used a series of Monte Carlo
simulations rather than finding an analytic solution. By altering
different parameters of the simulation we found how they affect the
error propagation in the system. A full Jupyter notebook can be found in
Appendix 1.</p>
<h4 id="methodology">Methodology</h4>
<p>The steps we took to conduct the simulations were as follows:</p>
<ol>
<li><p>Generate <span class="math inline">\(N\)</span> fiducicials. Each
of these is situated in the XY plane, at some radius <span
class="math inline">\(R\)</span> away from the origin. They are evenly
spaced around the origin <span class="math inline">\(\frac{2
\pi}{N}\)</span> radians apart from each other.</p></li>
<li><p>Each fiducial is randomly (normal distribution <span
class="math inline">\(\Delta \sim \text{Norm}(0, R / 5)\)</span>
perturbed in the X, Y and Z directions by some value. This step and the
previous step simulate the curves and non uniform shape of the back of a
patient. These points define the “Registered Fiducials” (<span
class="math inline">\(x_l\)</span>)</p></li>
<li><p>A random transform is created, with scale (s), euler rotation (R)
and translation (t). Then the same transform is applied to each of the
fiducials.</p></li>
<li><p>Each of the fiducials is perturbed once again by some small
amount in <span class="math inline">\(X_e\)</span>, <span
class="math inline">\(Y_e\)</span> and <span
class="math inline">\(Z_e\)</span> (each of them normally distributed:
<span class="math inline">\(\Delta_e \sim N(r, \sigma_e)\)</span>. We
define a new random variable : <span class="math display">\[E_T =
\sum_i^N \sqrt{X_{ei}^2 + Y_{ei}^2 + Z_{ei}^2}\]</span> Where <span
class="math inline">\(i\)</span> denotes the <span
class="math inline">\(i\)</span>th fiducial. This step simulates some
random mean squared error (RMSE) that is added during the registration
process. This new set of fiducials defines the “CT Fiducials” <span
class="math inline">\(x_r\)</span>.</p></li>
<li><p>We run Horns Algorithm to map the CT Fidcucials to the Registered
Fiducials (<span class="math inline">\(\textbf{H} x_r \to x_{rt} \approx
x_l\)</span>).</p></li>
<li><p>We find the RMSE error between the Transformed CT Fiducials and
the Registered Fiducials: <span class="math display">\[E_R = \sum_i^N
\sqrt{(X_{rt} - X_l)^2 + (Y_{rt} - Y_l)^2 + (Y_{rt} -
Y_l)^2}\]</span></p></li>
<li><p>To find how the errors propagate we compared the standard
deviations and means of <span class="math inline">\(E_T\)</span> and
<span class="math inline">\(E_R\)</span> (assuming they are normal
distribution by law of large numbers): <span
class="math display">\[\begin{aligned}        &amp;E_T \sim
\text{Norm}(\bar{T}, \sigma_T) \\        &amp;E_R \sim
\text{Norm}(\bar{R}, \sigma_R)    \end{aligned}\]</span> An example
result of the simulation can be seen in Figure <a
href="#fig:normal-dist" data-reference-type="ref"
data-reference="fig:normal-dist">20</a></p>
<figure id="fig:normal-dist">
<img src="figs/normal_dist.png" style="width:80.0%" />
<figcaption>An example output from the simulation, comparing the input
error and the error after Horn’s Algorithm has been used to transform
the noisy data.</figcaption>
</figure></li>
</ol>
<h4 id="results">Results</h4>
<p>The results can be split into two parts:</p>
<ol>
<li><p>Error changes with respect to fiducial distance from orgin (<span
class="math inline">\(r\)</span>): <span
class="math display">\[\begin{aligned}    f_X(r) &amp;= \frac{\text{X of
} E_T (r)}{\text{X of } E_R (r)} \\    \log|f_{\text{Mean}}(r)|
&amp;=  -0.438 \cdot r - 2.02 \quad
\text{(Figure~\ref{fig:mean_error})}\\    \log|f_{\text{STD}}(r)| &amp;=
-0.431 \cdot r - 3.2 \quad
\text{(Figure~\ref{fig:std_error})}    \end{aligned}\]</span> This is an
exponential decay. Where initial increases in the distance from the
origin decrease the errors in the registration greatly. However, this
effect drops off as the distance becomes large.</p>
<figure id="fig:error_propagation">
<figure id="fig:std_error">
<img src="figs/horns_std.png" />
<figcaption>Shows how the standard deviation of errors changes as <span
class="math inline">\(r\)</span> increases.</figcaption>
</figure>
<figure id="fig:mean_error">
<img src="figs/horns.png" />
<figcaption>Shows how the mean of errors changes as <span
class="math inline">\(r\)</span> increases.</figcaption>
</figure>
<figcaption>The results of how the errors propagate from horns
algorithm. Note these are logy graphs.</figcaption>
</figure></li>
<li><p>Error changes with respect to the number of fiducials (N) - our
results are only qualitative. However, the mean change in error
increases with the N, while the STD (precision) decreases with N
(Figure <a href="#fig:N_horns" data-reference-type="ref"
data-reference="fig:N_horns">26</a>).</p>
<figure id="fig:N_horns">
<figure id="fig:N_mean">
<img src="figs/horns_N.png" />
<figcaption>Shows how the mean of errors changes as <span
class="math inline">\(N\)</span> increases.</figcaption>
</figure>
<figure id="fig:N_std">
<img src="figs/horns_N_RMSE.png" />
<figcaption>Shows how the <strong>standard deviation</strong> of errors
changes as <span class="math inline">\(N\)</span>
increases.</figcaption>
</figure>
<figcaption>The results of how the errors propagate from horns
algorithm. Note these are logy graphs.</figcaption>
</figure></li>
</ol>
<h4 id="key-takeaways-and-limitations.">Key Takeaways and
Limitations.</h4>
<p>This analysis suggests that we should have a large distance between
the fiducials and keep the number of fiducials between three and five.
However, this analysis only shows the average error between coordinate
systems and does not show localised errors. It will be important to
investigate localised errors further as they are more relevant to our
application.<br />
So far, we have only used Horn’s algorithm on simulations using sets of
generated sample points with random error. We are assuming that the real
system will behave similarly to this simulation, but this may be a false
assumption. This limits the conclusions we can make from these
simulations. We will need to apply this algorithm to the actual
coordinates of fiducial markers registered using our spatial anchoring
procedure and see if we obtain acceptable results.</p>
<h1 id="conclusions">Conclusions</h1>
<h2 id="controller-attachments">Controller Attachments</h2>
<p>We have 3D printed controller attachment prototypes and qualitatively
tested the rigidity of their connection to the Quest 3 controllers
(Figure <a href="#fig:controller_pointer_picture"
data-reference-type="ref"
data-reference="fig:controller_pointer_picture">27</a>). In addition, we
have developed a software implementation of the proper calibration
procedure up until the optimization function.</p>
<figure id="fig:controller_pointer_picture">
<img src="figs/quest_controller.jpg" style="width:30.0%" />
<figcaption>Controller pointer attachment prototype</figcaption>
</figure>
<h2 id="spatial-anchors">Spatial Anchors</h2>
<p>We have created a Unity demo to allow the user to place and remove
spatial anchors at an arbitrary location with respect to the
controller.</p>
<h2 id="horns-algorithm">Horn’s Algorithm</h2>
<p>We have finished writing an implementation of the Horn’s algorithm in
a Jupyter notebook and C# script. The aforementioned error propagation
simulations for Horn’s algorithm has given us insight into the effects
of uncertainty on the mapping.</p>
<h2 id="d-meshing">3D Meshing</h2>
<p>We have fully implemented volumetric 3D rendering in Unity (Figure <a
href="#fig:volumetric_rendering" data-reference-type="ref"
data-reference="fig:volumetric_rendering">28</a>). The rendering is
interactable and transformable, allowing for us to define its location
with spatial anchors in the future.</p>
<figure id="fig:volumetric_rendering">
<img src="figs/volumetric_rendering.png" style="width:30.0%" />
<figcaption>Volumetric rendering of CT scans rendered in
Unity</figcaption>
</figure>
<h1 id="recommendations">Recommendations</h1>
<p>This is a two year project and we plan to implement all the features
outlined in our Proposed Solution (Section <a
href="#sec:ProposedSolution" data-reference-type="ref"
data-reference="sec:ProposedSolution">1.7</a>). While we have some of
the missing features are written out in either Python or C# we still
need to integrate them. The progress of incomplete sub-systems is
written out below:</p>
<ol>
<li><p>Registration with Horn’s Algorithm – Horns algorithm written out
in C# but not integrated with a Unity game world (“scene"). Registration
with spatial anchors is complete but not integrated with our
demo.</p></li>
<li><p>Slice Selection – Selection is implemented and integrated with
our demo. However, we are missing the ability to situate the slices in
the scene (see above) and draw a desired directory on the
slices.</p></li>
<li><p>Controller Registration – Mathematical theory has been worked out
but not implemented in code.</p></li>
<li><p>Controller Tracking and Angle Feedback – Not implemented on any
platform.</p></li>
<li><p>Runtime downloading of DICOM files from hospital servers, and
conversion and extraction of CT Slices – Not implemented on any
platform.</p></li>
</ol>
<p>Additionally, we need to evaluate the effectiveness of AR as a means
of guidance in clinical settings. This includes evaluating the:</p>
<ol>
<li><p>Tracking accuracy of the Meta Quest 3 controllers.</p></li>
<li><p>Consistency of Quest 3 headset in situating itself over long
periods of time.</p></li>
<li><p>User accuracy using our technique. We recommend doing this by
conducting tests where the headset user is asked to insert a needle into
a foam block using only the visual guidance of the headset. The
insertion and end points of the needle through the foam block would then
be compared with the intended trajectory to evaluate the accuracy of the
system.</p></li>
<li><p>Effectiveness of the different sub-systems our technique uses in
assisting the user (e.g. does the 3D model provide better assistance to
the user than hand tracking).</p></li>
<li><p>User experience of our systems based on feedback from
clinicians.</p></li>
</ol>
<h1 id="deliverables">Deliverables</h1>
<h2 id="mechanical">Mechanical</h2>
<p>CAD models for the controller attachments and testing rigs can be
found in an <a
href="https://cad.onshape.com/documents/a7669772db1e8cf42f0d84d7/w/a372f52852661928ae6b39d4/e/6cbc84bf2eabff7db7f6d995?renderMode=0&amp;uiState=661c9dc0dc1f8708bbbcbccf">Onshape
document.</a></p>
<h2 id="software">Software</h2>
<p>A majority of our work is contained in <a
href="https://github.com/okim1227/AR-Spinal-Injection.git"><u>a GitHub
Repository</u></a> including working Unity scenes, Jupyter (Python)
Notebooks and C# scripts.</p>
<ol>
<li><p>“<strong>ProjectFair/</strong>” is a Unity scene which
implements:</p>
<ol>
<li><p>Slice Selection,</p></li>
<li><p>3D Modelling with Marching Cubes.</p></li>
</ol></li>
<li><p>“<strong>Notebooks/Horns.ipynb</strong>” – Python Jupyter
Notebook showing how we implement Horn’s Algorithm and it’s error
propagation (.html file included as well).</p></li>
<li><p>“<strong>Scripts/Horns.cs</strong>” – Unity C# file that uses
Horns Algorithm and implements our rotation function optimiser.</p></li>
</ol>
<h1 class="unnumbered" id="references">References</h1>
<div id="refs" class="references csl-bib-body hanging-indent"
data-entry-spacing="0" role="list">
<div id="ref-MayoClinic" class="csl-entry" role="listitem">
Clinic, Mayo. 2022. <span>“X-Ray.”</span> <em>Mayo Clinic</em>, January.
<a
href="https://www.mayoclinic.org/tests-procedures/ct-scan/about/pac-20393675">https://www.mayoclinic.org/tests-procedures/ct-scan/about/pac-20393675</a>.
</div>
<div id="ref-3DRepresentations" class="csl-entry" role="listitem">
Gao, Mengran, Ningjun Ruan, Junpeng Shi, and Wanli Zhou. 2022.
<span>“Deep Neural Network for 3D Shape Classification Based on Mesh
Feature.”</span> <em>Sensors</em> 22 (18). <a
href="https://doi.org/10.3390/s22187040">https://doi.org/10.3390/s22187040</a>.
</div>
<div id="ref-ar" class="csl-entry" role="listitem">
Gillis, Alexander S. 2024. <span>“What Is Augmented Reality
(AR)?”</span> <em>TechTarget</em>. <a
href="https://www.techtarget.com/whatis/definition/augmented-reality-AR">https://www.techtarget.com/whatis/definition/augmented-reality-AR</a>.
</div>
<div id="ref-HoloInjections" class="csl-entry" role="listitem">
Heinrich, Florian, Lovis Schwenderling, Mathias Becker, Martin Skalej,
and Christian Hansen. 2019. <span>“HoloInjection: Augmented Reality
Support for CT-Guided Spinal Needle Injections.”</span> <em>Healthcare
Technology Letters</em> 6 (November). <a
href="https://doi.org/10.1049/htl.2019.0062">https://doi.org/10.1049/htl.2019.0062</a>.
</div>
<div id="ref-RoboticsRegistration" class="csl-entry" role="listitem">
Knowledgebase, Robotics. 2020. <span>“Registration Techniques in
Robotics.”</span> 2020. <a
href="https://roboticsknowledgebase.com/wiki/math/registration-techniques/">https://roboticsknowledgebase.com/wiki/math/registration-techniques/</a>.
</div>
<div id="ref-SebLague" class="csl-entry" role="listitem">
Lague, Sebastion. 2019. <span>“Marching Cubes.”</span> 2019. <a
href="https://github.com/SebLague/Marching-Cubes.git">https://github.com/SebLague/Marching-Cubes.git</a>.
</div>
<div id="ref-HopkinsMed" class="csl-entry" role="listitem">
Medicine, John Hopkins. 2023. <span>“Computed Tomography (CT)
Scan.”</span> <em>Www.hopkinsmedicine.org</em>. <a
href="https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/computed-tomography-ct-scan">https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/computed-tomography-ct-scan</a>.
</div>
<div id="ref-MarchingCubes" class="csl-entry" role="listitem">
Wikipedia, The Free Encyclopedia. 2023. <span>“Marching Cubes
Algorithm.”</span> Wikipedia, The Free Encyclopedia. 2023. <a
href="https://en.wikipedia.org/wiki/Marching_cubes">https://en.wikipedia.org/wiki/Marching_cubes</a>.
</div>
</div>
</body>
---
layout: default
title: Lars ten Hacken
---

<style>
  .home-section { max-width: 1100px; margin: 0 auto; padding: 3.5rem 1.5rem; }
  .home-section + .home-section { border-top: 1px solid #e5e7eb; }
  .welcome-section { text-align: center; padding-top: 2.5rem; }
  .welcome-section h1 { margin-bottom: 0.75rem; }
  .welcome-section p { max-width: 700px; margin: 0 auto; font-size: 1.15rem; }
  .profile-content { display: flex; align-items: center; gap: 2.5rem; }
  .profile-photo { width: 240px; height: 240px; flex: 0 0 240px; border-radius: 50%; object-fit: cover; }
  .profile-logos { display: flex; align-items: center; gap: 1.5rem; margin-top: 1.5rem; }
  .profile-logos img { width: 110px; max-height: 65px; object-fit: contain; }
  .project-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
  .project-card { position: relative; display: block; min-height: 230px; overflow: hidden; border-radius: 10px; background-image: url("{{ '/assets/images/main/banner.jpg' | relative_url }}"); background-position: center; background-size: cover; color: white !important; box-shadow: 0 5px 18px rgba(0, 0, 0, 0.16); transition: transform 180ms ease, box-shadow 180ms ease; }
  .project-card:nth-child(2) { background-position: center 35%; }
  .project-card:nth-child(3) { background-position: center 65%; }
  .project-card:nth-child(4) { background-position: center 80%; }
  .project-card::after { content: ""; position: absolute; inset: 0; background: linear-gradient(to top, rgba(5, 20, 35, 0.9), rgba(5, 20, 35, 0.16)); }
  .project-card:hover, .project-card:focus-visible { transform: translateY(-4px); box-shadow: 0 10px 24px rgba(0, 0, 0, 0.24); }
  .project-card-text { position: absolute; z-index: 1; right: 1.5rem; bottom: 1.35rem; left: 1.5rem; }
  .project-card-text strong, .project-card-text span { display: block; }
  .project-card-text strong { font-size: 1.25rem; }
  .project-card-text span { margin-top: 0.25rem; font-size: 0.9rem; opacity: 0.85; }
  @media (max-width: 700px) {
    .profile-content { flex-direction: column; align-items: flex-start; }
    .project-grid { grid-template-columns: 1fr; }
  }
</style>

<section class="home-section welcome-section" id="welcome">
  <h1>Welcome</h1>
  <p>Hi, I’m <strong>Lars ten Hacken</strong>. Welcome to my website!</p>
</section>

<section class="home-section" id="profile">
  <h2>Profile</h2>
  <div class="profile-content">
    <img class="profile-photo" src="{{ '/assets/images/main/profile.jpeg' | relative_url }}" alt="Portrait of Lars ten Hacken">
    <div>
      <p>I’m a MSc student in Applied Physics at Eindhoven University of Technology, pursuing the track Fluids, Bio- and Softmatter. I am passionate about <strong>fluid dynamics</strong>, <strong>soft matter physics</strong> and <strong>computational physics</strong>. Currently I am located in the United States for a six month appointment as visiting researcher at the Theoretical and Applied Fluid Dynamics Laboratory (<a href="https://taflab.berkeley.edu/">TAFLab</a>) of the University of California, Berkeley, working on a project in ocean wave reconstruction and prediction. In November, I return to the Netherlands to start my graduation project in collaboration with Tsinghua University, where I will conduct reasearch from February to May, on icing under complex conditions.</p>
      <div class="profile-logos">
        <img src="{{ '/assets/images/main/TUE.png' | relative_url }}" alt="Eindhoven University of Technology logo">
        <img src="{{ '/assets/images/main/Berkeley.png' | relative_url }}" alt="University of California, Berkeley logo">
      </div>
    </div>
  </div>
  <h3>Background</h3>
  <p>During my academic carreer I have developed proficiency in a multitude of programming languages and frameworks aimed at scientific computing, engineering and artificial intelligence. I consider myself well experienced in Python, having done projects involving object-oriented programming and writing modules. Besides Python, I have worked on projects involving control and simulation using Matlab and Simulink, used Wolfram Mathematica for symbolic math and scripting, and have experience working with Git, Linux, C and openACC on fluid simulations and HPC applications. Two projects I'd like to highlight are:</p>
</section>

<section class="home-section" id="projects">
  <h2>Projects</h2>
  <p>A selection of my physics and computational research projects. Full project pages will be added soon.</p>
  <div class="project-grid">
    <a class="project-card" href="#" aria-label="Project one — coming soon"><span class="project-card-text"><strong>Project One</strong><span>Coming soon</span></span></a>
    <a class="project-card" href="#" aria-label="Project two — coming soon"><span class="project-card-text"><strong>Project Two</strong><span>Coming soon</span></span></a>
    <a class="project-card" href="#" aria-label="Project three — coming soon"><span class="project-card-text"><strong>Project Three</strong><span>Coming soon</span></span></a>
    <a class="project-card" href="#" aria-label="Project four — coming soon"><span class="project-card-text"><strong>Project Four</strong><span>Coming soon</span></span></a>
  </div>
  <h3>Project highlights</h3>
  <ul>
    <li><p>Ocean wave reconstruction and prediction using the Higher Order Spectral (HOS) method and Ensemble Kalman Filtering (EnKF). Supported bij a €2.500 grant. During this project I made use of HOS-Ocean, an open-soure Fortran based solver for nonlinear waves. I developped my own Python code to run experiments and simulate ocean wave reconstruction using different methods. The final method used the HOS Method to solve the non-linear physics with Ensemble Kalman Filtering for data assimilation.</p></li>
    <li><p>High Performance Computing (HPC) implementation of the Lattice Boltmann Method in C using OpenACC. This project was an introduction into HPC and GPU parallelization for LBM simulations. I simulated classic fluid dynamics examples such as the Pouiselle flow and Karaman vortex street to validate the phsyics, while optimizing the code to maximimze the amount of lattice updates per second.</p></li>
  </ul>
</section>

<section class="home-section" id="about-me">
  <h2>About Me</h2>
  <p>Besides my academic carreer, I have been active in a multitude of organisations to broaden my horizon and develop myself both personally and professionaly. From these experiences I would like to highlight:</p>
  <ul>
    <li><p>A year as full time president of Junior Enterprises The Netherlands (<a href="https://www.unipartners.nl/nederland/">UniPartners Nederland</a>), where I was ultimately responsible for the national board and twelve local offices invloving 300+ students/consultants, € 800k turnover and 250+ projects.</p></li>
    <li><p>My role as trainer and speaker at <a href="https://www.deaiworkshop.nl/">De AI Workshop</a>, where I lead hands-on workshops on artificial intelligence and it's implementation for a wide range of audiences.</p></li>
    <li><p>Selected as delegate for the <a href="https://www.nahss.nl/en/">Netherlands Asia Honors Summer School</a>, a prestigious programme in Hong Kong and Ho Chi Minh City for the 70 best applicants across Dutch universities. The curriculum focussed on contemporary relations between East Asia and the West.</p></li>
    <li><p>Treasurer of <a href="https://www.business-core.nl/">Business Core Eindhoven</a>, managing a € 60k budget alongside other organisational tasks for Eindhoven's biggest student symposium.</p></li>
  </ul>
  <p>Check my <a href="{{ '/assets/Lars_ten_Hacken_CV.pdf' | relative_url }}">resume</a>.</p>
  <p>Other Links: <a href="https://www.cursor.tue.nl/en/campus/2025/juli/week-1/and-how-are-things-in-berkeley">University Paper (Cursor) Article</a></p>
</section>

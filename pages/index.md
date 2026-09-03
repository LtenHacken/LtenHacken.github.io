---
layout: default
title: Lars ten Hacken
permalink: /
---

<style>
  .home-section { box-sizing: border-box; width: 100%; max-width: none; margin: 0 auto; padding: 3.5rem 0; }
  .home-section + .home-section { border-top: 1px solid #e5e7eb; }
  .welcome-section { text-align: justify; padding-top: 2.5rem; }
  .welcome-section h1 { margin-bottom: 0.75rem; }
  .welcome-section p { max-width: none; margin: 0; }
  .profile-content { display: flex; align-items: center; gap: 2.5rem; }
  .profile-photo { width: 350px; height: 350px; flex: 0 0 350px; border-radius: 50%; object-fit: cover; }
  .profile-logos { display: flex; align-items: center; gap: 1.5rem; margin-top: 1.5rem; }
  .profile-logos img { width: 500px; max-height: 100px; object-fit: contain; }
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
  <div class="profile-content">
    <div>
      <p>Hi, I’m Lars ten Hacken. Welcome to my website!</p>
      <p>I recently graduated cum laude (GPA 8.9/10) with an MSc in Applied Physics from Eindhoven University of Technology, having specialized in Fluids, Bio- and Soft Matter. I am passionate about fluid dynamics, soft matter physics, and computational physics. My academic journey includes a visiting researcher appointment at UC Berkeley as well as Tsinghua University. As of September 2026, I am working as an R&D Engineer at FABBS, developing physics-based models for battery management systems, while preparing for PhD applications for the Fall 2027 cycle.</p>
    </div>
    <img class="profile-photo" src="{{ '/assets/images/main/profile.jpeg' | relative_url }}" alt="Portrait of Lars ten Hacken">
  </div>
  <div class="profile-logos">
        <img src="{{ '/assets/images/main/TUE.png' | relative_url }}" alt="Eindhoven University of Technology logo">
        <img src="{{ '/assets/images/main/UC_berkeley_logo.png' | relative_url }}" alt="University of California, Berkeley logo">
        <img src="{{ '/assets/images/main/tsinghua_logo.png' | relative_url }}" alt="Tsinghua University">
  </div>
</section>

<section class="home-section" id="projects">
  <h2>Projects</h2>
  <p>A selection of my physics and computational research projects. Full project pages will be added soon.</p>
  <div class="project-grid">
    <a class="project-card" href="{{ '/projects/project-one/' | relative_url }}" aria-label="Open Collective Motion with the Vicsek Model"><span class="project-card-text"><strong>Collective Motion with the Vicsek Model</strong><span>View project</span></span></a>
    <a class="project-card" href="{{ '/projects/project-two/' | relative_url }}" aria-label="Open project two"><span class="project-card-text"><strong>Project Two</strong><span>View project</span></span></a>
    <a class="project-card" href="{{ '/projects/project-three/' | relative_url }}" aria-label="Open project three"><span class="project-card-text"><strong>Project Three</strong><span>View project</span></span></a>
    <a class="project-card" href="{{ '/projects/project-four/' | relative_url }}" aria-label="Open project four"><span class="project-card-text"><strong>Project Four</strong><span>View project</span></span></a>
  </div>

  <h3 id="outputs">Outputs</h3>
  <p>Files, reports, presentations, and other project outputs.</p>
  {% assign output_count = 0 %}
  <ul class="output-list">
    {% for file in site.static_files %}
      {% if file.path contains '/assets/files/' and file.name != '.gitkeep' %}
        {% assign output_count = output_count | plus: 1 %}
        <li><a href="{{ file.path | relative_url }}">{{ file.name }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
  {% if output_count == 0 %}
    <p><em>No output files have been added yet.</em></p>
  {% endif %}
</section>

<section class="home-section" id="about-me">
  <h2>About Me</h2>
  <p>During my academic carreer I have developed proficiency in a multitude of programming languages and frameworks aimed at scientific computing, engineering and artificial intelligence. I consider myself well experienced in Python, having done projects involving object-oriented programming and writing modules. Besides Python, I have worked on projects involving control and simulation using Matlab and Simulink, used Wolfram Mathematica for symbolic math and scripting, and have experience working with Git, Linux, C and openACC on fluid simulations and HPC applications.</p>
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

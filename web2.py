<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Brian McHorney - Data Analyst</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background-color: #f5f5f5;
      color: #333;
      margin: 20px;
    }
    
    nav {
      display: flex;
      justify-content: center;
      align-items: center;
      color: #02050e;
    }

    a {
      margin: 0 2px;
      text-decoration: none;
      color: #f31e70;
    }

    header {
      text-align: center;
      margin-bottom: 20px;
    }

    h1 {
      color: #1e4094;
    }

    h2 {
      color: #1e4094;
    }

    h3 {
      color: #1e4094;
    }

    a {
      color: #1e4094;
      text-decoration: none;
    }

    .collapsible {
      cursor: pointer;
      padding: 18px;
      width: 100%;
      text-align: left;
      border: none;
      outline: none;
      transition: 0.4s;
      background-color: #1e4094;
      color: white;
      border-radius: 8px;
      margin-bottom: 10px;
    }

    .active,
    .collapsible:hover {
      background-color: #23395d;
    }

    .content {
      padding: 0 18px;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.2s ease-out;
    }

    .project-link {
      display: block;
      margin-bottom: 10px;
      color: #1e4094;
    }

    .experience-item {
      margin-bottom: 20px;
    }

    .education-item {
      margin-bottom: 20px;
    }
  </style>
</head>

<body>
  <header>
    <h1>Brian McHorney</h1>
    <p>Data Analyst | Sales Professional</p>
    <p>Tempe, AZ | Phone: (520) 429-1976 | Email: <a href="mailto:brianmchorney@gmail.com">brianmchorney@gmail.com</a></p>
    <p>LinkedIn: <a href="https://linkedin.com/in/brianmchorney/" target="_blank">linkedin.com/in/brianmchorney/</a> | GitHub: <a href="https://github.com/xbmm1" target="_blank">github.com/xbmm1</a></p>
  </header>

  <nav>
    <!-- Add navigation links with IDs that correspond to the section IDs -->
    <a href="#summary">Summary |</a>
    <a href="#technical-skills">Technical Skills |</a>
    <a href="#projects">Projects |</a>
    <a href="#experience">Experience |</a>
    <a href="#education">Education</a>
  </nav>

  <section id="summary">
    <h2>Summary</h2>
    <p>Accomplished data analyst with a sales background and ASU FinTech Bootcamp credentials. Blending expertise in finance, technology, and client relationship management, backed by comprehensive training in finance fundamentals, Python programming, data analysis, financial analysis, and machine learning applications in finance.</p>
  </section>

  <section id="technical-skills">
    <h2>Technical Skills</h2>
    <p>Tools: Python, Machine Learning, SQL, Algorithmic and Statistical Modeling, Time Series Analysis, AWS, Machine Learning, Solidity, Blockchain, Sales</p>
  </section>

  <section id="projects">
    <h2>Projects</h2>
    <button class="collapsible">Vote-Vault</button>
    <div class="content">
      <p>A program to elevate the democratic process to a new level of transparency and security with our cutting-edge "Vote-Vault" powered by Solidity and streamlined by Streamlit.</p>
      <p>I was responsible for creating the Solidity smart contract as well as the front-facing user interface. (Python, Solidity)</p>
    </div>

    <button class="collapsible">NBA-MoneyBall</button>
    <div class="content">
      <p>Used to predict the winner of the 2023 NBA Finals matchup between the Denver Nuggets and the Miami Heat.</p>
      <p>I was responsible for the machine learning and data cleaning process of the project. (Jupyter Notebook, Python)</p>
    </div>
  </section>

  <section id="experience">
    <h2>Experience</h2>

    <button class="collapsible">ONE (Open Network Exchange) | Sales Representative | 2022 – 2023 | Scottsdale, AZ</button>
    <div class="content">
      <ul>
        <li>Consistent Sales Leadership: Continuously led the sales team to surpass quarterly targets, achieving an average of 20% above expected revenue, demonstrating exceptional leadership.</li>
        <li>Special Sales Team Selection: Personally chosen for a high-performance sales team on multiple occasions.</li>
      </ul>
    </div>

    <button class="collapsible">Forest Highlands Golf Club | Bartender | 2020–2022 | Flagstaff, AZ</button>
    <div class="content">
      <ul>
        <li>Exceptional Off-Season Contribution: Invited to work multiple off-seasons.</li>
        <li>Privileged Private Event Participation: Regularly selected to work prestigious private events.</li>
      </ul>
    </div>

    <button class="collapsible">Arizona Snowbowl | Ski Instructor | 2019–2022 | Flagstaff, AZ</button>
<div class="content">
  <ul>
    <li>Outstanding Skill Progression: Consistently recognized for fostering exceptional skill development in young skiers.</li>
    <li>Received consistent praise and commendations from parents for exceptional communication, engaging teaching methods, and the positive impact on their children's confidence and enjoyment on the slopes.</li>
  </ul>
</div>


    <button class="collapsible">Flagstaff Chevrolet | Sales Representative | 2020 – 2021 | Flagstaff, AZ</button>
    <div class="content">
      <ul>
        <li>Utilized consultative selling techniques to understand customer preferences and requirements.</li>
        <li>Successfully closed sales deals, meeting or exceeding monthly targets.</li>
      </ul>
    </div>


  <section id="education">
    <h2>Education</h2>

    <div class="education-item">
      <h3>Northern Arizona University, Flagstaff, AZ (2017-2022)</h3>
      <p>Built a strong foundation in business finance, honing skills in financial analysis, risk management, and investment strategies. Actively engaged in extracurricular activities as the Apparel Chairman for Phi Gamma Delta fraternity, showcasing leadership, organizational, and communication abilities.</p>
    </div>

    <div class="education-item">
      <h3>ASU Fintech Bootcamp, Tempe, AZ (2023)</h3>
      <p>A 24-week Fintech boot camp focused on the practical technical skills needed to use data analytics, machine learning, and blockchain technologies in the Fintech industry. Throughout the course, I gained proficiency in Python, Pandas, SQL, AWS, and Ethereum.</p>
    </div>
  </section>

  <script>
    // Smooth scrolling effect for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
          behavior: 'smooth'
        });
      });
    });

    // Collapsible sections functionality
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
          content.style.maxHeight = null;
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
        }
      });
    }
  </script>
</body>

<marquee>Thanks for the consideration! 
    Feel free to call or Email (520)429-1976 or brianmchorney@gmail.com
</marquee>

</html>

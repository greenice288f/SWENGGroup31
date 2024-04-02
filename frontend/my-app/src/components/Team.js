import React from "react";
import "./Team.css"; // Assuming this is where your CSS file is located

// Importing images




function Team() {

  return (
    <section id="team">
    <div class="team-container">
        <div class="team-content">
            <h1 class="team-title">Meet Our Team</h1>
            <p class="team-text">
                They have worked hard making sure lungs are kept safe!!
            </p>
        </div>
      
        <ul class="team-card-group">
        <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/james.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">James</span>
                    <span class="team-job">Dear Leader</span>
                </div>
            </li>
            
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/mia.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Mia</span>
                    <span class="team-job">Head of Frontend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/balint.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Bálint</span>
                    <span class="team-job">Head of Backend</span>
                </div>
            </li>
    
            <li class="team-item">

                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/callum.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Callum</span>
                    <span class="team-job">Backend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/anna.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Anna</span>
                    <span class="team-job">backend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/flynn.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Flynn</span>
                    <span class="team-job">Backend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/Screenshot 2024-03-27 at 18.14.56.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Darryl</span>
                    <span class="team-job">Frontend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/andrew.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Andrew</span>
                    <span class="team-job">Backend</span>
                </div>
            </li>
           
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/daire.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Dáire</span>
                    <span class="team-job">Frontend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/emma.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Emma</span>
                    <span class="team-job">Backend</span>
                </div>
            </li>
    
            <li class="team-item">
                <picture class="team-picture">
                    <img aria-hidden="true" loading="lazy" decoding="async" src="/photos/richard.png" alt="Frontend" width="105" height="135"></img>
                </picture>
                <div class="team-info">
                    <span class="team-name">Richard</span>
                    <span class="team-job">Backend</span>
                </div>
            </li>
            
        </ul>
    </div>
</section>


  );
};



export default Team;
